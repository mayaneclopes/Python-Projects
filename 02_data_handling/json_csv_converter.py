"""
 Challenge: JSON-to-Excel Converter Tool

Create a Python utility that reads structured data (like you'd get from an API) from a `.json` file and converts it to a CSV file that can be opened in Excel.

Your program should:
1. Read from a file named `api_data.json` in the same folder.
2. Convert the JSON content (a list of dictionaries) into `converted_data.csv`.
3. Automatically extract field names as CSV headers.
4. Handle nested structures by flattening or skipping them.

Bonus:
- Provide feedback on how many records were converted
- Allow user to define which fields to extract
- Handle missing fields gracefully
"""

import json 
import csv
import os

INPUT_FILE = "api_data.json"
OUTPUT_FILE = "converted_data.csv"

def load_json_data(filename):
    """Reads the JSON file and returns its content"""
    if not os.path.exists(filename):
        print("JSON file not found")
        return []
    with open(filename, 'r', encoding="utf-8") as f: #opens file in read mode
        try:
            return json.load(f) #converts text from JSON to Python objects
        except: #validates error in json format, like missing commas
            print("Invalid JSON format") 
            return []

def convert_to_csv(data, output_file):
    """Converts a list of dictionaries into one CSV file
    if the list is empty, it breaks"""
    if not data:
        print("No data to convert")
        return
    #Extraction of keys from the JSON first register to use as columns headlines 
    fieldname = list(data[0].keys())
    #open/creates the output file 
    with open(output_file, "w", newline="", encoding="utf-8") as f: #newline prevents the creation of blank lines
        writer = csv.DictWriter(f, fieldnames=fieldname) #instancia o dictwriter e informa cabeçalhos
        writer.writeheader() #writes headlines on the first line
        for record in data: #loops through each register from the list and writes them as a new line on csv file
            writer.writerow(record)

    #Shows how many rows were successfully converted
    print(f"Coverted {len(data)} records to {output_file}")

def main():
    print("Converting JSON to CSV...")
    data = load_json_data(INPUT_FILE) #loads data from json file
    convert_to_csv(data, OUTPUT_FILE) #converts and saves as csv

if __name__ == "__main__":
    main()
