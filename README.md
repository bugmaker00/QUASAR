# QUASAR

**Quasi-stellar Object Analysis, Survey, and Reporting**

QUASAR is a modular Python library for ingesting, validating, and analysing
flux-density data for quasi-stellar objects (QSOs / quasars).  It provides a
`Detection` model, a luminosity calculator, a catalogue lookup layer, a
batch-processing `Pipeline`, and JSON / plain-text report generators.

---

## Project layout

```
quasar/
├── __init__.py    – public API
├── detector.py   – flux validation and luminosity calculation
├── pipeline.py   – step-based batch pipeline
├── catalog.py    – bundled and remote catalogue support
└── report.py     – JSON and plain-text report generation
tests/
└── test_detector.py
```

---

## Quick start

```bash
pip install -e .[dev]
pytest tests/ -v
```

---

## Remote TODOs

<!-- auto-generated – do not edit manually -->
<!-- last refreshed: 2026-03-27 | 12 items -->

- [ ] **quasar/detector.py:23:** - (alice): validate flux_density > 0 before logging; see https://arxiv.org/abs/2103.12345 for limits
- [ ] **quasar/detector.py:31:** - switch from linear to log scale for luminosity: note: values span 6 orders of magnitude
- [ ] **quasar/detector.py:40:** - (bob): cache the result; current call cost: ~200 ms per invocation
- [ ] **quasar/detector.py:49:** - raise QuasarDetectionError instead of bare ValueError: aligns with PEP 8 naming
- [ ] **quasar/pipeline.py:19:** - (carol): parallelise with ThreadPoolExecutor; ref: https://docs.python.org/3/library/concurrent.futures.html
- [ ] **quasar/pipeline.py:32:** - persist checkpoint to disk before shutdown; state key: "pipeline_v2_checkpoint"
- [ ] **quasar/pipeline.py:36:** - (alice): add retry logic; max_retries: 3, backoff: exponential
- [ ] **quasar/catalog.py:25:** - load catalog from https://heasarc.gsfc.nasa.gov/W3Browse/all/veroncat.html instead of bundled CSV
- [ ] **quasar/catalog.py:39:** - (dave): add angular-separation filter; precision: arcseconds, not degrees
- [ ] **quasar/report.py:12:** - escape colons in source IDs before writing JSON; example: "J123.4+56.7:A" breaks parsers
- [ ] **quasar/report.py:17:** - (carol): honour user timezone; default: UTC, override via QUASAR_TZ env var
- [ ] **tests/test_detector.py:32:** - assert error message includes the offending value; format: "flux_density: <value> out of range"

---

## License

MIT © QUASAR Contributors
