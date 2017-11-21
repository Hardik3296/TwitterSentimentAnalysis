
def create_dictionary():
    str1=[];
    dictionary={};
    file=open("words.txt","r");
    #file1=open("tweetdataset/indicated_output.txt","w")
    for line in file:
        str1 = line.split();
        #print (str1[0] + " " + str1[1]);
        dictionary[ str1[0] ] = int(str1[1]);
        #file1.write(str1[0]+"\t"+str1[1]+"\n");
    file.close();
    return dictionary;
    #file1.close();