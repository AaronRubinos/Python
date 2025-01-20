# Global Variables
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

# global keyword
def myGlobal():
    global x
    x = "fantastic"
    
myGlobal()

print("Python is " + x)

# change global value
x = "awesome"

def myChange():
    global x 
    x = "fantastic"
    
myChange()
print("Python is " + x)