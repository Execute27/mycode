count = 0

with open("dracula.txt", "r") as blood:
    with open("vampytimex.txt","w") as fang:
        for line in blood:
            if "vampire" in line.lower():
                print(line)
                count +=1
                fang.write(line)
print(count)
