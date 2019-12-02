# The folder directory is C://xxx/yyy/Baumberge.gpx'
import os

def checkOpen():
    path = os.path.join('C:\\', 'xxx', 'yyy', 'Baumberge.gpx')
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

