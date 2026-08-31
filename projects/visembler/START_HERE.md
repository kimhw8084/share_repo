# Company UI Visualizer R14 — Start Here

Use a fresh extraction; do not copy R14 over an older release directory.

## macOS or Linux

```bash
chmod +x *.sh
./setup.sh
./run_visualizer.sh
```

Open `http://127.0.0.1:8080/visualizer`. The default local data directory is `runtime_data/`; override it with `COMPANY_UI_VISUALIZER_DATA_DIR` when needed.

For exhaustive certification after setup:

```bash
./test_linux.sh
```

## Company PaaS

- Main file: `app.py`
- Requirements: `requirements.txt`
- Command: `python app.py`

Production requires a stable `COMPANY_UI_STORAGE_SECRET`. R14 does not add Kubernetes, Redis, ingress, TLS, proxy, or persistent-volume assumptions.

See `R14_PRODUCTION_SIGNOFF.md` and `R14_RELEASE_MANIFEST.json` for release evidence.
