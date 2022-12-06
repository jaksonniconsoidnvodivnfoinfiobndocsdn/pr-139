import pandas as pd 
import numpy as np 
df1 = pd.read_csv('sharedArticles.csv')
df2 = pd.read_csv('usersInteractions.csv')
print(df1.head())
print(df2.head())
df1 = df1[df1['eventType'] == 'CONTENT SHARED']
print(df1.head())
print(df2.shape)
print(df1.shape)
def findTotalEvents(df1Row):
    totalLikes = df2[(df2['contentId'] == df1Row['contentId']) & (df2['eventType'] == 'LIKE')].shape[0]
    totalViews = df2[(df2['contentId'] == df1Row['contentId']) & (df2['eventType'] == 'VIEW')].shape[0]
    totalBookmarks = df2[(df2['contentId'] == df1Row['contentId']) & (df2['eventType'] == 'BOOKMARK')].shape[0]
    totalFollows = df2[(df2['contentId'] == df1Row['contentId']) & (df2['eventType'] == 'FOLLOW')].shape[0]
    totalComments = df2[(df2['contentId'] == df1Row['contentId']) & (df2['eventType'] == 'COMMENT CREATED')].shape[0]
    return totalLikes + totalViews + totalBookmarks + totalFollows + totalComments
df1['totalEvents'] = df1.apply(findTotalEvents, axis = 1)
print(df1.head())
df1 = df1.sort_values(['totalEvents'], ascending = [False])
print(df1.head())