import pickle
import pandas as pd

movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', "rb"))

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    top_5 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    for i in top_5:
        movie_id = movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

movie_name=input("Enter the name of the movie you want to take recommendations from : ")
movies=recommend(movie_name)
for movie in movies:
    print(movie)