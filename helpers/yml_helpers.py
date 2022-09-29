
import yaml
import pathlib

class YmlHelper:
    """YmlHelper class: Helps to read and write yml files."""
    @staticmethod
    def readYmlFile(file_path : pathlib.Path) -> None:
        """Given file path as str it reads yml file."""
        with open(file_path, 'r') as infile:
            fruits_list = yaml.load(infile, Loader=yaml.FullLoader)

        return fruits_list

    @staticmethod
    def writeYmlFile(file_path : pathlib.Path, obj : dict) -> None:
        """Given path as a str and dictionary object it writes to YML file format"""
        with open(file_path, 'w') as outfile:
            yaml.dump(obj, outfile, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    path = pathlib.Path('DETECTIONS/DetectionExample/detection_example.yml')
    print(YmlHelper.readYmlFile(path))