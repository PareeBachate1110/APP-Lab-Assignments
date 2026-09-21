import csv
import json

# Define input and output file names
input_file = "input.csv"
output_file = "output.json"

# Open the CSV file and read its contents
with open(input_file, "r") as csv_file:
    reader = csv.DictReader(csv_file)

    # Convert CSV data into a list of dictionaries
    data = list(reader)

# Write the data to a JSON file
with open(output_file, "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data converted to JSON successfully.")