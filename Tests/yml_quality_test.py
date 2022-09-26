import unittest
import yaml, json
from cerberus import Validator

# class HuntExample(unittest.TestCase):

#     def test(self):
#         def load_doc():
#             with open('HUNTS/HuntExample/HuntExample.yml', 'r') as stream:
#                 try:
#                     return yaml.safe_load(stream)
#                 except yaml.YAMLError as exception:
#                     raise exception
#         hunt_schema = 'Tests/schemas/terraform_schema.py'
#         schema = eval(open(hunt_schema, 'r').read())
#         v = Validator(schema)
#         v.allow_unknown = True
#         doc = load_doc()
#         self.result = v.validate(doc, schema)
#         self.assertFalse(bool(v.errors), f'{v.errors}' )


if __name__ == '__main__':
    unittest.main(verbosity=2)