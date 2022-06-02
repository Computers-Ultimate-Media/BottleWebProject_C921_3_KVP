% rebase('layout.tpl', title=title, menu=menu, year=year)

<div class="container col-md-4 col-md-offset-4" style="margin: 0 auto; width:80%;">
    <div class="accordion" id="accordionDescription">
        <div class="accordion-item">
            <h2 class="accordion-header" id="headingOne">
                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne"
                        aria-expanded="true" aria-controls="collapseOne">
                    Описание работы алгоритма Флойда
                </button>
            </h2>
            <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne"
                 data-bs-parent="#accordionDescription" style="">
                <div class="accordion-body">
                    <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse
                    plugin adds the appropriate classes that we use to style each element. These classes control the
                    overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of
                    this with custom CSS or overriding our default variables. It's also worth noting that just about any
                    HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
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
        </fieldset>
    </form>

    <!-- Результирующая таблица с id=result-table для отображения через jquery -->
    <div id="result-table">
    </div>
</div>
