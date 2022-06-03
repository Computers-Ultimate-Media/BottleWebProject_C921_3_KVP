let matrixSize = 3; //размер матрицы по умолчанию

//функция для проверки того, является ли введенный текст числом
function isNumberKey(event) {
    const charCode = (event.which) ? event.which : event.keyCode;
    return !(charCode > 31 && (charCode < 48 || charCode > 57));
}


//очистить введенное поле
function clearEdge(event) {
    event.target.value = '';
}

//поставить 0 во введенное поле
function setZeroEdge(event) {
    if (event.target.value === '') {
        event.target.value = '0';
    }
}

// функция для отрисовки матрицы с заданным размером
function draw_matrix(size) {
    let body = $("#matrix").find('tbody');
    body.empty();

    let vertex = $("#vertex");
    vertex.empty();

    vertex.append($('<option>').text('Выберите вершину').prop('disabled', true).prop('selected', true));

    matrixSize = size;

    for (let i = 0; i < size; ++i) {
        //дополнение опции в выпадающем списке
        vertex.append($('<option>').text('' + i));

        let tr = body.append($('<tr>')); //вставка строки в таблицу
        for (let j = 0; j < size; ++j) {
            //вставка столбца в строку таблицы
            let input = $('<input>')
                .attr('class', 'matrix-input hide-arrows')
                .attr('type', 'number')
                .attr('id', i + '_' + j)
                .attr('name', i + '_' + j);

            if (i >= j) {
                //форматирование столбцов, которые дублируются серым цветом с отключением ввода в input
                input.prop('disabled', true);
                input.css("background-color", 'gray')
            } else {
                //установка полезных событий на все остальные input теги
                input
                    .attr('value', '0')
                    .attr('min', '0')
                    .attr('onkeypress', 'return isNumberKey(event)')
                    .attr('onclick', 'return clearEdge(event)')
                    .attr('onblur', 'return setZeroEdge(event)');
            }
            tr.append($('<td>').append($('<label>').append(input)));
        }
    }
}

draw_matrix(matrixSize); //отрисовка матрицы с размером по умолчанию

//обработчик нажатия на кнопку обновления размера матрицы
$("#button-update").click(function () {
    let size = Number.parseInt($("#input-size").val());

    let error = '';

    if (isNaN(size)) {
        error = 'Укажите размер матрицы';
    } else if (size < 3) {
        error = 'Размерность матрицы должна быть не менее 3';
    } else if (size > 15) {
        error = 'Размерность матрицы должна быть не более 15';
    }

    if (error !== '') {
        toastr.warning(error);
        return;
    }

    draw_matrix(size)
});

//обработчик нажатия на кнопку ввода матрицы из текста
$("#button-apply").click(function () {
    //переменная с пустой матрицей размером matrixSize
    let matrix = [];

    let lines = $('#matrixTextarea').val().split('\n');
    for (let i = 0; i < lines.length; i++) {
        let row = [];

        let line = lines[i];

        let parts = line.split(',');
        if (parts.length !== lines.length) {
            toastr.warning("Некорректая матрица расстояний");
            return;
        }

        for (let part of parts) {
            let number = Number.parseInt(part);
            if (isNaN(number)) {
                toastr.warning("Некорректые данные в тексте матрицы расстояний");
                return;
            }
            row.push(number);
        }

        matrix.push(row);
    }

    //обновить матрицу на странице
    matrixSize = lines.length;
    draw_matrix(matrixSize);

    console.log(matrix);

    for (let i = 0; i < matrixSize; ++i) {
        for (let j = 0; j < matrixSize; ++j) {
            if (i >= j) {
                continue;
            }
            $('#' + i + '_' + j).val('' + matrix[i][j]);
        }
    }
});

//функция для вывода данных из массива в html таблицу на сайте
function printResults(result) {
    let resultTable = $('#result-table');
    resultTable.empty();

    resultTable.append($('<label>').attr('class', 'form-label mt-4').text('Расстояния от начальной вершины до других'));

    let table = $('<table>').attr('class', 'table table-bordered table-striped');

    let thead = $('<thead>').append(
        $('<tr>')
            .append($('<th>').attr('scope', 'col').text('Индекс вершины'))
            .append($('<th>').attr('scope', 'col').text('Расстояние до вершины'))
    );

    let tbody = $('<tbody>');

    for (let i = 0; i < result.length; ++i) {
        tbody.append($('<tr>').append(
            $('<td>').text('' + i),
            $('<td>').text('' + result[i]),
        ));
    }

    resultTable.append(table.append(thead).append(tbody));
}

//обработчик событий для формы с вводом матрицы
function onSubmitMatrix() {
    //переменная с пустой матрицей размером matrixSize
    let matrix = [];

    //заполнение двумерного массива размером matrixSize * matrixSize
    for (let i = 0; i < matrixSize; ++i) {
        let row = [];
        for (let j = 0; j < matrixSize; ++j) {
            row.push(0);
        }
        matrix.push(row);
    }

    let isValidMatrix = true; //введены ли все поля в матрице?
    let selectedOption = $("#vertex").val(); //выбранная начальная вершина

    //заполнение матрицы данными из таблицы
    $("input[name]").each(function (index, element) {
        let data = element.name.split('_');

        let i = Number.parseInt(data[0]);
        let j = Number.parseInt(data[1]);

        if (i < j) {
            if (element.value === '') {
                isValidMatrix = false;
            } else {
                matrix[i][j] = element.valueAsNumber;
                matrix[j][i] = element.valueAsNumber;
            }
        }
    });

    let error = '';

    if (!isValidMatrix) {
        error = 'Заполните матрицу расстояний';
    } else if (selectedOption === null) {
        error = 'Укажите начальную вершину';
    }

    //отображение возможных ошибок на странице
    if (error !== '') {
        toastr.warning(error);
        return false;
    }

    //отправка POST запроса на маршрут /dijkstra_solver
    let request = new XMLHttpRequest();
    request.open('POST', 'dijkstra_solver', false);
    request.send(JSON.stringify({
        'matrix': matrix,
        'vertex': Number.parseInt(selectedOption),
    }));

    //обработка полученного ответа от сервера
    if (request.status === 200) {
        let data = JSON.parse(request.responseText);
        if ('status' in data && data.status === 'ok') {
            printResults(data['result']);
        } else if ('error' in data) {
            toastr.warning(data.error);
        }
    }

    return false;
}
