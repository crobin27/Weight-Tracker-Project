from asyncore import read
import matplotlib.pyplot as plt
from datetime import date
import numpy as np

#left off with the axes hard to see and an unfriendly graph
#look into better ways to use matplotlib to plot/customize graph
#maybe create a desktop shortcut to run the file?

#gets todays date in mm/dd/yy format, consider trying without year
def getDate():
    today = date.today()
    today = today.strftime("%m/%d/%y")
    return today

#get todays weigh in
def getWeight():
    weight = input("What Was Your Weight Today\n")
    return weight

#append given data to corresponding file
def writeFile(fileName, text):
    file = open(fileName, "a")
    file.write(text + "\n")
    file.close()

def readFile(fileName, floatflag):
    file = open(fileName, "r")
    fileData = file.readlines()
    #strip the trailing newline
    fileData = [string.rstrip() for string in fileData]
    #convert the weight values to floats
    if (floatflag):
        fileData = [float(value) for value in fileData]
    return fileData

def myplot(xAxis, yAxis):
    plt.plot(xAxis, yAxis, color='red', marker='o')
    plt.title("Cole's Weight Loss Over Time")
    plt.ylabel("Weight in lbs")
    plt.xlabel("Date")
    plt.grid(True)
    plt.show()


def main():
    #obtain todays date and weigh in
    todaysWeight = getWeight()
    todaysDate = getDate()
    #write the corresponding values to corresponding files
    writeFile("dates.txt", todaysDate)
    writeFile("weights.txt", todaysWeight)
    #obtain float lists of both sets of data
    dates = readFile("dates.txt", False)
    weights = readFile("weights.txt", True)

    print("Your weight has been logged, check out your progress plot")
    myplot(dates, weights)


main() 
