from aws_cdk import (
    Stack,
    aws_organizations as orgs
)
from constructs import Construct

class OrgGovernanceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Retrieve Root ID from context (or hardcode)
        root_id = self.node.try_get_context("org_root_id")

        # --- Level 1: Main Business OU ---
        surgical_plan_ou = orgs.CfnOrganizationalUnit(self, "SurgicalPlanOU",
            name="My Surgical Plan Limited",
            parent_id=root_id
        )

        # --- Level 2: Functional OUs ---
        infra_ou = orgs.CfnOrganizationalUnit(self, "InfraOU",
            name="Infrastructure",
            parent_id=surgical_plan_ou.attr_id
        )

        security_ou = orgs.CfnOrganizationalUnit(self, "SecurityOU",
            name="Security",
            parent_id=surgical_plan_ou.attr_id
        )

        workloads_ou = orgs.CfnOrganizationalUnit(self, "WorkloadsOU",
            name="Workloads",
            parent_id=surgical_plan_ou.attr_id
        )

        # --- Level 3: Security Accounts ---
        orgs.CfnAccount(self, "LogArchive",
            account_name="Log archive",
            email="aws-logs@mysurgicalplan.com",
            parent_ids=[security_ou.attr_id]
        )

        orgs.CfnAccount(self, "Aggregator",
            account_name="Aggregator account",
            email="aws-aggregator@mysurgicalplan.com",
            parent_ids=[security_ou.attr_id]
        )

        # --- Level 3: Workload Environments (Nested OUs) ---
        dev_parent_ou = orgs.CfnOrganizationalUnit(self, "DevParentOU",
            name="Development",
            parent_id=workloads_ou.attr_id
        )
        
        test_parent_ou = orgs.CfnOrganizationalUnit(self, "TestParentOU",
            name="Testing",
            parent_id=workloads_ou.attr_id
        )

        prod_parent_ou = orgs.CfnOrganizationalUnit(self, "ProdParentOU",
            name="Production",
            parent_id=workloads_ou.attr_id
        )

        # --- Level 4: Workload Accounts ---
        orgs.CfnAccount(self, "DevAccount",
            account_name="dev",
            email="aws-dev@mysurgicalplan.com",
            parent_ids=[dev_parent_ou.attr_id]
        )

        orgs.CfnAccount(self, "TestAccount",
            account_name="test",
            email="aws-test@mysurgicalplan.com",
            parent_ids=[test_parent_ou.attr_id]
        )

        orgs.CfnAccount(self, "ProdAccount",
            account_name="prod",
            email="aws-prod@mysurgicalplan.com",
            parent_ids=[prod_parent_ou.attr_id]
        )

