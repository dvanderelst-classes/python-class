# Quiz: Writing and reading files

## Question 1

Write a script that does the following:

+ Assign a string to variable, e.g, `my_string`.
+ Next, the script opens a file and writes `my_string` to the file. If there is already some text in the file, the string should be appended to the text.
+ Close the file.

## Question 2

Write a function that takes a filename as an argument. The function opens the provided file and reads in its contents. The contents of the file is returned and the file is closed.

## Question 3

Look at the code below. What will the types of variables `a` and `b` be?

```python
f = open('some_file.txt', 'r')
a = f.read()
b = f.readlines()
f.close()
```

