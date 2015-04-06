#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
import google_com
from google_com import register

registered_classes = register()

for registered_class in registered_classes:
    setattr(sys.modules[__name__],registered_class.represent(), registered_class)


