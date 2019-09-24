import pandas
import numpy
from matplotlib import pyplot

data = pandas.read_csv('body.csv')

pyplot.close('all')
pyplot.plot(data['ChestDia'], data['ElbowDia'], linestyle='none', marker='H', color='#002e4d')
pyplot.xlabel('Chest Diameter') 
pyplot.ylabel('Elbow Diameter')   
pyplot.title('Relation between two things')  


pyplot.figure()

women = data.query('Gender==0') 
men = data.query('Gender==1')       

pyplot.plot(men.Height, men.Weight, color='red', marker='s',linestyle='None', alpha=0.5)
pyplot.plot(women.Height, women.Weight, color='green',marker='o',linestyle='None', alpha=0.5)

pyplot.xlabel('Height (cm)')
pyplot.ylabel('Weight (kg)')
pyplot.title('Weight as a function of height');

pyplot.legend(['Men', 'Women']);


pyplot.figure()
pyplot.plot(data['Biiliac'], data['Hip'], linestyle='none', marker='H', color='#002e4d')
            
####
pyplot.figure()
data['age_group'] = numpy.floor(data['Age']/5) * 5

grp = data.groupby(['age_group'])
mns = grp.mean()
mns = mns.reset_index()

pyplot.plot(mns['age_group'], mns['Weight'], marker='s')

pyplot.xlabel('Age Group')
pyplot.ylabel('Average Weight')
pyplot.title('Weight as a function of age');

pyplot.figure()
pyplot.hist(data.Age)


