# Introduction

This document is written so you know what Users/Groups there are,
and most importantly, how to setup AWS credentials, so you
can easily push code to the right account.

## AWS Sign-in URL

As mentioned in [Accounts](Accounts.md), you login via a specific
URL and then select the right account to access the given 
environment and console. 

Our URL for My Surgical Plan, looks like the following:

* ```https://d-9c6.......awsapps.com/start/```

However, this gives you web/online access to the console.
But it is easier and better to provision services using
scripts and command line commands, as these are more consistent and
repeatable.

# Users/Groups/Permissions.

Here is a short summary of the setup:

* In the root account lives an [IAM Identity Center](https://aws.amazon.com/iam/identity-center/).
* We have 2 Users, A and B
* We have 2 Groups, Administrators, and Developers
* We have 3 permission sets: AdministratorAccess, PowerUserAccess, ReadOnlyAccess.
* Users are assigned to Groups
* Then for each account, we assign a Group or User and set of Permissions.
* For example on a Sandbox account, the User could have AdministratorAccess, and the DeveloperGroup could have ReadOnlyAccess. This means the specific user will have full control, and anyone in the developer group, read only.

## Command line Logins

Then when deploying infrastructure using CDK, you use the command line. 
First setup sso.

Run:

```commandline
aws configure sso
```
Answer the questions:

* SSO session name (Recommended): e.g. 'My Surgical Plan Limited'
* SSO start URL: The login URL
* SSO region [None]: eu-west-2
* Select account
* Profile name []: Give it a name, e.g. "mysandbox"

(otherwise, accept defaults).

The first time you run a cdk command, you will authenticate which lasts 
about 12 hours, and then behind the scenes, the command line program
is passing temporary keys back/forth for you. So they do not have to be
stored in environment variables, or in text files on the local disk.

Also, if you previously ran commands and used access keys, you may have
a ```~/.aws/credentials```, with a ```[default]``` section. Delete these.
This ```~/.aws/credentials``` file should be empty.

Then when you run a command, you simply specify the profile to run against.

For example:

```commandline
cdk deploy --profile mysandbox
```
