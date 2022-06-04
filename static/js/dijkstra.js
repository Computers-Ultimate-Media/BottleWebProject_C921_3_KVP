let matrixSize = 3; //default matrix size

//function to check if the entered text is a number
function isNumberKey(event) {
    const charCode = (event.which) ? event.which : event.keyCode;
    return !(charCode > 31 && (charCode < 48 || charCode > 57));
}


//clear the entered field
function clearEdge(event) {
    event.target.value = '';
}

//set 0 in the entered field
function setZeroEdge(event) {
    if (event.target.value === '') {
        event.target.value = '0';
    }
}

//function for drawing a matrix with a given size
function draw_matrix(size) {
    let body = $("#matrix").find('tbody');
    body.empty();

    let vertex = $("#vertex");
    vertex.empty();

    vertex.append($('<option>').text('Выберите вершину').prop('disabled', true).prop('selected', true));

    matrixSize = size;

    for (let i = 0; i < size; ++i) {
        //appending an option in the drop-down list
        vertex.append($('<option>').text('' + (i + 1)));

        let tr = body.append($('<tr>')); //inserting a row into a table
        for (let j = 0; j < size; ++j) {
            //inserting a column into a table row
            let input = $('<input>')
                .attr('class', 'matrix-input hide-arrows')
                .attr('type', 'number')
                .attr('id', i + '_' + j)
                .attr('name', i + '_' + j);

            if (i >= j) {
                //format columns that are duplicated in gray with input disabled
                input.prop('disabled', true);
                input.css("background-color", 'gray')
            } else {
                //set useful events on all other input tags
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

draw_matrix(matrixSize); //drawing a matrix with the default size

//handler is called when pressing the button to update the matrix size
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

//function to output data from an array to an html table on a website
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
            $('<td>').text('' + (i + 1)),
            $('<td>').text('' + result[i]),
        ));
    }

    resultTable.append(table.append(thead).append(tbody));
}

//event handler for a form with matrix input
function onSubmitMatrix() {
    //a variable with an empty matrix of size matrixSize
    let matrix = [];

    //filling a two-dimensional array with matrixSize * matrixSize
    for (let i = 0; i < matrixSize; ++i) {
        let row = [];
        for (let j = 0; j < matrixSize; ++j) {
            row.push(0);
        }
        matrix.push(row);
    }

    let isValidMatrix = true; //are all the fields in the matrix entered?
    let selectedOption = $("#vertex").val(); //chosen starting point

    //filling the matrix with data from the table
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

    //display possible errors on the page
    if (error !== '') {
        toastr.warning(error);
        return false;
    }

    //sending POST request to /dijkstra_solver route
    let request = new XMLHttpRequest();
    request.open('POST', 'dijkstra_solver', false);
    request.send(JSON.stringify({
        'matrix': matrix,
        'vertex': Number.parseInt(selectedOption) - 1,
    }));

    //processing the response received from the server
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
