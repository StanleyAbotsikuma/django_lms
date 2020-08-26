
var ini = 0;
$(document).ready(
    function () {


        $(".add_class_room").click(function(){
            $('.form_overlay').addClass('show').css('display','block');
          });



          
        $('.close , .close1').click(function(){
            $('.form_overlay').removeClass('show').css('display','none');
          });


          $('.add_file').on('click',function(){
            ini += 1;

            var newDiv = $('<div class="attachment_form row"><div class="col-md-4 col-sm-4"><input type="file" name="file" class="form-control" style="height: unset;" required="true"></div><div class="col-md-4 col-sm-4"><select  class="form-control" style="height: unset;" required="true"> <option value=" ">Attachment Type </option><option value="Pictures">Pictures</option><option value="Audios">Audios</option><option value="Videos">Videos</option><option value="Documents">Documents</option></select></div><div class="col-md-4 col-sm-4"><button class="form-control remove_attach" style="height: unset;background-color: #fd7777; color: white;" type="button" onclick="$(this).parent().parent().remove()"> Remove </button></div></div>');
            newDiv.find('input').attr('name', 'attachment'+ini.toString())
            newDiv.find('select').attr('name','attachmentType'+ini.toString())
            $('#add_attachments').append(newDiv);
            $('.num_of_a').val();
            $('.num_of_a').attr('value',ini)
     
          })

         
          //$('.remove_attach').on('click',function(){$(this).parents('.attachment_form').remove();}          )
       
    })