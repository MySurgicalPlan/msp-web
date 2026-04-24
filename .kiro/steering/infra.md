# Infrastructure

## Stack
- AWS CDK v2 (Python)
- Python 3.13
- CDK app entry point: `infra/app.py`
- Stack definition: `infra/infra/infra_stack.py`

## Deploying
```bash
cd infra
cdk deploy
```

## Synthesizing (dry run)
```bash
cd infra
cdk synth
```

## Testing
Run via tox from the project root (preferred):
```bash
tox -e test
```
Or directly:
```bash
pytest infra/tests/ --cov=infra --cov-report=term-missing
```

## Linting & formatting
```bash
tox -e lint
```
- `flake8` and `black` applied to `infra/infra/` and `infra/tests/`

## Security scanning
```bash
tox -e security
```
- `bandit` scans `infra/infra/`, excludes `infra/tests/`

## Conventions
- All AWS resources are defined in `infra/infra/infra_stack.py` or imported constructs under `infra/infra/`
- Do not change dependency versions without Engineering Lead approval
- The `/health` endpoint on the backend must always be reachable by the load balancer target group
- Tag all resources consistently for cost tracking and environment identification
