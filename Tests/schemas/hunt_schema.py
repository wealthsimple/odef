{
    'xsoar_status': {
        'required': True,
        'type': 'string',
        'allowed':['sunrise','midday','sunset']
    },
    'schedule': {
        'required': True,
        'type': 'string'
    },
    'baseline': {
        'required': False,
        'type': ['string', 'list']
    },
    'visualization': {
        'required': False,
        'type': ['string', 'list']
    },
    'event_limit': {
        'required': True,
        'type': 'integer'
    },
    'data_source': {
        'required': True,
        'type': 'string'
    },
    'mitre_id': {
        'required': True,
        'type': 'string'
    },
    'query':{
        'required': True,
        'type': 'string'
    },
    'data_location':{
        'required': True,   
        'type': 'string',
        'allowed': ['splunk','sentinelOne','elasticsearch']
    },
    'mitre_url':{
        'required': False,   
        'type': 'string'
    },
    'tactic':{
        'required': False,   
        'type': 'string',
        'allowed':['Reconnaissance','Resource Development','Initial Access','Execution','Persistence','Privilege Escalation','Defense Evasion','Credential Access','Discovery','Lateral Movement','Collection','Command and Control','Exfiltration','Impact']
    },
    'incident':{
        'required': True,
        'type': 'dict',
        'schema':{
            'name':{'type': 'string', 'required': True, 'minlength': 5},
            'type':{'type': 'string', 'required': True, 'allowed':['Security - Incident']},
            'description':{'type': 'string', 'required': True, 'minlength': 10},
            'severity':{'type': 'integer', 'required': True, 'allowed':[0,0.5,1,2,3,4]},
            'sla':{'type': 'integer', 'required': True}
        }
    },
}

