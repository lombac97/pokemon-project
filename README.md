# PokeAPI
## The pokemon API

 PokeAPI gives you information about pokemons, regions, locations, areas and more!
 You can also catch pokemons or include them in your party.




## Installation

1) First of all, you need to have Python (version 3.7 or above) and PostgreSQL 13.4 installed on your computer.

2) Clone this repo
3) A virtual environment is recommended, to create a virtual env:

    ```sh
    python3 -m venv "your-env-name"
    ```
    Activate it:
    - On Windows: ```path_to_your_env/Scripts/Activate.sh```
    - On Mac and Linux: ```source path_to_your_env/bin/activate```
And press enter

    For the virtual environment, you need to install.
    - asgiref == 3.5.2
    - autopep8==1.6.0
    - backports.zoneinfo==0.2.1
    - Django==4.0.4
    - django-cors-headers==3.12.0
    - django-debug-toolbar==3.4.0
    - django-rest-framework==0.1.0
    - djangorestframework==3.13.1
    - psycopg2==2.9.3
    - pycodestyle==2.8.0
    - pytz==2022.1
    - sqlparse==0.4.2
    - toml==0.10.2

    However, a requirements.txt file is included in the repository.

    Your can install all the dependencies by typing, with your env activated,
    
    ```sh
    python3 -m pip install -r requirements.txt
    ```
## Run the project

To run this project you will need to create a database, the run the migrations and load the data.

1) Create a database and connect your project to it

    There's a configuration in settings.py with some important parameters you'll need to configure:
    
    'NAME': 'pikachu' -> The name of the database you just created
    'USER': 'postgres' -> The user to authenticate to the server
    'PASSWORD': '9485326' -> The password to authenticate to the server
    'HOST': '127.0.0.1' -> The server IP, if running locally should remain the same
    'PORT': 5433 -> The port in which your server is listening for connections
 
 2) Once your database is created and the configurations in settings.py are set, you'll need to run the migrations
    ```sh
    python3 manage.py migrate
    ```
    This will create all the necessary tables in your database to run the project.

3) You'll need to load the data. There are two ways to achieve this:
    a) Under your project directory, run the command ```python3 manage.py populate_db```. This will run a custom function to load the database or,
    b) You can use the fixture provided, run the command ```python3 manage.py loaddata pokemon_backend/fixtures/pikachu.json```.

4) You can create a superuser to test the auth required endpoints:
    ```sh
        python3 manage.py createsuperuser
    ```

## Endpoints

Endpoint | Method | CRUD Method | Auth Required? | Result
-- | -- |-- | -- | -- 
`regions/` | GET | READ | No | List all the regions
`regions/:id/` | GET | READ | No | Get region details by id
`location/:id/` | GET | READ | No | Get location details by id
`areas/:id` | GET | READ | No | Get area details by id
`login/` | POST | CREATE | No| Login with a user to get the access token
`pokemons/:id/` | GET | READ | No | Get pokemon details by id 
`pokemons/own/` | GET | READ | Yes | List all the pokemons in your storage
`pokemons/own/` | POST | CREATE | Yes | Saves a new pokemon to your storage
`pokemons/own/:id/` | PUT, PATCH | UPDATE |Yes  | Change the nick_name to a pokemon in your storage by id
`pokemons/own/:id/` | DELETE | DELETE | Yes | Deletes a pokemon from your storage by id
`pokemons/own/party/` | GET | READ | Yes | List all the pokemons in your party
`pokemons/own/swap/` | POST | UPDATE | Yes | Include or exclude (or both) Pokemons from your party

> Note: For auth required endpoints an Authorization header must be sent, with value Token "token"
> For non auth required endpoints, that header should not be sent

All the necessary parameters for each endpoint are documented in the code

