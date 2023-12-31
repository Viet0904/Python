
with open("day24/224/Mail Merge Project Start/Input/Names/invited_names.txt") as file_name:
    data_name = file_name.readlines()
with open("day24/224/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
        data_mail = file.read()
        for name in data_name:
            name = name.strip("\n")
            data_mail_name = data_mail.replace("[name]", name)
            file_output = open(f"day24/224/Mail Merge Project Start/Output/ReadyToSend/{name}.txt",mode="w")
            file_output.write(data_mail_name)
        file_output.close()
        

            
        
