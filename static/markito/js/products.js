// $.ajax({
//     type: 'GET',
//     url: "/info/",
//     success: function (response) {
//         // console.log(response)
//
//         var datas = response
//         console.log(datas)
//         info = []
//         for (data of datas){
//             info.push(data["fields"])
//         }
//         console.log(info)    }
// })



$(document).ready(function () {
            $('#mytable').DataTable({
                // "serverSide": false,
                "serverSide": false,
                "processing": false,
                "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
                "iDisplayLength": 3,
                "responsive" : true,
                "ajax": {
                    url: "/info/",
                    type: 'GET',
                    dataSrc: "",

                },
                'columnDefs': [],
                "columns": [
                    {
                        "data": "fields.image",
                        "render": function(data, type, row, meta) {
                 return '<img src="/media/'+data+'" style="height:45px;width: 45px"/>';}

                    },
                    {"data": "fields.name"},
                    {"data": "fields.category"},
                    {"data": "fields.buy_price"},
                    {"data": "fields.sell_price"},
                    {"data": "fields.count"},
                    {"data": "fields.side_costs"},
                    {"data": "fields.is_active"},

                ]
            });

        });