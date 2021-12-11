
$(document).ready(function () {


        $('#mytable').DataTable({
            serverSide: true,
            "aLengthMenu": [[3, 5, 10, 25, 50,100,150], [3, 5, 10, 25, 50,100,150]],
            "iDisplayLength": 3,
            sAjaxSource: "/data/",
            columns: [
                {
                    name: "image", data: 0,
                    "render": function (data, type, row, meta) {
                        return '<img src="/media/'+data + '" style="height:45px; width:45px"/>';
                    }
                },
                {name: "name", data: 1},
                {name: "category", data: 2},
                {name: "buy_price", data: 3},
                {name: "sell_price", data: 4},
                {name: "count", data: 5},
                {name: "side_costs", data: 6},
                {name: "is_active", data: 7},
                          {
            "data": null,
            "defaultContent": '<button type="button" class="btn btn-info" data-toggle="modal" data-target="#editmodal">Edit</button>' + '&nbsp;&nbsp' +
            '<button type="button" class="btn btn-danger" data-toggle="modal" data-target="#deletemodal">Delete</button>'
        }
            ],

            select:true,

        });
    });










//
// $(document).ready(function () {
//         editor = new $.fn.dataTable.Editor( {
//         table: "#mytable",
//         fields: [
//             {
//                 label: "image",
//                 name: "image"
//             },
//             {
//                 label: "name",
//                 name: "name"
//             }, {
//                 label: "category",
//                 name: "category"
//             }, {
//                 label: "buy price:",
//                 name: "buy_price"
//             }, {
//                 label: "sell price",
//                 name: "sell_price"
//             }, {
//                 label: "count",
//                 name: "count"
//             },
//             {
//                 label: "side_costs:",
//                 name: "side_costs"
//             },
//             {
//                 label: "status",
//                 name: "is_active"
//             }
//         ]
//     } );
//
//         $('#mytable').DataTable({
//             serverSide: true,
//             "aLengthMenu": [[3, 5, 10, 25, 50,100,150], [3, 5, 10, 25, 50,100,150]],
//             "iDisplayLength": 3,
//             sAjaxSource: "/data/",
//             columns: [
//                 {
//                     name: "image", data: 0,
//                     "render": function (data, type, row, meta) {
//                         return '<img src="/media/'+data + '" style="height:45px; width:45px"/>';
//                     }
//                 },
//                 {name: "name", data: 1},
//                 {name: "category", data: 2},
//                 {name: "buy_price", data: 3},
//                 {name: "sell_price", data: 4},
//                 {name: "count", data: 5},
//                 {name: "side_costs", data: 6},
//                 {name: "is_active", data: 7},
//                           {
//             "data": null,
//             "defaultContent": '<button type="button" class="btn btn-info" data-toggle="modal" data-target="#editmodal">Edit</button>' + '&nbsp;&nbsp' +
//             '<button type="button" class="btn btn-danger" data-toggle="modal" data-target="#deletemodal">Delete</button>'
//         }
//             ],
//
//             select:true,
//             buttons: [
//             { extend: "create", editor: editor },
//             { extend: "edit",   editor: editor },
//             { extend: "remove", editor: editor }
//         ]
//
//         });
//     });


