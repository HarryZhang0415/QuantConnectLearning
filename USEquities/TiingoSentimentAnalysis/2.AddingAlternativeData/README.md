# Adding Alternative Data
Alpha models should not assume a specific list of securities so we should request alternative data for our securities in the Alpha Model's **OnSecuritiesChanged()** method when new securities are added. This allows our alpha to be easily applied on other universes.

    for security in changes.AddedSecurities:
        # When new assets are added to the universe, request data 
        news = algorithm.AddData(TiingoNews, security.Symbol)

## Accessing Alternative Data
We access alternative data with the **Get()** helper method. This helper returns a dictionary where each entry is a list of alternative data objects; keyed by the alt-data symbol. Like all data in QuantConnect, alternative data feeds also have a **Symbol**.

    # Example: Access the TiingoNews data dictionary 
    data = data.Get(TiingoNews)

Data dictionaries have a number of properties that can be accessed by iterating through the dictionary **Values**. You can find the properties of each alternative data object in alterative data documentation.

    # Examples: TiingoNews object properties
    self.Description   # Sentence summary of article
    self.Symbols       # Symbol list of mentioned companies

## Assigning Sentiment Scores to Paragraphs
Raw text is analyzed with Natural Language Processing (NLP) techniques that automate the process of assigning meaning to language-based data.

One application of NLP is analyzing text for its emotion, or sentiment. A basic form of sentiment analysis assigns a positive or negative polarity score to words in a document. We can create rules of what polarity scores to assign words that commonly occur in our documents.

    # Example of polarity score rules 
    {"bad": -0.5, "good": 0.5, "negative": -0.5, 
    "great": 0.5, "growth": 0.5, "fail": -0.5} 

To assign sentiment scores to text, iterate through the polarity score dictionary keys, and if the word is a word in the text, save the dictionary value, or score, to a list.

    for sentence in paragraph:
        # Parse the sentence into a list of words
        words = sentence.lower().split(" ")
        # Assign a sentiment score to a word if 
        # that word is in the polarity score dictionary
        # Sum the scores so each sentence has one score
        scores = sum([self.wordScores[word] for word in words
                    if word in self.wordScores])
