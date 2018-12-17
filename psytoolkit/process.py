#https://www.psytoolkit.org/cgi-bin/psy2.4.3/survey?s=rGFg3

import pandas

folder ='data'
data_columns = ['dummy','stimulus','response','color','condition','pressed','correct','rt']

data_file = folder + '/data.csv'
survey = pandas.read_csv(data_file,sep=',',index_col=False)
participants = list(survey['participant'].values)
files = list(survey['Experiment:1'].values)

nr = len(files)

survey['subject'] = list(range(1,nr+1))

all_data = None
for x in range(0,nr):
    pp = participants[x]
    fl = folder + '/' + files[x]
    
    data = pandas.read_csv(fl,sep='\s+',header=None)
    data.columns = data_columns
    data['participant'] = pp
    if not all_data is None: all_data = pandas.concat([all_data,data])
    if all_data is None: all_data = data
    
result = pandas.merge(survey,all_data, on = 'participant')
result = result.drop('participant', 1) 
result = result.drop('Experiment:1', 1)    
result = result.drop('TIME_start', 1)    
result = result.drop('TIME_end', 1)
result = result.drop('TIME_total', 1)

new_names = []
names = list(result.columns)

for x in names: 
    x  = x.replace(':1','')
    x = x.lower()
    new_names.append(x)

result.columns = new_names

###
result['congruent'] = result.condition.isin([1,3])
###

result.to_csv('data.csv')

grp = result.groupby(['subject','congruent'])
mns = grp.mean()
print(mns)

grp = result.groupby(['congruent'])
mns = grp.mean()
print(mns)
