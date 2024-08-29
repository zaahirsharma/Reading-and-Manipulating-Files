'''
with open("Celcius.dat.txt", "r") as myFile:
    newFile = open("Fahrenheit.dat", "w")
    line = myFile.readline()
    while line != "":
        num = int(line)
        num = (num*9/5)+32
        newFile.write(str(num)+"\n")
        line = myFile.readline()
'''
# The Celcius.dat.txt has not been uploaded but others can create their own
# with each Celcius temperature on a new line and use this code for conversion.
