vampcount = 0

with open("dracula.txt", "r") as bloody:
    with open("vampytimes.txt", "w") as mess:
        for line in bloody:
            if "vampire" in line.lower():
                print(line)
                vampcount += 1
                mess.write(line)


print(vampcount)
              

