import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df_marvel = pd.read_csv('data/marvel-wikia-data.csv')
df_dc = pd.read_csv('data/dc-wikia-data.csv')

df_marvel.head()
df_dc.head()
df_marvel.info()
