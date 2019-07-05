from pandas_ods_reader import read_ods
import pandas

sheet_idx = 1
data = read_ods('mobility.ods', sheet_idx)
data['Mobility26'] = data['Income Age 26 Intercept'] + 0.25 * data['Income Age 26 Slope']
data['College'] = data['College Age 19 Intercept'] + 0.25 * data['College Age 19 Slope']
data['cz'] = data['Commuting Zone']

# These properities are only available as snapshots in time
# Not for every birth cohort
properties = pandas.read_csv('health_ineq_online_table_10.csv')

data = pandas.merge(data, properties, on='cz')

data.to_csv('mobility.csv', index=False)

##
grp = data.groupby(['Birth Cohort'])
mns = grp.mean()
mns = mns.reset_index()