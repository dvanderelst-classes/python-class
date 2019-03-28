import pandas
from matplotlib import pyplot

link_to_data = 'http://tinyurl.com/y6orr2bg'

# Read the data
data = pandas.read_csv(link_to_data, index_col=0)

# print column names
a = data.columns
print(a)

# print first n lines
print(data.head(7))

# difference in number of f/m workers
data['diff'] = data.fnum - data.mnum


# diff_pct
data['diff_pct'] = 100 * (data.mwage - data.fwage) / data.fwage

pyplot.plot(data.age, data.diff_pct)
pyplot.show()

pyplot.plot(data.age, data['diff'])
pyplot.show()
