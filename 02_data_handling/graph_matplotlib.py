import csv
from collections import defaultdict #dict that avoids error while trying to register invalid keys
import matplotlib.pyplot as plt #chart lib

FILENAME = "weather_logs.csv"

def visualize_weather():
    """Reads all data from a csv file and creates 2 chart:
    1. Time line of temperatures and 2. Bar chart with weather counts"""
    date = []
    temps = []
    conditions = defaultdict(int) 
    #Opens CSV file in read mode
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f) #Dictreader reads each line of csv as a dict (key as column name)
        for row in reader:
            try: #extract data and appends from each line
                date.append(row["Date"])
                temps.append(row["Temperature"])
                conditions[row["Condition"]] += 1
            except: #If one line is invalid, jumps to the next one
                continue
    if not date: #func breaks if there's no data 
        print("No dates available")
        return

    plt.figure(figsize=(10, 7))
    plt.plot(date, temps, marker='o')
    plt.title("Temperature x Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature")
    plt.tight_layout()
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(7, 5))
    plt.bar(conditions.keys(), conditions.values(), color='skyblue')    
    plt.show()

visualize_weather()