$.ajax({
    type: 'GET',
    url: "/info/",
    success: function (response) {
        // console.log(response)

        var datas = response
        console.log(datas)
        info = []
        for (data of datas){
            info.push(data["fields"])
        }
        console.log(info)


        // $.ajax({
        //     type: 'GET',
        //     url: '/products/',
        //     data: data,
        //
        //     success: function (response) {
        //         console.log(data)
        //
        //     }
        // })


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
