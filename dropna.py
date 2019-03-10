import pandas as pd
import numpy as np
df = pd.read_csv('ans10000.csv')
df=df.dropna()
name='Cleandata.csv'
df.to_csv(name, encoding='utf-8', index=True)   