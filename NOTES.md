
+ nbviewer
+ tmpnb
+ traitlets
+ jupyterhub
+ nbconvert
+ notebook
+ ipywidgets
+ nbgrader jupyterhub integration
+ jupyterhub deployment for calpoly
+ pydata
+ strata
+ scipy
+ jupyter-drive
+ jupyter_logger 
+ hydrogen
+ qtconsole
+ atome notebook
+ 

# Boolean Filtering

## Use Boolean comparisons in indexing operations

## Retrieve all rows where column TEMP > 20

```python
df[df['TEMP'] > 20]
```
    

## Also works with loc and iloc

## Select all columns with a mean over 6

```python
grades.loc[:, (grades.mean() > 6)]
```

## Assigning Values

+ Indexing operators allow you to assign to them
+ Update an entire column or row

```python
grades['test_1'] += 1
grades['Mary'] += [6,8]

```

Also works with loc, iloc, etc.


```python
grades.loc['Join', ['test_1', 'test_2']] = 8

```

## Assigning Values Warning

Assigning values may give a warning

```python
grades['test_2']['Ann'] = 8
```

> SettingWithCopyWarning

A value is trying to be set on a copy of a slice from a DataFrame

+ Did the assignment actually work?
+ Depends on the situation
+ Avoid chained indexing(use loc/iloc)



## Sorting

### Sort by index

```python
captials.sort_index()

```

### Sort by a column

```python
captials.sort_values(by='Population')
```
`

### Sort by multiple columns

```python
grades.sort_values(by=['test_1', 'test_2'])

```

## Sorting: Arguments

### Reverse sort

```python
captials.sort_index(ascending=False)
```

### Sort rows, not columns

```python
captials.sort_index(axis=1)
```

### Sort original datastructure, don't return a copy

```python
captials.sort_index(inplace=true)
```

> All arguments work both for sort_index and sort_values



# Detecting Missing Data

+ isnull() returns True for every null that is NaN
+ any() returns True if a column is True at least once

## Which columns have missing values?

```python
df.isnull().any()
```

```python
# use axis = 1 for rows
df[df.isnull().any(axis=1)] 
```

## notnull() and all() work similar to isnull() and any()

## Removing Missing Values

+ You can use df.drop() to remove items
+ But df.dropna() is more powerfull in this case
+ df.dropna() removes rows with missing values
+ df.dropna(axis=1) removes columns with missing values
+ df.dropna(how='all') removes rows where all values are missing
+ df.dropna(how='any') removes rows where any values are missing
+ df.dropna(inplace=True)
+ df.dropna(thresh=2) removes rows where less than 2 values are missing
+ df.dropna(subset=['A', 'B']) removes rows where either A or B is missing

## Filling Missing Values

+ df.fillna() fills missing values
+ df.fillna(0) fills missing values with 0
+ df.fillna(df.mean()) fills missing values with the mean of the column
+ df.fillna(method='ffill') fills missing values with the previous value
+ df.fillna(method='bfill') fills missing values with the next value
+ df.fillna(method='bfill', limit=1) fills missing values with the next value, but only for the first missing value
+ df.fillna(method='ffill', limit=1) fills missing values with the previous value, but only for the first missing value
+ df.interpolate() interpolate(插值) fills missing values with linear interpolation