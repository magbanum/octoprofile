# octoprofile
<kbd> <img src="https://res.cloudinary.com/magbanum/image/upload/v1624796429/Octoprofile_utkgsy.png" /> </kbd>

Visualize your GitHub profile in a better way with Charts and the top repos sorted according to stars, forks and sizes. Give it a try. ⚡
Project Octoprofile uses GitHub API to collect user information from it's GitHub profile and with the help of ChartJS displays it in Graphical way.
This project is build in Django and deployed on the Heroku ( Free dyno ).

To view your Octoprofile visit [octoprofile.herokuapp.com](https://octoprofile.herokuapp.com/) and enter your GitHub username. Don't have GitHub profile, check mine by typing `magbanum` or by clicking [here](https://octoprofile.herokuapp.com/profile/?username=magbanum).
The website might be slower for first load as the project is deployed on Heroku's free dyno.



[![CodeFactor](https://www.codefactor.io/repository/github/magbanum/octoprofile/badge)](https://www.codefactor.io/repository/github/magbanum/octoprofile)

### Coded with
- Python
- JavaScript
- HTML5
- CSS3

### Built with
- [Django](https://www.djangoproject.com/) High-level Python Web framework
- [Django REST framework](https://www.django-rest-framework.org/) Powerful and flexible toolkit for building Web APIs.
- [ChartJS](https://www.chartjs.org/) Simple yet flexible JavaScript charting for designers & developers
- [ListJS](https://listjs.com/) Perfect library for adding search, sort, filters to tables, lists and various HTML elements.
- [GitHub API](https://docs.github.com/en/rest) Create calls to get the data you need to integrate with GitHub.
- [Jquery](https://jquery.com/) Fast, small, and feature-rich JavaScript library.

### Deployed on
- [Heroku](http://heroku.com/) Platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.




## Setup

Clone the repository:

```sh
$ git clone https://github.com/magbanum/octoprofile.git
$ cd octoprofile
```

Before proceeding further, you will need to add few credentials like `SECRET_KEY` from `settings.py` and `GITHUB_ACCESS_TOKEN` from `views.py`. Also, set `DEBUG` equal to `True`.
Do this to avoid any errors.

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
$ env\Scripts\activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `env`.

Once `pip` has finished downloading the dependencies, run the server:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.

Any Suggestions are always welcomed. Give it a ⭐ if you like your Octoprofile.

Inspired by the works of [Brittany Chiang](https://brittanychiang.com/).

