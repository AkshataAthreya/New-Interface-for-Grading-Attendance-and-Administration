import csv
from functools import cmp_to_key

# Read the CSV files into dictionaries
section_data = {}
with open('section.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        section_data[row['name'].lower()] = row['section']

usn_data = {}
with open('usn.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        usn_data[row['name'].lower()] = row['usn']

# Merge the data and create the output list
merged_data = []
for name in set(section_data.keys()) | set(usn_data.keys()):
    section = section_data.get(name, '')
    usn = usn_data.get(name, '')
    if section and usn:
        merged_data.append({'section': section, 'usn': usn, 'name': name.title()})

# Sort the merged data by section and then by usn
def sort_key(item):
    return item['usn']

merged_data.sort(key=sort_key)

# Write the merged and sorted data to a new CSV file
with open('BTech23_USN.csv', 'w', newline='') as file:
    fieldnames = ['section', 'usn', 'name']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(merged_data)

print("Merged data has been written to 'merged_data.csv'.")
