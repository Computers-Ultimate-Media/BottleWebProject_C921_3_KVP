<!doctype html>
<html lang="ru">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ title }} - GraphApp</title>
    <!-- Подключение bootstrap minty theme, иконок и toastr -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="/static/css/bootstrap-icons.min.css">
    <link rel="stylesheet" href="/static/css/toastr.min.css">
    %for style_link in styles:
    <link rel="stylesheet" href="{{ style_link }}">
    %end
</head>
<body>

<div class="col-lg-8 mx-auto p-3 py-md-5">
    <!-- Шапка сайта -->
    <header class="d-flex justify-content-center py-3">
        <ul class="nav nav-pills">
            %for option in menu:
            <li class="nav-item">
                <a href="{{ option.link }}" class="{{ option.class_name() }}">{{ option.name }}</a>
            </li>
            %end
        </ul>
    </header>

    <!-- Базовая часть страницы -->
    <main>
        {{!base}}
    </main>

    <!-- Информация о нас в footer'е -->
    <footer class="pt-5 my-5 text-muted border-top">
        GraphApp Team &copy; {{ year }}<br>
        <i class="bi-github" role="img"></i>
        <a style="margin: 2px; text-decoration: none"
           href="https://github.com/Computers-Ultimate-Media/BottleWebProject_C921_3_KVP">
            Source code
        </a>
    </footer>
</div>

<!-- Подключение bootstrap bundle, jquery, toastr -->
<script src="/static/js/bootstrap.bundle.min.js"></script>
<script src="/static/js/jquery.min.js"></script>
<script src="/static/js/toastr.min.js"></script>

%for script_link in scripts:
<script src="{{ script_link }}"></script>
%end

</body>
</html>
