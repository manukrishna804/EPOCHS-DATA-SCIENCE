"""Bootstrap for Render when Root Directory is the repo root."""
import os
import runpy
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(ROOT, "task-11")

os.chdir(APP_DIR)
sys.path.insert(0, APP_DIR)
runpy.run_path(os.path.join(APP_DIR, "app.py"), run_name="__main__")
