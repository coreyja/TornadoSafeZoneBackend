/**
 * Created by coreyja on 2/3/14.
 */

jQuery(function ($) {

    $('#submit-button').on('click', function (event) {
        var formToJson = function (form) {
            var data  = {};

            $(form).find('input[type="text"]').each(function () {

                var name = $(this).attr('name')

                if ($(this).parent('[name]').length === 0){
                    data[name] = $(this).val()
                } else {
                   var parentName = $(this).parent().attr('name')
                    if (!(parentName in data)) {
                        data[parentName] = {};
                    }
                    data[parentName][name] = $(this).val()
                }

            });

            return data;
        }

        var form = $('#insert-form');

        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: JSON.stringify(formToJson(form)),
            dataType: 'json',
            contentType: 'application/json',

            success: function (resp) {
                console.log(resp);
            }
        });

        event.preventDefault();
        return false;
    });

});