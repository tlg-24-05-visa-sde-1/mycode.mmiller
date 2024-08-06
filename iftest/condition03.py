#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")

    #if hostname is mtg, print "hostname matches expected config".
    print("hostname matches expected config")

    #ending program, display "exiting script"
    print("Exiting the script")

