from dataclasses import dataclass
from typing import Tuple


class Gender:
    Male = "Male"
    Female = "Female"
    Other = "Other"


class Subject:
    Maths = 'Maths'
    Accounting = 'Accounting'
    Arts = 'Arts'
    Social_Studies = 'Social Studies'
    English = 'English'
    Chemistry = 'Chemistry'
    Physics = 'Physics'
    Computer_Science = 'Computer Science'
    Economics = 'Economics'
    History = 'History'
    Civics = 'Civics'
    Hindi = 'Hindi'
    Biology = 'Biology'
    Commerce = 'Commerce'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    number_phone: str
    birthday: str
    subjects: Tuple[Subject]
    hobbies: str
    file: str
    address: str
    state: str
    city: str


user1 = User(
    first_name="Ivan",
    last_name="Ivanov",
    email="user123@test.com",
    gender=Gender.Male,
    number_phone="7904111222",
    birthday="25 January,1997",
    subjects=(Subject.Maths, Subject.Physics, Subject.Arts),
    hobbies="Music",
    file="file_test.jpg",
    address="Russia,Moscow",
    state="Haryana",
    city="Karnal"
)