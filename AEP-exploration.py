import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df_arr = pd.read_csv('AEP-arrivals-cleaned.csv')
df_dept = pd.read_csv('AEP-departures-cleaned.csv')

# Convert 'Scheduled Departure' to datetime and extract the hour
df_arr['Scheduled Arrival'] = pd.to_datetime(df_arr['Scheduled Arrival'])
df_arr['Hour'] = df_arr['Scheduled Arrival'].dt.hour

df_dept['Scheduled Departure'] = pd.to_datetime(df_dept['Scheduled Departure'])
df_dept['Hour'] = df_dept['Scheduled Departure'].dt.hour

# Arrivals Histogram
plt.figure(figsize=(10, 6))
sns.histplot(df_arr['Hour'], bins=range(25), kde=True, color='hotpink')
plt.title('Histogram of Arrival Times')
plt.xlabel('Hour of the Day')
plt.ylabel('Frequency')

# Departures Histogram
plt.figure(figsize=(10, 6))
sns.histplot(df_dept['Hour'], bins=range(25), kde=True)
plt.title('Histogram of Departure Times')
plt.xlabel('Hour of the Day')
plt.ylabel('Frequency')

# Combined Histogram
plt.figure(figsize=(10, 6))
sns.histplot(pd.concat([df_arr['Hour'], df_dept['Hour']]), bins=range(25), kde=True, color='orchid')
plt.title('Histogram of Overall Hourly Activity')
plt.xlabel('Hour of the Day')
plt.ylabel('Frequency')

plt.show()