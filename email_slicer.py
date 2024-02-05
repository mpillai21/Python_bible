#get user email address
string=input("What is your email address?:").strip()

#slice out user name
user_name=string[:string.index("@")]
print(user_name)

#slice domain name
domain_name=string[string.index("@"):-1].strip("@")
print(domain_name)

#format message
output="Your name is {} and your domain is {}".format(user_name,domain_name)

#display message
print(output)
