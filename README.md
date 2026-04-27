All code in this repository is 
copyright (c) 2026 My Surgical Plan Limited. All rights reserved.

# Introduction
Prototype web-app for CDI accelerator.

# Pre-requisites

1. Install Python 3.9 or later. I'm going to assume people are familiar with ```tox```, ```conda```, ```venv``` etc.
2. Install AWS command line interface: [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
3. Install Node.js. Version should be >= v18.0.0
* Matt: I'm using homebrew, so: ```brew install node``` or ```brew uprgade node```
4. Install nvm: ```curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash```
5. ```nvm install 22```
6. ```nvm use 22```
7. Install IDE of choice. Kiro, VSCode, Pycharm etc.
8.  Install AWS CDK Toolkit: [here](https://catalog.us-east-1.prod.workshops.aws/workshops/10141411-0192-4021-afa8-2436f3c66bd8/en-US/20-prerequisites/70-toolkit)

# Account Access

* When you got an email it had a URL like: https://something.awsapps.com/start/
* Click on that link. If first time, select "Forgot password" to setup a new password and MFA.
* Log in with user username, password, MFA.
* Then you should see a list of Account Name and Account ID that you have been assigned.
* Expand each Account Name, and you will see each role for each account that you have been assigned.
* You will also see "Access keys". These access keys enable you to log in. **They must not be checked into any git repo.**
* If you click on one of the roles, you will be taken to AWS Console, for that account and using that role.
* If you want to switch accounts/roles, sign out, and sign back in again.

# Further reading

While "logging into your Amazon account" sounds easy, we are running a multi-account
setup. So you need to understand how to authenticate, how to connect to the right account
and how to deploy to the right account. Please read the following:

* [Logins](docs/Logins.md)
* [Accounts](docs/Accounts.md)

