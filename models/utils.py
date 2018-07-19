#!/usr/bin/env python

# Created by Wazuh, Inc. <info@wazuh.com>.
# This program is a free software; you can redistribute it and/or modify it under the terms of GPLv2

import json as json

def read_json_from_file(path):
    with open(path) as f:
        json_loaded = json.loads(f.read())

    return json_loaded
