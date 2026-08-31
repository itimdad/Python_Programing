# logical operator

uname = "admin"
pwd = "admin@123"

print(uname == "admin" and pwd == "admin")
print(uname == "admin" or pwd == "admin@123")

#! (not) operator
is_logged_in = True
print(not is_logged_in)

###Membership operator  => check present or not
members = ["admin", "HR", "Manager"]
print("HR" in members)
print("Manager" not in members)

###Identity Operator => compare memory location
a = 10
b = 10
print(a is b)
print(a is not b)
