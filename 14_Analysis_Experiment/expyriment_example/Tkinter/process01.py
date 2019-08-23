import pandas
#import seaborn as sns
import scipy.stats as stats
from matplotlib import pyplot
 
data = pandas.read_csv('alldata.txt',header=None)
data.columns = ['date','subject','word','type','has_e','response','time','feedback']
data['correct'] = data.feedback == 'green'


## Which subjects completed the experiment?
#
#grp = data.groupby(['subject'])
#count = grp.count()
#count = count.reset_index()
#completed = count[count.response==60]
#print('++++++ Complete subjects:')
#print(completed.subject)
#
#data = data[data.subject.isin(completed.subject)]
#
## Remove outliers
#min_accept = 100
#max_accept = 1500
#
#pyplot.hist(data.time)
#data = data[(data.time > min_accept) & (data.time < max_accept)]
#
## Error rate per subject per category
#print('++++++ Error analysis')
#grp = data.groupby(['subject','type'])
#errors = grp.correct.mean()
#errors = errors.reset_index()
#errors_table = errors.pivot(index='subject',columns='type',values='correct')
#print(errors_table)
#
## error test
#print('Test for errors')
#test1 = stats.wilcoxon(errors_table.long, errors_table.short)
#print(test1)
#
## response time
#print('++++++ Response time analysis')
#correct_only = data[data.correct]
#grp = data.groupby(['subject','type'])
#reaction = grp.time.mean()
#reaction = reaction.reset_index()
#reaction_table = reaction.pivot(index='subject',columns='type',values='time')
#print(reaction_table)
#
## response time test
#print('Test for reaction times')
#test2 = stats.ttest_rel(reaction_table.long, reaction_table.short)
#print(test2)
#
## plots
#sns.set(font_scale=2,font='Ubuntu')
#pyplot.subplot(1,2,1)
#
#sns.barplot(x='type',y='correct',data=errors,color='grey')
#pyplot.ylabel('Accuracy')
#
#pyplot.subplot(1,2,2)
#sns.barplot(x='type',y='time',data=reaction,color='grey')
#pyplot.ylabel('Reaction Time (ms)')
#pyplot.tight_layout()
#pyplot.savefig('plot1.png',dpi=300)
#
## What about e/no e words
#print('++++++ Response time analysis per class')
#grp = data.groupby(['subject','has_e'])
#reaction_e = grp.time.mean()
#reaction_e = reaction_e.reset_index()
#reaction_table_e = reaction_e.pivot(index='subject',columns='has_e',values='time')
#print(reaction_table_e)
#
#pyplot.figure()
#sns.barplot(x='has_e',y='time',data=reaction_e,color='grey')
#pyplot.savefig('plot2.png',dpi=300)
