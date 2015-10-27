/**
 * Created by kevin on 08/10/15.
 */
$(".c-producto").change(function(){
    var s = $(this).attr("id");
    var r = /\d+/;
    var num = s.match(r);
    var precio,cantidad;
    console.log("form: "+parseInt(num[0]));
    console.log("valor: "+$(this).val());
    $.ajax({
        url: "/almacen/obtener-producto/"+parseInt($(this).val()),
        type: "GET",
        dataType: "json",
        async: true,
        success: function (j) {
            precio  = "#id_formset_producto-"+ num[0]+"-precio";
            cantidad = "#id_formset_producto-"+num[0]+"-cantidad";
            $(precio).val(j.precio);
            $(cantidad).attr("max", j.max_value);
        },
        error: function (xhr) {
            alert(xhr.status + ": " + xhr.responseText);
        }
    });
});


