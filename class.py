import os 
import shutil 
source = input("Enter the full path for the source") 
destination = input("Enter the destinaion folder") 
source = source + '/' 
destination = destination + '/' 
listoffiles = os.listdir(source) 
for file in listoffiles: 
    shutil.copy((source+file), destination)
