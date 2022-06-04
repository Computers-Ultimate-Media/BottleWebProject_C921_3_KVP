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
        MenuOption('Главная', '/'),
        MenuOption('Гамильтонов цикл', '/hamilton'),
        MenuOption('Алгоритм Дейкстры', '/dijkstra'),
        MenuOption('Алгоритм Флойда', '/floyd'),
        MenuOption('Авторы', '/about'),
    ]

    if idx is not None:
        options[idx].is_active = True

    return options


def base_page(extra: dict, styles: list = None, scripts: list = None):
    base_scripts = ['/static/js/main.js']
    if scripts is not None:
        for script in scripts:
            base_scripts.append(script)
    base_styles = []
    if styles is not None:
        for style in styles:
            base_styles.append(style)
    return {**dict(
        year=datetime.now().year,
        styles=base_styles,
        scripts=base_scripts,
    ), **extra}


@route('/')
@view('index')
def index():
    return base_page(dict(
        title='Главная',
        menu=menu(0),
    ))
    # styles=['/static/css/alg.css'], scripts=['/static/js/main1.js']


@route('/hamilton')
@view('hamilton')
def hamilton():
    return base_page(dict(
        title='Гамильтонов цикл',
        menu=menu(1),
    ), styles=['/static/css/hamilton.css'], scripts=['/static/js/hamilton.js'])


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


class Developer:
    name: str
    description: str
    image_link: str
    caption_1: str
    caption_2: str
    caption_3: str
    github_link: str

    def __init__(self, name: str, description: str, image_link: str, caption_1: str, caption_2: str, caption_3: str,
                 github_link: str):
        self.name = name
        self.description = description
        self.image_link = image_link
        self.caption_1 = caption_1
        self.caption_2 = caption_2
        self.caption_3 = caption_3
        self.github_link = github_link


@route('/about')
@view('about')
def about():
    return base_page(dict(
        title='Авторы',
        menu=menu(4),
        developers=[
            Developer(
                'Кулаков Роман',
                'Разработка алгоритма Гамильтона',
                'https://avatars.githubusercontent.com/u/68752471?v=4',
                'Джавист',
                'Напитонил',
                'хочет спать',
                'https://github.com/qwonix',
            ),
            Developer(
                'Волков Александр',
                'Разработка алгоритма Дейкстры',
                'https://avatars.githubusercontent.com/u/98341994?v=4',
                'Его вкусы весьма специфичны',
                'Умеет писать код',
                'Разработчик со стажем',
                'https://github.com/buff3r0verfl0w',
            ),
            Developer(
                'Прокопенко Артем',
                'Разработка алгоритма Флойда',
                'https://avatars.githubusercontent.com/u/60646160?v=4',
                'Предпочитает языки пониже',
                'Хорошо общается с детьми',
                'Основатель Computers-Ultimate-Media',
                'https://github.com/Gauliux',
            )
        ],
    ))
