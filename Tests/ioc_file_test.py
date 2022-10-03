import unittest
import yaml, json
from cerberus import Validator

class IOCFileValidation(unittest.TestCase):

    def test(self):
        def load_doc():
            with open('./IOCs/IOC_Library.yml', 'r') as stream:
                try:
                    return yaml.safe_load(stream)
                except yaml.YAMLError as exception:
                    raise exception
        doc = load_doc()
        schema = eval(open('Tests/schemas/ioc_schema.py', 'r').read())
        v = Validator(schema)
        v.allow_unknown = True
        if len(doc.get('IOC_List',[]))==0:
            assert self.result is False
        for i in doc.get('IOC_List'): 
            self.result = v.validate(i, schema)
        self.assertFalse(bool(v.errors), f'{v.errors}' )

if __name__ == '__main__':
    unittest.main()