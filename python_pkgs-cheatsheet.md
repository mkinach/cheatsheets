# Python Packages Cheatsheet

#### Index:

[Pandas](#pandas)

---

### Pandas

```python
import pandas as pd
import numpy  as np
```

Working with series (like a NumPy array, but with labels)
```python
# create a series
s1 = pd.Series(data = [46, 38, 29, 19, 17], index = ['USA','CHN','GBR','RUS','GER'])
s2 = pd.Series([46, 38, 29, 19, 17],['USA','CHN','GBR','RUS','GER'])  # equivalent
print(s1)
# USA    46
# CHN    38
# GBR    29
# RUS    19
# GER    17
# dtype: int64

# index a series (either by integer or label)
s1.iloc[0]  # 46
s1.iloc[1]  # 38
s1["USA"]   # 46
s1["USA":"RUS"]
# USA    46
# CHN    38
# GBR    29
# RUS    19
# dtype: int64

# operations on series are done label-wise
s2 = pd.Series([46, 26, 27], ['USA', 'CHN', 'GBR'])
s1 + s2
# CHN    64.0
# GBR    56.0
# GER     NaN
# RUS     NaN
# USA    92.0
# dtype: float64
```

Creating dataframes
```python
# create a dataframe with a NumPy array
d = np.array([[46, 46],
              [38, 26],
              [29, 27]])
c = ['2012', '2016']
i = ['USA', 'CHN', 'GBR']
df = pd.DataFrame(data=d, index=i, columns=c)
df
#      2012  2016
# USA    46    46
# CHN    38    26
# GBR    29    27

# create a dataframe with a dictionary
d = {'2012': [46, 38, 29],
     '2016': [46, 26, 27]}
i = ['USA', 'CHN', 'GBR']
df  = pd.DataFrame(d, i)
df0 = df
df
#      2012  2016
# USA    46    46
# CHN    38    26
# GBR    29    27
```

Indexing dataframes
```python
d = {'2012': [46, 38, 29],
     '2016': [46, 26, 27]}
i = ['USA', 'CHN', 'GBR']
df  = pd.DataFrame(d, i)
df0 = df
df
#      2012  2016
# USA    46    46
# CHN    38    26
# GBR    29    27

# index a dataframe by column
df['2012']
# USA    46
# CHN    38
# GBR    29
# Name: 2012, dtype: int64

# index a dataframe by multiple columns
df[['2012', '2016']]
#      2012  2016
# USA    46    46
# CHN    38    26
# GBR    29    27

# index a dataframe by row
# df["USA"] # doesn't work
df[:"USA"]  # does work
#      2012  2016
# USA    46    46

# index a dataframe by multiple rows
df["CHN":"GBR"]
#      2012  2016
# CHN    38    26
# GBR    29    27

# index a dataframe by row (via integer)
df.iloc[1]
# 2012    38
# 2016    26
# Name: CHN, dtype: int64

# index a dataframe by row (via label)
df.loc['CHN']
# 2012    38
# 2016    26
# Name: CHN, dtype: int64

# index a dataframe value (via integer)
df.iloc[2,1]
# 27

# index a dataframe value (via label)
df.loc['GBR', '2016']
# 27

# index a dataframe by specific rows and columns (via label)
df.loc[['USA', 'GBR'], ['2012']]
#      2012
# USA    46
# GBR    29

# list all row and column labels
df.index   # Index(['USA', 'CHN', 'GBR'], dtype='object')
df.column  # Index(['2012', '2016'], dtype='object')
list(df.columns)  # alternate way

# get basic info on dataset
df.info()
# <class 'pandas.core.frame.DataFrame'>
# Index: 3 entries, USA to GBR
# Data columns (total 2 columns):
# #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
# 0   2012    3 non-null      int64
# 1   2016    3 non-null      int64
# dtypes: int64(2)
# memory usage: 72.0+ bytes

# get statistics on dataset
df.describe(include='all')
#             2012       2016
# count   3.000000   3.000000
# mean   37.666667  33.000000
# std     8.504901  11.269428
# min    29.000000  26.000000
# 25%    33.500000  26.500000
# 50%    38.000000  27.000000
# 75%    42.000000  36.500000
# max    46.000000  46.000000

# get value counts
df["2012"].value_counts()
# 46    1
# 38    1
# 29    1
# Name: 2012, dtype: int64
df["2012"].value_counts(normalize=True,ascending=True)
# 46    0.333333
# 38    0.333333
# 29    0.333333
# Name: 2012, dtype: float64
```

Modifying dataframes
```python
d = {'2012': [46, 38, 29],
     '2016': [46, 26, 27]}
i = ['USA', 'CHN', 'GBR']
df  = pd.DataFrame(d, i)
df0 = df
df
#      2012  2016
# USA    46    46
# CHN    38    26
# GBR    29    27

# rename a column
df = df.rename(columns={"2012": "Twenty-Twelve"})
df.head()
#      Twenty-Twelve  2016
# USA             46    46
# CHN             38    26
# GBR             29    27

# rename all the columns at once
df.columns = ['~12', '~16']
df.head()
#     ~12  ~16
# USA  46   46
# CHN  38   26
# GBR  29   27

# add a constant column
df['~20'] = 17
df.head()
#      ~12  ~16  ~20
# USA   46   46   17
# CHN   38   26   17
# GBR   29   27   17

# drop a column
df = df.drop(columns="~20")
df.head()
#      ~12  ~16
# USA   46   46
# CHN   38   26
# GBR   29   27

# drop multiples columns
df = df.drop(columns=['~12', '~16'])
# Empty DataFrame
# Columns: []
# Index: [USA, CHN, GBR]

# extract a row
df=df0
last_row = df.iloc[-1]
last_row
# 2012    29
# 2016    27
# Name: GBR, dtype: int64

# add a row
df = df.append(last_row, ignore_index=True)  # deprecated
df.tail()
#      2012  2016
# USA    46    46
# CHN    38    26
# GBR    29    27
# GBR    29    27

# drop a row
df = df.drop(index="USA")
df
# 2012  2016
# CHN    38    26
# GBR    29    27
```

Sorting dataframes
```python
df = pd.read_csv('data/cycling_data.csv')
df.head()
#                      Date             Name  Type  Time  Distance  Comments
# 0   10 Sep 2019, 00:13:04   Afternoon Ride  Ride  2084     12.62  Rain
# 1   10 Sep 2019, 13:52:18     Morning Ride  Ride  2531     13.03  rain
# 2   11 Sep 2019, 00:23:50   Afternoon Ride  Ride  1863     12.52  Wet road but nice weather
# 3   11 Sep 2019, 14:06:19     Morning Ride  Ride  2192     12.84  Stopped for photo of sunrise
# 4   12 Sep 2019, 00:28:05   Afternoon Ride  Ride  1891     12.48  Tired by the end of the week

# sort by single column
df.sort_values(by="Time", ascending=False).head()
#                      Date             Name  Type   Time   Distance  Comments
# 10  19 Sep 2019, 00:30:01   Afternoon Ride  Ride  48062      12.48  Feeling good
# 12  20 Sep 2019, 01:02:05   Afternoon Ride  Ride   2961      12.81  Feeling good
# 8   18 Sep 2019, 13:49:53     Morning Ride  Ride   2903      14.57  Raining today
# 1   10 Sep 2019, 13:52:18     Morning Ride  Ride   2531      13.03  rain
# 31  10 Oct 2019, 13:47:14     Morning Ride  Ride   2463      12.79  Stopped for photo of sunrise

# sort by multiple columns
df.sort_values(by=['Name', 'Time'], ascending=[True, False]).head()
#                      Date             Name  Type   Time   Distance  Comments
# 10  19 Sep 2019, 00:30:01   Afternoon Ride  Ride  48062      12.48  Feeling good
# 12  20 Sep 2019, 01:02:05   Afternoon Ride  Ride   2961      12.81  Feeling good
# 9   18 Sep 2019, 00:15:52   Afternoon Ride  Ride   2101      12.48  Pumped up tires
# 0   10 Sep 2019, 00:13:04   Afternoon Ride  Ride   2084      12.62  Rain
# 14  24 Sep 2019, 00:35:42   Afternoon Ride  Ride   2076      12.47  Oiled chain, bike feels smooth

# sort by index
df.sort_index().head()
#                      Date             Name  Type  Time  Distance  Comments
# 0   10 Sep 2019, 00:13:04   Afternoon Ride  Ride  2084     12.62  Rain
# 1   10 Sep 2019, 13:52:18     Morning Ride  Ride  2531     13.03  rain
# 2   11 Sep 2019, 00:23:50   Afternoon Ride  Ride  1863     12.52  Wet road but nice weather
# 3   11 Sep 2019, 14:06:19     Morning Ride  Ride  2192     12.84  Stopped for photo of sunrise
# 4   12 Sep 2019, 00:28:05   Afternoon Ride  Ride  1891     12.48  Tired by the end of the week

# filter data
df.query('Time > 2500 and Distance < 13')
#                      Date             Name  Type   Time   Distance  Comments
# 10  19 Sep 2019, 00:30:01   Afternoon Ride  Ride  48062      12.48  Feeling good
# 12  20 Sep 2019, 01:02:05   Afternoon Ride  Ride   2961      12.81  Feeling good
df[(df['Time'] > 2500) & (df['Distance'] < 13)]  # alternate way
#                      Date             Name  Type   Time   Distance  Comments
# 10  19 Sep 2019, 00:30:01   Afternoon Ride  Ride  48062      12.48  Feeling good
# 12  20 Sep 2019, 01:02:05   Afternoon Ride  Ride   2961      12.81  Feeling good

# filter data by threshold
thresh = 2800
df.query('Time > @thresh')
#                      Date             Name  Type   Time   Distance  Comments
# 8   18 Sep 2019, 13:49:53     Morning Ride  Ride   2903      14.57  Raining today
# 10  19 Sep 2019, 00:30:01   Afternoon Ride  Ride  48062      12.48  Feeling good
# 12  20 Sep 2019, 01:02:05   Afternoon Ride  Ride   2961      12.81  Feeling good
```

Apply functions to dataframes
```python
df = pd.read_csv('data/cycling_data.csv')

# apply built-in function to data
# e.g. df.mean(), df.round(), df.min(), df.max(), df.sum(), etc.
df.mean()
# Time        3512.787879
# Distance      12.667419
# dtype: float64

# apply custom function to data
df[['Time', 'Distance']].head()
#     Time  Distance
# 0   2084     12.62
# 1   2531     13.03
# 2   1863     12.52
# 3   2192     12.84
# 4   1891     12.48
df[['Time', 'Distance']].apply(np.sin).head()
#          Time    Distance
# 0   -0.901866    0.053604
# 1   -0.901697    0.447197
# 2   -0.035549   -0.046354
# 3   -0.739059    0.270228
# 4   -0.236515   -0.086263
df[['Time']].apply(lambda x: x/60).head()
#          Time
# 0   34.733333
# 1   42.183333
# 2   31.050000
# 3   36.533333
# 4   31.516667

# apply scalar function to data
df[['Time']].apply(float).head() # fails
# TypeError: ("cannot convert the series to <class 'float'>", 'occurred at index Time')
df_float_1 = df[['Time']].applymap(float).head() # works with applymap
df_float_1
#       Time
# 0   2084.0
# 1   2531.0
# 2   1863.0
# 3   2192.0
# 4   1891.0
df_float_2 = df[['Time']].astype(float).head() # alternate way
df_float_2
#       Time
# 0   2084.0
# 1   2531.0
# 2   1863.0
# 3   2192.0
# 4   1891.0

# runtime comparison
import timeit
timeit.timeit(df[['Time']].applymap(float))
# 2.53 ms ± 85.7 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
timeit.timeit(df[['Time']].astype(float))
# 948 µs ± 37.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

Reading data from file
```python
# read from CSV
path = 'data/mydata.csv'
df = pd.read_csv(path, index_col=0, parse_dates=True)
df.head()  # you can also just append .head() to previous line
#    Bottle         Grape     Origin  Alcohol    pH  Colour   Aroma
# 0       1    Chardonnay  Australia    14.23  3.51   White  Floral
# 1       2  Pinot Grigio      Italy    13.20  3.30   White  Fruity
# 2       3   Pinot Blanc     France    13.16  3.16   White  Citrus
# 3       4        Shiraz      Chile    14.91  3.39     Red   Berry
# 4       5        Malbec  Argentina    13.83  3.28     Red  Fruity

# read from URL
url = 'https://data.ny.gov/api/views/d6yy-54nr/rows.csv'
df = pd.read_csv(url)
df.head()
# Draw        Date    Winning Numbers  Multiplier
#    0  09/26/2020  11 21 27 36 62 24         3.0
#    1  09/30/2020  14 18 36 49 67 18         2.0
#    2  10/03/2020  18 31 36 43 47 20         2.0
#    3  10/07/2020  06 24 30 53 56 19         2.0
#    4  10/10/2020  05 18 23 40 50 18         3.0

# read from other formats
path = 'data/mydata.xlsx'; pd.read_excel(path)
path = 'data/mydata.html'; pd.read_html(path)
path = 'data/mydata.json'; pd.read_json(path)
```
