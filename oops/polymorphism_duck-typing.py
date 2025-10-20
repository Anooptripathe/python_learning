class Vscode:
    def execute(self):
        print("Compiling")
        print("Running")

class Pycharm:
    def execute(self):
        print("Spelling check")
        print("Convention check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()

x=Vscode()
y=Pycharm()
lap1=Laptop()
print("Passing object of Vscode class")
lap1.code(x)
print('\n \n')
print("Passing object of Pycharm class")
lap1.code(y)