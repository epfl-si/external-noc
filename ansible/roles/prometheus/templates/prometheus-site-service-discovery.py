"""Automatically compute targets for the production WordPress Prometheus.

Every 60 seconds, enumerate Web sites in wp-veritas and produce a number
of dynamic targets for it.

See https://github.com/epfl-si/wp-ops/blob/master/ansible/roles/wordpress-openshift-namespace/templates/prometheus-menu-service-discovery.py
"""

import json
import logging
import os
import time
import traceback
import urllib.request


class DynamicConfig:
    def __init__(self, url="https://wp-veritas.epfl.ch/api/v1/sites"):
        self.url = url

    def _get_json(self):
        res = urllib.request.urlopen(self.url)
        return ''.join(res.read().decode("utf-8"))

    @property
    def sites(self):
        if not hasattr(self, '_sites'):
            self._sites = json.loads(self._get_json())
        return self._sites

    def enumerate(self):
        targets_by_wp_env = {}
        for s in self.sites:
            if not s['wpInfra']:
                continue
            wp_env = s['openshiftEnv']
            if wp_env.startswith('unm'):
                continue

            url = s['url']
            targets_by_wp_env.setdefault(wp_env, []).append(url)
        return targets_by_wp_env.items()

while True:
    try:
        with open("/srv/dynamic/targets.json", "w") as f:
            f.write(json.dumps([
                dict(
                    targets=targets,
                    labels=dict(wp_env=wp_env))
                for wp_env, targets in DynamicConfig().enumerate()]))
    except:  # noqa
        logging.error(traceback.format_exc())
    time.sleep(300)
