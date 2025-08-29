import pickle
import pandas as pd

movies = pickle.load(open("movies.pkl", "rb"))
print(type(movies))
print(movies.head())
print(movies.columns)
