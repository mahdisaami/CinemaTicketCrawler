# CinemaTicketRobot

#### The way to create tables or connect to your db:
for connecting to your db at the first you must create a dictionary
    called MY_DATABASE and fill it with your connection's information
    at the second you must call the create_table function to connect to your
    database and create tables.
    if you only want to connect to your db you must instead of create_table function
    call the connect_mysql function. [docs](https://docs.google.com/document/d/1vglnqYzsfDSnvUXul6yYkEiEnmbiTnO-4ky31qp4-Zk/edit?usp=sharing)
    
## Getting Started
 for starting crawler
 
### Step 1 (Create your Database)
Create a database and your Connection 
if you don't know you can use this [link](https://tecadmin.net/install-postgresql-server-on-ubuntu/)

### Step 2 (Clone files from git)

run this code for clone files from git

```
git clone https://github.com/mahdisaami/CinemaTicketCrawler.git
```
for more Detail you can [click this](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-clone)

### Step 3 (Config your connection)

* create local_config.py in models
* in local_config.py 
```
MY_DATABASE = {'user': 'Yourusername', "password": 'Yourusername', 'host': '127.0.0.1 or Your host'}
```

### Step 4 (Create your Tables)

```
from create_table import create_table
create_table()
```
### notice
You must call create_table() for creating you tables.
 for connecting to your db you must call connect_mysql().
