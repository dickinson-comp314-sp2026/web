# Detailed schedule and resources


## Class 1

The textbook is called *What Can Be Computed?*, which we abbreviate as
    *WCBC*.
      
Today we will go through the syllabus and an overview of the course,
corresponding to WCBC Chapter 1.

Today's PowerPoint: [01-intro.pptx](class01/01-intro.pptx).
  
If there's time, we will try to run and edit some Python programs
  using IDLE. Key points:

* Always use Version 3.x of Python for this course
* You can [download Python 3](https://www.python.org/downloads/) and
    install it on your own laptop etc.
* Python is also available on various college computers, and via online sites such as [pythonanywhere.com](https://www.pythonanywhere.com/).

Here is some code to paste in and experiment with:
```python	
def containsGAGA(inString): 
    if 'GAGA' in inString: 
        return 'yes' 
    else: 
        return 'no' 
```

Here's another one:
```python
def multiply(inString): 
    (M1, M2) = inString.split()
    product = int(M1) * int(M2) 
    return str(product)
```
