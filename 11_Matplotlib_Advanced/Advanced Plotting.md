
<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Read-in-the-data" data-toc-modified-id="Read-in-the-data-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Read in the data</a></span></li><li><span><a href="#Scatter" data-toc-modified-id="Scatter-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Scatter</a></span><ul class="toc-item"><li><span><a href="#Documentation" data-toc-modified-id="Documentation-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Documentation</a></span></li><li><span><a href="#Set-colors" data-toc-modified-id="Set-colors-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Set colors</a></span></li></ul></li><li><span><a href="#Histograms" data-toc-modified-id="Histograms-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Histograms</a></span></li><li><span><a href="#Multiple-plots:-the-subplot-command" data-toc-modified-id="Multiple-plots:-the-subplot-command-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Multiple plots: the subplot command</a></span></li><li><span><a href="#Themes" data-toc-modified-id="Themes-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Themes</a></span></li><li><span><a href="#Complete-Example:-From-data-to-production-plot" data-toc-modified-id="Complete-Example:-From-data-to-production-plot-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Complete Example: From data to production plot</a></span></li></ul></div>


```python
%matplotlib inline
from IPython.display import Image
```

## Read in the data


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



## Scatter


```python
from matplotlib import pyplot
pyplot.scatter(data.Height,data.Weight);
```


![png](Advanced%20Plotting_files/Advanced%20Plotting_5_0.png)


### Documentation

    scatter(x, y, s=20, c=None, marker='o', cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, hold=None, data=None, **kwargs)

The argument c: 

    c : color, sequence, or sequence of color, optional, default: ‘b’

    c can be a single color format string, or a sequence of color specifications of length N, or a sequence of N numbers to be mapped to colors using the cmap and norm specified via kwargs (see below). Note that c should not be a single numeric RGB or RGBA sequence because that is indistinguishable from an array of values to be colormapped. c can be a 2-D array in which the rows are RGB or RGBA, however, including the case of a single row to specify the same color for all points.

This tells us, we can use the argument c color for the points. We have actually a number of options to specify the color for each point:

+ single color format string
+ sequence of color specifications of length N
+ sequence of N numbers to be mapped to colors using the cmap and norm specified via kwargs (see below)
+ a 2-D array in which the rows are RGB or RGBA

### Set colors


```python
selection = data.query('Age < 61')
pyplot.scatter(selection.Height,selection.Weight, c=selection.Waist);
pyplot.xlabel('Height')
pyplot.ylabel('Weight')
pyplot.set_cmap('rainbow')
pyplot.colorbar()
```




    <matplotlib.colorbar.Colorbar at 0x7f3a91605940>




![png](Advanced%20Plotting_files/Advanced%20Plotting_7_1.png)


## Histograms


```python
women = data[data.Gender==0]
men = data[data.Gender==1]

#using histtype='barstacked' ensures the bars for the two data sets align
pyplot.hist(men.Bicep,alpha=0.5,histtype='barstacked', bins=25);
pyplot.hist(women.Bicep,alpha=0.5,histtype='barstacked', bins= 25);
pyplot.legend(['Men', 'Women'])
```




    <matplotlib.legend.Legend at 0x7f3abc30a390>




![png](Advanced%20Plotting_files/Advanced%20Plotting_9_1.png)


## Multiple plots: the subplot command


```python
pyplot.figure(figsize=(10,5))

blue = '#FD6E8A'
pink = '#80B3FF'

pyplot.subplot(1,2,1)

pyplot.scatter(men.Height,men.Weight,c=pink,alpha=0.5, s=30)
pyplot.scatter(women.Height,women.Weight,c=blue,alpha=0.5, s=30)
pyplot.xlabel('Height')               
pyplot.ylabel('Weight')
pyplot.legend(['Men', 'Women'])

pyplot.subplot(1,2,2)

pyplot.hist(men.Height,alpha=0.5, histtype='stepfilled',color=pink)
pyplot.hist(women.Height,alpha=0.5, histtype='stepfilled',color=blue)
pyplot.xlabel('Height')               
pyplot.ylabel('Count')
pyplot.legend(['Men', 'Women'])



pyplot.savefig('graph.png', dpi=300)
```


![png](Advanced%20Plotting_files/Advanced%20Plotting_11_0.png)


## Themes

matplotlib comes with a number of style sheets that can be applied to your plots. They're listed here: https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html

Obviously you can define your own style sheets, which comes in handy when you're plotting multiple graphs for a single project and want them have the same style.


```python
pyplot.style.use('default') # The only thing you need to do is switch the theme on. From then on, the defined style will be used
pyplot.hist(men.height,alpha=0.5, histtype='stepfilled')
pyplot.hist(women.height,alpha=0.5, histtype='stepfilled')
```




    (array([ 3.,  9., 23., 54., 44., 49., 37., 29.,  8.,  4.]),
     array([147.2 , 150.77, 154.34, 157.91, 161.48, 165.05, 168.62, 172.19,
            175.76, 179.33, 182.9 ]),
     <a list of 1 Patch objects>)




![png](Advanced%20Plotting_files/Advanced%20Plotting_13_1.png)



```python
pyplot.style.use('default')
pyplot.style.use('dark_background') # The only thing you need to do is switch the theme on. From then on, the defined style will be used
pyplot.hist(men.height,alpha=0.5, histtype='stepfilled')
pyplot.hist(women.height,alpha=0.5, histtype='stepfilled')
```




    (array([ 3.,  9., 23., 54., 44., 49., 37., 29.,  8.,  4.]),
     array([147.2 , 150.77, 154.34, 157.91, 161.48, 165.05, 168.62, 172.19,
            175.76, 179.33, 182.9 ]),
     <a list of 1 Patch objects>)




![png](Advanced%20Plotting_files/Advanced%20Plotting_14_1.png)



```python
pyplot.style.use('default')
pyplot.style.use('bmh')

pyplot.scatter(men.height,men.weight,c=pink,alpha=0.5, s=10)
pyplot.scatter(women.height,women.weight,c=blue,alpha=0.5, s=10)
```




    <matplotlib.collections.PathCollection at 0x7f369918f630>




![png](Advanced%20Plotting_files/Advanced%20Plotting_15_1.png)


## Complete Example: From data to production plot

Let's assume we are interested in the difference in weight between men and women as a function of height.


```python
import numpy
import pandas

data = pandas.read_csv('data/body.txt', sep='\t', header=None) 
data.columns = ['age','weight', 'height', 'gender']

women = data[data.gender==0]
men = data[data.gender==1]

wm = men.weight
ww = women.weight
hm = men.height
hw = women.height

# Define the colors
red = "#cc0000"
blue = "#6666ff"

# Set the style and the figure size
pyplot.style.use('bmh')
pyplot.figure(figsize=(15, 7))

#Let's try this later.
#pyplot.xkcd()

# We'll make a figure with two panels
pyplot.subplot2grid((2,2), (0, 0), rowspan=2)

# fit a regression line to the men data
x = [numpy.min(hm),numpy.max(hm)]
z = numpy.polyfit(hm, wm, 1)
pm = numpy.poly1d(z)

# Make a string of the fitted equation 
eq_m = '$w_m=' + str(round(z[1],1)) + '+' + str(round(z[0],1)) + 'h$'
print(eq_m)

# Plot the data for the men
pyplot.scatter(hm,wm,color=red, alpha=0.5)
pyplot.plot(x,pm(x),'-',color=red)

# fit a regression line to the women data
x = [numpy.min(hw),numpy.max(hw)]
z = numpy.polyfit(hw, ww, 1)
pw = numpy.poly1d(z)

# Make a string of the fitted equation
eq_w = '$w_w=' + str(round(z[1],1)) + '+' + str(round(z[0],1)) + 'h$'
print(eq_m)

# Plot the women data
pyplot.scatter(hw,ww,color=blue, alpha=0.5)
pyplot.plot(x,pw(x),'-',color=blue)

# Add a legend 
pyplot.legend(['Men','Women'])

# Add the axis labels
pyplot.xlabel('Height (cm)')
pyplot.ylabel('Weight (kg)')

# Add the equations to the plot
pyplot.text(145,110,eq_m,fontsize=15,color=red)
pyplot.text(175,40,eq_w,fontsize=15,color=blue)

pyplot.text(150,115,'(a)',fontsize=12)

# Now start the second panel
pyplot.subplot2grid((2,2), (0, 1))

xrange = numpy.arange(150,200,1)
ym = pm(xrange)
yw = pw(xrange)
diff = ym - yw
pyplot.plot(xrange, diff,color='k')
pyplot.xlabel('Height (cm)')
pyplot.ylabel('Weight Difference (kg)')
pyplot.text(150,12,'(b)',fontsize=12)

# Now start the third panel
pyplot.subplot2grid((2,2), (1, 1))
settings = pyplot.hist(men.age,alpha=0.5,color=red)

# Reuse the bins used for the men in plotting the women
bins = settings[1]
pyplot.hist(women.age,alpha=0.5,color=blue,bins=bins)
pyplot.ylabel('Age')
pyplot.xlabel('Count')
pyplot.text(60,70,'(c)',fontsize=12)

pyplot.savefig('weight_women_men.png')
```

    $w_m=-61.0+0.8h$
    $w_m=-61.0+0.8h$



![png](Advanced%20Plotting_files/Advanced%20Plotting_17_1.png)


# Recreating a graph from the Economist

As an exercise, we'll try our hand at recreating the following plot from the the economist.


```python
Image("hiv.png")
```




![png](Advanced%20Plotting_files/Advanced%20Plotting_19_0.png)


