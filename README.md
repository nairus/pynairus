# PYMATH APPLICATION

## INTRODUCTION

This application was made for training my daugther to do mathematical operations.

## INSTALL

To install the application, copy the `pynairus` package in your `Python` lib folder.

## USAGE

### IN COMMAND LINE

You can use the `run.py` script to launch the application in command line.

To show the help, type :

```python
python run.py -h
```

It will output:

```bash
usage: run.py [-h] [-o OPERATOR] [-t] [-l] [-c CONFIG] [-V] [-r] start end limit

positional arguments:
  start                 Start of the random range
  end                   End of the random range
  limit                 Limit of operations to generate

optional arguments:
  -h, --help            show this help message and exit
  -o OPERATOR, --operator OPERATOR
                        Add an operator (default: tuple('+', '-'))
  -t, --timer           Add a timer
  -l, --list_operator   Display the list of operators and exit
  -c CONFIG, --config CONFIG
                        Specify a config name
  -V, --version         Display the current version and exit
```

### IN PYTHON APP OR JUPYTER NOTEBOOK

You can also run the application by importing the lib like:

```python
from pynairus import pymath

# for multiplication tables
pymath.pymath(start=3, end=5, limit=10, operator="×")

# for multiplication with 1 digit factor
pymath.pymath(start=10, end=999, limit=10, operator="1×")

# for multiplication with multiple digit factor
pymath.pymath(start=10, end=999, limit=10, operator="n×")

# for euclidian division with single divisor
pymath.pymath(start=10, end=99, limit=10, operator="÷")

# for euclidian division with double divisor
pymath.pymath(start=10, end=99, limit=10, operator="2÷")

# for time addition: generate times between 20 minutes and 1 hour
pymath.pymath(start=1200, end=3600, limit=5, operator="t+")
```

The `start`, `end` and `limit` args are required. Exception will be raises if there are not present or if there not an `int`.
The other args are optionals:

1. `operator`: specify an operator, by default a tuple of ('+', '-') is set.
2. `timer`: launch a timer during the execution of the application. The total time is output at the end of the excecution.
3. `config`: specify a config name. For example in production we don't want debug log. So you can define a production config and specify it with this arg.

#### Euclidian divisions

The expected result has to be formatted like: `{quotian}r[rest}`.  
The rest is not required if the result has no one.

- **Example 1 :** 12 ÷ 6 = 2
- **Example 2 :** 13 ÷ 6 = 2r1

#### Time operations

For time addition and substraction, the result expected has to be formatted like: `{h}h{mm}m{ss}`.  
_Beware to add missing `0` digits for the minutes and the seconds._

- **Example 1:** 34m02s + 38m07s = 1h12m09s
- **Example 2:** 38m07s - 34m02s = 04m05s

### OPERATORS AVAILABLE

If you want see all the operators available you can do like this:

```python
from pynairus.strategies.operator_strategy import display_operators_list
display_operators_list()
```

Or in command line, launch:

```bash
python run.py -l
```

It will output something like that:

```python
Available Operators list:
(('+', 'Key for addition operation'),
 ('-', 'Key for substraction operation'),
 ('×', 'Key for table operation (ex. 4 × 3)'),
 ('1×', 'Key for simple mutliplication (ex. 45 × 2)'),
 ('n×', 'Key for complex multiplication (ex. 12 × 11)'),
 ('÷', 'Key for single divisor (ex. 35 ÷ 5)'),
 ('2÷', 'Key for double divisor (ex. 234 ÷ 25)'),
 ('t+', 'Key for time addition (ex. 34m24s + 54m31s)'),
 ('t-', 'Key for time substraction (ex. 54m48s - 45m21s)'))
```
