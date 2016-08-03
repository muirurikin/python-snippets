black = str(raw_input("What is your name ? "))

white = open("names.txt" , "r+")

def find():
    for i in white.readlines():
        if black in i:
            print "Hi"
        else:
            white.write(black)
            print "Invalid Choice"
    white.close()
find()