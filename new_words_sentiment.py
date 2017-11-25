
def new_words_sentiment(new_words,tweet={}):
    file=open("sentiment_new_words.txt","w");
    #print(new_words);
    #print(tweet);
    res = 0.0
    for words in new_words:
        #print(words);
        value = 0;
        count = 0;
        for line in tweet:
            #print(line);
            string = line.split();
            for word in string:
                if word == words:
                    value = value + tweet[line];
                    count = count + 1;
                    break;
        if count != 0:
            res = value/count;
            if res < -5:
                res = -5;
            elif res > 5:
                res = 5;
            else:
                res = int(res);
        file.write(words+" "+str(res)+"\n");
    file.close();
            