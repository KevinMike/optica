/**
 * Created by kevin on 08/10/15.
 */
$(".c-producto").click(function(){
    var r = /\d+/;
    var s = $(this).attr("id");
    var num = s.match(r);
    var almacen_actual = $(this).val();
    //Llenando el array producto con los productos ya seleccionados
    var productos = [ $(this).val() ];
    $(".c-producto").each(function() {
        var g = $(this).attr("id");
        var numero = g.match(r);
        var fila_actual = "id_formset-"+num+"-codigo_producto";
        var item_actual = String($(this).attr("id"));
        if( $(this).val() > 0 && $("#id_formset-"+ numero + "-id_almacen").val() == almacen_actual)
        {
            if(fila_actual != item_actual)
                productos.push($(this).val());
        }
    });
    //transformado la data a json
    data = '{"almacen":';
    for(var i=0;i<productos.length;i++)
    {
        if(i==0)
        {
            data += productos[i] + ',"productos":[';
        }
        else
        {
            if(i==productos.length-1)
                data += productos[i];
            else
                data += productos[i]+",";
        }
    }
    data += "]}";
    if ($(this).val() > 0)
    {
        $.ajax({
            url: "/almacen/obtener-producto/",
            type: "POST",
            data:  data,
            dataType: "json",
            async: true,
            success: function (j) {
                var options = '<option value="0">Escoja un Producto</option>';
                for (var i = 0; i < j.length; i++) {
                    options += '<option value="' + parseInt(j[i].codigo) + '">' + j[i].nombre + '</option>';
                }
                nextid = "#id_formset-" + num + "-codigo_producto";
                $(nextid).html(options);
                $(nextid + " option:first").attr('selected', 'selected');
                $(nextid).attr('disabled', false);
                $("#id_formset-"+ num +"-cantidad").attr('disabled', true);
            },
            error: function (xhr, errmsg, err) {
                alert(xhr.status + ": " + xhr.responseText);
            }
        });
    }
    else
    {
        $("#id_formset-"+ num +"-codigo_producto").attr('disabled', true);
        $("#id_formset-"+ num +"-cantidad").attr('disabled', true);
    }
});


