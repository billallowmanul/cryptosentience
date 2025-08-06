from .twitter_client import fetch_recent_tweets
from .sentiment_index import compute_sentiment_index
from .utils import visualize_mood_index

def run_sentiment_analysis(coin_symbol):
    query = f"${coin_symbol} OR {coin_symbol} crypto"
    print(f"Fetching tweets for query: {query}")
    tweets = fetch_recent_tweets(query)
    
    if not tweets:
        print("No tweets found.")
        return

    sentiment_df = compute_sentiment_index(tweets)
    print(sentiment_df.tail())
    visualize_mood_index(sentiment_df, coin_symbol)
