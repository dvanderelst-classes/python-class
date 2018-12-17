import pandas
from matplotlib import pyplot

data = pandas.read_sas('DEMO_I.XPT')
vars = ['SEQN','WTINT2YR']
names = ['id','sample_weight']
demo = data.loc[:, vars]
demo.columns = names

data = pandas.read_sas('AUQ_I.XPT')
vars = ['SEQN','AUQ250', 'AUQ255']
names = ['id','duration', 'frequency']
tinnitus = data.loc[:, vars]
tinnitus.columns = names

tinnitus = pandas.merge(tinnitus, demo)

tinnitus = tinnitus.dropna()
tinnitus = tinnitus[tinnitus.duration < 5]
tinnitus = tinnitus[tinnitus.frequency < 100]

# Add weights to compensate different time bins
categories = [1, 2, 3, 4, 5, 9]
weight = [3, 9, 36, 48, 1, 1]
weights = pandas.DataFrame({'duration': categories, 'weight': weight})
tinnitus = pandas.merge(tinnitus, weights)
tinnitus.weight = (1 / tinnitus.weight) * tinnitus.sample_weight

#
grp = tinnitus.groupby(['duration'])
duration_table = grp.sum()
duration_table = duration_table.reset_index()

normalized = duration_table.weight/duration_table.weight.max()

pyplot.bar(range(0,4),normalized)
pyplot.show()
