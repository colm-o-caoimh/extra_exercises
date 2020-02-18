# Colm O'Caoimh
# Create dictionary for student which contains subjects and grades
# Then print them out 

# This program was helpful with regards to the structuring, ordering and formatting
# of hard code in dictionaries. I learned a lot with regard to the syntax. Also,
# accessing lists and dictionaries within dictionaries was a skill learnt here.
# I'm better off not using capital letters for keys, values and variables.


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

print("Student:" + student_dict['Name'])

for course in student_dict['Courses']:
    print("\t{}: {}".format(course["Course_name"],course["Grade"]))