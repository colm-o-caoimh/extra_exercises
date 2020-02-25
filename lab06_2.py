def questions():
    print('What would you like to do?')
    print('(a) Add new student')
    print('(v) View students')
    print('(q) Quit')
    ans = input('Type one letter (a/v/q):').strip()
    return ans

ans = questions()
print("You chose " + ans)    
