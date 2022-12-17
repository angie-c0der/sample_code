# with open('ChatAnaghaAnne.txt', encoding="utf8") as f:
    # for line in  
    # lines = f.readline()
    # print(line)
    # print("hi")

file1 = open('chat_2.txt', encoding='utf8')
count = 0
line1 = file1.readline()
for line in file1:
    date_list = line.split(',')
    # print(date_list,len(date_list))
    
    date = date_list[0]
    # print(date)
    
    time_list = date_list[1].split('-')
    time = time_list[0]
    contact_text = time_list[1].split(':')
    contact = contact_text[0]
    message = contact_text[1]    
    print(date, time, contact, message)