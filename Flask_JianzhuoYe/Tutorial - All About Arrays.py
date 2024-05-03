def ArrayInfo():
    numarray = [4,2,10,5,22,0];
    stringarray = ["to","Welcome","my class!"];

    #Length an array
    numarraylen = len(numarray);
    print("The length of the array, num array is ",numarraylen);
    print("-------------");

    #Sorting an array
    stringarray.sort();
    print("The array, stringarray, in order is",stringarray);
    print("-------------");

    #Indexing an array - Selecting a specific index
    print(stringarray[0]);
    print(numarray[1]);
    print(stringarray[2]);
    print(numarray[3]);
    print("-------------");

    #Looping through an array
    for i in range(0,numarraylen):
        print(numarray[i]);
    print("-------------");

    #Slicing an array to access a specific range
    whichpos = stringarray[0:2];
    print(whichpos);
    print("-------------");

    #Adding new itmes to an array
    newword = "Hello";
    stringarray.append(newword);
    print(stringarray);
    print("-------------");

    #Inserting a new item into an array
    newword = "Hello!";
    stringarray.insert(0,newword);
    print(stringarray);
    print("-------------");

def main():
    ArrayInfo();

if __name__ == "__main__":
    main();
