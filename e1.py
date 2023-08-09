import glob
myfiles = glob.glob("*.txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())
        
import csv

with open("weather.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])
#%%        
import webbrowser

user_term = input("Enter a search term:")
webbrowser.open("https://www.google.com/search?q=" + user_term)
