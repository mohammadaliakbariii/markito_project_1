$.ajax({
    type: 'GET',
    url: "/info/",
    success: function (response) {
        console.log(response)
        var data = response
        console.log(data)

        $.ajax({
            type: 'POST',
            url: '/products/',
            data: data,

            success: function (response) {

                console.log("done")
            }
        })


    }
})

$('#dt-material-checkbox').dataTable({

    columnDefs: [{
        orderable: false,
        className: 'select-checkbox',
        targets: 0
    }],
    select: {
        style: 'os',
        selector: 'td:first-child'
    }
});
