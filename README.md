### Author
Luiz Alberto de Oliveira Campos

### Date created
January 31, 2021

### Bikeshare

### Description
Bikeshare is a interactive python program that reads 3 csv files containing bike share system data from 3 cities in the United States - New York, Washington and Chicago

After reading the data, the program provides some statistics about the data such as: 

* what is the most common month ?
* what is the total travel time ?
* what is the most common start station ?
* what is the gender distribution of the users that use the bike system?

and many more!

The program is interactive, which means, the program was created to ask how the user wants to analyse the data. Some information that the user must provide to the program:

* What city you want to analyse ? (chicago, new york or washington)
* You want to filter by month or day?
* If you want to filter by month, which month you want to analyse?

### External libraries

The bikeshare program uses 2 libraries that aren't include in default python installation.

**[pandas]** 

**[numpy]**

These libraries are used to compute statistics and work with arrays inside the program.

If you have a **standard python* installation, you might need to install both of these libraries in order to use the bikeshare program

Installing libraries using PIP package manager

```sh
pip install pandas
```

```sh
pip install numpy
```

**If you have installed python using Anaconda distribution, you're already have the numpy and pandas installed, since these libraries are heavily used in data science projects*

[pandas]: https://pandas.pydata.org/
[numpy]: https://numpy.org/


## Files used
The following files are being used in this project:

* bikeshare.py

    This is the actual program. It contains all python functions necessary to read, analyse and compute statistics related to the data files.


* Data files:

    These files contains the data being analysed and processed in the bikeshare program.

    * chicago.csv

    * new_york_city.csv

    * washington.csv

### Credits
During the project development, I've used some blogs and documentation as support material.


**[Unnamed column]** This helped me to replace the unnamed column inside the data frame (This happens when a column inside the source file doesn't have a name/header)

**[Pandas Documentation]** I've used several pandas methods to generate statistics about the data. So the panda's official documentation helped me a lot!

**[Stack Overflow]** Of course, stack overflow helped me! My project used a datetime.timedelta object and I wanted to convert seconds into minutes, hours and days. I used this thread to understand how to use the timedelad object.


[Unnamed column]: https://www.codegrepper.com/code-examples/python/name+unnamed+column+pandas

[Pandas Documentation]: https://pandas.pydata.org/

[Stack Overflow]: https://stackoverflow.com/questions/538666/format-timedelta-to-string