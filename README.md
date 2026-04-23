# Introduction
Prototype web-app for CDI accelerator

# Pre-requisites

1. Install AWS command line interface: [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
2. Ensure command line access to your AWS account: [here](https://catalog.us-east-1.prod.workshops.aws/workshops/10141411-0192-4021-afa8-2436f3c66bd8/en-US/20-prerequisites/40-account)

Specifically for us:

* When you got an email it had a URL like: https://something.awsapps.com/start/
* Click on that link, log in with user username, password, MFA.
* Then you should see a role like SandboxAdmin, as we are playing around in a Sandbox for now.
* Click on "Access Keys" for that role, and you will see methods for setting up environment variables for CLI, or using ```aws configure```

3. Install Node.js. Version should be >= v18.0.0

* Matt: I'm using homebrew, so: ```brew install node``` or ```brew uprgade node```

4. Install IDE of choice. VSCode, Pycharm etc.
5. Install AWS CDK Toolkit: [here](https://catalog.us-east-1.prod.workshops.aws/workshops/10141411-0192-4021-afa8-2436f3c66bd8/en-US/20-prerequisites/70-toolkit)
6. Install Python 3.9 or later. I'm going to assume people are familiar with ```tox```, ```conda```, ```venv``` etc.

# Training

Before getting started with this repo, the following training courses should be completed

1. AWS CDK Workshop: [here](https://catalog.us-east-1.prod.workshops.aws/workshops/10141411-0192-4021-afa8-2436f3c66bd8/en-US)
2. Kiro workshop, or Kiro "Get started" tutorial: [here](https://kiro.dev/docs/)

# Installation

This repo contains a front end (React), backend (FastAPI) and infrastructure (AWS CDK Python).


