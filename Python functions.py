import math
#define a basic function
#def function1():
   # print("I am a cute function")

#function that takes arguments
#def function2(arg1, arg2):
    #print(arg1, " ", arg2)

#funcion that returns a value
#def cube(x):
    #return x*x*x
#function with default value for an argument
def power(num, x = 1):
    result = 1
    for i in range(x):
        result =  result * num #it takes a number and raises it to the given power
    return result
#function with variable number of arguments
#def multi_add(*args): #the star character means I can pass a variable number of arguments
    #result = 0
    #for x in args:
       # result = result + x #the function loops over each argument and adds them all to a running total, which is then returned
        #return result

#"Parameter values" of the above functions
#function1() #functions are objects that can be passed around to other pieces of Python code
#print(function1()) #here the function is called inside the print statement the output should be "I am a cute function"
#print(function1) #this function doesn't return a value, therefore, the output is set to "None" meaning it is not executed because there are no parathesis

#function2(10,20)
#print(function2(10,20))
#print(cube(3))

print(power(2, 1))
print(power(2, 3))
print(power(x=3, num=2))#function can be called in no particular order, if you supply the names along with the values
print(math.pow(2,3))
#print(multi_add(30, 5, 10, 4))
