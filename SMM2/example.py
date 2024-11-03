from encryption import Save as EncryptedSave
from save import Save as DecryptedSave
from save import SLOT_STATUS
from encryption import Course as EncryptedCourse
from course import Course as DecryptedCourse
from typing import List
import yaml

def cls(): print('\033[2J\033[H', end='')
config = yaml.safe_load(open("./config.yml", "r+"))

if config == None: config = {}

if "save_path" not in config:
    print("The save path had not write.")
    exit()

try:
    encrypted_save = EncryptedSave(open(f'{config['save_path']}/save.dat', 'rb').read())
    encrypted_save.decrypt()
except:
    print("The save path is not correct.")
    exit()

decrypted_save = DecryptedSave(encrypted_save.data)
index = 0
courses : List[DecryptedCourse] = []
for course in decrypted_save.own_courses:
    if course[1] == SLOT_STATUS.OCCUPIED:
        encrypted_course = EncryptedCourse(open(f'{config['save_path']}/course_data_{str(course[0]).rjust(3, '0')}.bcd', 'rb').read())
        encrypted_course.decrypt()

        decrypted_course = DecryptedCourse(encrypted_course.data)
        courses.append(decrypted_course)
        print(f'{index}: {decrypted_course.HEADER.NAME}')
        index += 1
ind = int(input("Enter the course you want: "))
cls()
print(courses[ind].HEADER.DESCRIPTION)