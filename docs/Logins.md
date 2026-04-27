# Introduction

This document is written so you know what Users/Groups there are,
and most importantly, how to setup AWS credentials, so you
can easily send commands and deploy to the right account.

# AWS Sign-in URL

As mentioned in [Accounts](Accounts.md), you login via a specific
URL and then select the right account to access the given 
environment and AWS console. 

Our URL for My Surgical Plan, looks like the following:

* ```https://d-9c6.......awsapps.com/start/```

However, this gives you web/online access to the console.
But it is easier and better to provision services using
scripts and command line commands, as these are more consistent and
repeatable.

# IAM versus IAM Identity Center

There are two AWS services with confusingly similar names.

* AWS Identity and Access Management (IAM) - this used to be for all accounts. Now think of it as just for robot accounts, service level accounts.
* AWS IAM Identity Center - successor to AWS SSO. Used to manage users, groups and permissions.

So, users and groups are configured using the "IAM Identity Center", whereas things like an
Amplify service account that needs to deploy somewhere will have permissions set using IAM.

# Users/Groups/Permissions.

Here is a short summary of the setup:

* In the root account lives an [IAM Identity Center](https://aws.amazon.com/iam/identity-center/).
* We have 2 Users, A and B
* We have 2 Groups, Administrators, and Developers
* We have 3 permission sets: AdministratorAccess, PowerUserAccess, ReadOnlyAccess.
* Users are assigned to Groups
* Then for each account, we assign a Group or User and set of Permissions.
* For example on a Sandbox account, the User could have AdministratorAccess, and the DeveloperGroup could have ReadOnlyAccess. This means the specific user will have full control, and anyone in the developer group, read only.

# Configuring Command Line Sign On

Then when deploying infrastructure using CDK, you use the command line. 
First setup sso.

Run:

```commandline
aws configure sso
```
Answer the questions:

* SSO session name: e.g. 'MySurgicalPlanLimited'. Do not put spaces.
* SSO start URL: The login URL provided with your account.
* SSO region: eu-west-2, which is London.
* Select account, and repeat this process for each of your accounts
* Profile name []: Give it a name, e.g. "mysandbox", or "dev"

(otherwise, accept defaults).

Behind the scenes, the command line program
is passing temporary keys back/forth for you. So they do not have to be
stored in environment variables, or in text files on the local disk.

Also, if you previously ran commands for tutorials and used access keys, you may have
a ```~/.aws/credentials```, with a ```[default]``` section. Delete these.
This ```~/.aws/credentials``` file should be empty.

# Logging in on the Command Lin

Once configured, you need to login:

```commandline
aws sso login --profile dev
```

Then when you run a command, you simply specify the profile to run against.

For example:

```commandline
cdk deploy --profile dev
```

or you can set an environment variable.

```commandline
export AWS_PROFILE=dev
```

Verify you are accessing the dev account:

```commandline
aws sts get-caller-identity
```

# Boot strapping

Before CDK can deploy anything to an account, you need to bootstrap it.

```commandline
npx cdk bootstrap aws://ACCOUNT_ID/REGION --profile dev
```
for example, get the account ID from the AWS console, and look at
the list of servers, e.g. eu-west-2 is London.

```commandline
npx cdk bootstrap aws://123456789/eu-west-2 --profile dev
```

# Other commands:

* Check identity: ```aws sts get-caller-identity --profile dev```
* Check bootstrap status: ```aws cloudformation describe-stacks --stack-name CDKToolkit --profile dev```