import markdown
##with open("C:/Users/User/Documents/GitHub/Yr13-Digital-Outcome/13_Digit_project/data/Test.md","r") as md_file:
##    print(md_file.read())



class Output():
    def __init__(self, path):
        self.text = []
        with open(path,"r", encoding='utf-8') as md_file:
            while (line:=md_file.readline()):
                self.text.append(line)
    

class New():
    def __init__(self, path):
        self.md_file = open(path,"w",encoding='utf-8')

    def recieved_data(*args):
        for data in args:
            if type(data) == str:
path = "C:/Users/User/Documents/GitHub/Yr13-Digital-Outcome/13_Digit_project/data/Test.md"
test = Output(path)
