% rebase('layout.tpl', title=title, menu=menu, year=year)

<div class="container col-md-4 col-md-offset-4" style="margin: 0 auto; width:80%;">
    <form onsubmit="return onSubmitMatrix();">
        <table id="matrix" align="center">
            <tbody></tbody>
        </table>

        <fieldset>
            <div class="form-group">
                <label class="form-label mt-4">Размерность матрицы расстояний</label>
                <div class="form-group">
                    <div class="input-group mb-3">
                        <input type="number" class="form-control hide-arrows" placeholder="Введите размерность"
                               aria-describedby="button-update" id="input-size" onkeypress="return isNumberKey(event)">
                        <button class="btn btn-primary" type="button" id="button-update">Обновить</button>
                    </div>
                </div>
            </div>

            <div class="form-group">
                <label for="vertex" class="form-label mt-4">Начальная вершина</label>
                <select class="form-select" id="vertex" required>
                </select>
            </div>

            <br>

            <button type="submit" class="btn btn-primary">Найти расстояния</button>
        </fieldset>
    </form>

    <div id="result-table">
        <label class="form-label mt-4">Расстояния от начальной вершины до других</label>
        <table class="table table-bordered table-striped">
            <thead>
            <tr>
                <th scope="col">Индекс вершины</th>
                <th scope="col">Расстояние до вершины</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <th scope="row">Default</th>
                <td>Column content</td>
            </tr>
            <tr>
                <th scope="row">Default</th>
                <td>Column content</td>
            </tr>
            <tr>
                <th scope="row">Default</th>
                <td>Column content</td>
            </tr>
            </tbody>
        </table>
    </div>
</div>
