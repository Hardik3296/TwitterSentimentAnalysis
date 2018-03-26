from importlib import import_module
import sys

#Function to extract tweets for the file
def extract_tweet(line):
    string = line.split("\t");
    return string[2];


def main():
    dictionary = {};
    imp2 = import_module("create_dictionary");
    dictionary = imp2.create_dictionary();
    file = open(sys.argv[1],"r");
    file2 = open("temp.txt","w");
    #extracting individual tweet from the dataset
    for line in file:
        line = extract_tweet(line);
        file2.write(line+"\n");
    file2.close();
    file.close();
    file2 = open("temp.txt","r");
    file1 = open("tweetstemp.txt","w");
    #Removing the unwanted words and symbols from the tweet
    imp3 = import_module("processTweet");
    for line in file2:
        line = imp3.processTweet(line);
        file1.write(line+"\n");
    file1.close();
    file2.close();
    ignore_dict = {};
    imp1 = import_module("ignore_words");
    #Finding the words to be ignored
    ignore_dict = imp1.ignore_words();
    im = import_module("tweet_sentiment");
    #Calculating the sentiment value of each tweet
    (new_words , tweet) = im.tweet_sentiment(dictionary,ignore_dict);
    imp4 = import_module("new_words_sentiment");
    imp4.new_words_sentiment(new_words,tweet);

if __name__ == '__main__':
    main();
