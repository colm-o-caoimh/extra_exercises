# Colm O'Caoimh
# Write a functionthat will store a simple Dict to a file as JSON

import json

# Copied this dict from previous lab. Could not import it due to difficulty 
# with python path searching

student_dict = {
    'Name': 'Mary',
    'Courses': [
        {
            'Course_name': 'French',
            'Grade': 87
        },
        {
            'Course_name': 'Programming',
            'Grade': 98
        },
        {   
            'Course_name': 'Irish',
            'Grade': 82
        },
        {
            'Course_name': 'Mathematics',
            'Grade': 37
        },
    ]
}

# function to store dict to a JSON file
def fileJson(x):
    with open("dataFile.json", "w") as f:
        json.dump(x, f)


fileJson(student_dict)

