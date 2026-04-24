#!/usr/bin/env python3
import aws_cdk as cdk
from lib.org_stack import OrgGovernanceStack

app = cdk.App()

# This stack MUST be deployed to the Management Account
OrgGovernanceStack(app, "SurgicalPlanGovernance",
    env=cdk.Environment(account='YOUR_ROOT_ACCOUNT_ID', region='us-east-1')
)

app.synth()

