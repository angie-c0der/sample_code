# with open('ChatAnaghaAnne.txt', encoding="utf8") as f:
    # for line in  
    # lines = f.readline()
    # print(line)
    # print("hi")
from contextlib import redirect_stdout
file1 = open('chat_2.txt', encoding='utf8')
count = 0
line1 = file1.readline()
with open('oout.txt', 'w', encoding="utf8") as f:

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
        
        with redirect_stdout(f):
            print(date, time, contact, message, file=f)
    f.close()  
    # file_1 = open('output.txt', 'w')
    # file_1.write(print(date, time, contact, message))
    # print(date, time, contact, message)
# Closing file
# file_1.close()
  
# Checking if the data is
# written to file or not
# file_1 = open('output.txt', 'r')
# print(file_1.read())
# file_1.close()

# with open('out.txt', 'w', encoding="utf8") as f:
    # with redirect_stdout(f):
        # print(date, time, contact, message)
# f.close()

file_1 = open('out.txt', 'r')
print(file_1.read())
file_1.close()