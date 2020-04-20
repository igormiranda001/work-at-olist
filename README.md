
# Work At Olist

> It is a basic API for reading, registering, updating and deleting authors and books.
> In addition to the API, the system has an interface for use by ordinary users.
 
## Installation

Clone Repository

```
  
  git clone https://github.com/igormiranda001/work-at-olist.git
  
```

Create VirtualEnv

  

```

python3 -m venv ENVNAME

```

  

Active VirtualEnv

  

```

source ENVNAME/bin/activate

```

Install requirements package.

```sh

pip install -r requirements.txt

```

Migrate database

```sh

python manage.py migrate
python manage.py makemigrations olist_backend
python manage.py migrate

```
Run server

```sh

python manage.py runserver 0.0.0.0:8000

```  

## Test

  

  
  
To test the application's CRUD functions, run the command.

  

```sh

python manage.py test

```


## Requirements

  

* Python 3.7

* Django 3

* Django Rest Framework 3.11.0

* Django Filter 2.2.0

* Django Widget Tweaks 1.4.8

* Drf Yasg 1.17.1

* MySQL
  
## Endpoints
* /api/authors/
* /api/books/


## API Documentation

  
Documentation is available at the endpoint /api-documentation/


## Import Authors from a CSV File

  

1.  Create a CSV file with the following format inside the work-at-olist folder.

```
name
Luciano Ramalho
Osvaldo Santana Neto
David Beazley
Chetan Giridhar
Brian K. Jones
J.K Rowling
```

2.   In work-at-olist folder, run the following command:

```

python manage.py import_authors FILENAME.csv

```
You can pass any file name or directory as an argument.

```

Example: python manage.py import_authors authors.csv

Example2: python manage.py import_authors PATH/FILENAME.csv

```
  

## Screenshots

Some pictures of the simple template developed for CRUD.

Home.
![enter image description here](https://uploaddeimagens.com.br/images/002/601/234/original/Anota%C3%A7%C3%A3o_2020-04-20_102954.png?1587389766)

Author's list.
![enter image description here](https://uploaddeimagens.com.br/images/002/601/238/full/Anota%C3%A7%C3%A3o_2020-04-20_103650.png?1587389830)

Book's list.
![enter image description here](https://uploaddeimagens.com.br/images/002/601/243/full/Anota%C3%A7%C3%A3o_2020-04-20_103843.png?1587389966)

For more examples and usage, please access app webpage in [Heroku.](https://olist-igor.herokuapp.com/)

## Work Environment Setup.

* Ryzen 5 2600x

* 16Gb

* Ubuntu 18.4

* VSCode