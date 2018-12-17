# Programming for behavioral scientists

**Contact details**

Dieter Vanderelst
Office location: Edwards 1, 4th floor, office 4150F

vanderdt@ucmail.uc.edu

My website: https://bitsofbats.weebly.com/

Syllabus: [syllabus.md](syllabus.md)

## Quizzes FAQ

**Where can I find the Quizzes?** All quizzes can be found on the GitHub page, in the `Quizzes` folder: https://github.uc.edu/vanderdt/PythonCourse/tree/master/Quizzes. 

**How should I submit a quiz?** Copy paste your answers into a Word file or any other text document. Please include the question numbers, you name and the quiz name into the document. You can use the Word template in the Quizzes folder. Quizzes should be submitted in Blackboard. Goto `Course Content` and submit the quiz under the appropriate Assignment.

**When should I submit an assignment?** Each assignment has a due date, typically one week after being assigned, unless specified differently.

# Course package

For some parts of the course, we will be using a Python package I wrote for this course. This package can be downloaded here:  https://github.uc.edu/vanderdt/Course

We will be using the pyboard, based on the [Micro Maestro 6](https://www.pololu.com/product/1350). Most computers do not require a driver to be installed. However, if needed, the driver can be found here: https://www.pololu.com/docs/0J40/3.a

## Anaconda

In this course, we use the Anaconda Python distribution. This is a version of Python that comes with many scientific modules included. Also, it comes with a package manager that allows installing additional packages more easily. https://anaconda.org/. You do not need to make an account to download/use Anaconda. Head over to the download page at https://www.anaconda.com/download/.

## Online resources

+ A list of free Python books: https://www.onlineprogrammingbooks.com/python/. *Automate the Boring Stuff with Python* is a popular book, often recommended to beginners focusing on completing practical tasks using Python. https://automatetheboringstuff.com/
+ An interactive book on Python: https://runestone.academy/runestone/static/thinkcspy/index.html
+ A very extensive cheat sheet for Python. https://wilfredinni.github.io/python-cheatsheet/
+ This is a series of Youtube videos on data analysis using Pandas. https://tinyurl.com/ya2qfcuo
+ A gallery of plots and graphs made using Python - and the code used to make them. https://python-graph-gallery.com/
+ As a student at UC you have access to the courses on Lynda.com. This site features some complete Python courses, often focussing on data analysis. Go here to get started: https://kb.uc.edu/KBArticles/Lynda-Landing.aspx
+ Python exercises: https://www.w3resource.com/python-exercises/
+ Seaborn is a package that makes statistical plots easier: http://seaborn.pydata.org/index.html
+ A Youtube series on data visualization using Matplotlib: https://www.youtube.com/playlist?list=PLqEbL1vopgvs1p90E3Ig_OTY08wBTCj9B

## Sources of data

* This website lists datasets and the python code to read them in:
  * https://think.cs.vt.edu/corgis/python/index.html. The data is formated as a list of nested dictionaries. However, the following code  shows how to transform this a Pandas dataframe. 

```python
import collections
import pandas
import county_demographics

def flatten(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def data2frame(data_list):
    all_data = []
    for x in list_of_report:
        data = flatten(x)
        all_data.append(data)
    data = pandas.DataFrame(all_data)
    for x in data.columns: print(x)
    return data
    
list_of_report = county_demographics.get_all_counties()
data = data2frame(list_of_report)
```

* Plain text data sets:
  * https://www.data.gov/
  * https://ww2.amstat.org/publications/jse/jse_data_archive.htm
  * https://vincentarelbundock.github.io/Rdatasets/datasets.html
  * http://www.statsci.org/datasets.html
* Data APIs:
  * Quandl is a website that allows accessing data in pandas format directly. https://www.quandl.com/
* Google's data set search:
  * https://toolbox.google.com/datasetsearch

## Dealing with common errors and bugs

![Common errors](http://i.imgur.com/ZG4VcOp.jpg)

## Applications

- **Games** I often get the question whether Python can be used to make games. The answer: yes. There is pygame for 2D games: https://www.pygame.org. Here is a series of youtube lectures to get started: https://is.gd/rj8NIi. For 3D games, you need an engine you can script. This means you can use  Python to program the logic of the game while the engine handles graphics, physics and the design of the world.One possibility is to use blender: blender.org. Wikipedia has a list of 3d game engines. https://en.wikipedia.org/wiki/List_of_game_engines. Look at the scripting column to find engines that work with Python.
- **Signal processing** A free book on signal processing in Python: http://greenteapress.com/wp/think-dsp/
- **Scientific programming** Scipy lecture notes: http://www.scipy-lectures.org/index.html
- **Image processing** in Python: http://scikit-image.org/
- **Programming Experiments in Python** http://docs.expyriment.org/
- **Advanced statistics** Statmodels provides a number of advanced statistical test, including using the linear model: http://www.statsmodels.org/stable/index.html