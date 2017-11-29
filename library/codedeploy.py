#!/usr/bin/env python

from ansible.module_utils.basic import *
import boto3


def main():
    fields = {
        "aws_access_key": {"required": True, "type": "str"},
        "aws_secret_key": {"required": True, "type": "str"},
        "region": {"required": True, "type": "str"},
        "cd_name": {"required": True, "type": "str"},
        "cd_goup_name": {"required": True, "type": "str"},
        "ec2_name": {"required": True, "type": "str"},
        "iam_name": {"required": True, "type": "str"},
    }

    module = AnsibleModule(argument_spec=fields)

    iam = boto3.resource('iam',
                         aws_access_key_id=module.params['aws_access_key'],
                         aws_secret_access_key=module.params['aws_secret_key'],
                         )
    role = iam.Role(module.params['iam_name'])


    client = boto3.client('codedeploy',
                          aws_access_key_id=module.params['aws_access_key'],
                          aws_secret_access_key=module.params['aws_secret_key'],
                          region_name=module.params['region'],
                          )

    response = client.create_application(
    applicationName=module.params['cd_name']
    )

    response = client.create_deployment_group(
    applicationName=module.params['cd_name'],
    deploymentGroupName=module.params['cd_goup_name'],
    ec2TagFilters=[
        {
            'Key': 'Name',
            'Value': module.params['ec2_name'],
            'Type': 'KEY_AND_VALUE'
        },
    ],
    serviceRoleArn=role.arn,
)

    module.exit_json(changed=False, meta=response)

if __name__ == '__main__':
    main()
