{
    'actor': {
        'required': True,
        'type': 'string'
    },
    'reporter': {
        'required': True,
        'type': 'string'
    },
    'sha1_hashes': {
        'required': False,
        'type': 'list'
    },
    'sha256_hashes': {
        'required': False,
        'type': 'list'
    },
    'md5_hashes': {
        'required': False,
        'type': 'list'
    },
    'domains': {
        'required': False,
        'type': 'list'
    },
    'ip_addresses': {
        'required': False,
        'type': 'list'
    },
    'incident':{
        'required': True,
        'type': 'dict',
        'schema':{
            'name':{'type': 'string', 'required': True, 'minlength': 5},
            'type':{'type': 'string', 'required': True, 'allowed':['Security - IOC_Hit']},
            'description':{'type': 'string', 'required': True, 'minlength': 10},
            'severity':{'type': 'integer', 'required': True, 'allowed':[0,0.5,1,2,3,4]},
            'sla':{'type': 'integer', 'required': True},
        }
    }
}