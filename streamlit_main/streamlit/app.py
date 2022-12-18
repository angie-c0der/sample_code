
import csv
from csv import writer
import pandas as pd
import streamlit as st
from streamlit_chat import message
data = pd.read_csv("sorted_output.csv")   #reading the contents of 'sorted_output.csv' and storing it to 'data'
print(data)
st.dataframe(data, width=500, height=700)  #defining a streamlit dataframe with demensions of choice
st.table(data)

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



def is_user(contact,date,time,messagee):   #defining  functions to print chats from a certain contact name in the chat
    if(contact=="Alinae"):
        message(contact, date, time, messagee) 
    

def is_user1(contact,date,time,messagee):
    if(contact=="Angie ✨"):
        message(contact, date, time, messagee) 
    


st.title("WhatsApp DC")  #giving the tile for the streamlist interface as 'WhatsApp DC'

import csv
from csv import writer
# Open the input file in read mode
with open('sorted_output.csv', 'r', encoding="utf8") as file_obj:
      
    # Create reader object by passing the file 
    # object to reader method
    reader_obj = csv.reader(file_obj)
      
    # Iterate over each row in the csv 
    # file using reader object
    for row in reader_obj:
        # print(row)
        
        message("Hello bot!", is_user(contact,date,time,messagee))
        message("Next contact chat details", is_user1(contact,date,time,messagee))
file_obj.close()

# st.header
# data = pd.read_csv("sorted_output.csv")   #reading the contents of 'sorted_output.csv' and storing it to 'data'
# print(data)
# st.dataframe(data, width=500, height=700)  #defining a streamlit dataframe with demensions of choice
# st.table(data)
