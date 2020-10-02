#Working with classes

class myPythonClass():
    def method1(self):
        print("myPythonClass method1")

    def method2(self, someString):
        print("myPythonClass method2 " + someString)

def main(): #in the main function,I will instantiate the class
    c = myPythonClass()  #instantiating the class
    c.method1() #After instantiating the class, I can now call methods on any other object 
    c.method2("This is a just a string silly")

if __name__ == "__main__":
    main()