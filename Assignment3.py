"""
importing pandas,numpy library
importing urllib for importing and accessing data from provided link-url
seaborn and matplotlib for heatmap representation and ploting data in graph for data
visualization
"""
import pandas as pd
import numpy as np
import urllib
import pandas as pd
import numpy as np
from numpy.random import randn
import requests
import io
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
from urllib.request import urlretrieve
#url address for data import
#url=('https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv')
#df=urlretrieve(url,'FiveYData.csv')
#print(df)
#reading data in csv file
df1 = pd.read_csv('FiveYData.csv')
#creating dataFrame on csv file data
da=pd.DataFrame(df1)
print("DataFrame is:\n",da)
#reindexing data
print(da.reindex())
#printing and removing duplicate data
print("About DuplicateData:\n(True only for Unique elements)\n",da.duplicated())
print("Count of Dupliated values:\n",da.duplicated().sum())
print("Droping Duplicates:\n",da.drop_duplicates(inplace=True))
print("Droping from file:\n",df1.drop_duplicates(inplace=True))
#creating pivot_table
df2=da.pivot_table(index='continent',columns='year',values='lifeExp')
print("Pivote_table:\n",df2)
#assigning size to fig of heatma[
plt.figure(figsize=(2,2))
#creating heat map and providing color and margins
sns.heatmap(df2,fmt="g", linewidths=.5,cmap="plasma")
"""
labeling x and y axix along with giving name to Heatmap fig
"""
plt.title("FiveYearData")
plt.ylabel("continent")
plt.xlabel("Year")
#saving output image
plt.savefig("Save2.png")
plt.show()