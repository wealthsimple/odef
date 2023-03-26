# Open Detection Engineering Framework Repo

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/wealthsimple/odef?color=green)
![GitHub Release Date](https://img.shields.io/github/release-date/wealthsimple/odef)
![GitHub contributors](https://img.shields.io/github/contributors/wealthsimple/odef?color=teal)
![GitHub pull requests](https://img.shields.io/github/issues-pr/wealthsimple/odef)
![GitHub last commit](https://img.shields.io/github/last-commit/wealthsimple/odef?color=orange)

## Purpose

This is a template repository, it can be forked and customized to the needs of your organization. The repository provides the framework concepts and the adaptation is normally tailored based on the specific requirements. In some cases, there could be integration with ci/cd pipelines in other cases it can be used to only document and store security content and enable and promote knowledge sharing.

## Goals

1. The goal of the repository is to become a central security content knowledge management base where the content is stored, organized, shared, and interacted with.  
2. The goal of the python application is to assist with the process of detection documentation and can be extended to run unittests, quality checks, and more.
3. The repository also hosts the open detection engineering framework which can be used as a reference to tailor and craft internal processes accordingly.

## Important links

[Start here -> Open Detection Engineering Framework](Docs/ODEF-README.md)\
[ODEF Detection Template](templates/documentation-template.md)\
[ODEF Detection YML](templates/alert-template.yml)\
[ODEF Hunt YML](templates/hunt-template.yml)\
[Example Detection](DETECTIONS/DetectionExample/detection-example.yml)

## How to Install and Run the Project

* Use the template to create a new repository under your organization

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

There are two ways to contribute to the repository and the community. Via discussions where you can raise topics of interest that will help the detection engineering community or by submitting issues or PRs to push your change to the repository.

### Discussions

Feel free to start discussions on topics that you believe can help and support the community. Please make sure to follow the rules
**(No Spam / Advertising, Do not post “offensive” posts, links or images. Do not cross post questions. Remain respectful of other members at all times.)**
and [**github code of conduct**](https://docs.github.com/en/site-policy/github-terms/github-community-code-of-conduct)

### PRs & Issues

Feel free to submit an issue for any enhancements or bugs that you see, even better if you can submit a pull request with the fix or enhancement that you introduced. For issues/pr make sure to provide sufficient details and information about your change or request.

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
