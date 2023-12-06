import pandas as pd
import re

# Open the text file and read its contents
with open('AEP-departures.txt', 'r') as file:
    departure_data_string = file.read()

# Define the regular expression pattern
pattern = r'(\d{2}:\d{2}) (\d{2} \w{3}) (\w{3}) ([A-Za-z\s]+) (\w{2}\d{4}) ([A-Za-z\s]+)\\\'a\d{2} (\w+) (\d{2}:\d{2})'
matches = re.findall(pattern, departure_data_string)

df = pd.DataFrame(matches, columns=['Scheduled Departure', 'Date', 'Destination Code', 'Destination City', 'Flight Number', 'Airline', 'Status', 'Actual Departure Time'])

df.to_csv('AEP-departures-cleaned.csv', index=False)