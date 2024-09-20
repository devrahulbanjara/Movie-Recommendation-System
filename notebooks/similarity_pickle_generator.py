import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

with open("movie_dict.pkl", "rb") as f:
    movies_dict = pickle.load(f)

movies = pd.DataFrame(movies_dict)

def format_keywords(row):
    overview = row['overview'] if isinstance(row['overview'], str) else ''
    genres = ' '.join(row['genres']) if isinstance(row['genres'], list) else ''
    cast = ' '.join(row['cast']) if isinstance(row['cast'], list) else ''
    crew = ' '.join(row['crew']) if isinstance(row['crew'], list) else ''
    return overview + ' ' + genres + ' ' + cast + ' ' + crew

movies['allkeywords'] = movies.apply(format_keywords, axis=1)

cv = CountVectorizer(max_features=5000, stop_words="english")
vectors = cv.fit_transform(movies["allkeywords"]).toarray()
similarity = cosine_similarity(vectors)

with open("similarity.pkl", "wb") as f:
    pickle.dump(similarity, f)

print("similarity.pkl generated successfully.")
