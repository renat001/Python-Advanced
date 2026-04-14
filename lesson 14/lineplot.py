import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("avgQperCountry.csv")

avg_iq_by_continent = df.groupby("Continent")["Average IQ"].mean()
plt.figure(figsize=(10,6))

avg_iq_by_continent.plot(kind='line', marker='o',color='skyblue')

plt.title('Average IQ by Continent')
plt.xlabel('Continent')
plt.ylabel('Avarage IQ')

plt.grid(axis='both', linestyle='--', alpha= 1)
plt.show()

