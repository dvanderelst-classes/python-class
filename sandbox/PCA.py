#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 22:46:01 2018

@author: dieter
"""
import pandas
import numpy

from matplotlib import pyplot
from sklearn.decomposition import PCA
from sklearn.decomposition import FactorAnalysis



data = pandas.read_csv('bfi.csv', index_col=0,na_values='nan')


scores = data.loc[:,'A1':'O5']
scores = scores.dropna()
correlations = scores.corr()
pyplot.matshow(correlations)
pyplot.colorbar()


pca = PCA(n_components=10)
pca.fit_transform(scores)
loadings = numpy.abs(pca.components_)
explained = pca.explained_variance_ratio_

pyplot.figure()
pyplot.plot(explained, 's-');


pyplot.figure()
pyplot.imshow(loadings)