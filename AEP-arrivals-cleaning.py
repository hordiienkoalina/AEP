import pandas as pd
import re

# Open the text file and read its contents
with open('AEP-arrivals.txt', 'r') as file:
    data_string = file.read()

# Define the regular expression pattern
pattern = r'(\d{2}:\d{2})(\d{2} \w{3})(\w{3})([A-Za-z\s]+)(\w{2}\d{4})([A-Za-z\s]+)(\w+)? (\d{2}:\d{2})?'
matches = re.findall(pattern, data_string)

df = pd.DataFrame(matches, columns=['Scheduled Arrival', 'Date', 'Destination Code', 'Destination City', 'Flight Number', 'Airline', 'Status', 'Actual Arrival Time'])

df.to_csv('AEP-arrivals-cleaned.csv', index = False)