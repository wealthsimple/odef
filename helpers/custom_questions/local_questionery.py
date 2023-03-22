import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
from pprint import pprint
import questionary
from questionary import Style, Validator, ValidationError, prompt
from jinja2 import Environment, FileSystemLoader
from custom_dataclasses.contentName import ContentName
from yml_helpers import YmlHelper   

def create_dir(dirName):
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory ", dirName, " Created ")
    else:
        print("Directory ", dirName, " already exists")
        raise Exception


class NameValidator(Validator):
    def validate(self, document):
        dir_names = os.listdir("DETECTIONS")
        if ContentName(document.text).convert_case() in dir_names:
            raise ValidationError(
                message="Please enter an unique hunt/detection name!",
                cursor_position=len(document.text),
            )


class ContentQuestions:
    """Object containing custom questions and pulling some values from config"""
    def __init__(self, conf) -> None:
        """Requires the configuration file read as dict"""
        self.conf = conf

    custom_style_fancy = Style([
        ('qmark', 'fg:#fff35d bold'),  # token in front of the question
        ('question', 'bold'),  # question text
        ('answer', 'fg:#f44336 bold italic'),  # submitted answer text behind the question
        ('pointer', 'fg:#673ab7 bold'),  # pointer used in select and checkbox prompts
        ('highlighted', 'fg:#673ab7 bold'),  # pointed-at choice in select and checkbox prompts
        ('selected', 'fg:#cc5454'),  # style for a selected item of a checkbox
        ('separator', 'fg:#cc5454'),  # separator in lists
        ('instruction', ''),  # user instructions for select, rawselect, checkbox
        ('text', ''),  # plain text
        ('disabled', 'fg:#858585 italic')  # disabled choices for select and checkbox prompts
    ])

    def get_questions_detection(self) -> list:
        questions = [
            {
                'type': 'select',
                'message': 'What kind of detection is this?',
                'name': 'detection_kind',
                'choices': [
                    'endpoint',
                    'cloud',
                    'application',
                    'network',
                    'web',
                    'experimental'
                ]

            },
            {
                'type': 'text',
                'message': 'Enter Detection Name:',
                'name': 'detection_name',
                'default': 'Your Smart Detection Name',
                'validate': NameValidator
            },
            {  
                'type': 'autocomplete',
                'message': 'Enter Author Name:',
                'name': 'detection_author',
                'choices': self.conf.get('detection_author')
            },
            {
                'type': 'text',
                'message': 'Enter Description:',
                'name': 'description',
            },
            {
                'type': 'text',
                'message': 'Enter Search Query:',
                'name': 'query',
                'default': 'index= ...'
            },
            {
                'type': 'text',
                'message': 'Enter the index where the data resides:',
                'name': 'data_source',
                'default': ''
            },
            {
                'type': 'text',
                'message': 'Enter Baseline - items that are excluded from the search:',
                'name': 'baseline',
                'default': 'server!=server1000, network!=1.1.1.1 ...'
            },
            {
                'type': 'text',
                'message': 'Enter Visualization (spl):',
                'name': 'visualization',
                'default': '| table ...'
            },
            {
                'type': 'text',
                'message': 'Enter MITRE ATT&CK Technique IDs related to the detection, comma delimited for multiple:',
                'name': 'mitre_id',
                'default': 'T1003.002'
            },
            {
                'type': 'text',
                'message': 'Enter MITRE ATT&CK Technique URL:',
                'name': 'mitre_url',
                'default': 'https://attack.mitre.org/techniques/TXXXX.XXX/'
            },
            {
                'type': 'select',
                'message': 'detection disabled',
                'name': 'status',
                'choices': ['sunrise', 'midday','sunset'],
                'default': 'sunrise'
            },
            {
                'type': 'select',
                'message': 'Select tactic chain phases related to the detection:',
                'name': 'tactic',
                'choices': [
                    'Reconnaissance', 
                    'Resource Development', 
                    'Initial Access', 
                    'Execution', 
                    'Persistence', 
                    'Privilege Escalation', 
                    'Defense Evasion', 
                    'Credential Access', 
                    'Discovery', 
                    'Lateral Movement', 
                    'Collection', 
                    'Command and Control', 
                    'Exfiltration', 
                    'Impact'
                ]
            },
            {
                'type': 'text',
                'message': 'Enter cron schedule expression:',
                'name': 'schedule',
                'default': '*/5 * * * *'
            }
        ]
        return questions

    def get_questions_hunt(self) -> list:
        questions = [
            {
                'type': 'select',
                'message': 'What kind of detection is this?',
                'name': 'detection_kind',
                'choices': [
                    'endpoint',
                    'cloud',
                    'application',
                    'network',
                    'web',
                    'experimental'
                ]

            },
            {
                'type': 'text',
                'message': 'Enter Detection Name:',
                'name': 'detection_name',
                'default': 'Your Smart Detection Name',
                'validate': NameValidator
            },
            {  
                'type': 'autocomplete',
                'message': 'Enter Author Name:',
                'name': 'detection_author',
                'choices': self.conf.get('detection_author')
            },
            {
                'type': 'text',
                'message': 'Enter Description:',
                'name': 'description',
            },
            {
                'type': 'text',
                'message': 'Enter Search Query:',
                'name': 'query',
                'default': 'index= ...'
            },
            {
                'type': 'text',
                'message': 'Enter the index where the data resides:',
                'name': 'data_source',
                'default': ''
            },
            {
                'type': 'text',
                'message': 'Enter Baseline - items that are excluded from the search:',
                'name': 'baseline',
                'default': 'server!=server1000, network!=1.1.1.1 ...'
            },
            {
                'type': 'text',
                'message': 'Enter Visualization (spl):',
                'name': 'visualization',
                'default': '| table ...'
            },
            {
                'type': 'text',
                'message': 'Enter MITRE ATT&CK Technique IDs related to the detection, comma delimited for multiple:',
                'name': 'mitre_id',
                'default': 'T1003.002'
            },
            {
                'type': 'text',
                'message': 'Enter MITRE ATT&CK Technique URL:',
                'name': 'mitre_url',
                'default': 'https://attack.mitre.org/techniques/TXXXX.XXX/'
            },
            {
                'type': 'select',
                'message': 'detection disabled',
                'name': 'status',
                'choices': ['sunrise', 'midday','sunset'],
                'default': 'sunrise'
            },
            {
                'type': 'select',
                'message': 'Select tactic chain phases related to the detection:',
                'name': 'tactic',
                'choices': [
                    'Reconnaissance', 
                    'Resource Development', 
                    'Initial Access', 
                    'Execution', 
                    'Persistence', 
                    'Privilege Escalation', 
                    'Defense Evasion', 
                    'Credential Access', 
                    'Discovery', 
                    'Lateral Movement', 
                    'Collection', 
                    'Command and Control', 
                    'Exfiltration', 
                    'Impact'
                ]
            },
            {
                'type': 'text',
                'message': 'Enter cron schedule expression:',
                'name': 'schedule',
                'default': '*/5 * * * *'
            }
        ]
        return questions

    def entry_question(self) -> list:
        questions = [
            {
                'type': 'autocomplete',
                'message': 'What product is this for?',
                'name': 'product',
                'choices': self.conf.get('entry_question.choices'),
                'default': 'Detection'
            }
        ]
        return questions


if __name__ == "__main__":
    conf = YmlHelper.read_yml_file('config/config.yml')
    QuestionsObj = ContentQuestions(conf)

    answers = questionary.prompt(QuestionsObj.entry_question(), style=ContentQuestions.custom_style_fancy)

    if answers.get('product') == 'HUNT':

        answers = questionary.prompt(QuestionsObj.get_questions_detection())

    else:
        answers = questionary.prompt(QuestionsObj.get_questions_detection())

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template("alert_template.txt")

    output_from_parsed_template = template.render(answers)
    create_dir(answers.get('detection_name'))
    with open(answers.get('detection_name') + '/' + answers.get('detection_name') + '.tf', "w") as fh:
        fh.write(output_from_parsed_template)
