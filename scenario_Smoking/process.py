import pandas
from matplotlib import pyplot

data = pandas.read_csv('smoking.csv')
data= data.sort_values(by='Year')

select = data.query('State=="Texas"')
pyplot.plot(select.Year, select['Smoke everyday'])

select = data.query('State=="Florida"')
pyplot.plot(select.Year, select['Smoke everyday'])


pyplot.show()

