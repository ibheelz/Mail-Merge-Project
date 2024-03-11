name_content = open ("Mail-Merge-Project/Input/Names/invited_names.txt")
names = (name_content.readlines())

for i in range(len(names)):
    names[i]=names[i].replace('\n','')

letter_content = open ("Mail-Merge-Project/Input/Letters/starting_letter.txt")
letter = (letter_content.read())

for i in names:
    x = letter.replace("[name]", i)
    y = open(f"Mail-Merge-Project/Output/ReadyToSend/{i}.txt", "w")
    z = y.write(x)
  