<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Sources" data-toc-modified-id="Sources-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Sources</a></span></li><li><span><a href="#Pearson-correlation:-scipy" data-toc-modified-id="Pearson-correlation:-scipy-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Pearson correlation: scipy</a></span><ul class="toc-item"><li><span><a href="#Running-the-Pearson-correlation" data-toc-modified-id="Running-the-Pearson-correlation-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Running the Pearson correlation</a></span></li><li><span><a href="#Excersise" data-toc-modified-id="Excersise-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Excersise</a></span></li></ul></li><li><span><a href="#Independent-samples-t-test" data-toc-modified-id="Independent-samples-t-test-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Independent samples t-test</a></span><ul class="toc-item"><li><span><a href="#Running-the-t-test" data-toc-modified-id="Running-the-t-test-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Running the t-test</a></span></li><li><span><a href="#Looking-at-the-descriptive-statistics" data-toc-modified-id="Looking-at-the-descriptive-statistics-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Looking at the descriptive statistics</a></span></li><li><span><a href="#The-non-parametric-equivalent:--Kruskal-Wallis-H-test" data-toc-modified-id="The-non-parametric-equivalent:--Kruskal-Wallis-H-test-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>The non-parametric equivalent:  Kruskal-Wallis H-test</a></span></li><li><span><a href="#Excersise" data-toc-modified-id="Excersise-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Excersise</a></span></li></ul></li><li><span><a href="#Dependent-samples-t-test" data-toc-modified-id="Dependent-samples-t-test-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Dependent samples t-test</a></span><ul class="toc-item"><li><span><a href="#Example-1" data-toc-modified-id="Example-1-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Example 1</a></span></li><li><span><a href="#Example-2" data-toc-modified-id="Example-2-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Example 2</a></span></li><li><span><a href="#The-non-paramtric-equivalent:-Wilcoxon-test" data-toc-modified-id="The-non-paramtric-equivalent:-Wilcoxon-test-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>The non-paramtric equivalent: Wilcoxon test</a></span></li><li><span><a href="#T-test-using-the-stats-module" data-toc-modified-id="T-test-using-the-stats-module-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>T-test using the <code>stats</code> module</a></span></li></ul></li><li><span><a href="#Regression-using-the-stats-package" data-toc-modified-id="Regression-using-the-stats-package-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Regression using the <code>stats</code> package</a></span><ul class="toc-item"><li><span><a href="#Simple-lineair-regression:-one-predictor" data-toc-modified-id="Simple-lineair-regression:-one-predictor-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Simple lineair regression: one predictor</a></span></li><li><span><a href="#Exercises" data-toc-modified-id="Exercises-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Exercises</a></span></li><li><span><a href="#Multiple-Regression" data-toc-modified-id="Multiple-Regression-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Multiple Regression</a></span></li><li><span><a href="#Multiple-Regression---with-a-categorical-variable" data-toc-modified-id="Multiple-Regression---with-a-categorical-variable-5.4"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Multiple Regression - with a categorical variable</a></span></li><li><span><a href="#Multiple-regression-plot" data-toc-modified-id="Multiple-regression-plot-5.5"><span class="toc-item-num">5.5&nbsp;&nbsp;</span>Multiple regression plot</a></span></li><li><span><a href="#Logistic-Regression:-one-predictor" data-toc-modified-id="Logistic-Regression:-one-predictor-5.6"><span class="toc-item-num">5.6&nbsp;&nbsp;</span>Logistic Regression: one predictor</a></span></li><li><span><a href="#Logistic-regression-plot-using-seaborn" data-toc-modified-id="Logistic-regression-plot-using-seaborn-5.7"><span class="toc-item-num">5.7&nbsp;&nbsp;</span>Logistic regression plot using <code>seaborn</code></a></span></li><li><span><a href="#Multiple-Logistic-Regression" data-toc-modified-id="Multiple-Logistic-Regression-5.8"><span class="toc-item-num">5.8&nbsp;&nbsp;</span>Multiple Logistic Regression</a></span></li></ul></li><li><span><a href="#Exercises" data-toc-modified-id="Exercises-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Exercises</a></span><ul class="toc-item"><li><span><a href="#Purchases" data-toc-modified-id="Purchases-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Purchases</a></span></li><li><span><a href="#Weight-loss" data-toc-modified-id="Weight-loss-6.2"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>Weight loss</a></span></li><li><span><a href="#Mice" data-toc-modified-id="Mice-6.3"><span class="toc-item-num">6.3&nbsp;&nbsp;</span>Mice</a></span></li></ul></li><li><span><a href="#Regression-using-the-Statsmodels-package" data-toc-modified-id="Regression-using-the-Statsmodels-package-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Regression using the <code>Statsmodels</code> package</a></span><ul class="toc-item"><li><span><a href="#Example-1" data-toc-modified-id="Example-1-7.1"><span class="toc-item-num">7.1&nbsp;&nbsp;</span>Example 1</a></span></li><li><span><a href="#Example-2" data-toc-modified-id="Example-2-7.2"><span class="toc-item-num">7.2&nbsp;&nbsp;</span>Example 2</a></span></li><li><span><a href="#Plot-the-model" data-toc-modified-id="Plot-the-model-7.3"><span class="toc-item-num">7.3&nbsp;&nbsp;</span>Plot the model</a></span></li><li><span><a href="#Template-for-a-linear-regression" data-toc-modified-id="Template-for-a-linear-regression-7.4"><span class="toc-item-num">7.4&nbsp;&nbsp;</span>Template for a linear regression</a></span></li></ul></li></ul></div>

# Statistical Tests

## Sources

+ Online book: http://greenteapress.com/thinkstats2/html/index.html
+ Packages:
    + scipy statistics: https://docs.scipy.org/doc/scipy/reference/stats.html
    + sklearn: http://scikit-learn.org/stable/supervised_learning.html#supervised-learning
    + statsmodels: http://www.statsmodels.org/stable/index.html
    
+ ANOVA and Repeated Measures: https://www.marsja.se/repeated-measures-anova-in-python-using-statsmodels/


```python
%matplotlib inline
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



## Pearson correlation: scipy

For a Pearson correlation, each variable should be continuous.  If one or both of the variables are ordinal in measurement, then a Spearman correlation could be conducted instead. See [here](http://www.statisticssolutions.com/pearson-correlation-assumptions/) for more assumptions underlying the Pearson Correlation. 

### Running the Pearson correlation




```python
from matplotlib import pyplot
var1 = data.Bicep
var2 = data.Forearm
pyplot.scatter(var1,var2);
```


    
![png](Statistical%20Tests_files/Statistical%20Tests_4_0.png)
    



```python
# Running the pearson correlation
from scipy.stats import pearsonr
result = pearsonr(data.Bicep, data.Weight)
result # Returns the correlation and the p-value
```




    (0.8666722028122296, 1.2563310442380804e-154)



### Excersise

Select two variables from the data and run a correlation analysis. Try to find two variables that correlate strongly or weakly. Which variables should not be used for a correlation analysis?

## Independent samples t-test

The independent samples t-test whether there the associated population means are significantly different. See (here)[https://libguides.library.kent.edu/SPSS/IndependentTTest] for more information about the independent t-test.

### Running the t-test


```python
# Split the data into two groups: men and women
women = data.query('Gender==0')
men = data.query('Gender==1')
```


```python
# Perform the t-test
from scipy.stats import ttest_ind

result = ttest_ind(women.Height, men.Height)
result
```




    Ttest_indResult(statistic=-21.109478245457304, pvalue=2.2340956600230777e-71)




```python
# Degrees of freedom
df = len(women.Height) + len(men.Height) - 2
df
```




    505



### Looking at the descriptive statistics


```python
women.Height.describe()
```




    count    260.000000
    mean     164.872308
    std        6.544602
    min      147.200000
    25%      160.000000
    50%      164.500000
    75%      169.500000
    max      182.900000
    Name: Height, dtype: float64




```python
men.Height.describe()
```




    count    247.000000
    mean     177.745344
    std        7.183629
    min      157.200000
    25%      172.900000
    50%      177.800000
    75%      182.650000
    max      198.100000
    Name: Height, dtype: float64




### The non-parametric equivalent:  Kruskal-Wallis H-test


```python
pyplot.subplot(1,2,1);
pyplot.hist(women.Waist);
pyplot.subplot(1,2,2);
pyplot.hist(men.Waist);
```


    
![png](Statistical%20Tests_files/Statistical%20Tests_15_0.png)
    



```python
from scipy.stats import kruskal
kruskal(women.Waist, men.Waist)
```




    KruskalResult(statistic=251.4232515704874, pvalue=1.2710465503343314e-56)



### Excersise

Test whether people under 35 and over 35 differ significantly in weight or height.


```python
pyplot.hist(data.Age);
pyplot.title('Age distribution in data set');
```


    
![png](Statistical%20Tests_files/Statistical%20Tests_18_0.png)
    


## Dependent samples t-test

The dependent samples t-test evaluates whether repeated measures taken on a single group differ. See [here](https://statistics.laerd.com/statistical-guides/dependent-t-test-statistical-guide.php) for more information. This [webpage](https://www.statisticssolutions.com/manova-analysis-paired-sample-t-test/) lists the assumptions underlying a paired t-test.

### Example 1


```python
from scipy.stats import ttest_rel

result = ttest_rel(data.Forearm, data.Bicep)
result
```




    Ttest_relResult(statistic=-63.904013585663705, pvalue=1.9634191283434073e-244)




```python
#Degrees of freedom
df = len(data.Forearm) - 1
df
```




    506



### Example 2

The data is described [here](https://vincentarelbundock.github.io/Rdatasets/doc/DAAG/pair65.html).


```python
data = pandas.read_csv('data/bands.csv', index_col=0)
data
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
      <th>heated</th>
      <th>ambient</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>244</td>
      <td>225</td>
    </tr>
    <tr>
      <th>2</th>
      <td>255</td>
      <td>247</td>
    </tr>
    <tr>
      <th>3</th>
      <td>253</td>
      <td>249</td>
    </tr>
    <tr>
      <th>4</th>
      <td>254</td>
      <td>253</td>
    </tr>
    <tr>
      <th>5</th>
      <td>251</td>
      <td>245</td>
    </tr>
    <tr>
      <th>6</th>
      <td>269</td>
      <td>259</td>
    </tr>
    <tr>
      <th>7</th>
      <td>248</td>
      <td>242</td>
    </tr>
    <tr>
      <th>8</th>
      <td>252</td>
      <td>255</td>
    </tr>
    <tr>
      <th>9</th>
      <td>292</td>
      <td>286</td>
    </tr>
  </tbody>
</table>
</div>




```python
result = ttest_rel(data.heated, data.ambient)
result
```




    Ttest_relResult(statistic=3.1130812979723537, pvalue=0.014378322977309298)



### The non-paramtric equivalent: Wilcoxon test


```python
pyplot.hist(data.heated);
```


    
![png](Statistical%20Tests_files/Statistical%20Tests_26_0.png)
    



```python
from scipy.stats import wilcoxon
wilcoxon(data.heated, data.ambient)
```

    /home/dieter/anaconda3/envs/default/lib/python3.7/site-packages/scipy/stats/morestats.py:2778: UserWarning: Warning: sample size too small for normal approximation.
      warnings.warn("Warning: sample size too small for normal approximation.")





    WilcoxonResult(statistic=2.0, pvalue=0.014801612180980936)



### T-test using the ```stats``` module


```python
import stats

# Independent t-test
result = stats.ttest(data.heated, data.ambient, independent=True)
print(result)
print(result[3])
```

    (0.8686108222457811, 16, 0.3979023385863938, 't(16) = 0.87, p = 0.40')
    t(16) = 0.87, p = 0.40



```python
# Dependent t-test
result = stats.ttest(data.heated, data.ambient, independent=False)
print(result)
print(result[3])
```

    (3.1130812979723537, 8, 0.014378322977309298, 't(8) = 3.11, p = 0.01')
    t(8) = 3.11, p = 0.01


## Regression using the `stats` package

### Simple lineair regression: one predictor


```python
import stats
data = pandas.read_csv('data/body.csv')
result = stats.simple_regression('Weight','Height', data)
```


    
![png](Statistical%20Tests_files/Statistical%20Tests_33_0.png)
    



```python
print(result.keys())
```

    dict_keys(['fitted', 'summary', 'prediction', 'X', 'Y'])



```python
result['summary']
```




<table class="simpletable">
<tr>
        <td>Model:</td>               <td>OLS</td>         <td>Adj. R-squared:</td>     <td>0.514</td>  
</tr>
<tr>
  <td>Dependent Variable:</td>     <td>dependent</td>           <td>AIC:</td>         <td>3702.9106</td>
</tr>
<tr>
         <td>Date:</td>        <td>2019-10-03 13:58</td>        <td>BIC:</td>         <td>3711.3676</td>
</tr>
<tr>
   <td>No. Observations:</td>         <td>507</td>         <td>Log-Likelihood:</td>    <td>-1849.5</td> 
</tr>
<tr>
       <td>Df Model:</td>              <td>1</td>           <td>F-statistic:</td>       <td>535.2</td>  
</tr>
<tr>
     <td>Df Residuals:</td>           <td>505</td>       <td>Prob (F-statistic):</td> <td>2.83e-81</td> 
</tr>
<tr>
      <td>R-squared:</td>            <td>0.515</td>            <td>Scale:</td>         <td>86.640</td>  
</tr>
</table>
<table class="simpletable">
<tr>
       <td></td>         <th>Coef.</th>   <th>Std.Err.</th>     <th>t</th>     <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th> 
</tr>
<tr>
  <th>Intercept</th>   <td>-105.0113</td>  <td>7.5394</td>  <td>-13.9283</td> <td>0.0000</td> <td>-119.8237</td> <td>-90.1988</td>
</tr>
<tr>
  <th>independent</th>  <td>1.0176</td>    <td>0.0440</td>   <td>23.1346</td> <td>0.0000</td>  <td>0.9312</td>    <td>1.1040</td> 
</tr>
</table>
<table class="simpletable">
<tr>
     <td>Omnibus:</td>    <td>63.269</td>  <td>Durbin-Watson:</td>    <td>1.894</td>
</tr>
<tr>
  <td>Prob(Omnibus):</td>  <td>0.000</td> <td>Jarque-Bera (JB):</td> <td>93.738</td>
</tr>
<tr>
       <td>Skew:</td>      <td>0.840</td>     <td>Prob(JB):</td>      <td>0.000</td>
</tr>
<tr>
     <td>Kurtosis:</td>    <td>4.270</td>  <td>Condition No.:</td>    <td>3126</td> 
</tr>
</table>



### Exercises
+ Does age predict weight?
+ Re-assess the correlations above using simple linear regression.


### Multiple Regression
The `course` package also provides a function to easily perform multiple regression. In this case, no plot is provided. The model needs to specified using a formula.


```python
formula = 'Weight ~ Age + Bicep + Height'
result = stats.linear_regression(formula, data)
result['summary']
```




<table class="simpletable">
<tr>
        <td>Model:</td>               <td>OLS</td>         <td>Adj. R-squared:</td>     <td>0.820</td>  
</tr>
<tr>
  <td>Dependent Variable:</td>      <td>Weight</td>             <td>AIC:</td>         <td>3200.7034</td>
</tr>
<tr>
         <td>Date:</td>        <td>2019-10-03 13:58</td>        <td>BIC:</td>         <td>3217.6175</td>
</tr>
<tr>
   <td>No. Observations:</td>         <td>507</td>         <td>Log-Likelihood:</td>    <td>-1596.4</td> 
</tr>
<tr>
       <td>Df Model:</td>              <td>3</td>           <td>F-statistic:</td>       <td>769.7</td>  
</tr>
<tr>
     <td>Df Residuals:</td>           <td>503</td>       <td>Prob (F-statistic):</td> <td>1.69e-187</td>
</tr>
<tr>
      <td>R-squared:</td>            <td>0.821</td>            <td>Scale:</td>         <td>32.050</td>  
</tr>
</table>
<table class="simpletable">
<tr>
      <td></td>        <th>Coef.</th>  <th>Std.Err.</th>     <th>t</th>     <th>P>|t|</th>  <th>[0.025</th>   <th>0.975]</th> 
</tr>
<tr>
  <th>Intercept</th> <td>-76.7850</td>  <td>4.7514</td>  <td>-16.1606</td> <td>0.0000</td> <td>-86.1200</td> <td>-67.4500</td>
</tr>
<tr>
  <th>Age</th>        <td>0.0921</td>   <td>0.0267</td>   <td>3.4554</td>  <td>0.0006</td>  <td>0.0397</td>   <td>0.1445</td> 
</tr>
<tr>
  <th>Bicep</th>      <td>2.0927</td>   <td>0.0744</td>   <td>28.1269</td> <td>0.0000</td>  <td>1.9466</td>   <td>2.2389</td> 
</tr>
<tr>
  <th>Height</th>     <td>0.4553</td>   <td>0.0331</td>   <td>13.7454</td> <td>0.0000</td>  <td>0.3902</td>   <td>0.5204</td> 
</tr>
</table>
<table class="simpletable">
<tr>
     <td>Omnibus:</td>    <td>78.150</td>  <td>Durbin-Watson:</td>    <td>2.030</td> 
</tr>
<tr>
  <td>Prob(Omnibus):</td>  <td>0.000</td> <td>Jarque-Bera (JB):</td> <td>168.274</td>
</tr>
<tr>
       <td>Skew:</td>      <td>0.837</td>     <td>Prob(JB):</td>      <td>0.000</td> 
</tr>
<tr>
     <td>Kurtosis:</td>    <td>5.273</td>  <td>Condition No.:</td>    <td>3342</td>  
</tr>
</table>



### Multiple Regression - with a categorical variable


```python
formula = 'Weight ~ Height * C(Gender)'
result = stats.linear_regression(formula, data)
result['summary']
```




<table class="simpletable">
<tr>
        <td>Model:</td>               <td>OLS</td>         <td>Adj. R-squared:</td>     <td>0.566</td>  
</tr>
<tr>
  <td>Dependent Variable:</td>      <td>Weight</td>             <td>AIC:</td>         <td>3647.4550</td>
</tr>
<tr>
         <td>Date:</td>        <td>2019-10-03 13:58</td>        <td>BIC:</td>         <td>3664.3690</td>
</tr>
<tr>
   <td>No. Observations:</td>         <td>507</td>         <td>Log-Likelihood:</td>    <td>-1819.7</td> 
</tr>
<tr>
       <td>Df Model:</td>              <td>3</td>           <td>F-statistic:</td>       <td>220.7</td>  
</tr>
<tr>
     <td>Df Residuals:</td>           <td>503</td>       <td>Prob (F-statistic):</td> <td>2.48e-91</td> 
</tr>
<tr>
      <td>R-squared:</td>            <td>0.568</td>            <td>Scale:</td>         <td>77.359</td>  
</tr>
</table>
<table class="simpletable">
<tr>
            <td></td>              <th>Coef.</th>  <th>Std.Err.</th>    <th>t</th>     <th>P>|t|</th>  <th>[0.025</th>   <th>0.975]</th> 
</tr>
<tr>
  <th>Intercept</th>             <td>-43.8193</td>  <td>13.7788</td> <td>-3.1802</td> <td>0.0016</td> <td>-70.8903</td> <td>-16.7483</td>
</tr>
<tr>
  <th>C(Gender)[T.1]</th>        <td>-17.1341</td>  <td>19.5625</td> <td>-0.8759</td> <td>0.3815</td> <td>-55.5683</td>  <td>21.3002</td>
</tr>
<tr>
  <th>Height</th>                 <td>0.6333</td>   <td>0.0835</td>  <td>7.5842</td>  <td>0.0000</td>  <td>0.4693</td>   <td>0.7974</td> 
</tr>
<tr>
  <th>Height:C(Gender)[T.1]</th>  <td>0.1492</td>   <td>0.1143</td>  <td>1.3055</td>  <td>0.1923</td>  <td>-0.0754</td>  <td>0.3738</td> 
</tr>
</table>
<table class="simpletable">
<tr>
     <td>Omnibus:</td>    <td>92.455</td>  <td>Durbin-Watson:</td>    <td>1.952</td> 
</tr>
<tr>
  <td>Prob(Omnibus):</td>  <td>0.000</td> <td>Jarque-Bera (JB):</td> <td>183.581</td>
</tr>
<tr>
       <td>Skew:</td>      <td>1.011</td>     <td>Prob(JB):</td>      <td>0.000</td> 
</tr>
<tr>
     <td>Kurtosis:</td>    <td>5.146</td>  <td>Condition No.:</td>    <td>11343</td> 
</tr>
</table>




```python
t = data.groupby(['Gender','Height'])
t = t.mean()
t = t.reset_index()
men = t[t.Gender==1]
women = t[t.Gender==0]

pyplot.plot(men.Height,men.Weight,'r.');
pyplot.plot(women.Height,women.Weight,'g.');
```


    
![png](Statistical%20Tests_files/Statistical%20Tests_41_0.png)
    


### Multiple regression plot

The easiest way to plot a multiple regression is using the ```seaborn``` package. 


```python
import seaborn
seaborn.lmplot(x='Height', y='Weight', hue='Gender', data=data);
```


    
![png](Statistical%20Tests_files/Statistical%20Tests_43_0.png)
    



```python
result['summary']
```




<table class="simpletable">
<tr>
        <td>Model:</td>               <td>OLS</td>         <td>Adj. R-squared:</td>     <td>0.566</td>  
</tr>
<tr>
  <td>Dependent Variable:</td>      <td>Weight</td>             <td>AIC:</td>         <td>3647.4550</td>
</tr>
<tr>
         <td>Date:</td>        <td>2019-10-03 13:58</td>        <td>BIC:</td>         <td>3664.3690</td>
</tr>
<tr>
   <td>No. Observations:</td>         <td>507</td>         <td>Log-Likelihood:</td>    <td>-1819.7</td> 
</tr>
<tr>
       <td>Df Model:</td>              <td>3</td>           <td>F-statistic:</td>       <td>220.7</td>  
</tr>
<tr>
     <td>Df Residuals:</td>           <td>503</td>       <td>Prob (F-statistic):</td> <td>2.48e-91</td> 
</tr>
<tr>
      <td>R-squared:</td>            <td>0.568</td>            <td>Scale:</td>         <td>77.359</td>  
</tr>
</table>
<table class="simpletable">
<tr>
            <td></td>              <th>Coef.</th>  <th>Std.Err.</th>    <th>t</th>     <th>P>|t|</th>  <th>[0.025</th>   <th>0.975]</th> 
</tr>
<tr>
  <th>Intercept</th>             <td>-43.8193</td>  <td>13.7788</td> <td>-3.1802</td> <td>0.0016</td> <td>-70.8903</td> <td>-16.7483</td>
</tr>
<tr>
  <th>C(Gender)[T.1]</th>        <td>-17.1341</td>  <td>19.5625</td> <td>-0.8759</td> <td>0.3815</td> <td>-55.5683</td>  <td>21.3002</td>
</tr>
<tr>
  <th>Height</th>                 <td>0.6333</td>   <td>0.0835</td>  <td>7.5842</td>  <td>0.0000</td>  <td>0.4693</td>   <td>0.7974</td> 
</tr>
<tr>
  <th>Height:C(Gender)[T.1]</th>  <td>0.1492</td>   <td>0.1143</td>  <td>1.3055</td>  <td>0.1923</td>  <td>-0.0754</td>  <td>0.3738</td> 
</tr>
</table>
<table class="simpletable">
<tr>
     <td>Omnibus:</td>    <td>92.455</td>  <td>Durbin-Watson:</td>    <td>1.952</td> 
</tr>
<tr>
  <td>Prob(Omnibus):</td>  <td>0.000</td> <td>Jarque-Bera (JB):</td> <td>183.581</td>
</tr>
<tr>
       <td>Skew:</td>      <td>1.011</td>     <td>Prob(JB):</td>      <td>0.000</td> 
</tr>
<tr>
     <td>Kurtosis:</td>    <td>5.146</td>  <td>Condition No.:</td>    <td>11343</td> 
</tr>
</table>



### Logistic Regression: one predictor


```python
pyplot.scatter(data.Height, data.Gender);
```


    
![png](Statistical%20Tests_files/Statistical%20Tests_46_0.png)
    



```python
result = stats.simple_regression('Gender', 'Height', data, typ='log');
```

    Optimization terminated successfully.
             Current function value: 0.384208
             Iterations 7



    
![png](Statistical%20Tests_files/Statistical%20Tests_47_1.png)
    



```python
result['summary']
```




<table class="simpletable">
<tr>
        <td>Model:</td>              <td>Logit</td>      <td>Pseudo R-squared:</td>    <td>0.445</td>  
</tr>
<tr>
  <td>Dependent Variable:</td>     <td>dependent</td>          <td>AIC:</td>         <td>393.5864</td> 
</tr>
<tr>
         <td>Date:</td>        <td>2019-10-03 13:59</td>       <td>BIC:</td>         <td>402.0434</td> 
</tr>
<tr>
   <td>No. Observations:</td>         <td>507</td>        <td>Log-Likelihood:</td>    <td>-194.79</td> 
</tr>
<tr>
       <td>Df Model:</td>              <td>1</td>            <td>LL-Null:</td>        <td>-351.26</td> 
</tr>
<tr>
     <td>Df Residuals:</td>           <td>505</td>         <td>LLR p-value:</td>    <td>5.0192e-70</td>
</tr>
<tr>
      <td>Converged:</td>           <td>1.0000</td>           <td>Scale:</td>         <td>1.0000</td>  
</tr>
<tr>
    <td>No. Iterations:</td>        <td>7.0000</td>              <td></td>               <td></td>     
</tr>
</table>
<table class="simpletable">
<tr>
       <td></td>         <th>Coef.</th>  <th>Std.Err.</th>     <th>z</th>     <th>P>|z|</th>  <th>[0.025</th>   <th>0.975]</th> 
</tr>
<tr>
  <th>Intercept</th>   <td>-46.7633</td>  <td>4.0062</td>  <td>-11.6729</td> <td>0.0000</td> <td>-54.6152</td> <td>-38.9114</td>
</tr>
<tr>
  <th>independent</th>  <td>0.2729</td>   <td>0.0234</td>   <td>11.6692</td> <td>0.0000</td>  <td>0.2271</td>   <td>0.3188</td> 
</tr>
</table>



### Logistic regression plot using ```seaborn```


```python
seaborn.lmplot(y='Gender',x='Height', logistic=True, data=data);
```


    
![png](Statistical%20Tests_files/Statistical%20Tests_50_0.png)
    


### Multiple Logistic Regression


```python
formula = 'Gender ~ Height + Bicep'
result = stats.regression(formula, data, typ='log');
result['summary']
```

    Optimization terminated successfully.
             Current function value: 0.232869
             Iterations 8





<table class="simpletable">
<tr>
        <td>Model:</td>              <td>Logit</td>      <td>Pseudo R-squared:</td>    <td>0.664</td>   
</tr>
<tr>
  <td>Dependent Variable:</td>      <td>Gender</td>            <td>AIC:</td>         <td>242.1297</td>  
</tr>
<tr>
         <td>Date:</td>        <td>2019-04-16 10:23</td>       <td>BIC:</td>         <td>254.8152</td>  
</tr>
<tr>
   <td>No. Observations:</td>         <td>507</td>        <td>Log-Likelihood:</td>    <td>-118.06</td>  
</tr>
<tr>
       <td>Df Model:</td>              <td>2</td>            <td>LL-Null:</td>        <td>-351.26</td>  
</tr>
<tr>
     <td>Df Residuals:</td>           <td>504</td>         <td>LLR p-value:</td>    <td>5.3099e-102</td>
</tr>
<tr>
      <td>Converged:</td>           <td>1.0000</td>           <td>Scale:</td>         <td>1.0000</td>   
</tr>
<tr>
    <td>No. Iterations:</td>        <td>8.0000</td>              <td></td>               <td></td>      
</tr>
</table>
<table class="simpletable">
<tr>
      <td></td>        <th>Coef.</th>  <th>Std.Err.</th>     <th>z</th>     <th>P>|z|</th>  <th>[0.025</th>   <th>0.975]</th> 
</tr>
<tr>
  <th>Intercept</th> <td>-54.6049</td>  <td>5.3758</td>  <td>-10.1575</td> <td>0.0000</td> <td>-65.1414</td> <td>-44.0685</td>
</tr>
<tr>
  <th>Height</th>     <td>0.2151</td>   <td>0.0281</td>   <td>7.6427</td>  <td>0.0000</td>  <td>0.1599</td>   <td>0.2702</td> 
</tr>
<tr>
  <th>Bicep</th>      <td>0.5718</td>   <td>0.0628</td>   <td>9.1092</td>  <td>0.0000</td>  <td>0.4488</td>   <td>0.6949</td> 
</tr>
</table>



## Exercises

### Purchases


```python
data = pandas.read_csv('data/social_network.csv')
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
      <th>User ID</th>
      <th>Gender</th>
      <th>Age</th>
      <th>EstimatedSalary</th>
      <th>Purchased</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15624510</td>
      <td>Male</td>
      <td>19</td>
      <td>19000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15810944</td>
      <td>Male</td>
      <td>35</td>
      <td>20000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>15668575</td>
      <td>Female</td>
      <td>26</td>
      <td>43000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15603246</td>
      <td>Female</td>
      <td>27</td>
      <td>57000</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>15804002</td>
      <td>Male</td>
      <td>19</td>
      <td>76000</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



* Question: Model the prability of purchase as a function of salary, and as a function of salary and gender.

### Weight loss


```python
# https://vincentarelbundock.github.io/Rdatasets/doc/carData/WeightLoss.html
data = pandas.read_csv('https://tinyurl.com/y7asdwuj', index_col=0)
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
      <th>group</th>
      <th>wl1</th>
      <th>wl2</th>
      <th>wl3</th>
      <th>se1</th>
      <th>se2</th>
      <th>se3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Control</td>
      <td>4</td>
      <td>3</td>
      <td>3</td>
      <td>14</td>
      <td>13</td>
      <td>15</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Control</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
      <td>13</td>
      <td>14</td>
      <td>17</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Control</td>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>17</td>
      <td>12</td>
      <td>16</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Control</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>11</td>
      <td>11</td>
      <td>12</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Control</td>
      <td>5</td>
      <td>3</td>
      <td>2</td>
      <td>16</td>
      <td>15</td>
      <td>14</td>
    </tr>
  </tbody>
</table>
</div>



+ Question 1 : Did the diet group loose more weight (`wl1` + `wl2` + `wl3`) than the control group?
+ Question 2 : Does the total weight loss (`wl1` + `wl2` + `wl3`) predict the gain in self-esteem (`se1` + `se2` + `se3`)?

### Mice


```python
# https://vincentarelbundock.github.io/Rdatasets/doc/DAAG/litters.html
data = pandas.read_csv('https://tinyurl.com/y8o4vxtb', index_col=0)
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
      <th>lsize</th>
      <th>bodywt</th>
      <th>brainwt</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>9.447</td>
      <td>0.444</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>9.780</td>
      <td>0.436</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>9.155</td>
      <td>0.417</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>9.613</td>
      <td>0.429</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>8.850</td>
      <td>0.425</td>
    </tr>
  </tbody>
</table>
</div>



+ Question: Does the litter size affect the body weight of mice? Does it affect their brain weight?

## Regression using the `Statsmodels` package



```python
from statsmodels.regression.linear_model import OLS;
import statsmodels.api as sm;
```

### Example 1


```python
# Read in the data
data = pandas.read_csv('data/body.csv')

# Prepare the predictors
predictors = data.loc[:,('Height','Age','Forearm')]
X = sm.add_constant(predictors)

# Define the dependent
dependent = data.Bicep

# Run the analysis and get the results
model = OLS(dependent, X)
fitted = model.fit()
fitted.summary()
```




<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>          <td>Bicep</td>      <th>  R-squared:         </th> <td>   0.891</td> 
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.890</td> 
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   1372.</td> 
</tr>
<tr>
  <th>Date:</th>             <td>Tue, 16 Apr 2019</td> <th>  Prob (F-statistic):</th> <td>1.12e-241</td>
</tr>
<tr>
  <th>Time:</th>                 <td>10:23:33</td>     <th>  Log-Likelihood:    </th> <td> -890.05</td> 
</tr>
<tr>
  <th>No. Observations:</th>      <td>   507</td>      <th>  AIC:               </th> <td>   1788.</td> 
</tr>
<tr>
  <th>Df Residuals:</th>          <td>   503</td>      <th>  BIC:               </th> <td>   1805.</td> 
</tr>
<tr>
  <th>Df Model:</th>              <td>     3</td>      <th>                     </th>     <td> </td>    
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>    
</tr>
</table>
<table class="simpletable">
<tr>
     <td></td>        <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>   <td>   -3.3028</td> <td>    1.171</td> <td>   -2.820</td> <td> 0.005</td> <td>   -5.603</td> <td>   -1.002</td>
</tr>
<tr>
  <th>Height</th>  <td>   -0.0219</td> <td>    0.009</td> <td>   -2.492</td> <td> 0.013</td> <td>   -0.039</td> <td>   -0.005</td>
</tr>
<tr>
  <th>Age</th>     <td>    0.0177</td> <td>    0.007</td> <td>    2.686</td> <td> 0.007</td> <td>    0.005</td> <td>    0.031</td>
</tr>
<tr>
  <th>Forearm</th> <td>    1.4528</td> <td>    0.029</td> <td>   49.263</td> <td> 0.000</td> <td>    1.395</td> <td>    1.511</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>16.176</td> <th>  Durbin-Watson:     </th> <td>   1.928</td>
</tr>
<tr>
  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td>  16.870</td>
</tr>
<tr>
  <th>Skew:</th>          <td> 0.420</td> <th>  Prob(JB):          </th> <td>0.000217</td>
</tr>
<tr>
  <th>Kurtosis:</th>      <td> 3.304</td> <th>  Cond. No.          </th> <td>3.30e+03</td>
</tr>
</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.<br/>[2] The condition number is large, 3.3e+03. This might indicate that there are<br/>strong multicollinearity or other numerical problems.



### Example 2


```python
# Prepare the predictors
predictors = data.loc[:,('Height')]
X = sm.add_constant(predictors)

# Define the dependent
dependent = data.Weight

# Run the analysis and get the results
model = OLS(dependent, X)
fitted = model.fit()
fitted.summary()
```




<table class="simpletable">
<caption>OLS Regression Results</caption>
<tr>
  <th>Dep. Variable:</th>         <td>Weight</td>      <th>  R-squared:         </th> <td>   0.515</td>
</tr>
<tr>
  <th>Model:</th>                   <td>OLS</td>       <th>  Adj. R-squared:    </th> <td>   0.514</td>
</tr>
<tr>
  <th>Method:</th>             <td>Least Squares</td>  <th>  F-statistic:       </th> <td>   535.2</td>
</tr>
<tr>
  <th>Date:</th>             <td>Tue, 16 Apr 2019</td> <th>  Prob (F-statistic):</th> <td>2.83e-81</td>
</tr>
<tr>
  <th>Time:</th>                 <td>10:23:34</td>     <th>  Log-Likelihood:    </th> <td> -1849.5</td>
</tr>
<tr>
  <th>No. Observations:</th>      <td>   507</td>      <th>  AIC:               </th> <td>   3703.</td>
</tr>
<tr>
  <th>Df Residuals:</th>          <td>   505</td>      <th>  BIC:               </th> <td>   3711.</td>
</tr>
<tr>
  <th>Df Model:</th>              <td>     1</td>      <th>                     </th>     <td> </td>   
</tr>
<tr>
  <th>Covariance Type:</th>      <td>nonrobust</td>    <th>                     </th>     <td> </td>   
</tr>
</table>
<table class="simpletable">
<tr>
     <td></td>       <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
</tr>
<tr>
  <th>const</th>  <td> -105.0113</td> <td>    7.539</td> <td>  -13.928</td> <td> 0.000</td> <td> -119.824</td> <td>  -90.199</td>
</tr>
<tr>
  <th>Height</th> <td>    1.0176</td> <td>    0.044</td> <td>   23.135</td> <td> 0.000</td> <td>    0.931</td> <td>    1.104</td>
</tr>
</table>
<table class="simpletable">
<tr>
  <th>Omnibus:</th>       <td>63.269</td> <th>  Durbin-Watson:     </th> <td>   1.894</td>
</tr>
<tr>
  <th>Prob(Omnibus):</th> <td> 0.000</td> <th>  Jarque-Bera (JB):  </th> <td>  93.738</td>
</tr>
<tr>
  <th>Skew:</th>          <td> 0.840</td> <th>  Prob(JB):          </th> <td>4.42e-21</td>
</tr>
<tr>
  <th>Kurtosis:</th>      <td> 4.270</td> <th>  Cond. No.          </th> <td>3.13e+03</td>
</tr>
</table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.<br/>[2] The condition number is large, 3.13e+03. This might indicate that there are<br/>strong multicollinearity or other numerical problems.



### Plot the model

For a model with one predictor, we can plot the results.


```python
prediction = fitted.predict(X)
prediction.shape
```




    (507,)




```python
pyplot.scatter(predictors, dependent);
pyplot.plot(predictors, prediction,'r-');
```


    
![png](Statistical%20Tests_files/Statistical%20Tests_70_0.png)
    


### Template for a linear regression


```python
# Prepare the predictors
predictors = data.loc[:,('Height', 'Age')]
X = sm.add_constant(predictors)

# Define the dependent
dependent = data.Weight

# Run the analysis and get the results
model = OLS(dependent, X)
fitted = model.fit()
print(fitted.summary())

# Get the predicted values
prediction = fitted.predict(X)

if predictors.ndim == 1:
    pyplot.scatter(predictors, dependent);
    pyplot.plot(predictors, prediction,'r-');
else:
    print('Can not plot result for multiple predictors')

```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                 Weight   R-squared:                       0.540
    Model:                            OLS   Adj. R-squared:                  0.538
    Method:                 Least Squares   F-statistic:                     295.6
    Date:                Tue, 16 Apr 2019   Prob (F-statistic):           1.17e-85
    Time:                        10:23:35   Log-Likelihood:                -1835.9
    No. Observations:                 507   AIC:                             3678.
    Df Residuals:                     504   BIC:                             3691.
    Df Model:                           2                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    const       -109.0638      7.388    -14.762      0.000    -123.579     -94.548
    Height         1.0023      0.043     23.326      0.000       0.918       1.087
    Age            0.2213      0.042      5.260      0.000       0.139       0.304
    ==============================================================================
    Omnibus:                       63.655   Durbin-Watson:                   1.914
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):               96.899
    Skew:                           0.830   Prob(JB):                     9.09e-22
    Kurtosis:                       4.353   Cond. No.                     3.19e+03
    ==============================================================================
    
    Warnings:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
    [2] The condition number is large, 3.19e+03. This might indicate that there are
    strong multicollinearity or other numerical problems.
    Can not plot result for multiple predictors

