from transformers import pipeline

#Initialize the sentiment analysis model
sentiment_pipeline = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")

def analyze(text:str)->str:
    #Mapping prediction label to the desired output
    label_dict = {"POS":"positive", "NEU":"neutral", "NEG":"negative"}
    # Perform sentiment analysis on the text
    preds = sentiment_pipeline(text)
    # Return the corresponding label from the label dictionary
    return label_dict[preds[0]['label']]


if __name__ == "__main__":
    analyze("I love python.")
    print("All set.....")