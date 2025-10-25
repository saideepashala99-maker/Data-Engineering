from faker import Faker
import csv
import os
import platform
import subprocess

fake = Faker()
file_path = "mockdata.csv"

# Write the fake data
with open(file_path, 'w', newline='', encoding='utf-8') as output:
    header = ['name', 'age', 'street', 'city', 'state', 'zip', 'lng', 'lat']
    mywriter = csv.writer(output)
    mywriter.writerow(header)
    
    for _ in range(100000):
        mywriter.writerow([
            fake.name(),
            fake.random_int(min=18, max=80, step=1),
            fake.street_address(),
            fake.city(),
            fake.state(),
            fake.zipcode(),
            fake.longitude(),
            fake.latitude()
        ])

# Automatically open file location
system = platform.system()

#Auto Opens the file after saving
if system == "Windows":
    subprocess.run(["explorer", os.path.abspath(file_path)])
    print(f"File saved at: {os.path.abspath(file_path)}")
