#!/usr/bin/env python3
"""MNMiller | TLG Learning / Alta Research
   nesting an if-statement inside of a for loop"""

def main():

    # farms list of farms with dictionary
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}] 

    # print each animal from NE Farm
    NE_Farm = farms[0]["agriculture"]
    for x in NE_Farm:
        print(x)

    # prompt user to choose a farm, return the plants or animals raised there
    choose_farm = input("Choose a farm to learn more about what we raise there (NE Farm, W Farm, SE Farm)").lower()
    for x in choose_farm:
        print(f"{[0][agriculture]}")


