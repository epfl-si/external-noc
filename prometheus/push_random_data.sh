#!/bin/bash

# See https://github.com/prometheus/pushgateway/blob/master/README.md

cat <<EOF | curl -i --data-binary @- http://localhost:9091/metrics/job/nicolas_job/instance/nicolas_instance
  # TYPE nicolas_metric counter
  nicolas_metric{label="val1"} 42
  # TYPE another_metric gauge
  # HELP another_metric Just an example.
  another_metric 1337.42
EOF
