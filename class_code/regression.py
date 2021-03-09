#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 14:12:28 2021

@author: dieter
"""

# These lines are needed on my computer to be able to import the stats module. 
# You should place the stats.py file in your working directory.
import sys
sys.path.append('/home/dieter/Dropbox/Python-Class/class_code')
# end of code specific to my computer
from matplotlib import pyplot
import stats
import pandas
data = pandas.read_csv('https://tinyurl.com/ib5wvbqc') 
result = stats.simple_regression('Weight','Height', data)

from statsmodels.regression.linear_model import OLS;
import statsmodels.api as sm;


# Prepare the predictors
predictors = data.loc[:,('Height','Age','Forearm')]
X = sm.add_constant(predictors)

# Define the dependent
dependent = data.Bicep

# Run the analysis and get the results
model = OLS(dependent, X)
fitted = model.fit()
fitted.summary()


# Prepare the predictors
predictors = data.loc[:,('Chest')]
X = sm.add_constant(predictors)

# Define the dependent
dependent = data['Age']

pyplot.figer()
# Run the analysis and get the results
model = OLS(dependent, X)
fitted = model.fit()
print(fitted.summary())

# Get the predicted values
prediction = fitted.predict(X)

if predictors.ndim == 1:
    pyplot.scatter(predictors, dependent);
    pyplot.plot(predictors, prediction,'r-');
else:
    print('Can not plot result for multiple predictors')