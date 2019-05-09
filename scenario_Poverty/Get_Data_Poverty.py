import quandl
from matplotlib import pyplot



poverty25 = quandl.get("WPOV/NGA_SI_POV_25DAY", authtoken="NM55D4TthA7TzoF5NbYf")
poverty5 = quandl.get("WPOV/USA_SI_POV_5DAY", authtoken="NM55D4TthA7TzoF5NbYf")




pyplot.plot(poverty25)
pyplot.plot(poverty5)

pyplot.show()