
def test():
    print('Im a function')

def separator():
    print("-----------") 


print('Hello Python')

# variables 
name = 'Ladarius'
last = "Brooks"
age = 29
found = False
total = 23.43
products = []

print(name)
print(name + " " + last)

print(age + age)
print(name + str(age)) # cant concatenate str and int you have to pars it

separator()

# math operation
print(age-10)
print(age+10)
print(age*2)
print(age/2)
print(age%10) # mod operator

separator()

# if statements
if(age < 80):
    print('You are still young!')
    print('something else')
elif(age == 80):
    print('You are on the borderline')
else:
    print('Sorry, you are getting a little old')


