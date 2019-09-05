
<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Selecting-rows-based-on-a-criterion" data-toc-modified-id="Selecting-rows-based-on-a-criterion-1">Selecting rows based on a criterion</a></span></li><li><span><a href="#Single-criterion" data-toc-modified-id="Single-criterion-2">Single criterion</a></span></li><li><span><a href="#Multiple-criteria" data-toc-modified-id="Multiple-criteria-3">Multiple criteria</a></span></li><li><span><a href="#Selecting-multiple-values" data-toc-modified-id="Selecting-multiple-values-4">Selecting multiple values</a></span></li><li><span><a href="#Using-variables-in-a-query" data-toc-modified-id="Using-variables-in-a-query-5">Using variables in a query</a></span></li><li><span><a href="#Exercises" data-toc-modified-id="Exercises-6">Exercises</a></span><ul class="toc-item"><li><span><a href="#Exercise:-Titanic-Data" data-toc-modified-id="Exercise:-Titanic-Data-6.1">Exercise: Titanic Data</a></span></li><li><span><a href="#Exercise:-Car-data" data-toc-modified-id="Exercise:-Car-data-6.2">Exercise: Car data</a></span></li><li><span><a href="#Exercise:-film-data" data-toc-modified-id="Exercise:-film-data-6.3">Exercise: film data</a></span><ul class="toc-item"><li><span><a href="#Question-1" data-toc-modified-id="Question-1-6.3.1">Question 1</a></span></li><li><span><a href="#Question-2" data-toc-modified-id="Question-2-6.3.2">Question 2</a></span></li><li><span><a href="#Question-3" data-toc-modified-id="Question-3-6.3.3">Question 3</a></span></li><li><span><a href="#Question-4" data-toc-modified-id="Question-4-6.3.4">Question 4</a></span></li></ul></li></ul></li></ul></div>

# Filtering Data


```python
# Let's read in some data to work with
import pandas
file_location = 'https://tinyurl.com/y894ft6g'
data = pandas.read_csv(file_location,index_col=0,na_values='NA')
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



## Selecting rows based on a criterion

Often you want to select data based on criteria. The easiest way to select data is using the ```query``` method. The full documentation can be found here: http://tinyurl.com/ybgl4kmt.

The query function takes a string that acts as a 'search term'.

## Single criterion


```python
under_five = data.query('Age <= 5')
under_five.describe()
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
      <th>Age</th>
      <th>Survived</th>
      <th>SexCode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>36.000000</td>
      <td>36.000000</td>
      <td>36.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>2.413333</td>
      <td>0.777778</td>
      <td>0.472222</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.432596</td>
      <td>0.421637</td>
      <td>0.506309</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.170000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>2.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>4.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>5.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
under_five_females = under_five.query('Sex == "female"')
under_five_females.head()
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
      <th>2</th>
      <td>Allison, Miss Helen Loraine</td>
      <td>1st</td>
      <td>2.0</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>339</th>
      <td>Becker, Miss Marion Louise</td>
      <td>2nd</td>
      <td>4.0</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>479</th>
      <td>LaRoche, Miss Louise</td>
      <td>2nd</td>
      <td>1.0</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>480</th>
      <td>LaRoche, Miss Simonne</td>
      <td>2nd</td>
      <td>3.0</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>538</th>
      <td>Quick, Miss Phyllis May</td>
      <td>2nd</td>
      <td>2.0</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## Multiple criteria

You can combine criteria by using ```and```, ```or``` or ```not```.


```python
selection = data.query('Age < 5 or Age > 60')
selection.head()
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
      <th>2</th>
      <td>Allison, Miss Helen Loraine</td>
      <td>1st</td>
      <td>2.00</td>
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
    <tr>
      <th>7</th>
      <td>Andrews, Miss Kornelia Theodosia</td>
      <td>1st</td>
      <td>63.00</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Artagaveytia, Mr Ramon</td>
      <td>1st</td>
      <td>71.00</td>
      <td>male</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>68</th>
      <td>Compton, Mrs Alexander Taylor (Mary Eliza Inge...</td>
      <td>1st</td>
      <td>64.00</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
selection = data.query('Age < 5 and PClass == "3rd"')
selection.head()
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
      <th>617</th>
      <td>Aks, Master Philip</td>
      <td>3rd</td>
      <td>0.83</td>
      <td>male</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>628</th>
      <td>Andersson, Miss Ellis Anna Maria</td>
      <td>3rd</td>
      <td>2.00</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>634</th>
      <td>Andersson, Master Sigvard Harald Elias</td>
      <td>3rd</td>
      <td>4.00</td>
      <td>male</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>645</th>
      <td>Aspland, Master Edvin Rojj Felix</td>
      <td>3rd</td>
      <td>3.00</td>
      <td>male</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>658</th>
      <td>Baclini, Miss Eugenie</td>
      <td>3rd</td>
      <td>3.00</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
selection = data.query('Age < 5 and not(PClass == "3rd")')
selection.head()
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
      <th>2</th>
      <td>Allison, Miss Helen Loraine</td>
      <td>1st</td>
      <td>2.00</td>
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
    <tr>
      <th>87</th>
      <td>Dodge, Master Washington</td>
      <td>1st</td>
      <td>4.00</td>
      <td>male</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>339</th>
      <td>Becker, Miss Marion Louise</td>
      <td>2nd</td>
      <td>4.00</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>340</th>
      <td>Becker, Master Richard F</td>
      <td>2nd</td>
      <td>1.00</td>
      <td>male</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



## Selecting multiple values

A trick for using multiple value or a range of values: the ```in``` keyword.


```python
result = data.query('PClass in["1st", "3rd"]')
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




```python
result = data.query('Age in[7.0,9.0,10.0]')
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
      <th>434</th>
      <td>Hart, Miss Eva Miriam</td>
      <td>2nd</td>
      <td>7.0</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>631</th>
      <td>Andersson, Miss Ingeborg Constancia</td>
      <td>3rd</td>
      <td>9.0</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>644</th>
      <td>Asplund, Master Clarence Gustaf Hugo</td>
      <td>3rd</td>
      <td>9.0</td>
      <td>male</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>681</th>
      <td>Boulos, Miss Laura</td>
      <td>3rd</td>
      <td>9.0</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>739</th>
      <td>Coutts, Master William Leslie</td>
      <td>3rd</td>
      <td>9.0</td>
      <td>male</td>
      <td>1</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



## Using variables in a query

The query is a string. However, you can refer to variables by prefixing them with the ```@``` sign.


```python
my_range = range(7,116)
selected = data.query('Age in @my_range')
selected.head()
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
      <td>29.0</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Allison, Mr Hudson Joshua Creighton</td>
      <td>1st</td>
      <td>30.0</td>
      <td>male</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Allison, Mrs Hudson JC (Bessie Waldo Daniels)</td>
      <td>1st</td>
      <td>25.0</td>
      <td>female</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Anderson, Mr Harry</td>
      <td>1st</td>
      <td>47.0</td>
      <td>male</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Andrews, Miss Kornelia Theodosia</td>
      <td>1st</td>
      <td>63.0</td>
      <td>female</td>
      <td>1</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## Exercises

### Exercise: Titanic Data

+ Count the number of male survivors that were older than 25.
+ How many first class passengers where female?
+ How many female passengers survived?


### Exercise: Car data

The data file contains the following variables.

+ make: Manufacturer
+ model: Model
+ type: Type: Small, Sporty, Compact, Midsize, Large
+ min_price: Minimum Price (in 1,000) - Price for basic version of this model
+ mid_price: Midrange Price (in 1,000) - Average of Min and Max prices
+ max_price: Maximum Price (in 1,000) - Price for a premium version
+ mpg_city: City MPG (miles per gallon by EPA rating)
+ mpg_hgw: Highway MPG
+ aribag: Airbag: Air Bags standard - 0 = none, 1 = driver only, 2 = driver & passenger
+ drive: Drive train type - 0 = rear wheel drive, 1 = front wheel drive, 2 = all wheel drive
+ cylinders: Number of cylinders
+ engine: Engine size (liters)
+ horsepower: Horsepower (maximum)
+ rpm: RPM (revs per minute at maximum horsepower)
+ rpmile: Engine revolutions per mile (in highest gear)
+ manual: Manual transmission available - 0 = No, 1 = Yes
+ tank: Fuel tank capacity (gallons)
+ passengers: Passenger capacity (persons)
+ length: Length (inches)
+ wheelbase: Wheelbase (inches)
+ width: Width (inches)
+ uturn: U-turn space (feet)
+ rearseat: Rear seat room (inches)
+ luggage: Luggage capacity (cu. ft.)
+ weight: Weight (pounds)
+ domestic: Domestic - 0 = non-U.S. manufacturer, 1 = U.S. manufacturer


```python
link = 'https://tinyurl.com/yc5pxn7f'
cars = pandas.read_csv(link,index_col=0)
cars.head()
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
      <th>Manufacturer</th>
      <th>Model</th>
      <th>Type</th>
      <th>Min.Price</th>
      <th>Price</th>
      <th>Max.Price</th>
      <th>MPG.city</th>
      <th>MPG.highway</th>
      <th>AirBags</th>
      <th>DriveTrain</th>
      <th>...</th>
      <th>Passengers</th>
      <th>Length</th>
      <th>Wheelbase</th>
      <th>Width</th>
      <th>Turn.circle</th>
      <th>Rear.seat.room</th>
      <th>Luggage.room</th>
      <th>Weight</th>
      <th>Origin</th>
      <th>Make</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Acura</td>
      <td>Integra</td>
      <td>Small</td>
      <td>12.9</td>
      <td>15.9</td>
      <td>18.8</td>
      <td>25</td>
      <td>31</td>
      <td>None</td>
      <td>Front</td>
      <td>...</td>
      <td>5</td>
      <td>177</td>
      <td>102</td>
      <td>68</td>
      <td>37</td>
      <td>26.5</td>
      <td>11.0</td>
      <td>2705</td>
      <td>non-USA</td>
      <td>Acura Integra</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Acura</td>
      <td>Legend</td>
      <td>Midsize</td>
      <td>29.2</td>
      <td>33.9</td>
      <td>38.7</td>
      <td>18</td>
      <td>25</td>
      <td>Driver &amp; Passenger</td>
      <td>Front</td>
      <td>...</td>
      <td>5</td>
      <td>195</td>
      <td>115</td>
      <td>71</td>
      <td>38</td>
      <td>30.0</td>
      <td>15.0</td>
      <td>3560</td>
      <td>non-USA</td>
      <td>Acura Legend</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Audi</td>
      <td>90</td>
      <td>Compact</td>
      <td>25.9</td>
      <td>29.1</td>
      <td>32.3</td>
      <td>20</td>
      <td>26</td>
      <td>Driver only</td>
      <td>Front</td>
      <td>...</td>
      <td>5</td>
      <td>180</td>
      <td>102</td>
      <td>67</td>
      <td>37</td>
      <td>28.0</td>
      <td>14.0</td>
      <td>3375</td>
      <td>non-USA</td>
      <td>Audi 90</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Audi</td>
      <td>100</td>
      <td>Midsize</td>
      <td>30.8</td>
      <td>37.7</td>
      <td>44.6</td>
      <td>19</td>
      <td>26</td>
      <td>Driver &amp; Passenger</td>
      <td>Front</td>
      <td>...</td>
      <td>6</td>
      <td>193</td>
      <td>106</td>
      <td>70</td>
      <td>37</td>
      <td>31.0</td>
      <td>17.0</td>
      <td>3405</td>
      <td>non-USA</td>
      <td>Audi 100</td>
    </tr>
    <tr>
      <th>5</th>
      <td>BMW</td>
      <td>535i</td>
      <td>Midsize</td>
      <td>23.7</td>
      <td>30.0</td>
      <td>36.2</td>
      <td>22</td>
      <td>30</td>
      <td>Driver only</td>
      <td>Rear</td>
      <td>...</td>
      <td>4</td>
      <td>186</td>
      <td>109</td>
      <td>69</td>
      <td>39</td>
      <td>27.0</td>
      <td>13.0</td>
      <td>3640</td>
      <td>non-USA</td>
      <td>BMW 535i</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 27 columns</p>
</div>



+ Select all cars with at least 25 mpg in the city.
+ Select all BMW's
+ Are there any Large cars with more than 25 mpg in the city?
+ Which cars use over 50% more fuel on the highway than they do in the city?
+ Which cars have an action radius of over 400 miles on the highway?

### Exercise: film data

For this quiz, using the following data file: `films.dat` (in the Data folder). This file lists the title, year of release, length in minutes, number of cast members listed, rating, and number of lines of description are recorded for a simple random sample of 100 movies.

#### Question 1

Write code to select all films from 1980 to 1990 (including both 1980 and 1990) and assign the result of this operation to a new variable.

#### Question 2

Select all films with a rating of 1 and assign the result of this operation to a new variable.

#### Question 3

Write a short script that allows selecting all movies that were made in the five years before a given date.

The script starts by assigning a value (year) to a variable. The script selects all movies made in the 5 years preceding the year assigned to the variable and  prints the selected data to the screen. The earliest film in the data was made in 1924. Therefore, if the year assigned to the variable is before 1930, the script should print the message `No movies found`.

#### Question 4

Write a script that adds a new variable `ratio` to the data. This variable is obtained by dividing the number of actors (`Cast`) by the length of the movie (`Length`). Next, select the movies for which the ratio Cast/Length is at least 0.1. Print the selected movies to the screen.



```python

```
