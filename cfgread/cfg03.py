#!/usr/bin/env python3
## create file object in "r"ead mode

# prompt user for the name of the file to load
namedfile = input("Please enter the name of the file you want to load: ")

with open(namedfile, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)

# diplays the number of lines in the namedfile
print(f"The file {namedfile} has {len(configlist)} lines.")

