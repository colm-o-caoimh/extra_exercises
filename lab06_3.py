def questions():
    print('What would you like to do?')
    print('(a) Add new student')
    print('(v) View students')
    print('(q) Quit')
    ans = input('Type one letter (a/v/q):')
    return ans

def doAdd():
    print("in adding")

def doView():
    print("in viewing")

ans = questions()
print("You chose", ans)

if ans == "a":
    doAdd()
elif ans == "v":
    doView()
else:
    print("(base) ... ")