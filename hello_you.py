#Ask user for name

name=input("What is your name?: ")
print(name)

#Ask user for age

age=input("What is your age?: ")
print(age)

#Ask user for city

city=input("Where do you live?: ")
print(city)

#Ask user for interests

hobby=input("What is your hobby?: ")
print(hobby)

#Create output text
output="Hey {}.You are {} and you live in {}. You love {}".format(name,age,city,hobby)
#Print output to screen
print(output)
