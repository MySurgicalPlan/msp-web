# Introduction

This document is written, to speed up the understanding of our AWS account,
where to log into, and how that affects what we do.

# Multi-Account Setup

We use a Multi-Account strategy from Day 1. See this example [here](https://aws.amazon.com/blogs/mt/multi-account-strategy-for-small-and-medium-businesses/).
This means, we have 1 root account, where all billing details are held,
and then a sub-division of Organisational Units (OU) and within each OU, 
1 or more accounts or OUs. This is so that any security or configuration settings can
be placed at the appropriate point in the organisational chart, and it will
propagate to all structures below it.

# Logging In

## The root account

The root account is used to bootstrap the AWS org-chart. This root account
then holds an [IAM Identity Centre](https://aws.amazon.com/iam/?trk=40032cd2-744c-4b2c-ad0c-cf60894e0921&sc_channel=ps&ef_id=Cj0KCQjwkrzPBhCqARIsAJN460mBN6BHbklBtFHFkKebfoMelUI7unalfN84Mfm5VIY-rFDSyZRQaLAaAg_cEALw_wcB:G:s&s_kwcid=AL!4422!3!795811958070!p!!g!!iam!23528572748!198422384371&gad_campaignid=23528572748&gbraid=0AAAAADjHtp-e0Dt3OKhoMayN05jvqKVve&gclid=Cj0KCQjwkrzPBhCqARIsAJN460mBN6BHbklBtFHFkKebfoMelUI7unalfN84Mfm5VIY-rFDSyZRQaLAaAg_cEALw_wcB).
The IAM Identity Centre is used to create users, groups and permission sets. 
Once an administrative group has been created, and given permissions to create 
and provision all other things on AWS, then the root user is almost never required.
We mention it specifically here, so that all users know they should NOT be using the root account.

## AWS Console Page

If you Google for AWS Console Login, you get to [here](https://aws.amazon.com/console/).
There are options for logging in using:

* Root user email - this works, and is how the root user can login.
* IAM Account ID and IAM username - this should **not** be used it is only for **legacy** user accounts.

The correct way to login is via a specific URL, provided with your new
user account.

## AWS Sign-in URL

When the administrator creates a new user account, the new user email 
is sent to the user, with a login URL. Bookmark this URL. Bookmark this URL exactly, 
not any URL with context or session specific identifiers on it, as these will expire.
This is how you login. The first time, click "Forgot password", as you won't have
a password set, then create password, and your choice of MFA. 
When you login, you will see the "AWS access portal", 
which shows all the accounts you can log into. 
Select 1 of these accounts and continue. You will have the priviledges
assigned for you, according to your user/group for that specific account.
For example, on your Sandbox account, you will likely be administrator,
but on the Production account, you could be read-only.

Our URL for My Surgical Plan, looks like the following:

* ```https://d-9c6.......awsapps.com/start/```


To switch between accounts, specifically sign out, and sign back in again as the new role.

# AWS Structure

Note: This will be modified, and tidied up before the end of the 12-week period.
Im just documenting this now, so we understand it.  We then need to setup Amplify so 
that when you merge code to main/test/dev, the corresponding account gets redeployed.

We have the following structure:

```commandline
root - My Surgical Plan Limited
  - OU: Security
    - Account: Log archive
    - Account: Aggregator account
  - OU: Infrastructure
  - OU: Workloads
    - OU: Dev
      - Account: dev
    - OU: Test
      - Account: test
    - OU: Prod
      - Account: prod
  - OU: Sandbox
    - Account: Sandbox 1
    - Account: Sandbox 2
    - Account: Sandbox 3
    - Account: Sandbox 4
```
The reason for having OU for Dev, Test, Prod, and then accounts under that
is because we may eventually have multiple applications, or provision
multiple accounts for testing, and we can ensure they are all configured
the same, and you may need different configuration for Dev/Test/Prod.

For now, both developers should work in their own sandbox.

# Note: Sandboxes withing Sandboxes

A developer can work with one of the above Sandbox accounts, and use it like
any other account, e.g. dev/test/prod.

When you are doing a tutorial, you may see commands
like: 
```commandline
cdk deploy --profile sandbox
```
and you are creating/destroying infrastructure within your sandbox account.
So far so good. 

However, things get more complicated when you are using Amplify. Amplify is 
typically setup to link git branches to accounts. Then a build is triggered
when the git branch is updated. So, you typically might have
git branches dev/test/prod, and setup Amplify to build 3 separate environments.

However, if you are doing a tutorial, and you setup Amplify, and you link
a git repo to your Sandbox account, and then come across commands like:

```commandline
npx ampx sandbox
```
what is this?

This creates an additional ```sandbox``` within whatever account you were logged into.
If the **account** you were connected to is called sandbox, you now have a sandbox within a sandbox.

What this does is creates a copy of all your services, with a certain unique set of identifiers
and also creates a local ```amplify_outputs.json``` which is a local file, in the directory of the
where you ran the ```npx ampx sandbox``` command, which gives all the URLS and keys to
login and connect to the temporary sandbox. Secondly, this sets up a watcher, (i.e. the command
itself is a long running command that monitors the local file system for changes and triggers
infrastructure updates).

All this means you can have 1 terminal running the web server (i.e. ```npm run dev```),
and this command ```npx ampx sandbox``` which creates a temporary backend for the 
website to run against. 

When you Ctrl-C the ```npx ampx sandbox``` command, the watcher will exit, but the 
infrastructure will remain. Use the following command to tidy up:

```commandline
npx ampx sandbox delete
```
So, yes, you can have a sandbox within a sandbox. One set of resources is updated in real-time 
by the watcher. The other set will only be updated when you commit back to the git branch.
