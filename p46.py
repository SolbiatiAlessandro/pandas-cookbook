"""
task: is the director inside the cast
task: how many likes of the cast come from actor1,actor2,actor3
"""

import pandas as pd

movies = pd.read_csv('./data/movie.csv')
dc = movies['director_facebook_likes'].fillna(0) >= movies['cast_total_facebook_likes'].fillna(0) 
print("is director inside the cast?\n"+ str(dc.all()))

print("likes from actor1actor2actor3 in cast")
a = movies['actor_1_facebook_likes']+movies['actor_2_facebook_likes']+movies['actor_3_facebook_likes']
a.fillna(0)
res = a/movies['cast_total_facebook_likes']
print res.fillna(0).head(5)

