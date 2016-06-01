# coding=utf-8

from werkzeug.serving import run_simple

import os, sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from apb import app as application

if __name__ == "__main__":
    # Uniquement utilisé en debug
    application.debug = True
    run_simple('0.0.0.0', 5000, application, use_reloader=True, use_debugger=True)
