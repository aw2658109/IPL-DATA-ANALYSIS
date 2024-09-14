import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data1=pd.read_csv("deliveries.csv")
data2=pd.read_csv("matches.csv")

#EXPLORE MATCHES DATA:
print(data2.head(5))

#EXPLORE DELIVERIES DATA:
print(data1.head(5))

# FIND ROW AND COLUMNS:
print(data2.shape)
print(data1.shape)

# INFO FUNCTION:
print(data1.info())
print(data2.info())

#DESCRIBE FUNCTION:
print(data1.describe())
print(data2.describe())

#MERGING DATASET:
df=pd.merge(data1,data2,left_on='match_id',right_on='id')
print(df.head(5))

#DESCRIBE FUNCTION:
print(df.describe())

#DATA VISUALIZATION:
plt.figure(figsize=(16,8))
sns.countplot(x='season', data=data2)
plt.title("Number of match play in each season",fontsize=15)
plt.xlabel('season',fontsize=15)
plt.xticks(rotation=0,fontsize=15)
plt.ylabel("Number of matche", fontsize=15)
plt.show()

# TEAM PLAY EACH SEASON:
plt.figure(figsize=(16,8))
data2.groupby('season')['team1'].nunique().plot(kind='bar',color='m')
plt.title('Team play each season',fontsize=15)
plt.xlabel('season',fontsize=15)
plt.xticks(rotation=0,fontsize=15)
plt.ylabel('Number of team',fontsize=15)
plt.show()

#VENUE WHERE MOST MATCH OCCURED:
plt.figure(figsize=(16,8))
sns.countplot(x='venue', data=data2, order=data2['venue'].value_counts().index)
plt.title('Venue which hosted most number of IPL matches', fontsize=15)
plt.xlabel('Venue', fontsize=15)
plt.xticks(rotation=45, ha='right', fontsize=12) 
plt.ylabel('Number of matches', fontsize=15)
plt.tight_layout()
plt.show()

#MOST WINNING TEAM:
winning_team = data2[['season', 'winner']]
winner_team = {}

for i in sorted(winning_team.season.unique()):
    winner_team[i] = winning_team[winning_team.season == i]['winner'].tail(1).values[0]
winner_IPL = pd.Series(winner_team)

winner_IPL = pd.DataFrame(winner_IPL, columns=['yearly winning Team'])
print(winner_IPL)

# OUTSTANDING TEAM WHICH HAS WON MOST OF THE IPL MATCHES:
plt.figure(figsize=(16, 8))
winner_IPL['yearly winning Team'].value_counts().plot(kind='bar', color='b')
plt.title("Winner of IPL Across 11 Seasons", fontsize=15)
plt.xlabel("Name of Team", fontsize=15)
plt.xticks(rotation=45, fontsize=15)
plt.ylabel("Number of Seasons", fontsize=15)
plt.show()

#TOSS DECISION:
plt.figure(figsize=(16, 8))
(data2['toss_decision'].value_counts()).plot(
    kind='pie',
    startangle=210,
    autopct='%2.3f%%',
    shadow=True,
    explode=(0, 0.1),
    colors=['r', 'orange'],
    fontsize=15
)
plt.title('Decision Taken by Captain After Winning Toss', fontsize=15)
plt.show()

# INDIVIDUAL TEAM TOSS DECISION AFTER WINNING TOSS:
plt.figure(figsize=(16,8))
sns.countplot(x='toss_winner', data=data2, hue='toss_decision',palette='rocket')
plt.title('individual team toss decision after winning toss', fontsize=15)
plt.xlabel('Team',fontsize=15)
plt.xticks(rotation=90, fontsize=15)
plt.ylabel('Frequence',fontsize=15)
plt.show()

# TOP PLAYERS WITH MOST MAN OF THE MATCH:
plt.figure(figsize=(16,8))
sns.countplot(x='player_of_match', data=data2, order=data2['player_of_match'].value_counts().head(15).index)
plt.title('Top player with most man of the match',fontsize=15)
plt.xlabel('Players', fontsize=15)
plt.xticks(rotation=90, fontsize=15)
plt.ylabel('Frequency', fontsize=15)
plt.show()

# TOP WICKET TAKER OF IPL:
df.groupby('bowler')['player_dismissed'].count().sort_values(ascending=False).head(10).plot(kind='bar', figsize=(16, 8), color='purple')
plt.title('Top Wicket Taker of IPL', fontsize=15)
plt.xlabel('Bowlers', fontsize=15)
plt.xticks(rotation=90, fontsize=15)
plt.ylabel('Total Wickets Taken', fontsize=15)
plt.show()

