import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import init, Fore
import time
import sys

# Initialize colorama
init(autoreset=True)

# Load movie dataset
movies = pd.read_csv('movies.csv')

# Preprocess movie titles and genres
movies['genres'] = movies['genres'].str.split('|')
movies['genres'] = movies['genres'].apply(lambda x: ' '.join(x))

# Combine title and genres into a single 'tags' column
movies['tags'] = movies['title'] + ' ' + movies['genres']

# Initialize TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['tags'])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend movies based on a given title
def recommend_movie(title, cosine_sim=cosine_sim):
    idx = movies.index[movies['title'] == title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices]

# Function to analyze mood and suggest genre
def analyze_mood_and_suggest_genre(mood_input):
    sentiment = TextBlob(mood_input).sentiment.polarity
    if sentiment > 0.1:
        return 'Comedy'
    elif sentiment < -0.1:
        return 'Drama'
    else:
        return 'Action'

# Function to display a loading animation
def loading_animation():
    for _ in range(3):
        sys.stdout.write(Fore.GREEN + ".")
        sys.stdout.flush()
        time.sleep(0.5)
    print()

# Main function to run the recommendation system
def run_recommendation_system():
    print(Fore.CYAN + "Welcome to the AI Movie Recommendation System!")
    print("Available genres: Action, Comedy, Drama, Romance, Thriller")
    
    genre_input = input("Please select a genre: ").capitalize()
    mood_input = input("How are you feeling today? ")

    suggested_genre = analyze_mood_and_suggest_genre(mood_input)
    print(f"Based on your mood, we suggest {suggested_genre} movies.")

    print("Processing your request", end="")
    loading_animation()

    recommended_movies = recommend_movie('The Dark Knight')  # Example movie
    print(Fore.YELLOW + "Recommended Movies:")
    for movie in recommended_movies:
        print(movie)

    repeat = input("Would you like another recommendation? (yes/no): ").lower()
    if repeat == 'yes':
        run_recommendation_system()
    else:
        print("Thank you for using the AI Movie Recommendation System!")

# Run the recommendation system
if __name__ == "__main__":
    run_recommendation_system()
