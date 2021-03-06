/**
 * Created by coreyja on 2/3/14.
 */

jQuery(function ($) {

    var formToJson = function (form) {
        var data  = {};

        $(form).find('input').each(function () {

            var name = $(this).attr('name');
            var type = $(this).attr('type');
            var val = $(this).val();

            var jsonParent = $(this).attr('data-json-parent');

            // If val doesn't exist then don't add anything to the json
            if (val){
                // If it is a time type add the seconds thing to the end of val
                if (type === 'time') {
                    val += ':00.0';
                }

                if (jsonParent){
                    if (!(jsonParent in data)) {
                        data[jsonParent] = {};
                    }
                    data[jsonParent][name] = val
                } else {
                    data[name] = val
                }
            }

        });

        return data;
    };

    $('#submit-button').on('click', function (event) {
        var form = $('#insert-form');

        var json = formToJson(form);

        if (!json) {
            return false;
        }

        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: JSON.stringify(formToJson(form)),
            dataType: 'json',
            contentType: 'application/json',

            success: function (resp) {
                console.log(resp['id']);
                window.location.href = '/safezone/' + resp['id'];
            }
        });

        event.preventDefault();
        return false;
    });

});