# Search CSV
Search Challenge

The company have a list of product [search_dataset.csv](https://github.com/txemac/search_csv/blob/master/search_dataset.csv) with the next structure:
```sh
id1,name1,brand1
id2,name2,brand2
...
```

File [queries.txt](https://github.com/txemac/search_csv/blob/master/queries.txt) contains some queries.

The app takes the queries and searches inside of CSV file inside of names and brands. Return a list (max 10 items) with the search, order by score.

For calculate the score (you can change at settings):
- token complete: 10 points
- prefix: 5 points
- in name: x2
- in tokens: x1

# Setting
You can configure your parameters in 'settings.py'

# Run
To run app:
```sh
$ python search_csv.py
```
To run unit test suite, install requirements:
```sh
$ pip install -r ./requirements.txt
```
Run tests:
```sh
$ nosetests -v
```
# Author
Jose Bermudez

[www.josebermudez.co.uk](http://www.josebermudez.co.uk)

[info@josebermudez.co.uk](mailto: info@josebermudez.co.uk)
