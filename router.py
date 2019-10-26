import getpass
import sys
import telnetlib

host = raw_input("Router: ")
user = raw_input("Username: ")
password = getpass.getpass()

print "Connecting to router..."
tn = telnetlib.Telnet(host)
tn.read_until("Username: ")
tn.write(user + "\n")
tn.read_until("Password: ")
tn.write(password + "\n")
tn.write("ena\n")
tn.read_until("Password: ")
tn.write(password + "\n")

print "Fetching data..."
tn.write("term length 0 \n")
tn.write("show logging \n")
tn.write("show bgp summary\n")
tn.write("show ip int brief\n")
tn.write("sh ver | i Cisco IOS Software\n")
tn.write("sh ver | i uptime\n")
tn.write("exit\n")

print "Printing output..."
print tn.read_all()
