# R14 Company PaaS / NiceGUI publishing contract

R14 retains the existing application-level deployment contract and makes no unverified infrastructure assumptions.

# Publish as NiceGUI

Use the extracted package root as the publish directory.

```text
Main file: app.py
Requirements: requirements.txt
Command: python app.py
```

Runtime dependency contract:

```text
nicegui==3.15.0
python-pptx==1.0.2
Pillow==12.3.0
```

For production, configure:

```text
COMPANY_UI_ENVIRONMENT=prod
COMPANY_UI_STORAGE_SECRET=<stable company-managed secret, at least 32 characters>
```

Optionally configure:

```text
COMPANY_UI_VISUALIZER_DATA_DIR=<approved writable persistent location>
COMPANY_UI_HOST=<host; defaults to HOST then 0.0.0.0>
COMPANY_UI_PORT=<port; defaults to PORT then 8080>
```

R12 deliberately does not add Kubernetes manifests, Redis, ingress paths, replica assumptions, or proxy settings without evidence from the company platform.
