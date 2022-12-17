# opening the file in read mode
import pandas as pd
my_file = open("chat2.txt", "r")
  
# reading the file
data = my_file.readline()
  
# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
data_into_list = data.replace('\n', ' ').split(".")
  
# printing the data
# print(data_into_list)
df = pd.DataFrame(list1)
df.to_csv('chat2.csv', index=False)
my_file.close()