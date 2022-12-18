
import csv
from csv import writer
# Open the input file in read mode
with open('output.csv', 'w', newline="", encoding="utf8") as output_file:
    #opening the output csv file write mode
    thewriter=writer(output_file)
    heading =["date","time","contact","message"] #defining a header

    thewriter.writerow(heading)
    with open('chat_2.txt', 'r', encoding="utf8") as input_file:
        chumma=input_file.readline() #skip reading the first line
        for line in input_file:
            date_list = line.split(',') #splitting line with ','
            print(date_list)
            date = date_list[0].strip()  #obtaining date from the 0th element of date_list
            time_list = date_list[1].split('-')
            time = time_list[0].strip()  #obtaining time from the 0th element of time_list
            contact_text = time_list[1].split(':')
            contact = contact_text[0].strip()
            messagee = contact_text[1].strip() #obtaining time from the 0th element of time_list
            print(date,time,contact,messagee)  
            list1=[date, time, contact, messagee]  #declaring a list with the required elements
            thewriter.writerow(list1) #writing the contents of the list1 onto the output.csv file
    output_file.close()
input_file.close()

