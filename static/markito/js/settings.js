$(document).ready(function () {
        $('#mytable').DataTable({
            serverSide: true,
            "aLengthMenu": [[3, 5, 10, 25, 50,100,150], [3, 5, 10, 25, 50,100,150]],
            "iDisplayLength": 3,
            sAjaxSource: "/info/",
            columns: [
                {name: "channel__name", data: 0},
                {name: "name", data: 1},
                {name: "created_date", data: 2},
                {name: "updated", data: 3},

            ],
        });

    });




