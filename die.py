import pandas as pd
import matplotlib.pyplot as plt

die = pd.DataFrame([1, 2, 3, 4, 5, 6])
trial = 50
results = [die.sample(2, replace=True).sum().loc[0] for i in range(trial)]

freq = pd.DataFrame(results)[0].value_counts()
sort_freq = freq.sort_index()

print(sort_freq)

