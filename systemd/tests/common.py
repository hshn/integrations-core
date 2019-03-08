# -*- coding: utf-8 -*-

# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import os

HERE = os.path.dirname(os.path.abspath(__file__))

CONFIG = {
    'instances': [
        {
            "units": [
                "networking.service",
                "cron.service",
                "ssh.service"
            ],
            'collect_all_units': False

        }
    ]
}

DEFAULT_UNIT_ID = 'ssh.service'
DEFAULT_UNIT_STATE = 'active'