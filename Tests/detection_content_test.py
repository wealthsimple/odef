import unittest
import pathlib as pl
import glob, os

class TestCaseBase(unittest.TestCase):
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

class CheckForReadme(TestCaseBase):
    def get_folders(self):
        everything = glob.glob("./DETECTIONS/*")
        folders = [i for i in everything if "md" not in i]
        return folders
    
    def test(self):
        paths = self.get_folders()
        for path in paths: 
            path = pl.Path(path+"/readme.md")
            self.assertIsFile(path)

# class CheckForTerragruntHCL(TestCaseBase):
#     def get_folders(self):
#         everything = glob.glob("./DETECTIONS/*")
#         folders = [i for i in everything if "md" not in i]
#         return folders
    
#     def test(self):
#         paths = self.get_folders()
#         for path in paths: 
#             path = pl.Path(path+"/terragrunt.hcl")
#             self.assertIsFile(path)
           
if __name__ == '__main__':
    unittest.main()