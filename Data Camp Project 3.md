# Comparing Apps in the Android App Market

```
# Read in dataset
import pandas as pd
apps_with_duplicates = pd.read_csv('datasets/apps.csv')

print(apps_with_duplicates.head())
# # Drop duplicates from apps_with_duplicates
apps = apps_with_duplicates.drop_duplicates()

# # Print the total number of apps
print('Total number of apps in the dataset = ', str(apps.count()))

# # Have a look at a random sample of 5 rows
print(apps.sample(5))
```

```
# Output
   Unnamed: 0                                                App  \
0           0     Photo Editor & Candy Camera & Grid & ScrapBook   
1           1                                Coloring book moana   
2           2  U Launcher Lite – FREE Live Cool Themes, Hide ...   
3           3                              Sketch - Draw & Paint   
4           4              Pixel Draw - Number Art Coloring Book   

         Category  Rating  Reviews  Size     Installs  Type Price  \
0  ART_AND_DESIGN     4.1      159  19.0      10,000+  Free     0   
1  ART_AND_DESIGN     3.9      967  14.0     500,000+  Free     0   
2  ART_AND_DESIGN     4.7    87510   8.7   5,000,000+  Free     0   
3  ART_AND_DESIGN     4.5   215644  25.0  50,000,000+  Free     0   
4  ART_AND_DESIGN     4.3      967   2.8     100,000+  Free     0   

  Content Rating                     Genres      Last Updated  \
0       Everyone               Art & Design   January 7, 2018   
1       Everyone  Art & Design;Pretend Play  January 15, 2018   
2       Everyone               Art & Design    August 1, 2018   
3           Teen               Art & Design      June 8, 2018   
4       Everyone    Art & Design;Creativity     June 20, 2018   

          Current Ver   Android Ver  
0               1.0.0  4.0.3 and up  
1               2.0.0  4.0.3 and up  
2               1.2.4  4.0.3 and up  
3  Varies with device    4.2 and up  
4                 1.1    4.4 and up  
Total number of apps in the dataset =  Unnamed: 0        9659
App               9659
Category          9659
Rating            8196
Reviews           9659
Size              8432
Installs          9659
Type              9659
Price             9659
Content Rating    9659
Genres            9659
Last Updated      9659
Current Ver       9651
Android Ver       9657
dtype: int64
      Unnamed: 0                            App            Category  Rating  \
8516        9655  EO App. SelfCompassion to you  HEALTH_AND_FITNESS     NaN   
6888        7950                CV Formats 2018              FAMILY     4.3   
8130        9250                   Arrayanes EC           LIFESTYLE     NaN   
5664        6695                  BR Classified            BUSINESS     NaN   
7161        8235         DB for Fallout Shelter              FAMILY     4.0   

      Reviews  Size  Installs  Type Price Content Rating            Genres  \
8516        1   NaN      100+  Free     0       Everyone  Health & Fitness   
6888      374  26.0  100,000+  Free     0       Everyone         Education   
8130        2   7.9      100+  Free     0       Everyone         Lifestyle   
5664        0  28.0       50+  Free     0       Everyone          Business   
7161     3323  47.0  100,000+  Free     0       Everyone        Simulation   

            Last Updated         Current Ver         Android Ver  
8516  September 12, 2015  Varies with device  Varies with device  
6888     October 9, 2017                   1        4.0.3 and up  
8130       June 27, 2018                 3.5          4.4 and up  
5664     August 30, 2017                   1          4.2 and up  
7161      March 29, 2018                 1.9          4.0 and up
```

## Cleaning
```
# List of characters to remove
chars_to_remove = ['+', ',', '$', '</code>']
# List of column names to clean
cols_to_clean = ['Installs', 'Price']

# Loop for each column in cols_to_clean
for col in cols_to_clean:
    # Loop for each char in chars_to_remove
    for char in chars_to_remove:
        # Replace the character with an empty string
        apps[col] = apps[col].apply(lambda x: x.replace(char, ''))
        
# Print a summary of the apps dataframe
print(apps.info)
```

```
# Sample of Output
# checking to see if we've removed unnecessary characters from digits

                  Category  Rating  Reviews  Size  Installs  Type Price  \
0          ART_AND_DESIGN     4.1      159  19.0     10000  Free     0   
1          ART_AND_DESIGN     3.9      967  14.0    500000  Free     0   
2          ART_AND_DESIGN     4.7    87510   8.7   5000000  Free     0   
3          ART_AND_DESIGN     4.5   215644  25.0  50000000  Free     0   
4          ART_AND_DESIGN     4.3      967   2.8    100000  Free     0   
5          ART_AND_DESIGN     4.4      167   5.6     50000  Free     0   
6          ART_AND_DESIGN     3.8      178  19.0     50000  Free     0   
7          ART_AND_DESIGN     4.1    36815  29.0   1000000  Free     0   
8          ART_AND_DESIGN     4.4    13791  33.0   1000000  Free     0   
9          ART_AND_DESIGN     4.7      121   3.1     10000  Free     0   
10         ART_AND_DESIGN     4.4    13880  28.0   1000000  Free     0   
11         ART_AND_DESIGN     4.4     8788  12.0   1000000  Free     0   
12         ART_AND_DESIGN     4.2    44829  20.0  10000000  Free     0
```

## Correcting Data Types
```
import numpy as np

# Convert Installs to float data type
apps['Installs'] = apps['Installs'].astype(np.float)

# Convert Price to float data type
apps['Price'] = apps['Price'].astype(np.float)

# Checking dtypes of the apps dataframe
print(apps.dtypes)
```

```
# Output
Unnamed: 0          int64
App                object
Category           object
Rating            float64
Reviews             int64
Size              float64
Installs          float64
Type               object
Price             float64
Content Rating     object
Genres             object
Last Updated       object
Current Ver        object
Android Ver        object
dtype: object
```

## Exploring App Categories
```
import plotly
plotly.offline.init_notebook_mode(connected=True)
import plotly.graph_objs as go

# Print the total number of unique categories
num_categories = len(apps['Category'].unique())
print('Number of categories = ', num_categories)

# Count the number of apps in each 'Category'. 
num_apps_in_category = apps['Category'].value_counts()

# Sort num_apps_in_category in descending order based on the count of apps in each category
sorted_num_apps_in_category = num_apps_in_category.sort_values(ascending = False)

data = [go.Bar(
        x = num_apps_in_category.index, # index = category name
        y = num_apps_in_category.values, # value = count
)]

plotly.offline.iplot(data)
```

## Distribution of App Ratings
```
# Average rating of apps
avg_app_rating = apps['Rating'].mean()
print('Average app rating = ', avg_app_rating)

# Distribution of apps according to their ratings
data = [go.Histogram(
        x = apps['Rating']
)]

# Vertical dashed line to indicate the average app rating
layout = {'shapes': [{
              'type' :'line',
              'x0': avg_app_rating,
              'y0': 0,
              'x1': avg_app_rating,
              'y1': 1000,
              'line': { 'dash': 'dashdot'}
          }]
          }

plotly.offline.iplot({'data': data, 'layout': layout})
```

```
# Output: Average app rating = 4.173243045387994
```

## Size and Price of an App
```
%matplotlib inline
import seaborn as sns
sns.set_style("darkgrid")
import warnings
warnings.filterwarnings("ignore")

# Select rows where both 'Rating' and 'Size' values are present (ie. the two values are not null)
apps_with_size_and_rating_present = apps[(apps['Rating'].notna()) & (apps['Size'].notna())]

# Subset for categories with at least 250 apps
large_categories = apps_with_size_and_rating_present.groupby(['Category']).filter(lambda x: len(x) >= 250)

# Plot size vs. rating
plt1 = sns.jointplot(x = large_categories['Size'], y = large_categories['Rating'])

# Select apps whose 'Type' is 'Paid'
paid_apps = apps_with_size_and_rating_present[apps_with_size_and_rating_present['Type'] == 'Paid']

# Plot price vs. rating
plt2 = sns.jointplot(x = paid_apps['Price'], y = paid_apps['Rating'])
```
![[DataCampProject2.png]]
## Relationship between App Category and App Price
```
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
fig.set_size_inches(15, 8)

# Select a few popular app categories
popular_app_cats = apps[apps.Category.isin(['GAME', 'FAMILY', 'PHOTOGRAPHY',
                                            'MEDICAL', 'TOOLS', 'FINANCE',
                                            'LIFESTYLE','BUSINESS'])]

# Examine the price trend by plotting Price vs Category
ax = sns.stripplot(x = popular_app_cats['Price'], y = popular_app_cats['Category'], jitter=True, linewidth=1)
ax.set_title('App pricing trend across categories')

# Apps whose Price is greater than 200
apps_above_200 = apps[apps['Price'] > 200]
apps_above_200[['Category', 'App', 'Price']]
```
![[DataCampProject2_1.png]]

## Filter out Junk apps
```
# Select apps priced below $100
apps_under_100 = popular_app_cats[popular_app_cats['Price'] < 100]

fig, ax = plt.subplots()
fig.set_size_inches(15, 8)

# Examine price vs category with the authentic apps (apps_under_100)
ax = sns.stripplot(x = 'Price', y = 'Category', data = apps_under_100, jitter = True, linewidth = 1)
ax.set_title('App pricing trend across categories after filtering for junk apps')
```
![[DataCampProject2_2 1.png]]
## Popularity of Paid Apps vs Free Apps
```
trace0 = go.Box(
    # Data for paid apps
    y = apps[apps['Type'] == 'Paid']['Installs'],
    name = 'Paid'
)

trace1 = go.Box(
    # Data for free apps
    y = apps[apps['Type'] == 'Free']['Installs'],
    name = 'Free'
)

layout = go.Layout(
    title = "Number of downloads of paid apps vs. free apps",
    yaxis = dict(title = "Log number of downloads",
                type = 'log',
                autorange = True)
)

# Add trace0 and trace1 to a list for plotting
data = [trace0, trace1]
plotly.offline.iplot({'data': data, 'layout': layout})
```
![[Screenshot 2022-06-22 155046.png]]
## Sentiment Analysis of User Reviews
```
# Load user_reviews.csv
reviews_df = pd.read_csv('datasets/user_reviews.csv')

# # Join the two dataframes
merged_df = apps.merge(reviews_df, on='App' )

# Drop NA values from Sentiment and Review columns
merged_df = merged_df.dropna(subset = ['Sentiment', 'Review'])

sns.set_style('ticks')
fig, ax = plt.subplots()
fig.set_size_inches(11, 8)

# User review sentiment polarity for paid vs. free apps
ax = sns.boxplot(x = 'Type', y = 'Sentiment_Polarity', data = merged_df)
ax.set_title('Sentiment Polarity Distribution')
```

![[DataCampProject2_3.png]]
