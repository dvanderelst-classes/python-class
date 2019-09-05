
<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Reading-in-some-example-data" data-toc-modified-id="Reading-in-some-example-data-1">Reading in some example data</a></span></li><li><span><a href="#Simple-descriptive-statistics-of-numerical-variables" data-toc-modified-id="Simple-descriptive-statistics-of-numerical-variables-2">Simple descriptive statistics of numerical variables</a></span></li><li><span><a href="#Descriptive-statistics-of-categorical-variables" data-toc-modified-id="Descriptive-statistics-of-categorical-variables-3">Descriptive statistics of categorical variables</a></span></li><li><span><a href="#Excersises" data-toc-modified-id="Excersises-4">Excersises</a></span></li><li><span><a href="#Data-aggregation" data-toc-modified-id="Data-aggregation-5">Data aggregation</a></span><ul class="toc-item"><li><span><a href="#Grouping-data-according-to-a-single-variable" data-toc-modified-id="Grouping-data-according-to-a-single-variable-5.1">Grouping data according to a single variable</a></span></li><li><span><a href="#Grouping-according-to-multiple-variables" data-toc-modified-id="Grouping-according-to-multiple-variables-5.2">Grouping according to multiple variables</a></span></li><li><span><a href="#Resetting-the-indices" data-toc-modified-id="Resetting-the-indices-5.3">Resetting the indices</a></span></li><li><span><a href="#Using-the-course-package" data-toc-modified-id="Using-the-course-package-5.4">Using the <code>course</code> package</a></span></li></ul></li><li><span><a href="#Reorganizing-a-dataframe" data-toc-modified-id="Reorganizing-a-dataframe-6">Reorganizing a dataframe</a></span></li><li><span><a href="#Exercise-1" data-toc-modified-id="Exercise-1-7">Exercise 1</a></span></li><li><span><a href="#Exercise-2" data-toc-modified-id="Exercise-2-8">Exercise 2</a></span></li><li><span><a href="#Exercises-3" data-toc-modified-id="Exercises-3-9">Exercises 3</a></span></li></ul></div>

# Pandas: statistics

## Reading in some example data

The fossum data consists of nine morphometric measurements on each of 43 female mountain brushtail possums, trapped at seven sites from Southern Victoria to central Queensland:

https://vincentarelbundock.github.io/Rdatasets/doc/DAAG/fossum.html


```python
import pandas
link = 'http://tinyurl.com/y8ummdf9'
data = pandas.read_csv(link,index_col=0)
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
      <th>case</th>
      <th>site</th>
      <th>Pop</th>
      <th>sex</th>
      <th>age</th>
      <th>hdlngth</th>
      <th>skullw</th>
      <th>totlngth</th>
      <th>taill</th>
      <th>footlgth</th>
      <th>earconch</th>
      <th>eye</th>
      <th>chest</th>
      <th>belly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>C5</th>
      <td>2</td>
      <td>1</td>
      <td>Vic</td>
      <td>f</td>
      <td>6</td>
      <td>92.5</td>
      <td>57.6</td>
      <td>91.5</td>
      <td>36.5</td>
      <td>72.5</td>
      <td>51.2</td>
      <td>16.0</td>
      <td>28.5</td>
      <td>33.0</td>
    </tr>
    <tr>
      <th>C10</th>
      <td>3</td>
      <td>1</td>
      <td>Vic</td>
      <td>f</td>
      <td>6</td>
      <td>94.0</td>
      <td>60.0</td>
      <td>95.5</td>
      <td>39.0</td>
      <td>75.4</td>
      <td>51.9</td>
      <td>15.5</td>
      <td>30.0</td>
      <td>34.0</td>
    </tr>
    <tr>
      <th>C15</th>
      <td>4</td>
      <td>1</td>
      <td>Vic</td>
      <td>f</td>
      <td>6</td>
      <td>93.2</td>
      <td>57.1</td>
      <td>92.0</td>
      <td>38.0</td>
      <td>76.1</td>
      <td>52.2</td>
      <td>15.2</td>
      <td>28.0</td>
      <td>34.0</td>
    </tr>
    <tr>
      <th>C23</th>
      <td>5</td>
      <td>1</td>
      <td>Vic</td>
      <td>f</td>
      <td>2</td>
      <td>91.5</td>
      <td>56.3</td>
      <td>85.5</td>
      <td>36.0</td>
      <td>71.0</td>
      <td>53.2</td>
      <td>15.1</td>
      <td>28.5</td>
      <td>33.0</td>
    </tr>
    <tr>
      <th>C24</th>
      <td>6</td>
      <td>1</td>
      <td>Vic</td>
      <td>f</td>
      <td>1</td>
      <td>93.1</td>
      <td>54.8</td>
      <td>90.5</td>
      <td>35.5</td>
      <td>73.2</td>
      <td>53.6</td>
      <td>14.2</td>
      <td>30.0</td>
      <td>32.0</td>
    </tr>
  </tbody>
</table>
</div>



## Simple descriptive statistics of numerical variables

The describe() function can be used to get descriptives statistics of all *numerical* variables in a dataframe.


```python
data.describe()
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
      <th>case</th>
      <th>site</th>
      <th>age</th>
      <th>hdlngth</th>
      <th>skullw</th>
      <th>totlngth</th>
      <th>taill</th>
      <th>footlgth</th>
      <th>earconch</th>
      <th>eye</th>
      <th>chest</th>
      <th>belly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>43.000000</td>
      <td>43.000000</td>
      <td>43.000000</td>
      <td>43.000000</td>
      <td>43.000000</td>
      <td>43.000000</td>
      <td>43.000000</td>
      <td>42.000000</td>
      <td>43.000000</td>
      <td>43.000000</td>
      <td>43.000000</td>
      <td>43.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>43.418605</td>
      <td>2.976744</td>
      <td>3.976744</td>
      <td>92.148837</td>
      <td>56.588372</td>
      <td>87.906977</td>
      <td>37.104651</td>
      <td>69.111905</td>
      <td>48.576744</td>
      <td>14.811628</td>
      <td>27.337209</td>
      <td>32.883721</td>
    </tr>
    <tr>
      <th>std</th>
      <td>30.264888</td>
      <td>2.219914</td>
      <td>1.945549</td>
      <td>2.574913</td>
      <td>2.568788</td>
      <td>4.182241</td>
      <td>1.830815</td>
      <td>4.911321</td>
      <td>4.274444</td>
      <td>1.030074</td>
      <td>1.841069</td>
      <td>2.929402</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>84.700000</td>
      <td>51.500000</td>
      <td>75.000000</td>
      <td>32.000000</td>
      <td>60.300000</td>
      <td>40.300000</td>
      <td>13.000000</td>
      <td>23.000000</td>
      <td>25.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>18.000000</td>
      <td>1.000000</td>
      <td>3.000000</td>
      <td>90.750000</td>
      <td>55.200000</td>
      <td>85.250000</td>
      <td>36.000000</td>
      <td>64.850000</td>
      <td>44.650000</td>
      <td>14.100000</td>
      <td>26.000000</td>
      <td>31.250000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>40.000000</td>
      <td>2.000000</td>
      <td>4.000000</td>
      <td>92.500000</td>
      <td>56.400000</td>
      <td>88.500000</td>
      <td>37.500000</td>
      <td>70.450000</td>
      <td>50.800000</td>
      <td>14.800000</td>
      <td>28.000000</td>
      <td>33.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>64.500000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>93.800000</td>
      <td>57.650000</td>
      <td>90.500000</td>
      <td>38.250000</td>
      <td>72.800000</td>
      <td>52.300000</td>
      <td>15.450000</td>
      <td>28.500000</td>
      <td>34.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>104.000000</td>
      <td>7.000000</td>
      <td>9.000000</td>
      <td>96.900000</td>
      <td>67.700000</td>
      <td>96.500000</td>
      <td>41.000000</td>
      <td>77.900000</td>
      <td>53.900000</td>
      <td>17.400000</td>
      <td>31.000000</td>
      <td>40.000000</td>
    </tr>
  </tbody>
</table>
</div>



Isolating a single column and getting its descriptives works as well.


```python
a = data.age
a.describe()
```




    count    43.000000
    mean      3.976744
    std       1.945549
    min       1.000000
    25%       3.000000
    50%       4.000000
    75%       5.000000
    max       9.000000
    Name: age, dtype: float64



You can also get specific descriptices. 


```python
a.max()
```




    9




```python
a.min()
```




    1




```python
a.mean()
```




    3.9767441860465116




```python
a.std()
```




    1.9455489137665618




```python
a.count()
```




    43



**Table of descriptive functions**

This is a table of some of the descriptives that are available:

+ count.......Number of non-null observations
+ sum.........Sum of values
+ mean........Mean of values
+ mad.........Mean absolute deviation
+ median......Arithmetic median of values
+ min.........Minimum
+ max.........Maximum
+ mode........Mode
+ prod........Product of values
+ std.........Bessel-corrected sample standard deviation
+ var.........Unbiased variance
+ sem.........Standard error of the mean
+ skew........Sample skewness (3rd moment)
+ kurt........Sample kurtosis (4th moment)
+ quantile....Sample quantile (value at %)

## Descriptive statistics of categorical variables


```python
p = data['Pop']
p.value_counts()
```




    Vic      24
    other    19
    Name: Pop, dtype: int64




```python
p = data['sex']
p.value_counts()
```




    f    43
    Name: sex, dtype: int64




```python
p.mode()
```




    0    f
    dtype: object



## Excersises

+ What is the longest recorded possum?
+ What is the standard deviation of possum length?
+ The longest relative tail length?

## Data aggregation

### Grouping data according to a single variable

The ```groupby()``` function allows
+ grouping data according to variable values
+ calculating stastistics on each subgroup


```python
#Step 1: create the groups
grp = data.groupby(['Pop'])
grp
```




    <pandas.core.groupby.generic.DataFrameGroupBy object at 0x7f369f748c88>




```python
#Step 2: get the statistics
grp.mean()
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
      <th>case</th>
      <th>site</th>
      <th>age</th>
      <th>hdlngth</th>
      <th>skullw</th>
      <th>totlngth</th>
      <th>taill</th>
      <th>footlgth</th>
      <th>earconch</th>
      <th>eye</th>
      <th>chest</th>
      <th>belly</th>
    </tr>
    <tr>
      <th>Pop</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Vic</th>
      <td>20.333333</td>
      <td>1.208333</td>
      <td>4.041667</td>
      <td>92.412500</td>
      <td>56.645833</td>
      <td>88.333333</td>
      <td>36.333333</td>
      <td>73.021739</td>
      <td>51.758333</td>
      <td>14.695833</td>
      <td>27.750000</td>
      <td>32.541667</td>
    </tr>
    <tr>
      <th>other</th>
      <td>72.578947</td>
      <td>5.210526</td>
      <td>3.894737</td>
      <td>91.815789</td>
      <td>56.515789</td>
      <td>87.368421</td>
      <td>38.078947</td>
      <td>64.378947</td>
      <td>44.557895</td>
      <td>14.957895</td>
      <td>26.815789</td>
      <td>33.315789</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Getting statistics of a single variable
grp.hdlngth.max()
```




    Pop
    Vic      95.9
    other    96.9
    Name: hdlngth, dtype: float64



### Grouping according to multiple variables

You can also group by more than one variable


```python
data['young'] = data.age < 3
grp = data.groupby(['Pop','young'])
table = grp.mean()
table
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
      <th></th>
      <th>case</th>
      <th>site</th>
      <th>age</th>
      <th>hdlngth</th>
      <th>skullw</th>
      <th>totlngth</th>
      <th>taill</th>
      <th>footlgth</th>
      <th>earconch</th>
      <th>eye</th>
      <th>chest</th>
      <th>belly</th>
    </tr>
    <tr>
      <th>Pop</th>
      <th>young</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Vic</th>
      <th>False</th>
      <td>17.750000</td>
      <td>1.125000</td>
      <td>5.250000</td>
      <td>93.250000</td>
      <td>56.875000</td>
      <td>90.437500</td>
      <td>37.156250</td>
      <td>73.953333</td>
      <td>51.612500</td>
      <td>15.000000</td>
      <td>28.062500</td>
      <td>33.531250</td>
    </tr>
    <tr>
      <th>True</th>
      <td>25.500000</td>
      <td>1.375000</td>
      <td>1.625000</td>
      <td>90.737500</td>
      <td>56.187500</td>
      <td>84.125000</td>
      <td>34.687500</td>
      <td>71.275000</td>
      <td>52.050000</td>
      <td>14.087500</td>
      <td>27.125000</td>
      <td>30.562500</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">other</th>
      <th>False</th>
      <td>72.411765</td>
      <td>5.176471</td>
      <td>4.117647</td>
      <td>91.976471</td>
      <td>56.358824</td>
      <td>87.323529</td>
      <td>38.029412</td>
      <td>64.317647</td>
      <td>44.476471</td>
      <td>14.929412</td>
      <td>26.941176</td>
      <td>33.617647</td>
    </tr>
    <tr>
      <th>True</th>
      <td>74.000000</td>
      <td>5.500000</td>
      <td>2.000000</td>
      <td>90.450000</td>
      <td>57.850000</td>
      <td>87.750000</td>
      <td>38.500000</td>
      <td>64.900000</td>
      <td>45.250000</td>
      <td>15.200000</td>
      <td>25.750000</td>
      <td>30.750000</td>
    </tr>
  </tbody>
</table>
</div>




```python
grp.taill.max()
```




    Pop    young
    Vic    False    39.5
           True     36.5
    other  False    41.0
           True     39.0
    Name: taill, dtype: float64



### Resetting the indices

The results of calculating statstics by group, is a dataframe with the grouping variables as indices. This makes it less easy to use the result in subsequent operations.


```python
b = grp.taill.max()
b.index
```




    MultiIndex(levels=[['Vic', 'other'], [False, True]],
               codes=[[0, 0, 1, 1], [0, 1, 0, 1]],
               names=['Pop', 'young'])



Using the reset_index() function, the results can be converted to a 'clean' dataframe with only a single, numeric index. The indices will be converted to variables.


```python
print(table.index)
```

    MultiIndex(levels=[['Vic', 'other'], [False, True]],
               codes=[[0, 0, 1, 1], [0, 1, 0, 1]],
               names=['Pop', 'young'])



```python
table
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
      <th></th>
      <th>case</th>
      <th>site</th>
      <th>age</th>
      <th>hdlngth</th>
      <th>skullw</th>
      <th>totlngth</th>
      <th>taill</th>
      <th>footlgth</th>
      <th>earconch</th>
      <th>eye</th>
      <th>chest</th>
      <th>belly</th>
    </tr>
    <tr>
      <th>Pop</th>
      <th>young</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">Vic</th>
      <th>False</th>
      <td>17.750000</td>
      <td>1.125000</td>
      <td>5.250000</td>
      <td>93.250000</td>
      <td>56.875000</td>
      <td>90.437500</td>
      <td>37.156250</td>
      <td>73.953333</td>
      <td>51.612500</td>
      <td>15.000000</td>
      <td>28.062500</td>
      <td>33.531250</td>
    </tr>
    <tr>
      <th>True</th>
      <td>25.500000</td>
      <td>1.375000</td>
      <td>1.625000</td>
      <td>90.737500</td>
      <td>56.187500</td>
      <td>84.125000</td>
      <td>34.687500</td>
      <td>71.275000</td>
      <td>52.050000</td>
      <td>14.087500</td>
      <td>27.125000</td>
      <td>30.562500</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">other</th>
      <th>False</th>
      <td>72.411765</td>
      <td>5.176471</td>
      <td>4.117647</td>
      <td>91.976471</td>
      <td>56.358824</td>
      <td>87.323529</td>
      <td>38.029412</td>
      <td>64.317647</td>
      <td>44.476471</td>
      <td>14.929412</td>
      <td>26.941176</td>
      <td>33.617647</td>
    </tr>
    <tr>
      <th>True</th>
      <td>74.000000</td>
      <td>5.500000</td>
      <td>2.000000</td>
      <td>90.450000</td>
      <td>57.850000</td>
      <td>87.750000</td>
      <td>38.500000</td>
      <td>64.900000</td>
      <td>45.250000</td>
      <td>15.200000</td>
      <td>25.750000</td>
      <td>30.750000</td>
    </tr>
  </tbody>
</table>
</div>




```python
new = table.reset_index()
new
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
      <th>Pop</th>
      <th>young</th>
      <th>case</th>
      <th>site</th>
      <th>age</th>
      <th>hdlngth</th>
      <th>skullw</th>
      <th>totlngth</th>
      <th>taill</th>
      <th>footlgth</th>
      <th>earconch</th>
      <th>eye</th>
      <th>chest</th>
      <th>belly</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Vic</td>
      <td>False</td>
      <td>17.750000</td>
      <td>1.125000</td>
      <td>5.250000</td>
      <td>93.250000</td>
      <td>56.875000</td>
      <td>90.437500</td>
      <td>37.156250</td>
      <td>73.953333</td>
      <td>51.612500</td>
      <td>15.000000</td>
      <td>28.062500</td>
      <td>33.531250</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Vic</td>
      <td>True</td>
      <td>25.500000</td>
      <td>1.375000</td>
      <td>1.625000</td>
      <td>90.737500</td>
      <td>56.187500</td>
      <td>84.125000</td>
      <td>34.687500</td>
      <td>71.275000</td>
      <td>52.050000</td>
      <td>14.087500</td>
      <td>27.125000</td>
      <td>30.562500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>other</td>
      <td>False</td>
      <td>72.411765</td>
      <td>5.176471</td>
      <td>4.117647</td>
      <td>91.976471</td>
      <td>56.358824</td>
      <td>87.323529</td>
      <td>38.029412</td>
      <td>64.317647</td>
      <td>44.476471</td>
      <td>14.929412</td>
      <td>26.941176</td>
      <td>33.617647</td>
    </tr>
    <tr>
      <th>3</th>
      <td>other</td>
      <td>True</td>
      <td>74.000000</td>
      <td>5.500000</td>
      <td>2.000000</td>
      <td>90.450000</td>
      <td>57.850000</td>
      <td>87.750000</td>
      <td>38.500000</td>
      <td>64.900000</td>
      <td>45.250000</td>
      <td>15.200000</td>
      <td>25.750000</td>
      <td>30.750000</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(new.columns)
```

    Index(['Pop', 'young', 'case', 'site', 'age', 'hdlngth', 'skullw', 'totlngth',
           'taill', 'footlgth', 'earconch', 'eye', 'chest', 'belly'],
          dtype='object')


### Using the ```course``` package

*The following code is needed to be able to import `course` on my computer. You can ignore this if you have downloaded the `course` package to your working directory*


```python
import sys
import os
print(os.getcwd())
sys.path.append('/home/dieter/Dropbox/PythonRepos/')
print(sys.path)
```

    /home/dieter/Dropbox/PythonCourse/08_Pandas_Statistics
    ['/home/dieter/Dropbox/PythonCourse/08_Pandas_Statistics', '/home/dieter/anaconda3/envs/default/lib/python37.zip', '/home/dieter/anaconda3/envs/default/lib/python3.7', '/home/dieter/anaconda3/envs/default/lib/python3.7/lib-dynload', '', '/home/dieter/anaconda3/envs/default/lib/python3.7/site-packages', '/home/dieter/anaconda3/envs/default/lib/python3.7/site-packages/IPython/extensions', '/home/dieter/.ipython', '/home/dieter/Dropbox/PythonRepos/']


The ```course.stats``` module contains a function ```group()``` that simplifies getting group statistics from a dataframe.


```python
from course import stats
result = stats.group(data, ['sex', 'Age'], 'mean')
result.head()
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
      <th>sex</th>
      <th>age</th>
      <th>case</th>
      <th>site</th>
      <th>hdlngth</th>
      <th>skullw</th>
      <th>totlngth</th>
      <th>taill</th>
      <th>footlgth</th>
      <th>earconch</th>
      <th>eye</th>
      <th>chest</th>
      <th>belly</th>
      <th>young</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>f</td>
      <td>1</td>
      <td>20.666667</td>
      <td>1.333333</td>
      <td>90.833333</td>
      <td>58.000000</td>
      <td>85.000000</td>
      <td>35.333333</td>
      <td>71.700000</td>
      <td>53.400000</td>
      <td>13.966667</td>
      <td>28.000000</td>
      <td>29.333333</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>f</td>
      <td>2</td>
      <td>41.428571</td>
      <td>2.571429</td>
      <td>90.614286</td>
      <td>55.885714</td>
      <td>84.785714</td>
      <td>35.500000</td>
      <td>69.271429</td>
      <td>49.528571</td>
      <td>14.457143</td>
      <td>26.357143</td>
      <td>31.142857</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>f</td>
      <td>3</td>
      <td>64.272727</td>
      <td>4.363636</td>
      <td>92.409091</td>
      <td>56.418182</td>
      <td>88.136364</td>
      <td>37.772727</td>
      <td>67.218182</td>
      <td>46.318182</td>
      <td>14.863636</td>
      <td>26.681818</td>
      <td>33.000000</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>f</td>
      <td>4</td>
      <td>48.000000</td>
      <td>3.166667</td>
      <td>91.900000</td>
      <td>55.750000</td>
      <td>88.333333</td>
      <td>38.083333</td>
      <td>68.466667</td>
      <td>48.633333</td>
      <td>15.066667</td>
      <td>27.666667</td>
      <td>35.000000</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>f</td>
      <td>5</td>
      <td>39.666667</td>
      <td>2.500000</td>
      <td>93.066667</td>
      <td>56.900000</td>
      <td>87.833333</td>
      <td>36.500000</td>
      <td>68.460000</td>
      <td>46.333333</td>
      <td>15.450000</td>
      <td>28.000000</td>
      <td>34.750000</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python
result = stats.group(data, ['sex', 'Age'], 'std')
result.head()
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
      <th>sex</th>
      <th>age</th>
      <th>case</th>
      <th>site</th>
      <th>hdlngth</th>
      <th>skullw</th>
      <th>totlngth</th>
      <th>taill</th>
      <th>footlgth</th>
      <th>earconch</th>
      <th>eye</th>
      <th>chest</th>
      <th>belly</th>
      <th>young</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>f</td>
      <td>1</td>
      <td>16.802778</td>
      <td>0.577350</td>
      <td>5.371530</td>
      <td>8.560958</td>
      <td>8.674676</td>
      <td>1.258306</td>
      <td>2.598076</td>
      <td>0.200000</td>
      <td>0.873689</td>
      <td>2.645751</td>
      <td>3.785939</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>f</td>
      <td>2</td>
      <td>26.462912</td>
      <td>2.225395</td>
      <td>1.049490</td>
      <td>1.493797</td>
      <td>2.530763</td>
      <td>2.432420</td>
      <td>3.206095</td>
      <td>3.305911</td>
      <td>0.886674</td>
      <td>2.230738</td>
      <td>1.749149</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>f</td>
      <td>3</td>
      <td>27.291357</td>
      <td>2.248232</td>
      <td>2.568445</td>
      <td>2.002907</td>
      <td>3.918488</td>
      <td>1.633457</td>
      <td>5.676939</td>
      <td>3.909685</td>
      <td>1.246814</td>
      <td>1.692228</td>
      <td>2.924038</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>f</td>
      <td>4</td>
      <td>26.750701</td>
      <td>2.483277</td>
      <td>3.736844</td>
      <td>2.520913</td>
      <td>4.966555</td>
      <td>1.800463</td>
      <td>6.289568</td>
      <td>4.444172</td>
      <td>0.422690</td>
      <td>1.861899</td>
      <td>2.366432</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>f</td>
      <td>5</td>
      <td>20.353542</td>
      <td>1.516575</td>
      <td>2.671080</td>
      <td>1.532319</td>
      <td>3.356586</td>
      <td>1.264911</td>
      <td>4.087542</td>
      <td>5.358607</td>
      <td>1.139737</td>
      <td>0.632456</td>
      <td>3.416870</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
result = stats.group(data, ['gender', 'Age'], 'std')
result.head()
```

    Warning: Can not find variable gender





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
      <th>age</th>
      <th>case</th>
      <th>site</th>
      <th>hdlngth</th>
      <th>skullw</th>
      <th>totlngth</th>
      <th>taill</th>
      <th>footlgth</th>
      <th>earconch</th>
      <th>eye</th>
      <th>chest</th>
      <th>belly</th>
      <th>young</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>16.802778</td>
      <td>0.577350</td>
      <td>5.371530</td>
      <td>8.560958</td>
      <td>8.674676</td>
      <td>1.258306</td>
      <td>2.598076</td>
      <td>0.200000</td>
      <td>0.873689</td>
      <td>2.645751</td>
      <td>3.785939</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>26.462912</td>
      <td>2.225395</td>
      <td>1.049490</td>
      <td>1.493797</td>
      <td>2.530763</td>
      <td>2.432420</td>
      <td>3.206095</td>
      <td>3.305911</td>
      <td>0.886674</td>
      <td>2.230738</td>
      <td>1.749149</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>27.291357</td>
      <td>2.248232</td>
      <td>2.568445</td>
      <td>2.002907</td>
      <td>3.918488</td>
      <td>1.633457</td>
      <td>5.676939</td>
      <td>3.909685</td>
      <td>1.246814</td>
      <td>1.692228</td>
      <td>2.924038</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>26.750701</td>
      <td>2.483277</td>
      <td>3.736844</td>
      <td>2.520913</td>
      <td>4.966555</td>
      <td>1.800463</td>
      <td>6.289568</td>
      <td>4.444172</td>
      <td>0.422690</td>
      <td>1.861899</td>
      <td>2.366432</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>20.353542</td>
      <td>1.516575</td>
      <td>2.671080</td>
      <td>1.532319</td>
      <td>3.356586</td>
      <td>1.264911</td>
      <td>4.087542</td>
      <td>5.358607</td>
      <td>1.139737</td>
      <td>0.632456</td>
      <td>3.416870</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



## Reorganizing a dataframe


```python
c = new.pivot(index='young',columns='Pop', values='taill')
c
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
      <th>Pop</th>
      <th>Vic</th>
      <th>other</th>
    </tr>
    <tr>
      <th>young</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>False</th>
      <td>37.15625</td>
      <td>38.029412</td>
    </tr>
    <tr>
      <th>True</th>
      <td>34.68750</td>
      <td>38.500000</td>
    </tr>
  </tbody>
</table>
</div>



# Exercises

Use the following data for this quiz: `pizzasize.csv` (in the Data folder). The data give the diameters of 250 pizzas, 125 each from two pizza chains, for a variety of crust types and toppings.

## Exercise 1

 Write code that creates a dataframe (table) that lists for each `store` and each `CrustDescription`, the **average pizza diameter**.

 ## Exercise 2

 Write code that creates a dataframe (table) that lists for each `store` and each `CrustDescription`, the **maximum pizza diameter**.

## Exercises 3

Write code that creates a dataframe (table) that lists for each `store` and each `CrustDescription`, the **average pizza area**. Reorganize the table to have  `CrustDescription` as rows and `store` as columns.


```python

```
