
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

