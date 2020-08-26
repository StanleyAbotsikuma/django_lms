
function passwordValidation(password)
{
    var letters = /[a-z]/i;
    var numbers = /[0-9]/;
    if (password.length >= 6) {
        if ( letters.test(password) && numbers.test(password)){
        return "true"
    }

    else
    {
        return "false"
    }
        }else
{

}
}

$(document).ready(
    function()
    {
       
       
        $('#id_password').keyup(function(){
            if(passwordValidation( $('#id_password').val()) == 'true')
            {
                alert('its true')
            }
        })


        $('#confirm_password').keyup(function(){
            if( this.value == $('#id_password').val())
            {
                alert('its true')
            }
        })


        function readURL(input) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();
    
                reader.onload = function (e) {
                    $('#preview_image').attr('src', e.target.result);
                }
    
                reader.readAsDataURL(input.files[0]);
            }
        }
    
        $("#id_profile_picture").change(function () {
            readURL(this);
        });

       

    }
)




