
import yaml
import pathlib

class YmlHelper:
    """YmlHelper class: Helps to read and write yml files."""
    @staticmethod
    def read_yml_file(file_path : pathlib.Path) -> None:
        """Given file path as str it reads yml file."""
        with open(file_path, 'r') as infile:
            fruits_list = yaml.load(infile, Loader=yaml.FullLoader)

        return fruits_list

    @staticmethod
    def write_yml_file(file_path: str, obj: dict) -> None:
        with open(file_path, encoding="utf8", mode="w") as outfile:
            yaml.dump(obj, outfile, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    path = pathlib.Path('./DETECTIONS/YourSmartDetectionName/YourSmartDetectionName.yml')
    print(YmlHelper.write_yml_file(path, {"test": "test"}))