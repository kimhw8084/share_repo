#!/usr/bin/env python3
"""Canonical Company PaaS entrypoint: python app.py."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parent
SOURCE=ROOT/'source'
if (SOURCE/'company_ui'/'__init__.py').is_file():
    sys.path.insert(0,str(SOURCE))

from company_ui.products.visualizer.cli import main

if __name__ == '__main__':
    main()
