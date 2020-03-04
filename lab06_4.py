def questions():
    print('What would you like to do?')
    print('(a) Add new student')
    print('(v) View students')
    print('(q) Quit')
    ans = input('Type one letter (a/v/q):')
    return ans

ans = questions()
print("You chose", ans)

students = []


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



while ans != 'q':
    if ans == "a":
        doAdd()
        print(students)
    elif ans == "v":
        doView()
    else:
        print("Thank you. Have a nice day")

#doAdd()
#doAdd()
#print(students)


def doView():
    print("in viewing")



