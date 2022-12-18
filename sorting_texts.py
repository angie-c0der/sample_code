import pandas as pd
#to read csv int dataframe
df=pd.read_csv("output.csv")
#sorting
df.sort_values(by='time')
#to save the sorted file
df.to_csv("sorted_output.csv")

