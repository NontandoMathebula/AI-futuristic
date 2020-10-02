#Working with conditional statements

def main():
    x, y = 100, 100

    if(x > y):
        st = "X is greater than Y"
    elif( x == y):
        st = " X is equal to Y"
    else:
        st = "X is lesser than Y"
    print(st)

if __name__ == "__main__":
    main()
    
