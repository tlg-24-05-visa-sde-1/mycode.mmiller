#!/usr/bin/env python3

def main():

    # char_name marvel character info  prompt
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)").lower()

    # char_stat stat choice prompt
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)")

    marvelchars = {
            "Starlord":
            {"real name": "peter quill",
            "powers": "dance moves",
            "archenemy": "Thanos"},

            "Mystique":
            {"real name": "raven darkholme",
            "powers": "shape shifter",
            "archenemy": "Professor X"},

            "Hulk":
            {"real name": "bruce banner",
            "powers": "super strength",
            "archenemy": "adrenaline"}
    }
    
    # add the value variable
    value = marvelchars[char_name][char_stat]

    # print  <char_name>'s <char_stat> is: <value>
    print(f"{char_name.title()}'s {char_stat} is: {value}") # .title() will capitolize the hero's name

main()

    
