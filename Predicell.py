import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a pandas DataFrameD, data in ecgshirt.csv is ; separated
df = pd.read_csv('ecgshirt.csv', sep=';')

#clean rows with 0 values
df = df[df.ECG != 0]

#clean rows with unusually low ECG values
#df = df[df.ECG > 200]

#clean rows with unusually high ECG values
#df = df[df.ECG < 10000]

#add milliseconds to timestamp from 0 to 99 for all rows. Start from 1 and go up to 99 and start over again
df['Milliseconds'] = df.index % 100

#add milliseconds to timestamp 
df['Timesstamps'] = df['Timesstamps'] + '.' + df['Milliseconds'].astype(str)

#remove Timesstamps duplicates rows
df = df.drop_duplicates(subset='Timesstamps', keep='first')

 #print out the first 10 rows
print(df.head(10))



#clean rows with same timestamp values
#df = df.drop_duplicates(subset='Timesstamps', keep='first')

#show only between timestamp 19:05:00 and 19:10:00
df = df[df['Timesstamps'] > '2023-02-02 19:09:12']
df = df[df['Timesstamps'] < '2023-02-02 19:09:15']


# Calculate some basic summary statistics for each parameter
stats = df.describe()
print(stats)

# Draw a plot to visualize the skin temperature over time.
plt.plot(df['Timesstamps'], df['ECG'])
#plt.xlabel('Timesstamps')
#show x axis values only every 100th value and remove the date from the timestamp
plt.xticks(df['Timesstamps'][::100], df['Timesstamps'][::100].str[11:19])
plt.ylabel('ECG')
plt.show()
