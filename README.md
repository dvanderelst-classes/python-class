# Programming for behavioral scientists

## Contact details

Dieter Vanderelst
Office location: Edwards 1, 4th floor, office 4150K

Email: vanderdt@ucmail.uc.edu

My website: www.bitsofbats.net

Syllabus: [syllabus.md](syllabus.md)

## Using the GitHub files

All materials for the course are available on the UC GitHub. Every section of the class has a dedicated folder with some files and folders in it:

- File ending in```ipynb```: These are the course note files I use in class. When clicked, these files render in your browser.
- Files ending in ```md```: These are formatted text files. When clicked, they will render in your browser allowing you to read them.
- Files ending in ```odp```: These files are presentations. If you click these files, you will get a notice that the file can not be displayed. However, a *download* button will appear. Clicking this button will allow you to download the file and open it in PowerPoint or OpenOffice.
- Data files (ending in ```csv```, ```txt``` or ```dat```): For some sections of the course, you will need to download data files. These can typically be found in a sub folder called *data*. To download a data file click it.  You will see a rendering of the data file. Now click the *raw* button. This will give you access to the data file itself. Now, use your browser menu to save the file (For example, ```File> Save Page...```).

## Quizzes FAQ

**Where can I find the Quizzes?** All quizzes can be found on the GitHub page, in the `Quizzes` folder.

**How should I submit a quiz?** Copy paste your answers into a Word file or any other text document. Please include the question numbers, you name and the quiz name into the document. You can use the Word template in the Quizzes folder. Quizzes should be submitted in Blackboard. Goto `Course Content` and submit the quiz under the appropriate Assignment.

**When should I submit an assignment?** Each assignment has a due date, typically one week after being assigned, unless specified differently.

## Course package

For some parts of the course, we will be using a Python package I wrote for this course. This package can be downloaded here:  https://github.uc.edu/vanderdt/Course

We will be using the pyboard, based on the [Micro Maestro 6](https://www.pololu.com/product/1350). Most computers do not require a driver to be installed. However, if needed, the driver can be found here: https://www.pololu.com/docs/0J40/3.a

## Anaconda

In this course, we use the Anaconda Python distribution. This is a version of Python that comes with many scientific modules included. Also, it comes with a package manager that allows installing additional packages more easily. https://anaconda.org/. You do not need to make an account to download/use Anaconda. Head over to the download page at https://www.anaconda.com/download/.

Some helpful resources on Anaconda:

- This is a 2-page pdf document explaining what Anaconda is: http://docs.anaconda.com/anaconda/user-guide/cheatsheet/. 
- Managing the Anaconda installation can be done using the Anaconda Navigator. This link describes how to start the Navigator on Windows, Mac, and Linux: http://docs.anaconda.com/anaconda/navigator/getting-started/#navigator-starting-navigator
- Anaconda comes with a command line tool to install and update packages. There is a cheat sheet for this: https://conda.io/docs/user-guide/cheatsheet.html

## Online Resources

This is a list of resources that might be helpful while learning Python:

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
  * https://think.cs.vt.edu/corgis/python/index.html. The data is formatted as a list of nested dictionaries. However, the following code shows how to transform this a Pandas dataframe. 

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

[Click here to find a handy diagram to help you deal with common errors in Python.](http://i.imgur.com/ZG4VcOp.jpg)

## Applications

- **Games** I often get the question whether Python can be used to make games. The answer: yes. There is pygame for 2D games: https://www.pygame.org. Here is a series of youtube lectures to get started: https://is.gd/rj8NIi. For 3D games, you need an engine you can script. This means you can use  Python to program the logic of the game while the engine handles graphics, physics and the design of the world. One possibility is to use blender: blender.org. Wikipedia has a list of 3d game engines. https://en.wikipedia.org/wiki/List_of_game_engines. Look at the scripting column to find engines that work with Python.
- **Signal processing** A free book on signal processing in Python: http://greenteapress.com/wp/think-dsp/
- **Scientific programming** Scipy lecture notes: http://www.scipy-lectures.org/index.html
- **Image processing** in Python: http://scikit-image.org/
- **Programming Experiments in Python** http://docs.expyriment.org/
- **Advanced statistics** Statmodels provides a number of advanced statistical test, including using the linear model: http://www.statsmodels.org/stable/index.html
