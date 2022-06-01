let matrixSize = 3;

function isNumberKey(event) {
    const charCode = (event.which) ? event.which : event.keyCode;
    return (charCode == 48 || charCode == 49);
}

function draw_matrix(size) {
    let body = $("#matrix").find('tbody');
    body.empty();

    let vertex = $("#vertex");
    vertex.empty();

    vertex.append($('<option>').text('Выберите вершину').prop('disabled', true).prop('selected', true));

    matrixSize = size;

    for (let i = 0; i < size; ++i) {
        vertex.append($('<option>').text('' + i));

        let tr = body.append($('<tr>'));
        for (let j = 0; j < size; ++j) {
            let input = $('<input>')
                .attr('class', 'matrix-input hide-arrows')
                .attr('type', 'number')
                .attr('onkeypress', 'return isNumberKey(event)')
                .attr('name', i + '_' + j);
            if (i >= j) {
                input.prop('disabled', true);
                input.css("background-color", 'gray')
            }
            tr.append($('<td>').append($('<label>').append(input)));
        }
    }
}

draw_matrix(matrixSize);

$("#button-update").click(function () {
    let size = Number.parseInt($("#input-size").val());
    if (size < 3) {
        toastr.warning('Слишком маленький размер матрицы');
        return;
    }
    if (size > 15) {
        toastr.warning('Слишком большой размер матрицы');
        return;
    }
    draw_matrix(size)
});

function printResults(result) {
    console.log(result);

    let resultTable = $('#result-table');
    resultTable.empty();

    resultTable.append($('<label>').attr('class', 'form-label mt-4').text('Расстояния от начальной вершины до других'));

    let table = $('<table>').attr('class', 'table table-bordered table-striped');

    let thead = $('<thead>').append(
        $('<tr>')
            .append($('<th>').attr('scope', 'col').text('Индекс вершины'))
    );

    let tbody = $('<tbody>');

    for (let i = 0; i < result.length; ++i) {
        tbody.append($('<tr>').append(
            $('<td>').text('' + result[i]),
        ));
    }

    resultTable.append(table.append(thead).append(tbody));
}

function onSubmitMatrix() {
    let matrix = [];

    for (let i = 0; i < matrixSize; ++i) {
        let row = [];
        for (let j = 0; j < matrixSize; ++j) {
            row.push(0);
        }
        matrix.push(row);
    }

    let isValidMatrix = true;

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
    }

    if (error === '') {
        let input = {
            'matrix': matrix,
        };

        let request = new XMLHttpRequest();
        request.open('POST', 'hamilton_solver', false);
        request.send(JSON.stringify(input));

        if (request.status === 200) {
            let data = JSON.parse(request.responseText);
            if ('status' in data && data.status === 'ok') {
                printResults(data['result']);
            } else if ('error' in data) {
                toastr.warning(data.error);
            }
        }
    } else {
        toastr.warning(error);
    }

    return false;
}