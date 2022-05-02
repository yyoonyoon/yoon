with open("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letters = letter_file.read() #returned list ['dfdf','dfafd','fdffd']

with open("/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#24/Mail Merge Project Start/Input/Names/invited_names.txt") as name_file:
    name_list = name_file.readlines() #returned list ['a\n','b\n','c\n','d\n']
    for name in name_list:
        stripped_name = name.strip() #['a','b','c','d']
        new_text = letters.replace("[name]", stripped_name)
        with open(f"/Users/yeomsangyoon/Visual Studio/Practice File/100DaysOfPython#24/Mail Merge Project Start/Output/ReadyToSend/Letter_for_{stripped_name}.txt",mode="w") as final:
            final.write(new_text)
    

