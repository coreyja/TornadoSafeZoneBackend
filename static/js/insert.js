/**
 * Created by coreyja on 2/3/14.
 */

jQuery(function ($) {

    $('#submit-button').on('click', function (event) {
        var formToJson = function (form) {
            var data  = {};

            $(form).find('input[type="text"]').each(function () {
               var name = $(this).attr('name')
                data[name] = $(this).val()
            });

            return data;
        }

        var form = $('#insert-form');

        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: formToJson(form),
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