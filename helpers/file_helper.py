from dataclasses import dataclass
from jinja2 import Environment, FileSystemLoader, Template
import os, re 
import pathlib

class FileHelper:
     
    @staticmethod
    def readTfFile(file_path : pathlib.Path) :
        """Given a path reads the file and returns read object"""
        with open(file_path, 'r') as infile:
            return infile

    @staticmethod
    def writeTfFile(file_path : pathlib.Path, obj : dict) -> None:
        
        with open(file_path, 'w') as fh:
            fh.write(obj)
    
    @staticmethod
    def load_template(file_name, template_folder='templates') -> Template:
        """Loads and returns jinja template"""
        env = Environment(loader=FileSystemLoader(template_folder))
        template = env.get_template(file_name)

        return template


if __name__ == "__main__":
    tf = FileHelper()
    temp = tf.load_template('alert-template.yml')
    print(temp)