'''
Name: Jianzhuo Ye
Start Date: 5/2/24
End Date: 5/3/24
Description: This program introduces the use of the os.path library in python
'''
import os.path
from os import path


def main():
    print('W - Write, C - Create, R - Read, A - Append')
    selected = str(input("select an option")
    selected.toUpper()
    CheckFile();

def CheckFile():
    filename = str(input("Enter the file name to confirm if it exists: "));
    filename = filename + ".txt";

    ifexists = bool(path.exists(filename));

    if ifexists == False:
        #Create the file
        pythfile = open(filename,'w'); #'w' means write. This deletes all previous info. 'a' would append without deleting.
        print('File created successfully!');
    else:
        #Reads the contents of the file and displays it
        pythfile = open(filename,'r');
        print(pythfile.readline());

    pythfile.close();

if __name__ == "__main__":
    main();
