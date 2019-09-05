
<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Cheat-sheet" data-toc-modified-id="Cheat-sheet-1">Cheat sheet</a></span><ul class="toc-item"><li><span><a href="#Step-1:-read-in-the-data" data-toc-modified-id="Step-1:-read-in-the-data-1.1">Step 1: read in the data</a></span></li><li><span><a href="#Step-2:-look-at-the-data" data-toc-modified-id="Step-2:-look-at-the-data-1.2">Step 2: look at the data</a></span></li><li><span><a href="#Step-3:-selecting-data" data-toc-modified-id="Step-3:-selecting-data-1.3">Step 3: selecting data</a></span></li><li><span><a href="#Step-4:-Calculating-group-statistics" data-toc-modified-id="Step-4:-Calculating-group-statistics-1.4">Step 4: Calculating group statistics</a></span></li></ul></li></ul></div>

# Cheat sheet

In this cheat sheet, I use data sets from this website: https://vincentarelbundock.github.io/Rdatasets/datasets.html. I read in the data directly from the website. Therefore, you should be able to run the code below without having to download it to your computer. I mention the names of the dataset when I use them. You can visit the website to look at the description of the data.

## Step 1: read in the data


```python
import pandas
```

Pandas has several functions for reading in data: http://pandas.pydata.org/pandas-docs/stable/api.html#input-output. The most commonly used function to read in data is ```read_csv()```
: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html#pandas.read_csv.

The ```read_csv()``` can take **many** arguments to specify the format of the file you want to read in. The most important ones are the following:

* sep: Delimiter to use. Example: sep = '\t'
* header: Row number(s) to use for the variable names. Set to None if there is no header in the file: header = None
* index_col: Column to use as the row labels of the DataFrame. Some data files come with a column that can be used as the index. Example: index_col = 0
* na_values: The value of missing data. For example, na_values = 999
* delim_whitespace: Set this to True if the data is seperated by white space. Example: delim_whitespace = True


```python
# Tasting experiment that compared four apple varieties
link = 'http://ww2.amstat.org/publications/jse/datasets/homes76.dat.txt'
data = pandas.read_csv(link, sep='\t')
```

## Step 2: look at the data

Before analysing the data, always make sure the data has been read in correctly. Also look at the descriptives of the data to make sure the data looks uncorrupted.


```python
# Look at the first few lines...
data.head(3)
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
      <th>id</th>
      <th>Y</th>
      <th>X1</th>
      <th>X2</th>
      <th>X3</th>
      <th>X4</th>
      <th>X3X4</th>
      <th>year</th>
      <th>X5</th>
      <th>X5sq</th>
      <th>X6</th>
      <th>status</th>
      <th>D7</th>
      <th>elem</th>
      <th>D8</th>
      <th>D9</th>
      <th>D10</th>
      <th>D11</th>
      <th>D12</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>388.0</td>
      <td>2.180</td>
      <td>4</td>
      <td>3.0</td>
      <td>4</td>
      <td>12.0</td>
      <td>1940</td>
      <td>-3.0</td>
      <td>9.00</td>
      <td>0</td>
      <td>sld</td>
      <td>0</td>
      <td>edison</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>450.0</td>
      <td>2.054</td>
      <td>5</td>
      <td>3.0</td>
      <td>4</td>
      <td>12.0</td>
      <td>1957</td>
      <td>-1.3</td>
      <td>1.69</td>
      <td>2</td>
      <td>sld</td>
      <td>0</td>
      <td>edison</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>386.0</td>
      <td>2.112</td>
      <td>5</td>
      <td>2.0</td>
      <td>4</td>
      <td>8.0</td>
      <td>1955</td>
      <td>-1.5</td>
      <td>2.25</td>
      <td>2</td>
      <td>sld</td>
      <td>0</td>
      <td>edison</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# and the last ones.
data.tail(5)
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
      <th>id</th>
      <th>Y</th>
      <th>X1</th>
      <th>X2</th>
      <th>X3</th>
      <th>X4</th>
      <th>X3X4</th>
      <th>year</th>
      <th>X5</th>
      <th>X5sq</th>
      <th>X6</th>
      <th>status</th>
      <th>D7</th>
      <th>elem</th>
      <th>D8</th>
      <th>D9</th>
      <th>D10</th>
      <th>D11</th>
      <th>D12</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>71</th>
      <td>72</td>
      <td>249.9</td>
      <td>2.081</td>
      <td>5</td>
      <td>2.1</td>
      <td>4</td>
      <td>8.4</td>
      <td>1970</td>
      <td>0.0</td>
      <td>0.00</td>
      <td>1</td>
      <td>sld</td>
      <td>0</td>
      <td>harris</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>72</th>
      <td>73</td>
      <td>215.0</td>
      <td>2.044</td>
      <td>1</td>
      <td>1.1</td>
      <td>4</td>
      <td>4.4</td>
      <td>1936</td>
      <td>-3.4</td>
      <td>11.56</td>
      <td>0</td>
      <td>sld</td>
      <td>0</td>
      <td>parker</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>73</th>
      <td>74</td>
      <td>435.0</td>
      <td>2.253</td>
      <td>11</td>
      <td>2.0</td>
      <td>3</td>
      <td>6.0</td>
      <td>1979</td>
      <td>0.9</td>
      <td>0.81</td>
      <td>2</td>
      <td>sld</td>
      <td>0</td>
      <td>edge</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>74</th>
      <td>75</td>
      <td>274.9</td>
      <td>1.861</td>
      <td>4</td>
      <td>2.0</td>
      <td>4</td>
      <td>8.0</td>
      <td>1995</td>
      <td>2.5</td>
      <td>6.25</td>
      <td>2</td>
      <td>act</td>
      <td>1</td>
      <td>parker</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>75</th>
      <td>76</td>
      <td>349.5</td>
      <td>2.896</td>
      <td>4</td>
      <td>3.0</td>
      <td>5</td>
      <td>15.0</td>
      <td>1979</td>
      <td>0.9</td>
      <td>0.81</td>
      <td>2</td>
      <td>act</td>
      <td>1</td>
      <td>crest</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Look at the descriptives. The function describe() returns descriptives for the nummerical variables.
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
      <th>id</th>
      <th>Y</th>
      <th>X1</th>
      <th>X2</th>
      <th>X3</th>
      <th>X4</th>
      <th>X3X4</th>
      <th>year</th>
      <th>X5</th>
      <th>X5sq</th>
      <th>X6</th>
      <th>D7</th>
      <th>D8</th>
      <th>D9</th>
      <th>D10</th>
      <th>D11</th>
      <th>D12</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>76.000000</td>
      <td>76.000000</td>
      <td>76.000000</td>
      <td>76.000000</td>
      <td>76.000000</td>
      <td>76.000000</td>
      <td>76.000000</td>
      <td>76.000000</td>
      <td>76.000000</td>
      <td>76.000000</td>
      <td>76.000000</td>
      <td>76.000000</td>
      <td>76.000000</td>
      <td>76.000000</td>
      <td>76.000000</td>
      <td>76.000000</td>
      <td>76.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>38.500000</td>
      <td>285.795395</td>
      <td>1.970395</td>
      <td>3.986842</td>
      <td>2.207895</td>
      <td>3.447368</td>
      <td>7.672368</td>
      <td>1969.407895</td>
      <td>-0.059211</td>
      <td>5.449868</td>
      <td>1.565789</td>
      <td>0.328947</td>
      <td>0.157895</td>
      <td>0.184211</td>
      <td>0.039474</td>
      <td>0.078947</td>
      <td>0.197368</td>
    </tr>
    <tr>
      <th>std</th>
      <td>22.083176</td>
      <td>60.332686</td>
      <td>0.212420</td>
      <td>1.653227</td>
      <td>0.570325</td>
      <td>0.737468</td>
      <td>2.764663</td>
      <td>23.492511</td>
      <td>2.349251</td>
      <td>8.206546</td>
      <td>0.771760</td>
      <td>0.472953</td>
      <td>0.367065</td>
      <td>0.390232</td>
      <td>0.196013</td>
      <td>0.271448</td>
      <td>0.400657</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>155.500000</td>
      <td>1.440000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>1905.000000</td>
      <td>-6.500000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>19.750000</td>
      <td>242.750000</td>
      <td>1.860750</td>
      <td>3.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>6.000000</td>
      <td>1957.750000</td>
      <td>-1.225000</td>
      <td>0.250000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>38.500000</td>
      <td>276.000000</td>
      <td>1.966500</td>
      <td>4.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>6.300000</td>
      <td>1969.500000</td>
      <td>-0.050000</td>
      <td>1.220000</td>
      <td>2.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>57.250000</td>
      <td>336.750000</td>
      <td>2.107500</td>
      <td>5.000000</td>
      <td>3.000000</td>
      <td>4.000000</td>
      <td>9.000000</td>
      <td>1980.000000</td>
      <td>1.000000</td>
      <td>9.000000</td>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>76.000000</td>
      <td>450.000000</td>
      <td>2.896000</td>
      <td>11.000000</td>
      <td>3.100000</td>
      <td>6.000000</td>
      <td>15.000000</td>
      <td>2005.000000</td>
      <td>3.500000</td>
      <td>42.250000</td>
      <td>3.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# For categorical variables, you can list the count for each value.
data.status.value_counts()
```




    sld    38
    act    25
    pen    13
    Name: status, dtype: int64



## Step 3: selecting data


```python
# Data set: Sexual activity and lifespan of male fruitflies
link = 'http://ww2.amstat.org/publications/jse/datasets/fruitfly.dat.txt'
data = pandas.read_csv(link, delim_whitespace=True, header=None)
data.head(3)
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
      <th>4</th>
      <th>5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>8</td>
      <td>0</td>
      <td>35</td>
      <td>0.64</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>8</td>
      <td>0</td>
      <td>37</td>
      <td>0.68</td>
      <td>9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>8</td>
      <td>0</td>
      <td>49</td>
      <td>0.68</td>
      <td>49</td>
    </tr>
  </tbody>
</table>
</div>



Note: This data comes without headers. However, we can use a list of strings to set the variable names:


```python
names = ['ID', 'PARTNERS', 'TYPE', 'LONGEVITY', 'THORAX', 'SLEEP']
data.columns = names
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
      <th>ID</th>
      <th>PARTNERS</th>
      <th>TYPE</th>
      <th>LONGEVITY</th>
      <th>THORAX</th>
      <th>SLEEP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>125.000000</td>
      <td>125.000000</td>
      <td>125.000000</td>
      <td>125.000000</td>
      <td>125.000000</td>
      <td>125.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>13.000000</td>
      <td>3.600000</td>
      <td>2.200000</td>
      <td>57.440000</td>
      <td>0.820960</td>
      <td>23.464000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>7.240121</td>
      <td>3.625626</td>
      <td>3.443086</td>
      <td>17.563893</td>
      <td>0.077454</td>
      <td>15.878848</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>16.000000</td>
      <td>0.640000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>7.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>46.000000</td>
      <td>0.760000</td>
      <td>13.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>13.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>58.000000</td>
      <td>0.840000</td>
      <td>20.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>19.000000</td>
      <td>8.000000</td>
      <td>1.000000</td>
      <td>70.000000</td>
      <td>0.880000</td>
      <td>29.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>25.000000</td>
      <td>8.000000</td>
      <td>9.000000</td>
      <td>97.000000</td>
      <td>0.940000</td>
      <td>83.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
selected = data.query('PARTNERS == 1')
selected.describe()
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
      <th>ID</th>
      <th>PARTNERS</th>
      <th>TYPE</th>
      <th>LONGEVITY</th>
      <th>THORAX</th>
      <th>SLEEP</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>50.000000</td>
      <td>50.0</td>
      <td>50.000000</td>
      <td>50.00000</td>
      <td>50.000000</td>
      <td>50.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>13.000000</td>
      <td>1.0</td>
      <td>0.500000</td>
      <td>60.78000</td>
      <td>0.831600</td>
      <td>24.920000</td>
    </tr>
    <tr>
      <th>std</th>
      <td>7.284314</td>
      <td>0.0</td>
      <td>0.505076</td>
      <td>15.67305</td>
      <td>0.069762</td>
      <td>17.429555</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>1.0</td>
      <td>0.000000</td>
      <td>21.00000</td>
      <td>0.640000</td>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>7.000000</td>
      <td>1.0</td>
      <td>0.000000</td>
      <td>48.00000</td>
      <td>0.800000</td>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>13.000000</td>
      <td>1.0</td>
      <td>0.500000</td>
      <td>60.00000</td>
      <td>0.840000</td>
      <td>21.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>19.000000</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>70.00000</td>
      <td>0.880000</td>
      <td>28.750000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>25.000000</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>97.00000</td>
      <td>0.920000</td>
      <td>73.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# An example of using multiple selection criteria
selected = data.query('THORAX > 0.7 and SLEEP > 30')
selected.shape
```




    (26, 6)



## Step 4: Calculating group statistics


```python
link = 'http://ww2.amstat.org/publications/jse/datasets/impeach.dat.txt'
data = pandas.read_csv(link, delim_whitespace=True, header=None)
data.columns = ['senator', 'state', 'vote1', 'vote2', 'number_votes', 'party', 'degree', 'percent', 'year', 'first']
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
      <th>senator</th>
      <th>state</th>
      <th>vote1</th>
      <th>vote2</th>
      <th>number_votes</th>
      <th>party</th>
      <th>degree</th>
      <th>percent</th>
      <th>year</th>
      <th>first</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>shelby</td>
      <td>AL</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>92</td>
      <td>43</td>
      <td>2004</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>sessions</td>
      <td>AL</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>100</td>
      <td>43</td>
      <td>2002</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>murkowsk</td>
      <td>AK</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>68</td>
      <td>34</td>
      <td>2004</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>stevens</td>
      <td>AK</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>58</td>
      <td>34</td>
      <td>2002</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>kyl</td>
      <td>AZ</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>96</td>
      <td>47</td>
      <td>2000</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
grp = data.groupby(['party'])
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
      <th>vote1</th>
      <th>vote2</th>
      <th>number_votes</th>
      <th>degree</th>
      <th>percent</th>
      <th>year</th>
      <th>first</th>
    </tr>
    <tr>
      <th>party</th>
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
      <th>0</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>9.955556</td>
      <td>50.088889</td>
      <td>2002.177778</td>
      <td>0.288889</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.818182</td>
      <td>0.909091</td>
      <td>1.727273</td>
      <td>77.872727</td>
      <td>44.945455</td>
      <td>2001.890909</td>
      <td>0.454545</td>
    </tr>
  </tbody>
</table>
</div>




```python
grp = data.groupby(['party'])
grp.max()
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
      <th>senator</th>
      <th>state</th>
      <th>vote1</th>
      <th>vote2</th>
      <th>number_votes</th>
      <th>degree</th>
      <th>percent</th>
      <th>year</th>
      <th>first</th>
    </tr>
    <tr>
      <th>party</th>
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
      <th>0</th>
      <td>wyden</td>
      <td>WV</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>40</td>
      <td>62</td>
      <td>2004</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>warner</td>
      <td>WY</td>
      <td>1</td>
      <td>1</td>
      <td>2</td>
      <td>100</td>
      <td>60</td>
      <td>2004</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>


