import yaml 
from enum import Enum
import os
import questionary 
from jinja2 import Template
from helpers.yml_helpers import YmlHelper
from helpers.file_helper import FileHelper
from helpers.custom_questions.local_questionery import ContentQuestions
from helpers.abstract.abstract_classes import *
from helpers.custom_exceptions.custom_exceptions import DirExist



class DetectionFileExporter(Exporter):
    """Exports the provided DETECTION information to a YML file """

    def prepare_export(self, data_to_export: dict, template_file: Template, doc_template: Template) -> None:
        print("Preparing DETECTION data for YML export.")

        self.output_from_parsed_template = template_file.render(data_to_export)
        self.doc_output = doc_template.render(data_to_export)
        self.output_from_parsed_template = yaml.safe_load(self.output_from_parsed_template)
        
    def create_folder(self, dirName):
        """Creates a folder if does not exist"""
        
        print("Create folder for DETECTION YML file")

        path = os.path.join('DETECTIONS', dirName)
        if not os.path.exists(path):
            os.mkdir(path=path)
            print("Directory " , dirName ,  " Created ")
        else:    
            # print("Directory " , dirName ,  " already exists")
            raise DirExist(f"Directory with the same name '{dirName}' already exists")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting DETECTION data to YML file to {folder}.")
        path = os.path.join('./','DETECTIONS', folder, folder.split("/")[1] + '.yml')
        YmlHelper.write_yml_file(path, self.output_from_parsed_template)
        md_path = os.path.join('./','DETECTIONS', folder, folder.split("/")[1] + '.md')
        FileHelper.writeTfFile(md_path, self.doc_output)

class HuntFileExporter(Exporter):
    """Exports the provided Hunt information to a YML file """

    def prepare_export(self, data_to_export:dict, template_file: Template, doc_template: Template) -> None:
        print("Preparing HUNT data for YML export.")
        self.output_from_parsed_template = template_file.render(data_to_export)
        self.doc_output = doc_template.render(data_to_export)
        self.output_from_parsed_template = yaml.safe_load(self.output_from_parsed_template)

    def create_folder(self, dirName):
        """Creates a folder if does not exist"""
        print("Create folder for HUNT YML file")

        path = os.path.join('HUNTS', dirName)
        if not os.path.exists(path):
            os.mkdir(path=path)
            print("Directory " , dirName ,  " Created ")
        else:    
            print("Directory " , dirName ,  " already exists")
            raise DirExist(f"Directory with the same name '{dirName}' already exists")
    
    def do_export(self, folder: pathlib.Path):
        print(f"Exporting HUNT data to YML file to {folder}.")
        path = os.path.join('HUNTS', folder.name, folder.name + '.yml')
        YmlHelper.writeYmlFile(path, self.output_from_parsed_template)
        md_path = os.path.join('HUNTS', folder.name, folder.name + '.md')
        FileHelper.writeTfFile(md_path, self.doc_output)

class DetectionDataCollector(DataCollector):
    """Data collector using DETECTION questions schema to collect"""

    def collector(self, Questions) -> dict:
        print("Collection DETECTION data")
        return questionary.prompt(Questions.get_questions_detection(), style=Questions.custom_style_fancy)

class HuntDataCollector(DataCollector):
    """Data collector using HUNT questions schema to collect """

    def collector(self, Questions) -> dict:
        print("Collecting Hunt Data")
        return questionary.prompt(Questions.get_questions_hunt(), style=ContentQuestions.custom_style_fancy)

class UnittestsHuntYmlExporter(UnittestsYmlExporter):
    """Concrete implementation"""
    def __init__(self, content_name: str, unittest_template_name: str, unittest_file_path: str) -> None:
        self.content_name = content_name
        self.unittest_template_name = unittest_template_name
        self.yml_unittest_file_path = 'Tests/yml_quality_test.py'
        self.terraform_unittest_file_path = 'Tests/terraform_quality_test.py'

    def get_template(self):
        """Get the template file """

        self.template_file =  FileHelper.load_template(self.unittest_template_name)
       

    def get_unittest(self):
        """Get the unittest file """
        with open(self.unittest_file_path,'r') as f:
            self.unittest_file = f.read()
    
    def prepare_tests(self):
        """Modifies the file using jinja"""
        self.template_file = self.template_file.render({"HuntName":self.content_name})

    def modify_tests_file(self):
        """String concat, inserts the new unittests"""
        self.modified_unittest_content = self.unittest_file[:self.unittest_file.find("if __")] + self.template_file + self.unittest_file[self.unittest_file.find("if __"):]

    def write_unittest(self):
        """Writes the output file"""
        with open(self.unittest_file_path, 'w') as f: 
            f.write(self.modified_unittest_content)

class UnittestsDetectionYmlExporter(UnittestsYmlExporter):
    """Concrete implementation"""
    def __init__(self, content_name: str, unittest_template_name: str, unittest_file_path: str) -> None:
        self.content_name = content_name
        self.unittest_template_name = unittest_template_name
        self.yml_unittest_file_path = 'Tests/yml_quality_test.py'
        self.terraform_unittest_file_path = 'Tests/terraform_quality_test.py'

    def get_template(self):
        """Get the template file """

        self.template_file =  FileHelper.load_template(self.unittest_template_name)
       

    def get_unittest(self):
        """Get the unittest file """
        with open(self.unittest_file_path,'r') as f:
            self.unittest_file = f.read()
    
    def prepare_tests(self):
        """Modifies the file using jinja"""
        self.template_file = self.template_file.render({"HuntName":self.content_name})

    def modify_tests_file(self):
        """String concat, inserts the new unittests"""
        self.modified_unittest_content = self.unittest_file[:self.unittest_file.find("if __")] + self.template_file + self.unittest_file[self.unittest_file.find("if __"):]

    def write_unittest(self):
        """Writes the output file"""
        with open(self.unittest_file_path, 'w') as f: 
            f.write(self.modified_unittest_content)

class DetectionExporter(ExporterFactory):
    """Factory for exporting Detections to YML and Terraform"""

    def collect_data(self) -> DetectionDataCollector:
        return DetectionDataCollector()

    def get_exporter(self) -> DetectionFileExporter:
        """Returns a YML exporter belonging to this factory."""
        return DetectionFileExporter()
  
    def get_unittest_yml_exporter(self) -> UnittestsYmlExporter:
        """Returns a Terraform exporter belonging to this factory."""
        return UnittestsDetectionYmlExporter()
    
class HuntExporter(ExporterFactory):
    """Factory for exporting HUNT to YML and Terraform"""
    
    def collect_data(self) -> HuntDataCollector:
        return HuntDataCollector()

    def get_exporter(self) -> HuntFileExporter:
        """Returns a YML exporter belonging to this factory."""
        return HuntFileExporter()
    
    def get_unittest_yml_exporter(self) -> UnittestsYmlExporter:
        """Returns a Terraform exporter belonging to this factory."""
        return UnittestsHuntYmlExporter()

class ContentType(Enum):
    DETECTION =  DetectionExporter()
    HUNT =  HuntExporter() 

class TemplateType(Enum):
    DETECTION = ["alert-template.yml", "documentation-template.md"]
    HUNT = ["hunt-template.yml","documentation-template.md"]
