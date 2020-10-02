#Working with loops

def main():
    x = 0 
    #while loop
    while(x<10):
        x = x + 1
        print(x)

    #for loop
    for x in range(5, 10):
        #if(x == 8):break #break statement is used to break the execution of the loop if a condition is met
        if(x % 2 ==0):continue
        print(x)
    #for loop over a collection
    days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
    for d in days:
        print(d)

    #enumerate() function to get index
    days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
    for i, d in enumerate(days):
        print(i, d)

if __name__ =="__main__":
    main()