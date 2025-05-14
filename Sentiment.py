from textblob import TextBlob
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Extract polarity and subjectivity
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    
    # Determine sentiment category
    if polarity > 0:
        sentiment = "Positive"
        color = Fore.GREEN
    elif polarity < 0:
        sentiment = "Negative"
        color = Fore.RED
    else:
        sentiment = "Neutral"
        color = Fore.YELLOW
    
    # Display results with color
    print(color + f"Sentiment: {sentiment}")
    print(f"Polarity: {polarity:.2f}")
    print(f"Subjectivity: {subjectivity:.2f}")

# Sample text for analysis
sample_text = "I absolutely love this product! It's amazing."

# Analyze and display sentiment
analyze_sentiment(sample_text)
