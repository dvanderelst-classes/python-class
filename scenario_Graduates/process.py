#https://think.cs.vt.edu/corgis/python/graduates/graduates.html
import pandas
from matplotlib import pyplot

data = pandas.read_csv('graduates.csv')
print(data.describe())

print(data.Education_Major.value_counts())

field = 'Biological Sciences'
field_data = data.query('Education_Major == @field')

pyplot.plot(field_data.Year, field_data.Education_Degrees_Bachelors, '+-')


field = 'Psychology'
field_data = data.query('Education_Major == @field')

pyplot.plot(field_data.Year, field_data.Education_Degrees_Bachelors, '+-')
pyplot.show()
