def Check(string, pass_dot, indx):
    if string[indx].isnumeric() and string[0:2] != ["0","0"]:
        Check(string, pass_dot, indx:=indx+1)
    elif string[indx] == "." and not pass_dot and indx != 0:
        Check(string, pass_dot:=True, indx:=indx+1)
    else: raise ZeroDivisionError
def finite(string, pass_dot=False):
    try:
        Check(list(string), pass_dot, indx=0)
        return True
    except IndexError:
        return True
    except:
        return False

while True:
    print(finite(input("Enter Number: ")))
