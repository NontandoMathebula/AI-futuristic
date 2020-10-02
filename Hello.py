
import platform

def main():
    message()

def message():

    print("\nHi famo, welcome to the most exciting journey")
    print("This is python version " + str (platform.python_version()) + str (" Let's get started\n"))

    if False: #For block purposes. check if they're under a common indentation
        print("\nit's only the beginning, hold tight")
    else:
        print("This line is cool")


if __name__ == "__main__":
    main()
