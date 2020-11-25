# yourSpot Set Up
Repository to hold setup instructions for yourSpot.

# Setup
- [Windows](#windows-setup)
- [Linux](#linux-setup)
- [MySQL Database Setup](#mysql-database-setup)
- [MySQL Schema Setup](#mysql-schema-setup)
- [Pycharm Setup](#pycharm-ide-setup)
- [Running Project](#run-project)
- [Additional Styling](#styling)
- [Tasks to Complete For Lab](#api)

# Windows Setup
- Install git [if not already installed](https://git-scm.com/download/win)
- Clone project *run in cmd as admin*
```
git clone hhttps://github.com/cassidylinhares/yourSpot
```
- Install [Python 2.7 (Recommended)](https://www.python.org/downloads/release/python-2712/)
- Add Python and Python scripts to path variable, **no spaces**

![path](img/img/path.PNG)

- Install dependencies *run in cmd as admin in project folder*
```
pip install -r requirements-2.7.txt
pip install wheel
pip install MySQL_python-1.2.5-cp27-none-win_amd64.whl
pip install mysqlclient-1.3.13-cp27-cp27m-win_amd64.whl
python setup.py build
python setup.py install
```

- Install [MySQL Server](https://dev.mysql.com/downloads/mysql/)


# Linux Setup
- Install git if not already installed
```
sudo apt-get install git
```
- setup virtual environment in project folder [more documentation](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
```
sudo apt install python-pip python-dev build-essential libpq-dev
sudo apt-get install mysql-server mysql-workbench libmysqlclient-dev
pip install -r requirements-2.7.txt
python setup.py build
python setup.py install
```


# MySQL Database Setup
- Install [MySQL](http://dev.mysql.com/downloads/installer/)
- When installing, make sure to include the MySQL Workbench in the installation
- Select the default developer installation

![installation](img/img/mysql-install-default.PNG)

![encryption](img/img/authentication-setup.PNG)

- The installation should allow you the option to create a user. Enter in the following info.

| Username           | Password  |
| ------------- | ----- |
| root | root |

![creating user](img/img/user-creation.PNG)

![user created](img/img/user-created.PNG)

# MySQL Schema Setup
- When creating a database, make sure to create a database with the following info
- Click on new schema button (disk with plus sign at top toolbar)

| Schema       |
| ------------- |
| yourSpot     |

![MySQL Setup](img/img/schema-windows.PNG)

- Use the `dump.sql` to populate and create all the tables/views

![table created](img/img/import-dump.PNG)


### Additional MySQL Setup

```py
sqlalchemy.exc.OperationalError: (_mysql_exceptions.OperationalError) (2059, "Authentication plugin 'caching_sha2_password' cannot be loaded: The specified module could not be found.\r\n")
```
**Fix:** *Run the SQL query shown into MySQL.*
```sql
ALTER USER '[YOURUSERNAME]'@'localhost' IDENTIFIED WITH mysql_native_password BY '[YOURPASSWORD]';
```

# PyCharm IDE Setup
- download and install [PyCharm](https://www.jetbrains.com/pycharm/)
- you can get a free license from JetBrains if you are a [student](https://www.jetbrains.com/student/)


### PyCharm Debugging
- click on the dropdown arrow ![Arrow](img/img/arrow.png) and select edit configurations
- add a python configuration with the following settings

**For Web Server**
![Configuration Setup Web](img/img/web-config.png)

### Run Project

=======
1. Run the `web.py` script to start the web server
2. Open your broswer and go to ```localhost:5000/``` and the web page should display


#### Troubleshooting the Connection of the Webpage to the Database
If for any reason you can't get it to connect to the database, please go to `db/helper.py` and make sure the database, hoset, username, and password are the same

