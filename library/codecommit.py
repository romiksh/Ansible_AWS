#!/usr/bin/env python

from ansible.module_utils.basic import *
import boto3


def main():

    fields = {
        "aws_access_key": {"required": True, "type": "str"},
        "aws_secret_key": {"required": True, "type": "str"},
        "region": {"required": True, "type": "str"},
        "repo_name": {"required": True, "type": "str"},
        "repo_disc": {"required": False, "type": "str"},
        "create": {"required": False, "type": "bool", "default":False},
    }

    module = AnsibleModule(argument_spec=fields)

    client = boto3.client('codecommit',
                          aws_access_key_id=module.params['aws_access_key'],
                          aws_secret_access_key=module.params['aws_secret_key'],
                          region_name=module.params['region'],
                          )

    try:
        response = client.get_repository(
            repositoryName=module.params['repo_name'],
        )
    except:
        if module.params['create'] == True:
             response = client.create_repository(
               repositoryName=module.params['repo_name'],
               repositoryDescription=module.params['repo_disc']
             )

    module.exit_json(changed=False, meta=response)


if __name__ == '__main__':
    main()
