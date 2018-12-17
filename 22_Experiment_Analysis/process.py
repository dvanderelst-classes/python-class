import pandas
import seaborn
from matplotlib import pyplot
from scipy.stats import ttest_rel, wilcoxon

# Read data

data = pandas.read_csv('data.csv')

## Add a column that indicates whether the trial was consistent
## Consistent means that the arrow pointed to the same side as the
## required response

response = data['response']
stimulus = data['stimulus']
consistent = response.str[0:3] == stimulus.str[0:3]
data['consistent'] = consistent

#
## Initial Look at some descriptives

print('+' * 30)
print('Raw Descriptives')
print(data['rt'].describe())

#
## Throw out some of the reaction time that do not look ok
#

data = data.query('rt > 150 and rt < 1000')
data = data.query('name != "zorro"')
print('+' * 30)
print('Filtered Descriptives')
print(data['rt'].describe())

#
##
## Reaction time analysis
##
#
## Only keep the correct responses for the reaction time analysis
#
correct_data = data.query('status == 1')
print('+' * 30)
print('Correct Descriptives')
print(correct_data['rt'].describe())

#
## Get the means per consistent value and subject name
#
grp = correct_data.groupby(['consistent', 'name'])
mns_rt = grp.mean()
mns_rt = mns_rt.reset_index()
table_rt = mns_rt.pivot(index='name',columns='consistent', values='rt')

print('+' * 30)
print('Mean Reaction Time per subject')
print(table_rt)
#
##
## Error analysis
##
#
## Add a column to data that gives 1 for correct and 0 for incorrect responses
#
data['correct'] = data['status'] == 1
#
## Get the proportion correct responses per consistent value and subject name
#
grp = data.groupby(['consistent', 'name'])
mns_cr = grp.mean()
mns_cr = mns_cr.reset_index()
table_cr = mns_cr.pivot(index='name',columns='consistent', values='correct')

print('+' * 30)
print('Proportion correct per subject')
print(table_cr)

print('+' * 30)
print('Proportion correct (descriptives)')
print(table_cr.describe())

#
##
## Run statistical test
##
#
#
## Reaction times
#
print('+' * 30)
print('T-test result')
result = ttest_rel(table_rt[True], table_rt[False])
dof = len(table_rt) - 1
text = 't(%i) = %.2f, p = %.2f' % (dof, result[0], result[1])
print(result)
print(text)
#
## Proportion correct responses
#
print('+' * 30)
print('Wilcoxon result')
result = wilcoxon(table_cr[True], table_cr[False])
text = 'W = %.2f, p = %.2f' % result
print(result)
print(text)
#
##
## Plot result
##
#
pyplot.style.use('default')
pyplot.style.use('ggplot') # See http://tinyurl.com/y7h3cqh9

pyplot.figure(figsize=(10, 5))
pyplot.subplot(1,2,1)
seaborn.barplot(x='consistent', y='rt', data=mns_rt)
pyplot.title('Reaction time')
pyplot.xticks([0,1], ['Inconsistent', 'Consistent'])
pyplot.xlabel('')
pyplot.ylabel('Reaction Time (ms)')
#
pyplot.subplot(1,2,2)
seaborn.barplot(x='consistent', y='correct', data=mns_cr)
pyplot.title('Proportion correct responses')
pyplot.xticks([0,1], ['Inconsistent', 'Consistent'])
pyplot.xlabel('')
pyplot.ylabel('Proportion correct responses')
#
pyplot.savefig('plot.png')