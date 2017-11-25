#Function to calculate the sentiment value of each tweet
def tweet_sentiment(dictionary={},ignore_dict={}):
    file = open("tweetstemp.txt","r");
    file1 = open("sentmentFile.txt","w");
    file2 = open("new_words.txt","w");
    file3 = open("words_already_present.txt","w");
    #Dictionary to store value of individual tweet
    tweet={};
    #List to store the new words present in the tweet
    new_words=[];
    for line in file:
        string = line.split();
        ans=0;
        for words in string:
            #Adding the sentiment value of each individual word
            if words in dictionary:
                ans = ans + dictionary[words];
            else:
              key = ignore_dict.get(words,False);
              #Ignoring the common words
              if key is False:
                  new_words.append(words);
                  file2.write(words+"\n");
              elif key is True:
                  file3.write(words+"\n");
        file1.write(line+"\t"+str(ans)+"\n");
        tweet[line]=ans;
    file.close();
    file2.close();
    file1.close();
    file3.close();
    return (new_words,tweet);
