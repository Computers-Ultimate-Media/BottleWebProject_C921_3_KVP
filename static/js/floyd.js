let matrixSize = 0; //размер матрицы по умолчанию

//функция для проверки того, является ли введенный текст числом
function isNumberKey(event) {
    const charCode = (event.which) ? event.which : event.keyCode;
    return !(charCode > 31 && (charCode < 48 || charCode > 57) && charCode === 189);
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

    matrixSize = size;

    for (let i = 0; i < size; ++i) {
        let tr = body.append($('<tr>')); //вставка строки в таблицу
        for (let j = 0; j < size; ++j) {
            //вставка столбца в строку таблицы
            let input = $('<input>')
                .attr('class', 'matrix-input hide-arrows')
                .attr('type', 'number')
                .attr('name', i + '_' + j);

            if (i >= j) {
                //форматирование столбцов, которые дублируются серым цветом с отключением ввода в input
                input.prop('disabled', true);
                input.css("background-color", 'gray')
            } else {
                //установка полезных событий на все остальные input теги
                input
                    .attr('value', '0')
                    .attr('min', '-1')
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
    } else if (size < 2) {
        error = 'Слишком маленький размер матрицы';
    } else if (size > 15) {
        error = 'Слишком большой размер матрицы';
    }

    if (error !== '') {
        toastr.warning(error);
        return;
    }

    draw_matrix(size)
});

function printShortest(src, size) {
    let body = $("#result-shortest").find('tbody');
    body.empty();

    for (let i = 0; i < size; ++i) {

        let tr = body.append($('<tr>')); //вставка строки в таблицу
        for (let j = 0; j < size; ++j) {
            //вставка столбца в строку таблицы
            let input = $('<input>')
                .attr('class', 'matrix-input hide-arrows')
                .attr('type', 'number')
                .attr('name', i + '_' + j);

                input.prop('disabled', true);
                input.css("background-color", 'white')
                input.attr('value', src[i][j])
            
            tr.append($('<td>').append($('<label>').append(input)));
        }
    }
}

function printPaths(src, size) {
    let body = $("#result-paths").find('tbody');
    body.empty();

    for (let i = 0; i < size; ++i) {

        let tr = body.append($('<tr>')); //вставка строки в таблицу
        for (let j = 0; j < size; ++j) {
            //вставка столбца в строку таблицы
            let input = $('<input>')
                .attr('class', 'matrix-input hide-arrows')
                .attr('type', 'number')
                .attr('name', i + '_' + j);

            input.prop('disabled', true);
            input.css("background-color", 'white');
            input.attr('value', src[i][j]);

            tr.append($('<td>').append($('<label>').append(input)));
        }
    }
}

//функция для вывода данных из массива в html таблицу на сайте
function printResults(result) {

    let textShortest = $('#text-shortest');
    let textPaths = $('#text-paths');

    textShortest.text('Матрица кратчайших путей:');
    textPaths.text('Матрица путей:');

    printShortest(result['shortest'], matrixSize);
    printPaths(result['paths'], matrixSize);
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

    if (!isValidMatrix || !matrixSize) {
        error = 'Заполните матрицу расстояний';
    }

    //отображение возможных ошибок на странице
    if (error !== '') {
        toastr.warning(error);
        return false;
    }

    //отправка POST запроса на маршрут /floyd_solver
    let request = new XMLHttpRequest();
    request.open('POST', 'floyd_solver', false);
    request.send(JSON.stringify({
        'matrix': matrix,
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
