#integer
f = 0
#print(f)

#string
#f = "Ntandokazi"
#print(f)

#Variable of different types cannot be combined i.e a string & integer(print("Ntandokazi" + 2271))
#You have to have the arguments be the same
#print("Ntandokazi " + str (2271))

#Global vs Local variables
def specialFunction():
    global f
    f = "Something Cool"
    print(f)

specialFunction()
print(f)

del f #del statement deletes the the definition of variable that was previously defined
print(f) #Can undefine variables in real time by using del statement