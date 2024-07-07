
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

# Removing Duplicates

df.duplicated() returns a Series of Booleans, which is True whenever a row is a duplicate

df[df.duplicated()] returns the duplicate rows

df.drop_duplicates() removes duplicate rows

df.drop_duplicates(subset=['A', 'B']) removes duplicate rows where A and B are the same

df.drop_duplicates(keep='first') keeps the first duplicate row and removes the rest

df.drop_duplicates(keep='last') keeps the last duplicate row and removes the rest

df.drop_duplicates(keep=False) removes all duplicate rows

df.drop_duplicates(inplace=True) removes duplicate rows in place

df.unique() does the same but return a numpy array



# Converting types

df.astype() converts the data type of a column

df['some_column'].astype('int') converts the data type of a column to int

df.astype('float') converts the data type of a column to float

df.astype('str') converts the data type of a column to str

df.astype('category') converts the data type of a column to category

df.astype({'A': 'int', 'B': 'float'}) converts the data type of columns A and B to int and float respectively


> Note: All values have to fit into the new data type, otherwise an error will be raised.


Data Types

Strings(nullable)
Python: str
Numpy: np.object

Floats(nullable)
Python: float
Numpy: np.float64

Integers(non-nullable)
Python: int
Numpy: np.int64

Others
bool/np.bool
complex/np.complex64


## Fix indeces


Set the index to a simple range 0..n

```python
df.reset_index(drop=True, inplace=True)  # don't keep the original index
```


Set the index from a column


```python
df.reset_index('id', drop=True, inplace=True)
```


## rename

df.rename(columns={'old_name': 'new_name'}) renames a column

df.rename(columns={'old_name': 'new_name'}, inplace=True) renames a column in place

df.rename(index={0: 'new_index'}) renames an index

df.rename(index={0: 'new_index'}, inplace=True) renames an index in place

df.rename(columns={'old_name': 'new_name'}, index={0: 'new_index'}) renames a column and an index

df.rename(columns={'old_name': 'new_name'}, index={0: 'new_index'}, inplace=True) renames a column and an index in place


# Operating on Two Series

Returns a new Series object

Will all indices from both inputs

Results only filled where indices overlap; NaN everywhere else

```python
df1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
df2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])
df1 + df2
```


## Binary Operator Functions

These support the axis argument

+ df.add(x); df + x
+ df.radd(x): x + df
+ df.sub(x); df -x
+ df.rsub(x); x - df
+ df.mul(x); df * x
+ df.rmul(x); x*df
+ df.div(x); df / x
+ df.rdiv(x); x / df
+ df.floordiv(x); df // x
+ df.rfloordiv(x); x // df
+ df.truediv(x); df / x
+ df.mod(x); df % x
+ df.rmod(x); x % df
+ df.pow(x); df ** x
+ df.rpow(x); x ** df


compute the sine of all cells in df

np.sin(df)

compute e^x for every x in df

np.exp(df)

## Numpy ufuncs

Functions that work on entire DataFrame/Series


DataFrame.applymap() applies a function to each cell

df.applymap(my_func)

## Apply Functions to Cells

Pass the function to df.applymap() - no parentheses!

Returns a new DataFrame with results

Equivalent function on a Series is called apply()



df.applymap(lambda x: my_func(x))

Series.apply() does the same for values in a Series
s.apply(my_func)


Applying Functions to Cells


df.apply(f) Apply f to every column of df
df.apply(sum) caculate sum of every column
df.apply(sum, axis=1) caculate sum of every row



Applying Functions to Rows/Columns

DataFrame.apply() and Series.apply() do different things!

DataFrame.apply() applies a function to entire rows/columns



# Groupby

Select one ore more columns on the groupby object

Before doing any actual calculations

```python
athletes.groupby('sport')['gold'].sum()
```

Group on multiple columns

```python
athletes.groupby(['sport', 'nationality'])['gold'].sum()
```


Function available for Groupby Objects

+ count(),sum()
+ mean(),median()
+ min(),max()
+ std(),var()
+ skew(),kurt()
+ describe()
+ first(),last()
+ cumsum(),cumprod()
+ cummax(),cummin()
+ diff()
+ pct_change()


# Structural transformation

+ Columns to rows
+ Rows to columns
+ stack(), unstack()
+ pivot(), melt()


```python
df.pivot('index', 'columns', 'values')
```

Pivot: Transforming One column into Many

Pivot() takes 3 arguments: index, columns and values

Each of these takes a column name from teh origin DataFrame,

Returns a  DataFrame: rows and columns taken from index and columns, values take from values





```python
df.melt(id_vars='prod_id')
```

Melt: Transforming Many Columns into One

Melt() takes 2 arguments: id_vars and value_vars

id_vars: columns to keep as is

value_vars: columns to transform into one column

Column labels will go into 'variable' column

All other values not set as id_vars will end up in 'value' column



stack() moves all data into 1 column

with a multi level index


unstack() creates columns for the innermost index level

and moves data from the rows into these columns

df.unstack()

