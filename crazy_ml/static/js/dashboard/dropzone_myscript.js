$(document).ready(function () {
    $('#select-category').on("change", function () {
        $('#select-category').css('color', '#555');
    });

    $('#discard').on("click", function () {
        $('#select-category').css('color', '#555');
    });
    Dropzone.autoDiscover = false;

    $("#dropzonePreview").dropzone( {
        autoDiscover: false,
        maxFiles: 1,
        maxFilesize: 30, //mb
        addRemoveLinks: true,
        autoProcessQueue: false, // this is important as you dont want form to be submitted unless you have clicked the submit button
        paramName: 'pic', // this is optional Like this one will get accessed in php by writing $_FILE['pic'] // if you dont specify it then bydefault it taked 'file' as paramName eg: $_FILE['file']
        previewsContainer: '#dropzonePreview', // we specify on which div id we must show the files
        clickable: '#dropzonePreview',
        acceptedFiles: 'image/*',
        url: 'temp',
        accept: function(file, done) {
            $('.dz-progress').hide();
            file.previewElement.classList.add("dz-success");
        },
        addedfiles: function () {
            var usedInput = this.hiddenFileInput;
            usedInput.name = "file";
            usedInput.id = 'file_div'
            alert(usedInput.id);
            if($("#file_div").length) {
                $('#file_div').val(usedInput.value);
            }
            else {
                $('.dropzone').append(usedInput);
            }
        }
    });

    $('#submit').on("click", function () {
    alert($('#file_div').val());
    });

    $('#discard').on('click', function () {
         $('#select-category').prop('selectedIndex',0);
         $('form[name="title"]').val();
         $('#compose-textarea').html('Please do not send us information about the frontend bugs.\n' +
        'All others information and suggestions are very welcome.\n' +
        'Thanks a lot ;)')

    })
});
