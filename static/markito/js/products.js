$(document).ready(function () {


        let table = $('#mytable').DataTable({
            serverSide: true,
            "aLengthMenu": [[3, 5, 10, 25, 50, 100, 150], [3, 5, 10, 25, 50, 100, 150]],
            "iDisplayLength": 3,
            sAjaxSource: "/data/",
            "bInfo" : false,
            columns: [
                {
                    name: "image", data: 0,
                    "render": function (data, type, row, meta) {
                        return '<img src="/media/' + data + '" style="height:45px; width:45px"/>';
                    }
                },
                {name: "name", data: 1},
                {name: "category", data: 2},
                {name: "buy_price", data: 3},
                {name: "sell_price", data: 4},
                {name: "count", data: 5},
                {name: "side_costs", data: 6},
                {name: "is_active", data: 7},
                {name: "id", data: 8},
                {
                    "data": null,
                    "defaultContent": '<button type="button" class="btn btn-info" data-toggle="modal" data-target="#editmodal">Edit</button>' + '&nbsp;&nbsp' +
                        '<button type="button" class="btn btn-danger" data-toggle="modal" data-target="#deletemodal">Delete</button>'
                }
            ],

            select: true,

        });
        $(document).ready(function () {
            $('#mytable tbody').on('click', 'button', function () {
                var data = table.row($(this).parents('tr')).data();
                console.log(data)
                console.log(data[8])
                var id = data[8]
                let class_name = $(this).attr('class');
                if (class_name == 'btn btn-info') {
                    // EDIT button
                    $('#name').val(data['name']);
                    $('#category').val(data['category']);
                    $('#buy_price').val(data['buy_price']);
                    $('#sell_price').val(data['sell_price']);
                    $('#side_costs').val(data['side_costs']);
                    $('#count').val(data['count']);
                    $('#type').val('edit');
                    $('#modal_title').text('EDIT');
                    $("#myModal").modal();
                    //    --------------------------------------------------------------------------------------------------
                } else {
                    // DELETE button
                    $('#modal_title').text('DELETE');
                    $("#confirm").modal();
                    //    --------------------------------------------------------------------------------------------------
                }


                $('form').on('submit', function (e) {
                    e.preventDefault();
                    let $this = $(this);
                    console.log($this.serialize())
                    let type = $('#type').val();
                    let method = '';
                    let url = '/update/' + id + '/';
                    method = "POST";
                    $.ajax({
                        url: url,
                        method: method,
                        data: $this.serialize(),
                        success: function (data, textStatus, jqXHR) {
                            location.reload(),
                                console.log("done")
                        },
                        error: function () {
                            console.log("not done")
                            console.log(jqXHR)

                        }
                    });
                    //    -----------------------------------------------------------------------------------------------------

                });
                $("#delete").click(function (e) {
                    e.preventDefault();
                    console.log("hello")
                    let $this = $(this);
                    console.log($this.serialize())
                    let type = $('#type').val();
                    let method = '';
                    $.ajax({
                        url: '/delete/' + id + '/',
                        method: 'POST',
                        data: $this.serialize(),
                        success: function (data, textStatus, jqXHR) {
                            location.reload();
                            console.log('done')
                        },
                        error: function (jqXHR, textStatus, errorThrown) {
                            console.log(jqXHR)
                        }
                    })
                });

            });
        })

    },
);


