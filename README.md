# TwitterSentimentAnalysis
This project involves extracting the tweets from the twitter page on a particular topic and calculating its sentiment value using AFINN-111.txt file.
The approach of the project is to select a particular tweet, remove all the unwanted characters from the tweet, find out the total value of the tweet by summing the values of the individual words whose values are already defined in AFINN-111.txt file. The new words encountered are also to be provided new values defining their sentiment value. For this I calculae the sum of the values of the tweet in which the new words appeared and then divided the sum by the number of different tweets in which they appeared.

## Explanantion for different files
<dl>
	<dt>create_dictionary.py</dt>
	<dd>This code is used to create a python dictionary out of the word present in AFINN-111.txt. The words are used as the keys while their sentiment values are used as values in the dictionary</dd>
	<dt>ignore_words.py</dt>
	<dd>This code creates the dictionary of the words that are to be ignored when finding new words whose sentiment value needs to be calculated.</dd>
	<dt>new_words_sentiment.py</dt>
	<dd>This code is used to claculate the sentiment values of the new wird that are found in the tweet, after ignoring the common words. Since the sentiment value can range between <strong>-5</strong> and <strong>5</strong>, therefore if the average value comes out to be less than <b>-5</b> or greater than <b>5</b>, then they are given values equal to their respective limits.</dd>
	<dt>processTweet.py</dt>
	<dd>This code is used to refine the extracted tweets by removing all the unnecessary characters that are not part of the words like <b>#</b>, <b>usernames</b>, etc. For this purpose I have used Regular Expressions.</dd>
	<dt>tweet_sentiment.py</dt>
	<dd>This code is used to fin the overall sentiment value of each individual tweet on the basis of the different words present in the tweet.</dd>
</dl>
	For any suggestions or query , feel free to contact me at @hardikgaur@geu.ac.in
