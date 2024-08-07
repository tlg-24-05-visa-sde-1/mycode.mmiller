#!/usr/bin/env python3

def main():

    print("You are stranded in the galaxy...")
    print("... you've found what appears to be a safe planet to land...")
    print("...but it isn't as safe as it appears to be...")

    weapon_choice == input("What is your weapon of choice? (Blaster Pistol, Thermal Detonator Grenade, or a Gaffi Stick)").lower()

    if weapon_choice == "blaster pistol":
        print("You have chosen Blaster Pistol")
        print("You can fire at enemies from a distance, but you have limited ammo")

    elif weapon_choice == "thermal detonator grenade":
        print("You have chosen Thermal Detonator Grenade")
        print("You can inflict a great deal of damage and take out multiple monsters, but you only have one")

    elif weapon_choice == "gaffi stick":
        print("You have chosen the Gaffi Stick")
        print("You can be deadly in close combat, but will not fare well in a ranged attack")
    else:
        print("Invalid choice, you must choose a weapon, or you will certainly perish here!")

    print("\nYou realize you are on Tatooine, and decide to head to Mos Eisley Cantina.")
    print("Suddenly, you stumble upon the Great Pit of Carkoon, home of the deadly Sarlacc!")
    print("You're too close to the pit! The Sarlacc is angry and particularly hungry...")

    survival_choice == input("\nWhat will you do? (Use your weapon (use), Run away(run), Pray to the Sarlacc for mercy(pray))").lower()

    if survival_choice == "use weapon":
        if weapon_choice == "blaster pistol":
            print("\nThe Sarlacc grabs you with its tentacle!")
            print("You shoot the tentacle and the Sarlacc recoils in pain, releasing you!")
            print("You can now continue to Mos Eisley Cantina, where it is surely time for a drink")

        elif weapon_choice == "thermal detonator grenade":
            print("You throw your grenade into the pit with the Sarlacc")
            print("BOOM!! goes the explosion, you have blown off part of the Sarlacc's tentacles")
            print("But alas, you have now angered Jabba thr Hutt and will now surely be fed to the Sarlacc!!")
            print("Game over!")
        
        elif weapon_choice == "gaffi stick":
            print("\nYou bravely swing and jab your Gaffi Stick at the Sarlacc")
            print("Right when you think you will surviv this, you see more tentacles emerge and the Sarlacc pulls you into its spiny teeth... CHOMP!!!")
            print("You have been pulled into the pit and swallowed by the Sarlacc!!")
            print("Game over!")
        else:
            print("Without a proper weapon, you're defenseless and will surely perish on any planet of the galaxy!")
            print("Game Over!")

main()
