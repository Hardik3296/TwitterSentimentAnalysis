#Function to create dictionary from the words already present in words.txt
def create_dictionary():
    str1=[];
    dictionary={};
    file=open("words.txt","r");
    for line in file:
        str1 = line.split();
        dictionary[ str1[0] ] = int(str1[1]);
    file.close();
    return dictionary;
