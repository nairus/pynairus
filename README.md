# PYMATH APPLICATION

## INTRODUCTION

This application was made for training my daugther to do mathematical operations.

## INSTALL

To install the application, copy the `pynairus` package in your `Python` lib folder.

## USAGE

You can use the `run.py` script to launch the application in command line.

To show the help, type :

```python
python run.py -h
```

It will output:

```bash
usage: run.py [-h] [-o OPERATOR] [-t] [-l] start end range

positional arguments:
  start                 Start of the random range
  end                   End of the random range
  range                 Number of operations to generate

optional arguments:
  -h, --help            show this help message and exit
  -o OPERATOR, --operator OPERATOR
                        Add an operator (default: tuple('+', '-'))
  -t, --timer           Add a timer
  -l, --list_operator   Display the list of operators and exit
```

You can also run the application by importing the lib like:

```python
from pynairus import pymath

# for multiplication tables
pymath.pymath(3, 5, 10, "*", False)

# for multiplication with 1 digit factor
pymath.pymath(10, 999, 10, "1*", False)

# for multiplication with multiple digit factor
pymath.pymath(10, 999, 10, "n*", False)
```

If you want see all the operators available you do like this:

```python
from pynairus.strategies.operator_strategy import display_operators_list
display_operators_list()
```

It will output something like that:

```python
Available Operators list:
(('+', 'Key for addition operation'),
 ('-', 'Key for substraction operation'),
 ('*', 'Key for table operation (ex. 4*3)'),
 ('1*', 'Key for simple mutliplication (ex. 45*2)'),
 ('n*', 'Key for complex multiplication (ex. 12*11)'))
```
