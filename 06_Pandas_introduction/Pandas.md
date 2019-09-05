
<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Importing-pandas" data-toc-modified-id="Importing-pandas-1">Importing pandas</a></span></li><li><span><a href="#Reading-in-data" data-toc-modified-id="Reading-in-data-2">Reading in data</a></span><ul class="toc-item"><li><span><a href="#The-read_csv-function" data-toc-modified-id="The-read_csv-function-2.1">The read_csv function</a></span></li><li><span><a href="#Some-important-options-for-the-read_csv()-function" data-toc-modified-id="Some-important-options-for-the-read_csv()-function-2.2">Some important options for the <code>read_csv()</code> function</a></span></li></ul></li><li><span><a href="#Important-notice:-reading-in-files-from-your-computer" data-toc-modified-id="Important-notice:-reading-in-files-from-your-computer-3">Important notice: reading in files from your computer</a></span></li><li><span><a href="#Exploring-the-data" data-toc-modified-id="Exploring-the-data-4">Exploring the data</a></span><ul class="toc-item"><li><span><a href="#Exploring-the-data-in-the-spyder-variable-explorer" data-toc-modified-id="Exploring-the-data-in-the-spyder-variable-explorer-4.1">Exploring the data in the spyder variable explorer</a></span></li><li><span><a href="#Exploring-the-data-using-code" data-toc-modified-id="Exploring-the-data-using-code-4.2">Exploring the data using code</a></span></li></ul></li><li><span><a href="#Columns-and-indices" data-toc-modified-id="Columns-and-indices-5">Columns and indices</a></span></li><li><span><a href="#Accessing-the-columns" data-toc-modified-id="Accessing-the-columns-6">Accessing the columns</a></span></li><li><span><a href="#Creating-new-variables-(columns)" data-toc-modified-id="Creating-new-variables-(columns)-7">Creating new variables (columns)</a></span></li><li><span><a href="#Exercises" data-toc-modified-id="Exercises-8">Exercises</a></span><ul class="toc-item"><li><span><a href="#Exercise-1" data-toc-modified-id="Exercise-1-8.1">Exercise 1</a></span></li><li><span><a href="#Exercise-2" data-toc-modified-id="Exercise-2-8.2">Exercise 2</a></span></li><li><span><a href="#Exercise-3" data-toc-modified-id="Exercise-3-8.3">Exercise 3</a></span></li><li><span><a href="#Exercise-4" data-toc-modified-id="Exercise-4-8.4">Exercise 4</a></span></li></ul></li></ul></div>

# Pandas: introduction

## Importing pandas

pandas is part of the anaconda python distribution and can be directly imported.


```python
import pandas
```



## Reading in data

###  The read_csv function

The most common scenario is to read in a data file from disk. Pandas has powerful functions to read in data. For example, the ```read_csv()```function has many (and I mean many) options:

```read_csv(filepath_or_buffer, sep=', ', delimiter=None, header='infer', names=None, index_col=None, usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True, parse_dates=False, infer_datetime_format=False, keep_date_col=False, date_parser=None, dayfirst=False, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, escapechar=None, comment=None, encoding=None, dialect=None, tupleize_cols=False, error_bad_lines=True, warn_bad_lines=True, skipfooter=0, skip_footer=0, doublequote=True, delim_whitespace=False, as_recarray=False, compact_ints=False, use_unsigned=False, low_memory=True, buffer_lines=None, memory_map=False, float_precision=None)```

Documentation: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html

Luckily, we wont be needing most of the options most of the time.

Here, I will use example data on the survivorship on the Titanic. The data is described here: https://vincentarelbundock.github.io/Rdatasets/doc/datasets/Titanic.html

You can also use this link: https://tinyurl.com/y894ft6g


```python
# options used: read in column 0 as the index, 'NA' is read as missing values.
data = pandas.read_csv('https://tinyurl.com/y894ft6g',index_col=0,na_values='NA')
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>PClass</th>
      <th>Age</th>
      <th>Sex</th>
      <th>Survived</th>
      <th>SexCode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Allen, Miss Elisabeth Walton</td>
      <td>1st</td>
      <td>29.00</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Allison, Miss Helen Loraine</td>
      <td>1st</td>
      <td>2.00</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Allison, Mr Hudson Joshua Creighton</td>
      <td>1st</td>
      <td>30.00</td>
      <td>male</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Allison, Mrs Hudson JC (Bessie Waldo Daniels)</td>
      <td>1st</td>
      <td>25.00</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Allison, Master Hudson Trevor</td>
      <td>1st</td>
      <td>0.92</td>
      <td>male</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### Some important options for the ```read_csv()``` function

Some options will come in handy. These include the ```separator``` option and the ```header``` option. Often, data files use different seperators or do not come with a header (i.e., a row of column names). If so, these options allow reading in the file correctly. The default values for these options are:

+ separator: ```sep=', '```
+ header:  ```header='infer```




```python
import pandas
silly_data = pandas.read_csv('data/silly.txt')
silly_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>123*234*123*1234</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4543*2342*123*224</td>
    </tr>
    <tr>
      <th>1</th>
      <td>456*1223*1234*123</td>
    </tr>
  </tbody>
</table>
</div>




```python
silly_data = pandas.read_csv('data/silly.txt', sep='*')
silly_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>123</th>
      <th>234</th>
      <th>123.1</th>
      <th>1234</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4543</td>
      <td>2342</td>
      <td>123</td>
      <td>224</td>
    </tr>
    <tr>
      <th>1</th>
      <td>456</td>
      <td>1223</td>
      <td>1234</td>
      <td>123</td>
    </tr>
  </tbody>
</table>
</div>




```python
silly_data = pandas.read_csv('data/silly.txt', sep='*', header=None)
silly_data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>123</td>
      <td>234</td>
      <td>123</td>
      <td>1234</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4543</td>
      <td>2342</td>
      <td>123</td>
      <td>224</td>
    </tr>
    <tr>
      <th>2</th>
      <td>456</td>
      <td>1223</td>
      <td>1234</td>
      <td>123</td>
    </tr>
  </tbody>
</table>
</div>



## Important notice: reading in files from your computer

The ```read_csv()``` can only find the data file if the data file are in the same folder.

![title](Selection_318.png)

If you do not place the python script and the data file in the same folder, you need to provide the (relative) path to the file.

## Exploring the data

### Exploring the data in the spyder variable explorer

[...]


### Exploring the data using code

Print the top rows of the dataset


```python
print(data.head(3))
```

                                      Name PClass   Age     Sex  Survived  SexCode
    1         Allen, Miss Elisabeth Walton    1st  29.0  female         1        1
    2          Allison, Miss Helen Loraine    1st   2.0  female         0        1
    3  Allison, Mr Hudson Joshua Creighton    1st  30.0    male         0        0


How big is our dataset?


```python
print(data.shape)
```

    (1313, 6)


Remember, the dataframe allows for multiple data types.


```python
print(data.dtypes)
```

    Name         object
    PClass       object
    Age         float64
    Sex          object
    Survived      int64
    SexCode       int64
    dtype: object


## Columns and indices


```python
a = data.columns
print(a)
```

    Index(['Name', 'PClass', 'Age', 'Sex', 'Survived', 'SexCode'], dtype='object')



```python
b = data.index
print(b)
```

    Int64Index([   1,    2,    3,    4,    5,    6,    7,    8,    9,   10,
                ...
                1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313],
               dtype='int64', length=1313)


## Accessing the columns


```python
sex = data.SexCode
print(sex)
```

    1       1
    2       1
    3       0
    4       1
    5       0
    6       0
    7       1
    8       0
    9       1
    10      0
    11      0
    12      1
    13      1
    14      0
    15      0
    16      1
    17      0
    18      0
    19      0
    20      1
    21      0
    22      0
    23      0
    24      1
    25      0
    26      0
    27      0
    28      1
    29      1
    30      0
           ..
    1284    1
    1285    0
    1286    0
    1287    0
    1288    0
    1289    0
    1290    0
    1291    0
    1292    0
    1293    0
    1294    1
    1295    0
    1296    0
    1297    0
    1298    0
    1299    0
    1300    0
    1301    0
    1302    0
    1303    0
    1304    0
    1305    1
    1306    0
    1307    1
    1308    1
    1309    0
    1310    0
    1311    0
    1312    0
    1313    0
    Name: SexCode, Length: 1313, dtype: int64



```python
name = data.Age
print(name.head())
```

    1    29.00
    2     2.00
    3    30.00
    4    25.00
    5     0.92
    Name: Age, dtype: float64


## Creating new variables (columns)

You can make new variables (columns) based on existing variables. And add the new columns to the dataframe.


```python
data['Months'] = data.Age * 12
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>PClass</th>
      <th>Age</th>
      <th>Sex</th>
      <th>Survived</th>
      <th>SexCode</th>
      <th>Months</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Allen, Miss Elisabeth Walton</td>
      <td>1st</td>
      <td>29.00</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
      <td>348.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Allison, Miss Helen Loraine</td>
      <td>1st</td>
      <td>2.00</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
      <td>24.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Allison, Mr Hudson Joshua Creighton</td>
      <td>1st</td>
      <td>30.00</td>
      <td>male</td>
      <td>0</td>
      <td>0</td>
      <td>360.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Allison, Mrs Hudson JC (Bessie Waldo Daniels)</td>
      <td>1st</td>
      <td>25.00</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
      <td>300.00</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Allison, Master Hudson Trevor</td>
      <td>1st</td>
      <td>0.92</td>
      <td>male</td>
      <td>1</td>
      <td>0</td>
      <td>11.04</td>
    </tr>
  </tbody>
</table>
</div>




```python
data['Child'] = data.Age < 18
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>PClass</th>
      <th>Age</th>
      <th>Sex</th>
      <th>Survived</th>
      <th>SexCode</th>
      <th>Months</th>
      <th>Child</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Allen, Miss Elisabeth Walton</td>
      <td>1st</td>
      <td>29.00</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
      <td>348.00</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Allison, Miss Helen Loraine</td>
      <td>1st</td>
      <td>2.00</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
      <td>24.00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Allison, Mr Hudson Joshua Creighton</td>
      <td>1st</td>
      <td>30.00</td>
      <td>male</td>
      <td>0</td>
      <td>0</td>
      <td>360.00</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Allison, Mrs Hudson JC (Bessie Waldo Daniels)</td>
      <td>1st</td>
      <td>25.00</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
      <td>300.00</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Allison, Master Hudson Trevor</td>
      <td>1st</td>
      <td>0.92</td>
      <td>male</td>
      <td>1</td>
      <td>0</td>
      <td>11.04</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
data['Silly'] = data.Months / data.Age
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>PClass</th>
      <th>Age</th>
      <th>Sex</th>
      <th>Survived</th>
      <th>SexCode</th>
      <th>Months</th>
      <th>Child</th>
      <th>Silly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Allen, Miss Elisabeth Walton</td>
      <td>1st</td>
      <td>29.00</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
      <td>348.00</td>
      <td>False</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Allison, Miss Helen Loraine</td>
      <td>1st</td>
      <td>2.00</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
      <td>24.00</td>
      <td>True</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Allison, Mr Hudson Joshua Creighton</td>
      <td>1st</td>
      <td>30.00</td>
      <td>male</td>
      <td>0</td>
      <td>0</td>
      <td>360.00</td>
      <td>False</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Allison, Mrs Hudson JC (Bessie Waldo Daniels)</td>
      <td>1st</td>
      <td>25.00</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
      <td>300.00</td>
      <td>False</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Allison, Master Hudson Trevor</td>
      <td>1st</td>
      <td>0.92</td>
      <td>male</td>
      <td>1</td>
      <td>0</td>
      <td>11.04</td>
      <td>True</td>
      <td>12.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
data['Child'] =  data.Age < 18
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>PClass</th>
      <th>Age</th>
      <th>Sex</th>
      <th>Survived</th>
      <th>SexCode</th>
      <th>Months</th>
      <th>Child</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Allen, Miss Elisabeth Walton</td>
      <td>1st</td>
      <td>29.00</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
      <td>348.00</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Allison, Miss Helen Loraine</td>
      <td>1st</td>
      <td>2.00</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
      <td>24.00</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Allison, Mr Hudson Joshua Creighton</td>
      <td>1st</td>
      <td>30.00</td>
      <td>male</td>
      <td>0</td>
      <td>0</td>
      <td>360.00</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Allison, Mrs Hudson JC (Bessie Waldo Daniels)</td>
      <td>1st</td>
      <td>25.00</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
      <td>300.00</td>
      <td>False</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Allison, Master Hudson Trevor</td>
      <td>1st</td>
      <td>0.92</td>
      <td>male</td>
      <td>1</td>
      <td>0</td>
      <td>11.04</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>



## Exercises

### Exercise 1

+ Read in the cars.txt file (download it or read it in from http://tinyurl.com/ybbw5gwg)
+ Print the first lines of the data
+ Print the number of rows and columns of data
+ Print the column names
+ Assign one of the columns to a variable
+ Calculate the difference in mpg on the highway and the city, add this difference as a new variable to the data frame.


### Exercise 2


Download the `wages1833.csv` data file (from the data folder) and save it to your computer. You can also use this direct url: http://tinyurl.com/y6orr2bg

This file contains data on the wages of Lancashire cotton factory workers in 1833.  For each age category, the file lists the following:

* `age`: age in years
* `mnum:` number of male workers of the corresponding age
* `mwage`: average wage of male workers of the corresponding age
* `fnum`: number of female workers of the corresponding age
* `fwage`: average wage of female workers of the corresponding age

More info on the data can be found in this paper:  Boot, H.M. 1995. How Skilled Were the Lancashire Cotton Factory Workers in 1833? Economic History Review 48: 283-303.

Write a script that does the following:

* Read in the data as a pandas dataframe
* Prints the column names
* Prints the first 7 lines of the data
* Adds a new variable that lists the difference between the number of male and female workers
* Adds a new variable ```diff_pct``` that gives the difference in average wage between the male and female workers expressed as a percentage of the female wage. For example, if the average female wage is 90 and the male wage is 135, this new column lists the number 50. In the form of an equation, this gives:

$$
diff_{pct} = 100 \times \frac{(mwage - fwage)}{fwage}
$$



### Exercise 3


Suppose, I want to read in a file named `data.txt`. The columns of the data are separated by tabs. How can I make sure that pandas reads this data correctly? Complete the blank in the following piece of code:

```python
data = pandas.read_csv('data.txt', _______)
```


### Exercise 4

Suppose, my data file named `data.csv` has no header (no variable names). How can I read in this file correctly?


```python

```
