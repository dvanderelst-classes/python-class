
<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Read-in-data" data-toc-modified-id="Read-in-data-1">Read in data</a></span></li><li><span><a href="#The-plot-function" data-toc-modified-id="The-plot-function-2">The plot function</a></span><ul class="toc-item"><li><span><a href="#As-simple-as-it-gets" data-toc-modified-id="As-simple-as-it-gets-2.1">As simple as it gets</a></span></li><li><span><a href="#Changing-the-markers" data-toc-modified-id="Changing-the-markers-2.2">Changing the markers</a></span></li><li><span><a href="#Changing-the-color" data-toc-modified-id="Changing-the-color-2.3">Changing the color</a></span></li></ul></li><li><span><a href="#Dressing-up-the-graph" data-toc-modified-id="Dressing-up-the-graph-3">Dressing up the graph</a></span></li><li><span><a href="#Multiple-data-sets-on-one-graph" data-toc-modified-id="Multiple-data-sets-on-one-graph-4">Multiple data sets on one graph</a></span></li><li><span><a href="#Exercises" data-toc-modified-id="Exercises-5">Exercises</a></span><ul class="toc-item"><li><span><a href="#Exercise-1:-scatter-plot" data-toc-modified-id="Exercise-1:-scatter-plot-5.1">Exercise 1: scatter plot</a></span></li><li><span><a href="#Exercise-2" data-toc-modified-id="Exercise-2-5.2">Exercise 2</a></span></li><li><span><a href="#Exercise-3" data-toc-modified-id="Exercise-3-5.3">Exercise 3</a></span></li></ul></li></ul></div>


```python
# This is just some code I need to make sure my code below results in the default layout
%matplotlib inline
from matplotlib import pyplot
pyplot.style.use('default')
```

# Pandas Plotting

## Read in data


```python
import pandas
data = pandas.read_csv('data/body.csv')
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
      <th>Biacromial</th>
      <th>Biiliac</th>
      <th>Bitrochanteric</th>
      <th>ChestDepth</th>
      <th>ChestDia</th>
      <th>ElbowDia</th>
      <th>WristDia</th>
      <th>KneeDia</th>
      <th>AnkleDia</th>
      <th>Shoulder</th>
      <th>...</th>
      <th>Bicep</th>
      <th>Forearm</th>
      <th>Knee</th>
      <th>Calf</th>
      <th>Ankle</th>
      <th>Wrist</th>
      <th>Age</th>
      <th>Weight</th>
      <th>Height</th>
      <th>Gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>42.9</td>
      <td>26.0</td>
      <td>31.5</td>
      <td>17.7</td>
      <td>28.0</td>
      <td>13.1</td>
      <td>10.4</td>
      <td>18.8</td>
      <td>14.1</td>
      <td>106.2</td>
      <td>...</td>
      <td>32.5</td>
      <td>26.0</td>
      <td>34.5</td>
      <td>36.5</td>
      <td>23.5</td>
      <td>16.5</td>
      <td>21</td>
      <td>65.6</td>
      <td>174.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>43.7</td>
      <td>28.5</td>
      <td>33.5</td>
      <td>16.9</td>
      <td>30.8</td>
      <td>14.0</td>
      <td>11.8</td>
      <td>20.6</td>
      <td>15.1</td>
      <td>110.5</td>
      <td>...</td>
      <td>34.4</td>
      <td>28.0</td>
      <td>36.5</td>
      <td>37.5</td>
      <td>24.5</td>
      <td>17.0</td>
      <td>23</td>
      <td>71.8</td>
      <td>175.3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40.1</td>
      <td>28.2</td>
      <td>33.3</td>
      <td>20.9</td>
      <td>31.7</td>
      <td>13.9</td>
      <td>10.9</td>
      <td>19.7</td>
      <td>14.1</td>
      <td>115.1</td>
      <td>...</td>
      <td>33.4</td>
      <td>28.8</td>
      <td>37.0</td>
      <td>37.3</td>
      <td>21.9</td>
      <td>16.9</td>
      <td>28</td>
      <td>80.7</td>
      <td>193.5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>44.3</td>
      <td>29.9</td>
      <td>34.0</td>
      <td>18.4</td>
      <td>28.2</td>
      <td>13.9</td>
      <td>11.2</td>
      <td>20.9</td>
      <td>15.0</td>
      <td>104.5</td>
      <td>...</td>
      <td>31.0</td>
      <td>26.2</td>
      <td>37.0</td>
      <td>34.8</td>
      <td>23.0</td>
      <td>16.6</td>
      <td>23</td>
      <td>72.6</td>
      <td>186.5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>42.5</td>
      <td>29.9</td>
      <td>34.0</td>
      <td>21.5</td>
      <td>29.4</td>
      <td>15.2</td>
      <td>11.6</td>
      <td>20.7</td>
      <td>14.9</td>
      <td>107.5</td>
      <td>...</td>
      <td>32.0</td>
      <td>28.4</td>
      <td>37.7</td>
      <td>38.6</td>
      <td>24.4</td>
      <td>18.0</td>
      <td>22</td>
      <td>78.8</td>
      <td>187.2</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 25 columns</p>
</div>




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
      <th>Biacromial</th>
      <th>Biiliac</th>
      <th>Bitrochanteric</th>
      <th>ChestDepth</th>
      <th>ChestDia</th>
      <th>ElbowDia</th>
      <th>WristDia</th>
      <th>KneeDia</th>
      <th>AnkleDia</th>
      <th>Shoulder</th>
      <th>...</th>
      <th>Bicep</th>
      <th>Forearm</th>
      <th>Knee</th>
      <th>Calf</th>
      <th>Ankle</th>
      <th>Wrist</th>
      <th>Age</th>
      <th>Weight</th>
      <th>Height</th>
      <th>Gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>...</td>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>507.000000</td>
      <td>507.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>38.811440</td>
      <td>27.829980</td>
      <td>31.980473</td>
      <td>19.226036</td>
      <td>27.973767</td>
      <td>13.385207</td>
      <td>10.542604</td>
      <td>18.810651</td>
      <td>13.863314</td>
      <td>108.195069</td>
      <td>...</td>
      <td>31.169625</td>
      <td>25.942998</td>
      <td>36.202959</td>
      <td>36.078304</td>
      <td>22.157396</td>
      <td>16.097436</td>
      <td>30.181460</td>
      <td>69.147535</td>
      <td>171.143787</td>
      <td>0.487179</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3.059132</td>
      <td>2.206308</td>
      <td>2.030916</td>
      <td>2.515877</td>
      <td>2.741650</td>
      <td>1.352906</td>
      <td>0.944361</td>
      <td>1.347595</td>
      <td>1.247351</td>
      <td>10.374834</td>
      <td>...</td>
      <td>4.246941</td>
      <td>2.830579</td>
      <td>2.617570</td>
      <td>2.847661</td>
      <td>1.862337</td>
      <td>1.380931</td>
      <td>9.608472</td>
      <td>13.345762</td>
      <td>9.407205</td>
      <td>0.500329</td>
    </tr>
    <tr>
      <th>min</th>
      <td>32.400000</td>
      <td>18.700000</td>
      <td>24.700000</td>
      <td>14.300000</td>
      <td>22.200000</td>
      <td>9.900000</td>
      <td>8.100000</td>
      <td>15.700000</td>
      <td>9.900000</td>
      <td>85.900000</td>
      <td>...</td>
      <td>22.400000</td>
      <td>19.600000</td>
      <td>29.000000</td>
      <td>28.400000</td>
      <td>16.400000</td>
      <td>13.000000</td>
      <td>18.000000</td>
      <td>42.000000</td>
      <td>147.200000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>36.200000</td>
      <td>26.500000</td>
      <td>30.600000</td>
      <td>17.300000</td>
      <td>25.650000</td>
      <td>12.400000</td>
      <td>9.800000</td>
      <td>17.900000</td>
      <td>13.000000</td>
      <td>99.450000</td>
      <td>...</td>
      <td>27.600000</td>
      <td>23.600000</td>
      <td>34.400000</td>
      <td>34.100000</td>
      <td>21.000000</td>
      <td>15.000000</td>
      <td>23.000000</td>
      <td>58.400000</td>
      <td>163.800000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>38.700000</td>
      <td>28.000000</td>
      <td>32.000000</td>
      <td>19.000000</td>
      <td>27.800000</td>
      <td>13.300000</td>
      <td>10.500000</td>
      <td>18.700000</td>
      <td>13.800000</td>
      <td>108.200000</td>
      <td>...</td>
      <td>31.000000</td>
      <td>25.800000</td>
      <td>36.000000</td>
      <td>36.000000</td>
      <td>22.000000</td>
      <td>16.100000</td>
      <td>27.000000</td>
      <td>68.200000</td>
      <td>170.300000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>41.150000</td>
      <td>29.250000</td>
      <td>33.350000</td>
      <td>20.900000</td>
      <td>29.950000</td>
      <td>14.400000</td>
      <td>11.200000</td>
      <td>19.600000</td>
      <td>14.800000</td>
      <td>116.550000</td>
      <td>...</td>
      <td>34.450000</td>
      <td>28.400000</td>
      <td>37.950000</td>
      <td>38.000000</td>
      <td>23.300000</td>
      <td>17.100000</td>
      <td>36.000000</td>
      <td>78.850000</td>
      <td>177.800000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>47.400000</td>
      <td>34.700000</td>
      <td>38.000000</td>
      <td>27.500000</td>
      <td>35.600000</td>
      <td>16.700000</td>
      <td>13.300000</td>
      <td>24.300000</td>
      <td>17.200000</td>
      <td>134.800000</td>
      <td>...</td>
      <td>42.400000</td>
      <td>32.500000</td>
      <td>49.000000</td>
      <td>47.700000</td>
      <td>29.300000</td>
      <td>19.600000</td>
      <td>67.000000</td>
      <td>116.400000</td>
      <td>198.100000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
<p>8 rows × 25 columns</p>
</div>



## The plot function

The plot function is the most basic graphing function in matplotlib.

### As simple as it gets


```python
from matplotlib import pyplot
pyplot.plot(data.Height, data.Weight);
```


![png](Pandas%20Plot_files/Pandas%20Plot_7_0.png)


### Changing the markers

See http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot for a list of markers.


```python
pyplot.plot(data.Height, data.Weight, marker='.', linestyle='None')
```




    [<matplotlib.lines.Line2D at 0x7fa7f70b1ac8>]




![png](Pandas%20Plot_files/Pandas%20Plot_9_1.png)



```python
pyplot.plot(data.Height, data.Weight, marker='*', linestyle='None');
```


![png](Pandas%20Plot_files/Pandas%20Plot_10_0.png)


### Changing the color

Matplotlib knows a number of standard colors by name. You can find a list of these colors here: https://matplotlib.org/examples/color/named_colors.html

You can also specify your own colors in a number of formats. Including hex format. 


```python
pyplot.plot(data.Height, data.Weight, marker='.', linestyle='None', color='salmon');
```


![png](Pandas%20Plot_files/Pandas%20Plot_12_0.png)



```python
my_color = '#647f92'
pyplot.plot(data.Height, data.Weight, marker='s', linestyle='None', color= my_color);
```


![png](Pandas%20Plot_files/Pandas%20Plot_13_0.png)


## Dressing up the graph


```python
my_color = '#647f92'
pyplot.plot(data.Height, data.Weight, '+', color= my_color, markersize=5)

pyplot.xlabel('Height (cm)')
pyplot.ylabel('Weight (kg)')
pyplot.title('Weight as a function of height');
```


![png](Pandas%20Plot_files/Pandas%20Plot_15_0.png)


## Multiple data sets on one graph


```python
women = data.query('Gender==0') 
men = data.query('Gender==1')
men.head()
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
      <th>Biacromial</th>
      <th>Biiliac</th>
      <th>Bitrochanteric</th>
      <th>ChestDepth</th>
      <th>ChestDia</th>
      <th>ElbowDia</th>
      <th>WristDia</th>
      <th>KneeDia</th>
      <th>AnkleDia</th>
      <th>Shoulder</th>
      <th>...</th>
      <th>Bicep</th>
      <th>Forearm</th>
      <th>Knee</th>
      <th>Calf</th>
      <th>Ankle</th>
      <th>Wrist</th>
      <th>Age</th>
      <th>Weight</th>
      <th>Height</th>
      <th>Gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>42.9</td>
      <td>26.0</td>
      <td>31.5</td>
      <td>17.7</td>
      <td>28.0</td>
      <td>13.1</td>
      <td>10.4</td>
      <td>18.8</td>
      <td>14.1</td>
      <td>106.2</td>
      <td>...</td>
      <td>32.5</td>
      <td>26.0</td>
      <td>34.5</td>
      <td>36.5</td>
      <td>23.5</td>
      <td>16.5</td>
      <td>21</td>
      <td>65.6</td>
      <td>174.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>43.7</td>
      <td>28.5</td>
      <td>33.5</td>
      <td>16.9</td>
      <td>30.8</td>
      <td>14.0</td>
      <td>11.8</td>
      <td>20.6</td>
      <td>15.1</td>
      <td>110.5</td>
      <td>...</td>
      <td>34.4</td>
      <td>28.0</td>
      <td>36.5</td>
      <td>37.5</td>
      <td>24.5</td>
      <td>17.0</td>
      <td>23</td>
      <td>71.8</td>
      <td>175.3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>40.1</td>
      <td>28.2</td>
      <td>33.3</td>
      <td>20.9</td>
      <td>31.7</td>
      <td>13.9</td>
      <td>10.9</td>
      <td>19.7</td>
      <td>14.1</td>
      <td>115.1</td>
      <td>...</td>
      <td>33.4</td>
      <td>28.8</td>
      <td>37.0</td>
      <td>37.3</td>
      <td>21.9</td>
      <td>16.9</td>
      <td>28</td>
      <td>80.7</td>
      <td>193.5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>44.3</td>
      <td>29.9</td>
      <td>34.0</td>
      <td>18.4</td>
      <td>28.2</td>
      <td>13.9</td>
      <td>11.2</td>
      <td>20.9</td>
      <td>15.0</td>
      <td>104.5</td>
      <td>...</td>
      <td>31.0</td>
      <td>26.2</td>
      <td>37.0</td>
      <td>34.8</td>
      <td>23.0</td>
      <td>16.6</td>
      <td>23</td>
      <td>72.6</td>
      <td>186.5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>42.5</td>
      <td>29.9</td>
      <td>34.0</td>
      <td>21.5</td>
      <td>29.4</td>
      <td>15.2</td>
      <td>11.6</td>
      <td>20.7</td>
      <td>14.9</td>
      <td>107.5</td>
      <td>...</td>
      <td>32.0</td>
      <td>28.4</td>
      <td>37.7</td>
      <td>38.6</td>
      <td>24.4</td>
      <td>18.0</td>
      <td>22</td>
      <td>78.8</td>
      <td>187.2</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 25 columns</p>
</div>




```python
pyplot.plot(men.Height, men.Weight, color='red', marker='s',linestyle='None', alpha=0.5)
pyplot.plot(women.Height, women.Weight, color='green',marker='o',linestyle='None', alpha=0.5)

pyplot.xlabel('Height (cm)')
pyplot.ylabel('Weight (kg)')
pyplot.title('Weight as a function of height');

pyplot.legend(['Men', 'Women']);
```


![png](Pandas%20Plot_files/Pandas%20Plot_18_0.png)


## Exercises

### Exercise 1: scatter plot

+ Choose two variables and create a scatter plot using orange triangles as markers. 
+ Calculate the average weight for 5-year age groups. Plot the average weight per age group.
+ Plot the weight as a function of age, for the men only
+ Plot the wrist diameter and the Ankle diameter as a function of weight on the same plot using two different colors.
+ Add a label for the x and the y-axis for one of your plots above.

### Exercise 2 

Read in the data file `breslow.csv` . Plot the the number of deaths attributed to coronary artery disease per number of person-years (calculated as `y/n`) for the smokers and non-smokers, for each 10 year age-group. The data is described here: https://vincentarelbundock.github.io/Rdatasets/doc/boot/breslow.html

### Exercise 3

Use the data in `cats.csv`. Generate a scatter plot of the heart weight (`Hwt`) as a function of body weight (`Bwt`). Plot the data for the female and male cats in different colors. Add a legend to the plot that shows which color corresponds to the genders. Add a regression line for each gender (in the corresponding color). The data is described here: https://vincentarelbundock.github.io/Rdatasets/doc/boot/catsM.html



```python

```
