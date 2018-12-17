import numpy
from matplotlib import pyplot

#Read in the data
#Let's have a look at the data (also in the variable explorer)
data = numpy.loadtxt('hiv.csv',delimiter=',',skiprows=1)

## Set the style to the default one: classic
pyplot.style.use('classic')
#
## get the data, these are the fields: year,hiv_upper,hiv,hiv_lower,aids_upper,aids,aids_lower,med
year = data[:,0]
hiv_upper = data[:,1]
hiv = data[:,2]
hiv_lower = data[:,3]
aids_upper = data[:,4]
aids = data[:,5]
aids_lower = data[:,6]
therapy = data[:,7] * 5
#
##The graph does not have treatement data for the first years
therapy[0:10] = numpy.NAN
#
## define the colors - there is an Easy way of getting the exact colors from the graph.
blue = '#00587B'
cyan = '#19A2DA'
red = '#E61B22'
#
##close all figures and create a figure with the right dimensions
pyplot.close('all')
#
pyplot.figure(figsize=(14,10),facecolor='white')
#pyplot.figure(figsize=(7,5),facecolor='white')
#
## The shading trick
## http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.fill_between
#
## plot infections per year
color = blue
pyplot.fill_between(year,hiv_lower,hiv_upper,color=color,alpha=0.25)
pyplot.plot(year,hiv,color=color,linewidth=4)
pyplot.plot(year,hiv_upper,color=color,linewidth=1)
pyplot.plot(year,hiv_lower,color=color,linewidth=1)
#
## plot deaths per year
color = cyan
pyplot.fill_between(year,aids_lower,aids_upper,color=color,alpha=0.25)
pyplot.plot(year,aids,color=color,linewidth=4)
pyplot.plot(year,aids_upper,color=color,linewidth=1)
pyplot.plot(year,aids_lower,color=color,linewidth=1)
#
## The trick with the second axis
## http://matplotlib.org/faq/howto_faq.html#multiple-y-axis-scales
ax1 = pyplot.gca()
ax2 = ax1.twinx()

pyplot.plot(year, therapy,color=red,linewidth=4)
#
## This concludes the basic plotting tasks. All that is left to do now is dress up the graph (how hard can that be?).
## This is also the point at which I started googling a lot.
#
## Set the limit of the x axis and y axis
ax1.set_xlim([1989,2016])
ax2.set_ylim([0,20*1.01])
ax1.set_ylim([0,4*1.01])
#
## Set minor and major ticks on the x axis
ax1.tick_params(axis='x',labelsize=14,which='major',length=10)
ax1.tick_params(axis='x',labelsize=14,which='minor',length=5)
ax1.set_xticks(numpy.arange(1990,2016,1),minor=True)
ax1.set_xticks(numpy.arange(1990,2020,5),minor=False)
ax1.set_xticklabels(['1990','95','2000','05','2010','15'],minor=False)
#
## Set the color and the position of the y ticks for both axis
ax1.tick_params(axis='y', colors=cyan,length=0,labelsize=15)
ax1.set_yticks(numpy.arange(0,4.5,0.5))
ax2.tick_params(axis='y', colors=red,length=0,labelsize=15)
ax2.set_yticks(numpy.arange(0,22.5,2.5))
#
## Set the grid lines 
pyplot.grid(color = '0.65' ,linestyle='-',axis='y',linewidth=2,alpha=0.5)
#
## Now we have to remove the lines around the graph - this took me a while, to be honest
ax1.spines['left'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
#
ax2.spines['left'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
#
ax1.xaxis.set_ticks_position('bottom')
ax2.xaxis.set_ticks_position('bottom')
#
## Lets annotate the graph as well
ax1.text(1995,3.7,'New HIV infections per year',color=blue,fontsize=16)
ax1.text(1999,1.1,'Aids related deaths per year',color=cyan,fontsize=16)
ax2.text(2007,16,'People receiving anti-\nretroviral therapy, total',color=red,fontsize=16)
#
pyplot.subplots_adjust(top=0.8)
ax1.text(1988,4.5,'Keeping the pressure up',fontsize=24,weight='bold')
#
## We'll leave it at this. Further tuning would include trying to use the exact same font and drawing the legends.
## If I were to draw the legends for this figure, I draw them manually using the annotatation tools in matplotlib. 
## These allow drawing arrows, boxes, etc. on the plot.
## We could also measure the locations of annotations and titles on the figure to try and match  their exact positions.
#
## Let's save this piece of art.
pyplot.savefig('my_hiv_plot.png')
pyplot.show()


print('done')