import csv  # import module

with open('data.csv') as csvfile:  # read csv file
    your_id = raw_input("Enter id: ") # Prompt  user
    readCSV = csv.reader(csvfile, delimiter=',')  # read the file

    for id_ in readCSV:
        if your_id == id_[0]:
            print 'First Name: ' + id_[1] + 'Last Name: ' + id_[2] + 'Email Address: ' + id_[3] + 'Gender: ' + id_[4]
        else:
            pass
