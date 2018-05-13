# check_naming_convention
Clone repository and check naming convention for multiple-word identifiers

This version of the script supports only github repository with python projects. 


**From command line:**

```
$ python3 check_nc.py freq 
```
Now we have only one sub-commands **'freq'** and it means that we want to get statistic for part's of speech frequency in code.

In the future the script will have more parameters and features to analyze. 

**Options to run**

The script has ___ option to run:

**freq** -  

**-p (--pos)** - part of speech to analyze, two options available now: verbs, nouns 

*default:* verbs 

```
example: $ python3 check_nc.py -p nouns
```

**-w (--where)** - Select place to search names - functions of local variables, two options available now: func, var 

*default:* func 

```
example: $ python3 check_nc.py -p nouns
```

**-o (--output)** - Select destination to output results, three options available now: stdout, json, csv

*default:* stdout
```
$ python3 check_nc.py -o json 
```
**-f (--file)"** - We can choose path and name for file to store 

*default:* for json format "./results.json", for csv format "./results.csv"  
```
$ python3 check_nc.py -o csv "./my_results.csv" 
```

**-r (--repo)** - web url for repository (for this version github repository only) 

**default:** 'https://github.com/django/django.git' 

```
example: $ python3 check_nc.py -v 'https://github.com/pallets/flask.git'
```

**-pl (--language)** - programming language to parse, one options available now: python 

**default:** python 

```
example: $ python3 check_nc.py -pl python
```
