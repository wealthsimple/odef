import abc 
from abc import abstractmethod
import pathlib

class YmlExporter(abc.ABC):
    """Basic representation of yml exporter."""

    @abstractmethod
    def prepare_export(self, data):
        """Prepares data for exporting."""

    @abstractmethod
    def create_folder(self, folder):
        """Creates a folder if does not exist"""
    
    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the data to a folder."""

class TerraformExporter(abc.ABC):
    """Basic representation of terraform exporter."""

    @abstractmethod
    def prepare_export(self, terraform_data, terragrunt_data):
        """Prepares data for exporting."""

    @abstractmethod
    def create_folder(self, folder):
        """Creates a folder if does not exist"""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the data to a folder."""

class DataCollector(abc.ABC):
    """Basic representation of data collector object"""
    @abstractmethod
    def collector(self) -> dict:
        """Collects answers to the questions"""

class UnittestsYmlExporter(abc.ABC):
    """Basic representation of unittest exporter."""

    @abstractmethod
    def get_template(self, data):
        """Gets the unittest template file"""

    @abstractmethod
    def get_unittest(self, folder):
        """Gets the unittests file"""

    @abstractmethod
    def prepare_tests(self, folder: pathlib.Path):
        """Prepares the new unittest"""

    @abstractmethod
    def modify_tests_file(self, folder: pathlib.Path):
        """Modifies the """

    def write_unittest(self, unittest_file_path: pathlib.Path, new_unittest: dict ):
        """Writes and replaces the old unittest with new one"""

class UnittestsTerraformExporter(abc.ABC):
    """Basic representation of unittest exporter."""

    @abstractmethod
    def get_template(self, data):
        """Gets the unittest template file"""

    @abstractmethod
    def get_unittest(self, folder):
        """Gets the unittests file"""

    @abstractmethod
    def prepare_tests(self, folder: pathlib.Path):
        """Prepares the new unittest"""

    @abstractmethod
    def modify_tests_file(self, folder: pathlib.Path):
        """Modifies the """

    def write_unittest(self, unittest_file_path: pathlib.Path, new_unittest: dict ):
        """Writes and replaces the old unittest with new one"""

class ExporterFactory(abc.ABC):
    """
    Factory that represents a combination of YML and Terraform Exporters.
    The factory doesn't maintain any of the instances it creates.
    """
    @abstractmethod
    def collect_data(self) -> DataCollector:
        """Collects data from questionary to pass over for export"""

    @abstractmethod
    def get_yml_exporter(self) -> YmlExporter:
        """Returns a new Yml exporter belonging to this factory."""

    @abstractmethod
    def get_terraform_exporter(self) -> TerraformExporter:
        """Returns a new Terraform exporter belonging to this factory."""

    @abstractmethod
    def get_unittest_yml_exporter(self) -> UnittestsYmlExporter:
        """Returns a Terraform exporter belonging to this factory."""

    @abstractmethod
    def get_unittest_terraform_exporter(self) -> UnittestsTerraformExporter:
        """Returns a Terraform exporter belonging to this factory."""
