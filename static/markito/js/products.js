$.ajax({
    type:'GET',
    url: "{% url 'markito:products' %}",
    dataType:"json",
    success:function (json) {
        data:""
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
