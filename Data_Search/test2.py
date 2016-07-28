import csv


with open('data.csv') as csvfile:
        your_id = int(raw_input("Enter id:"))
	readCSV = csv.reader(csvfile ,delimiter=',')
	print(readCSV)
	
	for id in readCSV:
		print (id)

