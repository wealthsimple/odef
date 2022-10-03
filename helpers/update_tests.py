from fileinput import filename
from jinja2 import Template

import jinja2

class TestWritter:

    def __init__(self, hunt_name: str, unittest_template: Template) -> None:
        self.hunt_name = hunt_name

    def get_template(self, unittest_template):
        """Get the template file """
        # with open(file_location,'r') as f:
        #     self.template_file = f.read()
        self.template_file = unittest_template

    def get_unittest(self, file_location):
        """Get the unittest file """
        with open(file_location,'r') as f:
            self.unittest_file = f.read()
    
    def modify_template(self):
        """Modifies the file using jinja"""
        self.template_file = self.template_file.render({"HuntName":self.hunt_name})

    def modify_tests_file(self):
        """String concat, inserts the new unittests"""
        ready = self.unittest_file[:self.unittest_file.find("if __")] + self.template_file + self.unittest_file[self.unittest_file.find("if __"):]

        return ready
    
    @staticmethod
    def write_modifieid(modified, location):
        """Writes the output file"""
        with open(location, 'w') as f: 
            f.write(modified)

def main(template_writter: TestWritter, test_file: str, unittest_file_location: str) -> None: 
    
    template_writter.get_template(test_file)
    template_writter.get_unittest(unittest_file_location)
    template_writter.modify_template()
    ready = template_writter.modify_tests_file()
    template_writter.write_modifieid(modified=ready,location=unittest_file_location)

if __name__ == "__main__":
    from tf_helper import TfHelper
    import jinja2

    template_file_location = 'yml_test_template.txt'
    unittest_file_location = 'Tests/yml_quality_test.py'
    template_writter = TestWritter("TESTHUNT", jinja2)
    main(template_writter, template_file_location, unittest_file_location)