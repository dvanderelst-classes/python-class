
# Examples

##  Consideration of Future Consequences

### Data

The following items were rated on a likert scale where 1=extremely uncharacteristic, 2=somewhat uncharacteristic, 3=uncertain, 4=somewhat characteristic, 5=extremely characteristic (0=no answer chosen).

+ Q1. I consider how things might be in the future, and try to influence those things with my day to day behavior.  
+ Q2. Often I engage in a particular behavior in order to achieve outcomes that may not result for many years.  
+ Q3. I only act to satisfy immediate concerns, figuring the future will take care of itself.  
+ Q4. My behavior is only influenced by the immediate (i.e., a matter of days or weeks) outcomes of my actions.  
+ Q5. My convenience is a big factor in the decisions I make or the actions I take.  
+ Q6. I am willing to sacrifice my immediate happiness or well-being in order to achieve future outcomes.  
+ Q7. I think it is important to take warnings about negative outcomes seriously even if the negative outcome will not occur for many years.  
+ Q8. I think it is more important to perform a behavior with important distant consequences than a behavior with less-important immediate consequences.  
+ Q9. I generally ignore warnings about possible future problems because I think the problems will be resolved before they reach crisis level.  
+ Q10. I think that sacrificing now is usually unnecessary since future outcomes can be dealt with at a later time.

+ Q11. I only act to satisfy immediate concerns, figuring that I will take care of future problems that may occur at a later date.  
+ Q12. Since my day to day work has specific outcomes, it is more important to me than behavior that has distant outcomes.

On the next page the following three variables were entered:

age. entered as text (ages < 13 removed)
gender. chosen from drop down list (1=male, 2=female, 3=other).
accuracy. Entered as text, prompt: "Please estimate how accurate your answers were about yourself on a scale of 0-100, where 100 means completely accurate (you had no doubts about any of your answers) and 0 means you answered the items randomly. If you do not want your answers used for research, enter 0." <= 0 removed.

The following value was calculated from technical information

country	ISO country code, calculated with MaxMind GeoIPLite


```python
import pandas
data = pandas.read_csv('data/cfcs.csv',sep='\t')
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
      <th>Q1</th>
      <th>Q2</th>
      <th>Q3</th>
      <th>Q4</th>
      <th>Q5</th>
      <th>Q6</th>
      <th>Q7</th>
      <th>Q8</th>
      <th>Q9</th>
      <th>Q10</th>
      <th>Q11</th>
      <th>Q12</th>
      <th>age</th>
      <th>gender</th>
      <th>accuracy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>15035.000000</td>
      <td>15035.000000</td>
      <td>15035.000000</td>
      <td>15035.000000</td>
      <td>15035.000000</td>
      <td>15035.000000</td>
      <td>15035.000000</td>
      <td>15035.000000</td>
      <td>15035.000000</td>
      <td>15035.000000</td>
      <td>15035.000000</td>
      <td>15035.000000</td>
      <td>1.503500e+04</td>
      <td>15035.000000</td>
      <td>1.503500e+04</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3.792152</td>
      <td>3.265846</td>
      <td>2.741669</td>
      <td>2.751912</td>
      <td>3.531360</td>
      <td>3.610243</td>
      <td>3.888992</td>
      <td>3.520319</td>
      <td>2.591819</td>
      <td>2.568540</td>
      <td>2.672032</td>
      <td>2.965281</td>
      <td>5.988844e+04</td>
      <td>1.551314</td>
      <td>3.522619e+05</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.135067</td>
      <td>1.342266</td>
      <td>1.349635</td>
      <td>1.358036</td>
      <td>1.240528</td>
      <td>1.231759</td>
      <td>1.156209</td>
      <td>1.125979</td>
      <td>1.339726</td>
      <td>1.279491</td>
      <td>1.316785</td>
      <td>1.171189</td>
      <td>7.339911e+06</td>
      <td>0.526608</td>
      <td>2.607475e+07</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-1.000000</td>
      <td>-1.000000</td>
      <td>-1.000000</td>
      <td>-1.000000</td>
      <td>-1.000000</td>
      <td>-1.000000</td>
      <td>-1.000000</td>
      <td>-1.000000</td>
      <td>-1.000000</td>
      <td>-1.000000</td>
      <td>-1.000000</td>
      <td>-1.000000</td>
      <td>1.300000e+01</td>
      <td>0.000000</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>3.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>4.000000</td>
      <td>3.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>1.800000e+01</td>
      <td>1.000000</td>
      <td>8.000000e+01</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>2.200000e+01</td>
      <td>2.000000</td>
      <td>9.000000e+01</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>5.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>3.300000e+01</td>
      <td>2.000000</td>
      <td>9.500000e+01</td>
    </tr>
    <tr>
      <th>max</th>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>9.000000e+08</td>
      <td>3.000000</td>
      <td>2.147484e+09</td>
    </tr>
  </tbody>
</table>
</div>




```python
countries = data['country']
counts = countries.value_counts()
counts.head()
```




    US    7893
    GB    1447
    CA     847
    AU     764
    IN     602
    Name: country, dtype: int64




```python
data = data.query('age < 75 and age > 17 and accuracy <=100 and accuracy >=0')
data = data.query('country in ["US","GB","CA"]')
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
      <th>Q1</th>
      <th>Q2</th>
      <th>Q3</th>
      <th>Q4</th>
      <th>Q5</th>
      <th>Q6</th>
      <th>Q7</th>
      <th>Q8</th>
      <th>Q9</th>
      <th>Q10</th>
      <th>Q11</th>
      <th>Q12</th>
      <th>age</th>
      <th>gender</th>
      <th>accuracy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>7579.000000</td>
      <td>7579.000000</td>
      <td>7579.000000</td>
      <td>7579.000000</td>
      <td>7579.000000</td>
      <td>7579.000000</td>
      <td>7579.000000</td>
      <td>7579.000000</td>
      <td>7579.000000</td>
      <td>7579.000000</td>
      <td>7579.000000</td>
      <td>7579.000000</td>
      <td>7579.000000</td>
      <td>7579.000000</td>
      <td>7579.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3.803800</td>
      <td>3.280908</td>
      <td>2.662357</td>
      <td>2.635308</td>
      <td>3.388574</td>
      <td>3.670537</td>
      <td>3.916876</td>
      <td>3.502045</td>
      <td>2.566566</td>
      <td>2.498747</td>
      <td>2.570920</td>
      <td>2.920042</td>
      <td>32.170471</td>
      <td>1.553239</td>
      <td>85.899063</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.129702</td>
      <td>1.367870</td>
      <td>1.341570</td>
      <td>1.354055</td>
      <td>1.280250</td>
      <td>1.201759</td>
      <td>1.143540</td>
      <td>1.131422</td>
      <td>1.329029</td>
      <td>1.262297</td>
      <td>1.308489</td>
      <td>1.187799</td>
      <td>13.456761</td>
      <td>0.524319</td>
      <td>14.417180</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>18.000000</td>
      <td>0.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>4.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>4.000000</td>
      <td>3.000000</td>
      <td>1.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>21.000000</td>
      <td>1.000000</td>
      <td>80.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>2.000000</td>
      <td>3.000000</td>
      <td>28.000000</td>
      <td>2.000000</td>
      <td>90.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>5.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>42.000000</td>
      <td>2.000000</td>
      <td>97.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>74.000000</td>
      <td>3.000000</td>
      <td>100.000000</td>
    </tr>
  </tbody>
</table>
</div>



### Plots

+ Generate a plot comparing the average age of the respondents for the different countries
+ Generate a plot comparing the answers to one of the questions for different countries, as a function of age

## Humor Styles

### Data

This data was collection with an interactive online version of the Humor Styles Questionnaire from

*Martin, R. A., Puhlik-Doris, P., Larsen, G., Gray, J., & Weir, K. (2003). Individual differences in uses of humor and their relation to psychological well-being: Development of the Humor Styles Questionnaire. Journal of Research in Personality, 37, 48-75.*

The variables Q1 through Q32 were statements rated on a five point scale where 1=Never or very rarely true, 2=Rarely true, 3= Sometimes true, 4= Often true, 5=Very often or always true (-1=did not select an answer). The exact statements were can be looked up here: https://openpsychometrics.org/_rawdata/

Test takers were prompted for three more variables:

+ age. entered as as text then parsed to an interger.
+ gender. chosen from drop down list (1=male, 2=female, 3=other)
+ accuracy. How accurate they thought their answers were on a scale from 0 to 100, answers were entered as text and + parsed to an integer. They were instructed to enter a 0 if they did not want to be included in research.	

The four scale scores of the HSQ were calculated as such (php code):

+ affiliative
+ selfenhancing
+ aggressive
+ selfdefeating


```python
data = pandas.read_csv('data/hsq.csv',sep=',')
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
      <th>Q1</th>
      <th>Q2</th>
      <th>Q3</th>
      <th>Q4</th>
      <th>Q5</th>
      <th>Q6</th>
      <th>Q7</th>
      <th>Q8</th>
      <th>Q9</th>
      <th>Q10</th>
      <th>...</th>
      <th>Q30</th>
      <th>Q31</th>
      <th>Q32</th>
      <th>affiliative</th>
      <th>selfenhancing</th>
      <th>agressive</th>
      <th>selfdefeating</th>
      <th>age</th>
      <th>gender</th>
      <th>accuracy</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>4</td>
      <td>5</td>
      <td>4</td>
      <td>3</td>
      <td>4</td>
      <td>3</td>
      <td>...</td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>4.0</td>
      <td>3.5</td>
      <td>3.0</td>
      <td>2.3</td>
      <td>25</td>
      <td>2</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
      <td>4</td>
      <td>3</td>
      <td>...</td>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>3.3</td>
      <td>3.5</td>
      <td>3.3</td>
      <td>2.4</td>
      <td>44</td>
      <td>2</td>
      <td>90</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>3</td>
      <td>3</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
      <td>4</td>
      <td>...</td>
      <td>5</td>
      <td>4</td>
      <td>2</td>
      <td>3.9</td>
      <td>3.9</td>
      <td>3.1</td>
      <td>2.3</td>
      <td>50</td>
      <td>1</td>
      <td>75</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>4</td>
      <td>3</td>
      <td>5</td>
      <td>4</td>
      <td>3</td>
      <td>-1</td>
      <td>4</td>
      <td>...</td>
      <td>5</td>
      <td>3</td>
      <td>3</td>
      <td>3.6</td>
      <td>4.0</td>
      <td>2.9</td>
      <td>3.3</td>
      <td>30</td>
      <td>2</td>
      <td>85</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>5</td>
      <td>4</td>
      <td>1</td>
      <td>4</td>
      <td>4</td>
      <td>...</td>
      <td>5</td>
      <td>4</td>
      <td>2</td>
      <td>4.1</td>
      <td>4.1</td>
      <td>2.9</td>
      <td>2.0</td>
      <td>52</td>
      <td>1</td>
      <td>80</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 39 columns</p>
</div>



### Plots

+ Generate a plot to show whether women's or men's humor becomes more or less aggressive as a function of age.
+ Generate a plot to investigate whether people with a lower accurcy score have a more selfdefeating humor style.

## Close relationships

### Data

This data was collected from an interactive version of the Experinces in Close Relationships Scale by Kelly Brennan, Catherine Clark and Phillip Shaver. [The data is described here.](data/erc_codebook.html)


```python
data = pandas.read_csv('data/erc.csv',sep=',')
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
      <th>Q1</th>
      <th>Q2</th>
      <th>Q3</th>
      <th>Q4</th>
      <th>Q5</th>
      <th>Q6</th>
      <th>Q7</th>
      <th>Q8</th>
      <th>Q9</th>
      <th>Q10</th>
      <th>...</th>
      <th>Q30</th>
      <th>Q31</th>
      <th>Q32</th>
      <th>Q33</th>
      <th>Q34</th>
      <th>Q35</th>
      <th>Q36</th>
      <th>age</th>
      <th>gender</th>
      <th>country</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>...</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>32</td>
      <td>2</td>
      <td>US</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>...</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>5</td>
      <td>35</td>
      <td>1</td>
      <td>US</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>3</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>1</td>
      <td>5</td>
      <td>...</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>19</td>
      <td>1</td>
      <td>IL</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>5</td>
      <td>1</td>
      <td>4</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>...</td>
      <td>3</td>
      <td>2</td>
      <td>4</td>
      <td>4</td>
      <td>5</td>
      <td>4</td>
      <td>3</td>
      <td>32</td>
      <td>1</td>
      <td>US</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>3</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>3</td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>...</td>
      <td>5</td>
      <td>4</td>
      <td>4</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>4</td>
      <td>27</td>
      <td>1</td>
      <td>IE</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 39 columns</p>
</div>



### Plots

Freedom!
