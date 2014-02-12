/**
 * Created by coreyja on 2/3/14.
 */

jQuery(function ($) {

    $('#submit-button').on('click', function (event) {
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
                        data[jsonParent][name] = $(this).val()
                    } else {
                        data[name] = $(this).val()
                    }
                }

            });

            return data;
        }

        var form = $('#insert-form');

        var json = formToJson(form);

        if (!json) {
            console.log('tst');
            return false;
        }

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

        console.log(formToJson(form));

        event.preventDefault();
        return false;
    });

});