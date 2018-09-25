
def check_name(name_lst, name):  #Di
    if name in name_lst:
        return(True)
    else:
        return(False)


computing = ['preston', 'jolee', 'kim', 'devon', 'driston', 'james']


student = input('Login with name:')
student = student.lower()
login = False
while login is False:
    if check_name(computing, student) is True:
        login = True
        print('Login Successful')
        break
    else:
        login = False
        print('Login Failed ')
        student = input('Try Again:')
