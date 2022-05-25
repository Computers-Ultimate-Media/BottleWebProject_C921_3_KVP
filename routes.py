"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime
from impl.dijkstra import handler
from impl.floyd import handler
from impl.hamilton import handler


class MenuOption:
    name: str
    link: str
    is_active: bool

    def __init__(self, name: str, link: str, is_active: bool = False):
        self.name = name
        self.link = link
        self.is_active = is_active

    def class_name(self):
        name = "nav-link"
        if self.is_active:
            name += " active"
        return name


def menu(idx=None):
    options = [
        MenuOption('На главную', '/'),
        MenuOption('Гамильтонов цикл', '/hamilton'),
        MenuOption('Алгоритм Дейкстры', '/dijkstra'),
        MenuOption('Алгоритм Флойда', '/floyd'),
        MenuOption('Авторы', '/about'),
    ]

    if idx is not None:
        options[idx].is_active = True

    return options


def base_page(extra: dict, scripts: list = None):
    base_scripts = ['static/js/main.js']
    if scripts is not None:
        for script in scripts:
            base_scripts.append(script)
    return {**dict(
        year=datetime.now().year,
        scripts=base_scripts,
    ), **extra}


@route('/')
@view('index')
def index():
    return base_page(dict(
        title='Главная',
        menu=menu(0),
    ))
    # , scripts=['static/js/main1.js']


@route('/hamilton')
@view('hamilton')
def hamilton():
    return base_page(dict(
        title='Гамильтонов цикл',
        menu=menu(1),
    ))


@route('/dijkstra')
@view('dijkstra')
def dijkstra():
    return base_page(dict(
        title='Алгоритм Дейкстры',
        menu=menu(2),
    ))


@route('/floyd')
@view('floyd')
def floyd():
    return base_page(dict(
        title='Алгоритм Флойда',
        menu=menu(3),
    ))


@route('/about')
@view('about')
def about():
    return base_page(dict(
        title='Авторы',
        menu=menu(4),
    ))
