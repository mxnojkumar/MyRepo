import re

def validIP(IP):
    
    IPv4 = re.compile(r"^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$")
    
    IPv6 = re.compile(r"^((([0-9 a-f A-F]{1,4}):){7}([0-9 a-f A-F]{1,4}))$")
    
    if IPv4.match(IP):
        return "IPv4"
    
    elif IPv6.match(IP):
        return "IPv6"
    
    else:
        return "Neither"
    
IP = "256.256.256.256"
print(validIP(IP))