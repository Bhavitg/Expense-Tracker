# Expense-Tracker

Expense tracker is a desktop application that helps to manage daily expenses. The expenses are stored into a database and analysis is done which can be seen through Pie chart and Bar graphs. It is an overall powerful personal finance tool that helps to improve productivity, saves time and money.

There are two types of themes.
Dark
![Example:](/screenshots/main.png)
Light
![Example:](/screenshots/Main Gui Light.png)

Add Expenses
![Example:](/screenshots/Add expenses.png)

Analysis Option
![Example:](/screenshots/Graph.png)

Pie Chart
![Example:](/screenshots/Pie Chart.png)

Settings
![Example:](/screenshots/Settings.png)



## Prerequisites

  - **pyqt5** - to make the Graphical User Interface of the application
  - **matplotlib** - to display the pie chart and bar graph that would be used to show the daily expenses
  - **pymongo** - ORM to connect to a MongoDB instance hosted on Atlas

## Installation

Expense Tracker requires [Python](https://www.python.org/) and of the python some packages to run. It also uses a MongoDB instance created on the Atlas service to store the data.

Install the dependencies from pip:

```sh
$ python -m pip install -r requirements.txt
```

## Development

This was a project built as the Summer Inhouse Project in a month. It helped to learn the basics of PyQt5 and MongoDB integration into a Python application.

## License

MIT License
