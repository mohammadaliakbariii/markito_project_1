$.ajax({
    type: 'GET',
    url: "/info/",
    success: function (response) {
        datas = response
        info=[]
        for ( data of datas){
            // console.log(dat["fields"])
            info.push(data["fields"])
        }
        console.log(info)
        for (kala of info){
            $('<tr className="odd"> <td valign="top" colSpan="6" className="dataTables_empty"></td></tr>').appendTo("<tbody></tbody>").html(kala.name)
            console.log(kala.name)

                $.ajax(
                    {
                        type: "POST",
                        url:"/products/",
                        data:info,
                        success(response){
                            response["info"]
                        }
                    }
                )
        }
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
