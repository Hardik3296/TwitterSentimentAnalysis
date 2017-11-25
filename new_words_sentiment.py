#Function to calculate sentiment value of new words found in the tweet
def new_words_sentiment(new_words,tweet={}):
    file=open("sentiment_new_words.txt","w");
    res = 0.0
    #Loop to calculate the new word from the tweet that are not present in dictionary
    for words in new_words:
        value = 0;
        count = 0;
        #Reading each line in tweet
        for line in tweet:
            string = line.split();
            for word in string:
                #Checking every word of the string in dictionary
                if word == words:
                    #If word is new calculate the net value of the word
                    value = value + tweet[line];
                    #Calculate thefrequency of the word
                    count = count + 1;
                    break;
        if count != 0:
            res = value/count;
            #If value goes beyond lower range the bring the value to the lower limit
            if res < -5:
                res = -5;
                #If value goes beyond upper limit the bring the value to upper limit
            elif res > 5:
                res = 5;
            else:
                res = int(res);
        #Storing the value of the new word with the new word in a file
        file.write(words+" "+str(res)+"\n");
    file.close();
