#!/usr/bin/env python

from ansible.module_utils.basic import *
from os.path import expanduser
from ansible_vault import Vault




def main():
    home = expanduser("~")
    failed = False
    fields = {
        "file": {"required": True, "type": "str"},
        "region": {"required": True, "type": "str"},
        "roles" : {"required": True, "type": "list"},
    }

    module = AnsibleModule(argument_spec=fields)
    try:
      file = open(home + "/" + module.params['file'],"r")
      access_key = file.readline().rstrip('\n')
      secret_key = file.readline().rstrip('\n')
      file.close()
      file = open(home + "/" + "passwd/ansible-passwd","r")

      data = {"region": module.params['region'] ,"access_key": access_key, "secret_key": secret_key }

      vault = Vault(file.readline().rstrip('\n'))

      awsconffile = open(home + "/" + ".aws/credentials","w")
      awsconffile.write('[default]\n')
      awsconffile.write('aws_access_key_id = '+access_key+'\n')
      awsconffile.write('aws_secret_access_key= '+secret_key+'\n')
      awsconffile.close()

      awsconffile = open(home + "/" + ".aws/config","w")
      awsconffile.write('[default]\n')
      awsconffile.write('region = '+ module.params['region']+'\n')
      awsconffile.close()




      for role in  module.params['roles']:
          vault.dump(data, open("./roles/"+role+"/vars/vault.yml", "w"))

      response = "Done"

    except:
      response = "Error"
      failed = True

    module.exit_json(changed=False, meta=response, failed=failed)


if __name__ == '__main__':
    main()
