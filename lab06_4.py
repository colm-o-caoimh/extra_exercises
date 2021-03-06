# Colm O'Caoimh
# Week 6 lab. Program to add and view students to a module

students = []

def questions():
    print('What would you like to do?')
    print('(a) Add new student')
    print('(v) View students')
    print('(q) Quit')
    ans = input('Type one letter (a/v/q):')
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

# main program
ans = questions()
while ans != 'q':
    if ans == "a":
        doAdd()
    elif ans == "v":
        doView()
    elif ans != 'q':
        print("please select either a, v or q.")
    ans = questions()

#doAdd()
#doAdd()
#print(students)




