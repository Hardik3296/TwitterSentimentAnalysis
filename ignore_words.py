
def ignore_words():
    words={};
    #print("In ignore.txt");
    file=open("ignore.txt","r");
    for w in file:
        string = w.split('\n');
        words[string[0]]=True;
    file.close();
    return words;