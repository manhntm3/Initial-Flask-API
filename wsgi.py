#!/usr/bin/python
# -*- coding: utf8 -*-

import ssl
import os

from app import create_app

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     # Legacy Python that doesn't verify HTTPS certificates by default
#     pass
# else:
#     # Handle target environment that doesn't support HTTPS verification
#     ssl._create_default_https_context = _create_unverified_https_context

app = create_app()

if __name__ == '__main__':
    app.run(debug = True, threaded=True, host = "0.0.0.0", port=9000)
