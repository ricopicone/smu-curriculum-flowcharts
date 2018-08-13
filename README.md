# smu-curriculum-flowcharts

This repository contains the source code for generating curriculum flowcharts for the Saint Martin's University (SMU) Department of Mechanical Engineering. It could rather easily be adopted to other programs and universities.

The project is written in Python and relies on Graphviz. Required Python packages can be installed using the following command.

```console
pip install -r requirements
```

Now install Graphviz itself from [here](http://www.graphviz.org/Download.php). With homebrew on macOS, the following command should work.

```console
brew install graphviz
```

## How to use it

The script `flowchart_generator.py` is the heart of the project. 
Inside is a bit of a tangle because constructing graphics always is (he said, conveniently absolving himself for messy code). 
This script uses the Ruby graphviz API `graphviz` to construct a flowchart.
Users can edit the `courses_2017.py` (or create a similar) file, for instance, which defines a number of `course` class instances. One such definition is

```python
new_course('ME 498',3,'4F',False) \
	.add_prereq('ME 302') \
	.add_prereq('ME 370') \
	.add_coprereq('ME 430')
```

The first line means "define a new instance of the `course` class with name `ME 498`, which is `3` credits, is to be taken in the Fall term of the fourth year (`4F`), and has not yet been completed (`False`)." 
The three (continuation) lines afterward say `ME 498` has prerequisites `ME 302` and `ME 370` and has concurrent prerequisite (can be taken before or concurrently) `ME 430`.

Once you have a file with such statements, let's just say it's `courses_2017.py`, you can run it through `flowchart_generator.py` with the following statement.

```console
python flowchart_generator.py courses_2017.py
```

If a student (or her advisor) wanted to keep track of their own progress, she could mark a course as "completed" by changing the `completed` boolean of a course instance to `True`. There are (at least) two ways to do this. Within the `courses_2017.py` script, for instance, where the course, let's call it `MTH 171`, is defined using the `new_course` function, we could make the following simple statement.

```python
new_course('MTH 171',4,'4F',True)
```

However, if we wanted, we could "mark" an existing instance of a course as completed by the following statement.

```python
courses['MTH 171'].set_completed(True)
```

This is because our `new_course` function saves each `course` instance into the `dict`ionary `courses` with the lookup key being the course name (e.g. `MTH 171`).
