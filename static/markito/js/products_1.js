			$(document).ready(function () {
				$('#items-table').dataTable({
					serverSide: true,
					sAjaxSource: "/data/",  // new url
                                        columns: [
                                            {name: "image", data: 0},
                                            {name: "name", data: 1},
                                            {name: "count", data: 2},
                                        ],
				});
			});