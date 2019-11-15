#I have to write a function
import os

def checkOpen():
    path = os.path.join('C:\\', 'Munster', 'Python', 'Baumberge.gpx')
    isExist = os.path.exists(path)
    if(isExist):
        #print("the file is there")
        openfile = open(path, "r")
        show = openfile.read()
        openfile.closed
        print(show)
    else:
        print("none")
    
checkOpen()

