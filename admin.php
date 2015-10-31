<html>

  
    <div class="row-fluid">
     
    <div class="span12">
        <form id="uploadimage" action="fileUpload.php" method="post" enctype="multipart/form-data">
   
   Job Description:<br /> <input type="file" name="classnotes" value="" /><br />
   <p><input type="submit" name="submit" value="Submit" /></p>
</form>




        </div>
    </div>

        <div class="row-fluid">

     <div class="span12">
            <div id="loadResults">
               
            </div>
    </div>
    </div>




     <!-- Modal -->
    <div id="myModal">
        <div class="close-myModal popClose" style="cursor:pointer;float:right;color:white;font-size:200%;padding:20px;"> 
            <i class="fa fa-times"></i>
        </div>
        <div class="modal-content" style="padding:20px;">
            
        <div class="row-fluid">
            <div class="span12"> 
                <h3 id="resultTitle"></h3>
                <br/><div class="exportBtn" style="float:right;cursor:pointer;">Download&nbsp<i class="fa fa-download"></i></div>

            </div>
        </div>
            
        <div class="row-fluid text-left">
        <div class="span12 text-center">
              <div id="resultContent"></div>  
            </div>
        </div>
    </div>
                
    
     <script type="text/javascript">
        
         $('#myModal').hide();

         $( '#uploadimage' ).submit( function( e ) 
    {
             e.preventDefault();
        $.ajax({
                  url: 'uploadJob.php',
                  type: 'POST',
                  data: new FormData( this ),
                  processData: false,
                  contentType: false,
                  success: function(result) {
                    
                      
                       $.ajax({    //create an ajax request to load_page.php
            type: "POST",
            url: "loadResults.php",
            data: "id=1",  //with the page number as a parameter
            dataType: "html",   //expect html to be returned
            success: function(msg){

                if(parseInt(msg)!=0)    //if no errors
                {
                    $("#loadResults").html(msg).hide().fadeIn('2000');
                    //$('.mainBody').html(msg).hide().fadeIn('2000');    //load the returned html into pageContet
                    //$('#loading').css('visibility','hidden');   //and hide the rotating gif
                }
            },
            error: function()
            {
                //alert('error');
            }

        });
                    
                  }
                });
        });
         
         //http://button.csscook.com/
         
         $('body').on('click', '.loadQuestionLink', function(e) 
    {
             e.preventDefault();
        $( ".loadQuestionLink" ).each(function( index ) {
            $(this).children().first().css("background", "white");
});
//        
        $(this).children().first().css("background", "#ecf0f1");
        
             
             
              document.body.style.overflow = "hidden";
            e.preventDefault();
              if($(this).attr('data-once') == 'false')
                {
                    $(this).animatedModal({modalTarget:'myModal',color: 'rgba(0,0,0,0.8)'});
                    $(this).attr('data-once','true');
                    $(this).trigger('click');
                }
                else
                {
                                     $('#myModal').show();
                                        $('#myModal').css("color", "white");
                }
        
                         // pdfId = $(this).attr('href');
             $('#resultTitle').html($(this).attr('data-pdf'));
             
              $('#resultContent').html("<iframe style='body{margin: 0;}' src=uploads/"+$(this).attr('data-pdf')+".pdf?#zoom=100' type='application/pdf' width=850 height='100%'<param name='view'/></iframe>");



            
    });
         
    </script>

</html>