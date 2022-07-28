import pandas as pd
import numpy as np

url1 = 'https://www.nrc.nl/feeds/wilde-tuin/kaart.csv'
df = pd.read_csv(url1)
df.loc[(df['soortgroep'] != 'Planten') & (df['soortgroep'] != 'Vogels')]
df = df[['datum','soort','soortgroep','foto']]
print(df.head(10))
df.to_csv(r'beestjesselectie.csv', index = True)
