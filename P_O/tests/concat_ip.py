ip = input("enter ip addr")
print(type(ip))
result = '.'.join(ip.split(".")[0:3])+".1"
print(type(result))
print(result)
