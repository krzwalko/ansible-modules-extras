#!/usr/bin/python

DOCUMENTATION = '''
---
module: netapp
short_description: Manage ONTAP netapp volumes
description:
    - Create a volume on ONTAP netapp storage
version_added: 2.2
author: "Krzysztof Walkowicz (@krzwalko)"
notes:
    - Testing on ONTAP x.x
requirements:
    - NetAapp
options:
    server:
        description:
            - Storage server to create a volume
        required: True
        default: None
'''

def main():
    module = AnsibleModule(
        argument_spec=dict(
            server=dict(required=True§)
        )
    )

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
