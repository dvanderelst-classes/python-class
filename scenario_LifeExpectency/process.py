import pandas
import seaborn
from matplotlib import pyplot
data = pandas.read_csv('NCHS_-_Death_rates_and_life_expectancy_at_birth.csv')

data = data.query('Race =="All Races"')

seaborn.lineplot(x='Year', y='Average Life Expectancy (Years)', hue='Sex', data=data)

pyplot.show()
