with open("Input/Names/invited_names.txt", "r") as file:
    lines = file.readlines()

names = []
for line in lines:
    names.append(line.strip())

print(names)

#create the letter for each person
 # for each name in names
for name in names:
    #open an output file and write the message
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as letter_file:
        letter_file.write(f"Dear {name},\n")
        letter_file.write("You are invited to my birthday this Saturday.\n")
        letter_file.write("Hope you can make it!\n")
        letter_file.write("Sid\n")


