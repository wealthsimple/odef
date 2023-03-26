import datetime
import glob
import os
from dataclasses import dataclass

import yaml
from custom_exceptions.custom_exceptions import MissingConfigKey

"""Used in Github Actions"""


def read_yaml_file(file_path) -> dict:
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def get_all_detections(detection_folder: str, pattern: str = "*.yml") -> list:
    all_detections = []
    for root, dirs, files in os.walk(detection_folder):
        detections = glob.glob(os.path.join(root, pattern))
        all_detections.extend(detections)
    return all_detections


def check_if_type_is_datetime_date(value):
    try:
        datetime.datetime.strptime(value, "%Y-%m-%d")
        return True
    except:
        return False


def get_date_from_string(date_string: str) -> datetime.date:
    if isinstance(date_string, datetime.date):
        return date_string
    elif check_if_type_is_datetime_date(date_string):
        return datetime.date.fromisoformat(date_string)
    else:
        return datetime.date.fromisoformat("2100-01-01")


@dataclass
class Detection:
    raw_yml: dict
    inactive_detection: bool = False

    def set_detection_status(self):
        if self.status == "true":
            return True
        else:
            return False

    def get_name(self):
        return self.raw_yml.get("name", "")

    def get_status(self):
        return self.raw_yml.get("status", "")

    def get_created_date(self):
        val = self.raw_yml.get("created_date", "")
        return get_date_from_string(val)

    def get_last_updated_date(self):
        val = self.raw_yml.get("last_updated_date", "")
        if val == "" or val is None:
            return self.created_date
        else:
            return get_date_from_string(val)

    def get_detection_age(self):
        if self.last_updated_date != datetime.date(2100, 1, 1):
            age = datetime.date.today() - self.last_updated_date
        else:
            age = datetime.date.today() - self.created_date
        return age.days

    def __post_init__(self):
        self.name = self.get_name()
        self.status = self.get_status()
        self.author = self.raw_yml.get("author", "")
        self.created_date = self.get_created_date()
        self.inactive_detection = self.set_detection_status()
        self.last_updated_date = self.get_last_updated_date()
        self.detection_age = self.get_detection_age()


def create_review(detection: Detection, max_age: int) -> tuple[str, str]:
    if detection.detection_age > max_age:
        return (detection.name, detection.author)


def email_to_github_username(email: str, list_of_users: dict) -> str:
    return list_of_users.get(email, "")


def clean_up_list(list_to_clean: list) -> list[str]:
    clean_list = [str(x) for x in list_to_clean if x not in ["", None]]
    clean_list = set(clean_list)
    return list(clean_list)


def print_detections_to_review(
    detection_review_list: list[str], user_list: list[str]
) -> None:
    """Function that prints the results of the script for Github Actions"""
    if len(detection_review_list) > 0:
        user_list = clean_up_list(user_list)
        user_list = ",".join(user_list)
        detection_review = ",".join(detection_review_list)
        print(f"Authors: {user_list}; Detections to review: {detection_review}")
    else:
        print("Authors: None; Detections to review: None")


def main():
    config = read_yaml_file("config/config.yml")
    list_of_users = config.get("detection_author", {})
    max_age_in_days = config.get("max_detection_age", None)
    detections_folder = config.get("detections_folder", "")

    if not max_age_in_days:
        raise MissingConfigKey(
            message="\nMax_detection_age is not defined in config.yml",
            key='"max_detection_age"',
        )

    detections_paths = get_all_detections(detection_folder=detections_folder)

    detection_review_list = list()
    user_list = list()
    for d_path in detections_paths:
        detection = Detection(raw_yml=read_yaml_file(d_path))
        if not detection.inactive_detection:
            review = create_review(detection=detection, max_age=max_age_in_days)
            if review:
                detection_review_list.append(review[0])
                user_list.append(email_to_github_username(review[1], list_of_users))

    print_detections_to_review(
        detection_review_list=detection_review_list, user_list=user_list
    )


if __name__ == "__main__":
    main()
