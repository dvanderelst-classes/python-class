import pandas
import seaborn
from matplotlib import pyplot
import numpy

data = pandas.read_csv('DALYS.csv')
selected = data.query('GHE==880 and country=="Belgium"')
seaborn.barplot(x='group', y='daly_norm_pm', hue='sex', data=selected)
pyplot.show()

#%%
pyplot.figure()
selected = data.query('sex =="Persons" and group == "DALYs 0-4" and GHE==120')

x = numpy.log10(selected['gdp'])
y = numpy.log10(selected['daly_norm_pm'])
pyplot.scatter(x,y)
pyplot.tight_layout()
pyplot.show()

#%%

pyplot.figure()
selected = data.query('sex =="Persons" and group == "DALYs 0-4" and GHE==490')

x = numpy.log10(selected['gdp'])
y = numpy.log10(selected['daly_norm_pm'])
pyplot.scatter(x,y)
pyplot.tight_layout()
pyplot.show()



