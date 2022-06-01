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

            <br>

            <button type="submit" class="btn btn-primary">Найти цикл</button>
        </fieldset>
    </form>

    <div id="result-table">
    </div>
</div>
