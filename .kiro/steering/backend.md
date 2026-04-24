# Backend

## Stack
- Python 3.13
- FastAPI 0.136.0
- Uvicorn 0.46.0
- Source lives in `backend/`; API routes go under `backend/api/`

## Running locally
```bash
uvicorn backend.main:app --reload --port 8000
```

## Testing
Run via tox (preferred):
```bash
tox -e test
```
Or directly:
```bash
pytest backend/tests/ --cov=backend --cov-report=term-missing
```

## Linting & formatting
```bash
tox -e lint
```
- `flake8` for style, `black` for formatting
- Format targets: `backend/api`, `backend/tests`
- Always run `black` before committing

## Security scanning
```bash
tox -e security
```
- `bandit` scans `backend/api/`, excludes `backend/tests/`

## Conventions
- New routes belong in `backend/api/` as separate modules, imported into `main.py`
- Do not change dependency versions without Engineering Lead approval
- CORS is configured for `http://localhost:5173` (Vite dev server) — update `allow_origins` for production
- The `/health` endpoint must remain functional — it is used by AWS Load Balancers
