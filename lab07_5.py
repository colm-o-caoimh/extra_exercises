# Colm O'Caoimh
# With the program we made last week, create a new menu item called save.
# When the user selects the doSave() function should be called 
# (the do save can do nothing but printout doSave for the moment.

import json

students = []

def questions():
    print('What would you like to do?')
    print('\t (a) Add new student')
    print('\t (v) View students')
    print('\t (s) Save students')
    print('\t (l) Load students')
    print('\t (q) Quit')
    
    ans = input('Type one letter (a/v/s/l/q):')
    return ans


def doAdd():
    student_dict = {}
    student_dict["name"] = input("Enter name: ")
    students.append(student_dict)
    student_dict["modules"] = read_modules()
    

def read_modules():
    module_array = []
    moduleName = input("Enter the first Module name (blank to quit): ")
    
    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = input("enter grade: ")
        module_array.append(module)
        moduleName = input("Enter next module name (blank to quit): ")
       

    return module_array

def displayModules(module_array):
    print("\tName \t\tGrade")
    for module in module_array:
        print("\t{} \t{}".format(module["name"], module["grade"]))

def doView():
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

# write function to save student data as JSON file
def saveDict():
    with open("studentData.json", "w") as f:
        json.dump(students, f)
        print("Student info. has been saved")

def doSave():
    saveDict()

def readDict():
    loadDict = input('Enter file for loading: ')
    with open(loadDict, "r") as f:
        json.load(f)
        students.append(f)
        return students

def doLoad():
    global students 
    students = readDict()

# main program
ans = questions()
while ans != 'q':
    if ans == "a":
        doAdd()
    elif ans == "v":
        doView()
    elif ans == "s":
        doSave()
    elif ans == "l":
        doLoad()
    elif ans != 'q':
        print("please select either a, v, s or q.")
    ans = questions()

#doAdd()
#doAdd()
#print(students)




