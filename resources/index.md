# Detailed schedule and resources

## Class 2

* _Class will take place in Tome 117 today._
* _If campus is closed on Monday, class will take place online via Zoom. The link and details are on the course home page._

### Minilab: Using WCBC programs from a different folder

Chapter 2 of the textbook explains how to use programs that are saved and run from same folder as the WCBC utilities. It's fine to work like this, but it becomes difficult to keep your files organized in separate folders. This minilab demonstrates how use the WCBC programs while also storing your own Python files somewhere else. 

* Download and extract [`wcbc-programs-v1.1.zip`](../wcbc-programs/wcbc-programs-v1.1.zip) into your `comp314` folder.
* Download [`use_containsGAGA.py`](class02/use_containsGAGA.py) and organize as follows:
```
comp314
├── classes
│   ├── class01
│   └── class02
│       └── use_containsGAGA.py
├── hw
└── wcbc-programs-v1.1
```
* Open `use_containsGAGA.py` in IDLE or your favorite Python environment. 
* Run it, check that it works correctly, add a few more test strings to the source code and rerun. Note the use of
```python
import sys
sys.path.append('../../wcbc-programs-v1.1')
```
to make the WCBC utils accessible.
* Write your own `use_isEven.py`.
* Write your own `use_countLines.py`. What inputs can you use? How about some files?

### Lecture for today

Required reading: Chapters 1 and 2 of WCBC.

Today's PowerPoint: [02-computer-programs.pptx](class02/02-computer-programs.pptx).


## Class 1

The textbook is called *What Can Be Computed?*, which we abbreviate as
    *WCBC*.
      
Today we will go through the syllabus and an overview of the course,
corresponding to WCBC Chapter 1.

Today's PowerPoint: [01-intro.pptx](class01/01-intro.pptx).
  
If there's time, we will try to run and edit some Python programs
  using IDLE. Key points:

* You can [download Python](https://www.python.org/downloads/) and
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
