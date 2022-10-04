# Open Detection Engineering Framework Repo 

## Purpose 
This is a template repository, it can be forked and customized to the needs of the organization. The repository provides the framework concepts and the adaptation is normally tailored based on the needs. In some cases, there could be integration with ci/cd pipelines in other cases it can be used to only document and store security content. 

## Important links
[Open Detection Engineering Framework](Docs/ODEF-README.md)\
[ODEF Detection Template](templates/documentation_template.md)\
[ODEF Detection YML](templates/alert_template.yml)\
[ODEF Hunt YML](templates/hunt_template.yml)\
[Example Detection](DETECTIONS/DetectionExample/detection_example.yml)

## How to Install and Run the Project
* Fork the repository

* Clone it locally to your development machine 

* Next, create virtual virtual environment
```bash 
virtualenv venv 
```
Or if you don't use virtualenv
```bash 
python3 -m venv {name of venv}
```
[More information on venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
* Activate your virtual environment 
```bash 
source venv/bin/activate
```
* Then install the requirements 
```bash 
pip install -r requirements.txt
```

* Run the python app 
```bash 
python main.py
```
* Follow the process and once completed ensure that all files are present and your detection is well documented

## How to contribute
TBD

## Project Folder Structure
*There are several folders that are important in the project and will be explained below*
#### <u>Folders</u>
<p align="justify">
<ol>
<li>Root folder - Contains the project and number of helper files.</li>
<li>HUNTS - Subfolder under this folder are meant to organize and contain complex hunts.</li>
<li>DETECTIONS - The folder where all detections are organized. Each detection should have a subfolder containing.</li>
<li>IOC - The folder where indicators of compromise are stored.</li>
<li>Tests - Standard folder for storing unittest.</li>
<li>MitreMap - Contains a file used to report TTPs that have been covered.</li>
<li>screenshots - Storing screenshots or other artefact that are to be displayed as part of documentation.</li>
<li>DataDictionary - Storing data dictionaries for different data sets and indexes that are utilized.</li>
<li>Docs - Contains documentation related to ODEF</li>
</ol>
</p>