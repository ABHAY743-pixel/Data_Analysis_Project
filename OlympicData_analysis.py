# importing all necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# read athlete events data
data = pd.read_csv(r"C:\Users\gupta\Downloads\athlete_events.csv")

# data.head() display first 5 entry
# data.describe  about model
# data.info give info about data
print(data.head(), data.describe(), data.info())

# regions and country noc data csv file
regions = pd.read_csv(r"C:\Users\gupta\Downloads\datasets_31029_40943_noc_regions.csv")
print(regions.head())

# merging to data and regions frame
merged = pd.merge(data, regions, on='NOC', how='left')
print(merged.head())

# creating goldmedal dataframes
goldMedals = merged[(merged.Medal == 'Gold')]
print(goldMedals.head())


# Plotting the distribution of Gold Medals by Age

plt.figure(figsize=(20, 10))
plt.title('Distribution of Gold Medals')
sns.countplot(goldMedals['Age'])
plt.show()

#Print the number of athletes who are gold medalists and whose age is greater than 50 with their info.
goldMedals = merged[(merged.Medal == 'Gold')]
print('The no of athletes is',
      goldMedals['ID'][goldMedals['Age'] > 50].count(), '\n')
print(goldMedals[goldMedals['Age'] > 50])

#Creating a new dataframe called masterDisciplines in which we will insert this new set of people
masterDisciplines = goldMedals['Sport'][goldMedals['Age'] > 50]
plt.figure(figsize=(20, 10))
plt.tight_layout()
sns.countplot(masterDisciplines)
plt.title('Gold Medals for Athletes Over 50')
plt.show()

#Display all women athletes who have played in the summer season
womenInOlympics = merged[(merged.Sex == 'F') &
                         (merged.Season == 'Summer')]
print(womenInOlympics.head(10))

sns.set(style="darkgrid")
plt.figure(figsize=(20, 10))
sns.countplot(x='Year', data=womenInOlympics)
plt.title('Women medals per edition of the Games')
plt.show()

#Here we are going to print the top 5 countries and show them in the graph with catplot.

print(goldMedals.region.value_counts().reset_index(name='Medal').head())

totalGoldMedals = goldMedals.region.value_counts()
.reset_index(name='Medal').head(5)
g = sns.catplot(x="index", y="Medal", data=totalGoldMedals,
                height=6, kind="bar", palette="muted")
g.despine(left=True)
g.set_xlabels("Top 5 countries")
g.set_ylabels("Number of Medals")
plt.title('Medals per Country')
plt.show()

#Players weight analysis:- Here we are going to see how weight over year for Male Lifters via graphical representation using pointplot.

MenOverTime = merged[(merged.Sex == 'M') &
                     (merged.Season == 'Summer')]
wlMenOverTime = MenOverTime.loc[MenOverTime['Sport'] == 'Weightlifting']

plt.figure(figsize=(20, 10))
sns.pointplot('Year', 'Weight', data=wlMenOverTime, palette='Set2')
plt.title('Weight over year for Male Lifters')
plt.show()

