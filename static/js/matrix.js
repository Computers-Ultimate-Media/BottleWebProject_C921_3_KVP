function isNumberKey(event) {
    const charCode = (event.which) ? event.which : event.keyCode;
    return !(charCode > 31 && (charCode < 48 || charCode > 57));
}

function draw_matrix(size) {
    let body = $("#matrix").find('tbody');
    body.empty();

    for (let i = 0; i < size; ++i) {
        let tr = body.append($('<tr>'));
        for (let j = 0; j < size; ++j) {
            let input = $('<input>')
                .attr('class', 'matrix-input hide-arrows')
                .attr('type', 'number')
                .attr('onkeypress', 'return isNumberKey(event)');
            if (i >= j) {
                input.prop('disabled', true);
                input.css("background-color", 'gray')
            }
            tr.append($('<td>').append($('<label>').append(input)));
        }
    }
}

draw_matrix(3);

$("#button-update").click(function () {
    let size = $("#input-size").val();
    if (size < 3) {
        toastr.warning('Слишком маленький размер матрицы')
        return;
    }
    if (size > 15) {
        toastr.warning('Слишком большой размер матрицы')
        return;
    }
    draw_matrix(size)
});
