#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


names = open("/Users/programing/Desktop/programing/Mail Merge Project Start/Input/Names/invited_names.txt")

content = names.readlines()

names.close()
print(content[1])

# change_name = open("/Users/programing/Desktop/programing/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode='r')
with open("/Users/programing/Desktop/programing/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:

    content_for_change = file.read()
    for i in content:
        new_text = content_for_change.replace('[name]', i)
        next_gen_text = new_text.replace('Angela', 'Tato')
        create_new_mail = open(f"/Users/programing/Desktop/programing/Mail Merge Project Start/Output/ReadyToSend/{i}.txt", mode="w")
        create_new_mail.write(next_gen_text)


