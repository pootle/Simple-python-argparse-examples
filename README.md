# Simple-python-argparse-examples

A few very simple examples of using argparse for:

* flag parameters
* lists of things
* calling an app with all paramaters 

The files are:

#### args01final.py
very basic - a single positional argument

#### args02final_multi.py
a multi-valued argument - passes a list to the app. Use with wildcards on linux to return (potentially huge) lists of files

#### args03flags.py
adds in flag type arguments which result in True or False (and can work either way round

#### args04types.py
getting arguments parsed (e.g. as int or float)

#### args05owntypes.py
using your own functions to validate and process a parameter

#### args06app_call.py
a simple trick to pass all aruments as keywords to the function

#### args07app.py
A very simple calculator with it's own unique syntax!
