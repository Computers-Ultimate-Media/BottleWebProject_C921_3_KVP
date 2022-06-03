% rebase('layout.tpl', title=title, menu=menu, year=year)

<!-- модальное окно для ввода матрицы из текста -->
<div class="modal fade" id="modalInputMatrix" tabindex="-1" aria-labelledby="modalInputMatrixLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="modalInputMatrixLabel">Введите матрицу через запятую по строкам</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <textarea class="form-control" id="matrixTextarea" rows="10"></textarea>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-primary" id="button-apply">Применить</button>
            </div>
        </div>
    </div>
</div>

<div class="container col-md-4 col-md-offset-4" style="margin: 0 auto; width:80%;">
    <div class="accordion" id="accordionDescription">
        <div class="accordion-item">
            <h2 class="accordion-header" id="headingOne">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne"
                        aria-expanded="true" aria-controls="collapseOne">
                    Описание работы алгоритма Дейкстры
                </button>
            </h2>
            <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne"
                 data-bs-parent="#accordionExample" style="">
                <div class="accordion-body">
                    <div class="row">
                        <div class="col align-self-center" style="text-indent: 30px">
                            <img height="auto" width="90%" src="https://i.imgur.com/DdyaJpG.gif">
                        </div>
                        <div class="col">
                            <div class="row">
                                <p>
                                    <strong>Неформальное объяснение</strong><br>
                                    Каждой вершине из <strong>V</strong> сопоставим метку — минимальное известное
                                    расстояние от этой вершины до <strong>a</strong>.

                                    Алгоритм работает пошагово — на каждом шаге он «посещает» одну вершину и пытается
                                    уменьшать метки.
                                    Работа алгоритма завершается, когда все вершины посещены.
                                </p>
                            </div>
                            <div class="row">
                                <p>
                                    <strong>Инициализация.</strong><br>Метка самой вершины <strong>a</strong> полагается
                                    равной 0, метки остальных вершин — бесконечности. Это отражает то, что расстояния от
                                    <strong>a</strong> до других вершин пока неизвестны. Все вершины графа помечаются
                                    как непосещённые.
                                </p>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col">
                            <div class="row">
                                <p>
                                    <strong id="alg-step">Шаг алгоритма.</strong><br>

                                    Если все вершины посещены, алгоритм завершается.
                                    <br>

                                    В противном случае, из ещё не посещённых вершин выбирается вершина
                                    <strong>u</strong>,
                                    имеющая
                                    минимальную метку.
                                    <br>

                                    Мы рассматриваем всевозможные маршруты, в которых <strong>u</strong> является
                                    предпоследним пунктом.
                                    Вершины, в которые ведут рёбра из <strong>u</strong>, назовём соседями этой вершины.
                                    Для каждого
                                    соседа вершины <strong>u</strong>, кроме отмеченных как посещённые, рассмотрим новую
                                    длину пути,
                                    равную сумме значений текущей метки <strong>u</strong> и длины ребра, соединяющего
                                    <strong>u</strong> с этим
                                    соседом.
                                    <br>

                                    Если полученное значение длины меньше значения метки соседа, заменим значение метки
                                    полученным значением длины. Рассмотрев всех соседей, пометим вершину
                                    <strong>u</strong> как
                                    посещённую и повторим <a href="#alg-step">шаг алгоритма</a>.
                                    <br>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <br>

    <!-- Форма с кастомный обработчиком событий -->
    <form onsubmit="return onSubmitMatrix();">
        <!-- Пустая таблица с id=matrix для отображения через jquery -->
        <table id="matrix" align="center">
            <tbody></tbody>
        </table>

        <fieldset>
            <!-- input для ввода матрицы расстояний, id=input-size -->
            <div class="form-group">
                <label class="form-label mt-4">Размерность матрицы расстояний</label>
                <div class="form-group">
                    <div class="input-group mb-3">
                        <input type="number" class="form-control hide-arrows" placeholder="Введите размерность"
                               aria-describedby="button-update" id="input-size" onkeypress="return isNumberKey(event)">
                        <!-- кнопка для обновления размера матрицы, id=button-update -->
                        <button class="btn btn-primary" type="button" id="button-update">Обновить</button>
                    </div>
                </div>
            </div>

            <!-- input для начальной вершины, id=vertex -->
            <div class="form-group">
                <label for="vertex" class="form-label mt-4">Начальная вершина</label>
                <select class="form-select" id="vertex" required>
                </select>
            </div>

            <br>

            <button type="submit" class="btn btn-primary">Найти расстояния</button>

            <!-- button для открытия модального окна на сайте -->
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modalInputMatrix">
                Ввести матрицу текстом
            </button>
        </fieldset>
    </form>

    <!-- Результирующая таблица с id=result-table для отображения через jquery -->
    <div id="result-table">
    </div>
</div>
