# NEEDS REVIEWING - POSSIBLY OBSOLETE (already!)

# Installation

This repo contains a front end (React), backend (FastAPI) and infrastructure (AWS CDK Python).

Start with a clean python environment containing tox. To illustrate the point,
one way of doing this is:
```commandline
conda create -n msp python=3.13
conda activate msp
pip install tox
tox
```
The above sequence creates a new environment, installs tox, and then uses tox
to build the ```test```, ```lint``` and ```security``` environments. See ```tox.ini```

The virtual environments with all the dependencies installed are in:

```commandline
.tox/test
.tox/lint
.tox/security
```

# Running the Backend
The backend can be run with:
```commandline
source .tox/test/bin/activate
cd backend
uvicorn main:app --reload
```
the ```--reload``` causes the API to be reloaded each time you make a modification.

You can access the API via ``http://localhost:5173``` in your browser.

# Running the Frontend
The frontend can be run with:
```commandline
cd frontend
npm run dev
```
then open ```http://localhost:5173``` in your browser.

The backend and frontend commands both run servers, so you will normally need 
two terminal sessions to keep them running.

# Running AWS CDK
After having completed all the pre-requisites, you can run CDK commands by:
```commandline
source .tox/test/bin/activate
cd infra
cdk <whatever>
```
As with backend and frontend, it may be useful to have a separate console
for CDK commands. So, 3 console windows in total.
