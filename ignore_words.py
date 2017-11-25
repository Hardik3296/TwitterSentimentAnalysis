#Function to create dictionary of common words that need to be ignore_words
#when checking for new words like a, an, the, is, if,etc
def ignore_words():
    words={};
    file=open("ignore.txt","r");
    for w in file:
        string = w.split('\n');
        words[string[0]]=True;
    file.close();
    return words;
