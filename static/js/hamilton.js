let matrixSize = 3;

// input validation
function isNumberKey(event) {
    const charCode = (event.which) ? event.which : event.keyCode;
    return !(charCode > 31 && (charCode < 48 || charCode > 57));
}

// node input validation
function isGraphArcWeightNumberKey(event) {
    const charCode = (event.which) ? event.which : event.keyCode;
    return (charCode == 48 || charCode == 49);
}

// change node value onclick
function changeNode(event) {
    if(event.target.value === '0') {
        event.target.value = '1';
    }
    else if(event.target.value === '1') {
        event.target.value = '0';
    }

}

// set node value if none 
function setZeroToNode(event) {
    if (event.target.value === '') {
        event.target.value = '0';
    }
}

// draw matrix by size
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
                .attr('id', i + '_' + j)
                .attr('name', i + '_' + j);
            if (i >= j) {
                input.prop('disabled', true);
                input.css("background-color", 'gray')
            } else {
                input
                    .attr('value', '0')
                    .attr('maxlength', 1)
                    .attr('onkeypress', 'return isGraphArcWeightNumberKey(event)')
                    .attr('onclick', 'return changeNode(event)')
                    .attr('onblur', 'return setZeroToNode(event)');
            }
            tr.append($('<td>').append($('<label>').append(input)));
        }
    }
}

draw_matrix(matrixSize);

// redraw matrix on update button
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


//handler is called when pressing the matrix input button from the text
$("#button-apply").click(function () {
    //a variable with an empty matrix of size matrixSize
    let matrix = [];

    let lines = $('#matrixTextarea').val().split('\n');
    for (let i = 0; i < lines.length; i++) {
        let row = [];

        let line = lines[i];

        let parts = line.split(',');
        if (parts.length !== lines.length) {
            toastr.warning("Некорректая матрица смежности");
            return;
        }

        for (let part of parts) {
            let number = Number.parseInt(part);
            if (isNaN(number)) {
                toastr.warning("Некорректые данные в тексте матрицы смежности");
                return;
            }
            if (number !== 0 && number !== 1) {
                toastr.warning("Матрица задается только 0 и 1");
                return;
            }
            row.push(number);
        }

        matrix.push(row);
    }

    if (!(lines.length >= 3 && lines.length <= 15)) {
        toastr.warning("Размерность матрицы должна быть не менее 3 и не более 15");
        return;
    }

    //update the matrix on the page
    matrixSize = lines.length;
    draw_matrix(matrixSize);

    for (let i = 0; i < matrixSize; ++i) {
        for (let j = 0; j < matrixSize; ++j) {
            if (i >= j) {
                continue;
            }
            $('#' + i + '_' + j).val('' + matrix[i][j]);
        }
    }

    toastr.success("Была создана матрица размерностью " + matrixSize);
    $('#modalInputMatrix').modal('hide');
});


// print algorithm results
function printResults(result) {
    console.log(result);

    let resultTable = $('#result-table');
    resultTable.empty();

    resultTable.append($('<label>').attr('class', 'form-label mt-4').text('Порядок вершин, образующих Гамильтонов цикл'));

    let table = $('<table>').attr('class', 'table table-bordered table-striped');

    let thead = $('<thead>').append(
        $('<tr>')
        .append($('<th>').attr('scope', 'col').text('Индекс вершины'))
    );

    let tbody = $('<tbody>');

    for (let i = 0; i < result.length; ++i) {
        tbody.append($('<tr>').append(
            $('<td>').text(result[i]),
        ));
    }

    resultTable.append(table.append(thead).append(tbody));
}

// send reqest to backend and print results
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

    $("input[name]").each(function(index, element) {
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