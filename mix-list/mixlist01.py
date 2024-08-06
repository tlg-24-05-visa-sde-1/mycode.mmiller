#!/usr/bin/env python3

#create a list
my_list = [ "192.168.0.5", 5060, "UP" ]

#return the IP address from the list
print("The first item in the list (IP): " + my_list[0] )

#return the port 5060
print("The second item in the list (port): " + str(my_list[1]) )

#return last item in list, the state
print("The last item in the list (state): " + my_list[2] )

#Challenge 01
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

#display only the IP addresses from iplist
print("The IP addresses from the list are:", iplist[3], "and", iplist[4])


