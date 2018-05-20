# check_naming_convention
Clone repository and check naming convention for multiple-word identifiers

This version of the script supports only github repository with python projects. 


**From command line:**

```
$ python3 check_nc.py freq 
```

Requirements
--
- at least python 3.5
- nltk=>3.2.5
- GitPython=>2.1.10


Installation
--

just clone the project and install the requirements:

```
$ git clone https://github.com/PyExplorer/check_naming_convention.git
$ cd check_nc
$ pip3 install -r requirements.txt
$ python -m nltk.downloader averaged_perceptron_tagger
```

Docs
--

Now we have only one sub-commands **'freq'** and it means that we want to get statistic for part's of speech frequency in code.

In the future the script will have more options and features to analyze. 

The script has 1 mandatory command to run:

**freq**

**options with freq**

**-p (--pos)** - part of speech to analyze, two options available now: verbs, nouns 

*default:* verbs 

```
example: $ python3 check_nc.py freq -p nouns
```

**-n (--node)** - Select node to search names - functions of local variables, two options available now: func, var 

*default:* func 

```
example: $ python3 check_nc.py freq -p nouns -n func
```

**Common script options**

**-o (--output)** - Select format to output results, three options available now: text, json, csv

*default:* text
```
$ python3 check_nc.py -o json freq
```
**-f (--file)"** - We can choose path and name for file to store 

*default:* stdout
```
$ python3 check_nc.py -o csv -f "results.csv" freq
```

**-r (--repo)** - web url for repository (for this version github repository only) 

**default:** 'https://github.com/PyExplorer/check_naming_convention.git' 

```
example: $ python3 check_nc.py -r 'https://github.com/pallets/flask.git' freq
```

**--plang** - programming language to parse, one options available now: python 

**default:** python 

```
example: $ python3 check_nc.py -plang python freq
```

**-d (--dir)** - select local directory for store repo

**default:**  repos

```
example: $ python3 check_nc.py -d 'source' freq
```

**-l (--log)** - path and filename to store logs

**default:**  stdout

```
example: $ python3 check_nc.py -l './logs' freq
```


**Flags:**

**--noclone** - no clone from repo - take only from dir (-d) 

**default:**  False

```
example: $ python3 check_nc.py -d 'source' --noclone freq
```

**--clear** - clear repo after script finished

**default:**  False

```
example: $ python3 check_nc.py --clear freq
```

Contributing
--

To contribute, pick an issue to work on and leave a comment saying that you've taken the issue. Don't forget to mention when you want to submit the pull request.


Launch tests
--

Not yet...