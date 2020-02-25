def questions():
    print('What would you like to do?')
    print('(a) Add new student')
    print('(v) View students')
    print('(q) Quit')
    ans = input('Type one letter (a/v/q):')
    return ans

def doAdd():
    name = input("Enter name: ")
    modules = input("Enter modules: ")
    student_dict = {'name': name, "modules": []}
    student_array = []
    student_array.append(student_dict)
    print(student_dict)
    print(student_array)

def doView():
    print("in viewing")

ans = questions()
print("You chose", ans)

if ans == "a":
    doAdd()
elif ans == "v":
    doView()
else:
    print("Thank you. Have a nice day")