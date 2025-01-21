import pandas as pd

filename = r'/Users/rumana/Documents/YouTube/TaylorSpark/DrSpark_MSE2001python/module_examples/data_for_exercises/fantasy_sets.csv'
df = pd.read_csv(filename)

LoTR = df['LOTR'].dropna()
StarWars = df['SW'].dropna()
HarryPotter = df['HP'].dropna()

LoTR = set(LoTR)
StarWars = set(StarWars)
HarryPotter = set(HarryPotter)
