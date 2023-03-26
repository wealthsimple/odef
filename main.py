import pathlib
from typing import Dict, Any, Type
import questionary
import os, sys
import yaml
from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum
from jinja2 import Template

from helpers.file_helper import FileHelper
from helpers.update_coverage import update_coverage
from helpers.update_dep_tree import update_dep_tree
from helpers.yml_helpers import YmlHelper
from helpers.update_tests import TestWritter

from helpers.abstract.abstract_classes import *
from helpers.abstract.concrete_classes import * 
from helpers.custom_dataclasses.contentName import ContentName

def read_factory(detection_type: Dict[str, Any], type_object: Type[Enum]) -> Type[ExporterFactory]:
    """Constructs an exporter factory based on the user's preference."""

    for name in type_object:
        if name.name == detection_type.get("product", "").upper():
            return name.value


def load_config(path:pathlib.Path) -> dict:
    """Loads config file"""
    config_obj = YmlHelper.read_yml_file(path)
    return config_obj
        
def main(fac:ExporterFactory, custom_config: dict) -> None:
    """Main function."""
    
    # retrieve the exporters
    data_collector = fac.collect_data()
    exporter = fac.get_exporter()

    #collect data 
    # data = data_collector.collector(ContentQuestioner) # TODO remove the line below and uncomment this one
    data = {'detection_kind': 'endpoint', 'detection_name': 'YourSmartDetectionName', 'detection_author': '', 'description': '', 'query': 'index= ...', 'data_source': '', 'baseline': 'server!=server1000, ....1.1.1 ...', 'visualization': '| table ...', 'mitre_id': 'T1003.002', 'mitre_url': 'https://attack.mitre...TXXXX.XXX/', 'status': 'sunrise', 'tactic': 'Reconnaissance', 'schedule': '*/5 * * * *'}
    #prepare data
    content_name = ContentName(data.get("detection_name"))
    content_name = content_name.convert_case()
    data["detection_name"] = content_name

    #load templates
    yml_file_name=read_factory(prompt_answer, TemplateType).get('yml_file')
    md_temp_file_name = read_factory(prompt_answer, TemplateType).get('md_file')
    yml_template = FileHelper.load_template(file_name=yml_file_name)
    md_temp = FileHelper.load_template(file_name=md_temp_file_name)

    # prepare the export
    exporter.prepare_export(data, yml_template, md_temp)
    sub_folder = pathlib.Path(content_name)
    folder = pathlib.Path(custom_config.get("tactic_to_folder").get(data.get("tactic")) +"/"+sub_folder.name)
    #Create folder

    exporter.create_folder(folder)

    # do the export
    exporter.do_export(str(folder))

    # write unittests
    # unittest_writer_yml = fac.get_unittest_yml_exporter()
    # # unittest_writer = unittest_writer_yml(content_name=content_name, 
    # #                                     unittest_file_location=read_factory(detection_type, TemplateType)[0],              
    # #                                     unittest_template=read_factory(detection_type, TemplateType)[0]
    # #                                     )

    # unittest_template = TfHelper.load_template("yml_test_template.txt")
    # unittest_file_location = 'Tests/yml_quality_test.py'
    

    # template_writter = TestWritter(content_name, unittest_template=unittest_template)
    # template_writter.get_template(unittest_template)
    # template_writter.get_unittest(unittest_file_location)
    # template_writter.modify_template()
    # ready = template_writter.modify_tests_file()
    # template_writter.write_modifieid(modified=ready,location=unittest_file_location)
    

    # update coverage
    update_coverage()

    # update deptree
    update_dep_tree()


if __name__ == "__main__":
    # load config 
    conf = load_config('config/config.yml')
    ContentQuestioner = ContentQuestions(conf)
    #collect detection type 
    prompt_answer = questionary.prompt(ContentQuestioner.entry_question(),
                                        style=ContentQuestioner.custom_style_fancy,
                                        )

    # create the factory
    factory = read_factory(prompt_answer, ContentType)

    # perform the exporting job
    main(factory, conf)
