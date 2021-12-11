$(document).ready(function () {
        $('#mytable').DataTable({
            serverSide: true,
            "aLengthMenu": [[3, 5, 10, 25, -1], [3, 5, 10, 25, "All"]],
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
                {name: "stock", data: 5},
                {name: "side_costs", data: 6},
                {name: "is_active", data: 7},
            ],
        });
    });