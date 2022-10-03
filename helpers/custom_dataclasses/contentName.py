from dataclasses import dataclass
from re import sub 

@dataclass
class ContentName:
    """Class that modifies object"""
    given_name: str

    def convert_case(self):
        """Replaces special chars and returns title case word"""
        string_in_camel = sub(r"(\W|_)+", " ", self.given_name).title().replace(" ", "")
        return ''.join(string_in_camel)