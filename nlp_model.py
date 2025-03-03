from transformers import pipeline  
import pandas as pd  

def analyze_esg_sentiment(texts: list) -> dict:  
    """Detect negative sentiment in news headlines using DistilBERT."""  
    classifier = pipeline('sentiment-analysis', model='distilbert-base-uncased')  
    results = {"negative": 0, "positive": 0}  
    for text in texts:  
        result = classifier(text[:512])[0]  # Trim to model limit  
        results[result['label'].lower()] += 1  
    return results  

# Example usage:  
# news_titles = ["Company X accused of deforestation", "Company Y invests in solar energy"]  
# sentiment = analyze_esg_sentiment(news_titles)  
