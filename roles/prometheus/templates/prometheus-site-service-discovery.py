"""Automatically compute targets for the production WordPress Prometheus.

Every 300 seconds, enumerate Web sites in wp-veritas and produce a number
of dynamic targets for it.

See https://github.com/epfl-si/wp-ops/blob/master/ansible/roles/wordpress-openshift-namespace/templates/prometheus-menu-service-discovery.py
"""

from datetime import datetime
import json
import logging
import os
import socket
import time
import traceback
import urllib.request

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S"
)

class DynamicConfig:

    targetPath = "/srv/dynamic/targets.json"

    def __init__(self, url="https://wp-veritas.epfl.ch/api/v1/sites", targetPath=None, frequency=300):
        self.url = url
        if targetPath:
            self.targetPath = targetPath
        else:
            self.targetPath = DynamicConfig.targetPath
        self.frequency = frequency
        logging.info(
            "Configurator started! url=%s dynamic_file=%s frequency=%ss",
            self.url, self.targetPath, self.frequency
        )

    def _get_json(self):
        res = urllib.request.urlopen(self.url, timeout=30)
        return ''.join(res.read().decode("utf-8"))

    @property
    def sites(self):
        if not hasattr(self, '_sites'):
            self._sites = json.loads(self._get_json())
        return self._sites

    @property
    def targets(self):
        return [ self.canonical_url(s['url'])
                 for s in self.sites
                 if s.get('monitored', True) ]

    def _write(self, struct):
        tmpTarget = self.targetPath + '.tmp'
        with open(tmpTarget, "w") as f:
            f.write(json.dumps(struct))
        os.rename(tmpTarget, self.targetPath)

    def write_targets(self):
        self._write([dict(targets=self.targets)])

    def canonical_url(self, url):
        return url if url.endswith('/') else url + '/'

while True:
    dc = DynamicConfig()
    try:
        logging.info("Updating targets...")
        dc.write_targets()
        logging.info("Targets updated successfully (%d targets written to %s). Sleeping %ss.",
                     len(dc.targets), dc.targetPath, dc.frequency)
    except socket.timeout:
        logging.error("Request timed out after 30s.")
    except Exception:  # noqa
        logging.error("Error during target update: %s", traceback.format_exc())
    time.sleep(dc.frequency)
