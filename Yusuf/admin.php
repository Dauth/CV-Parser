
<html>
<style>
    input[type=text]
{
    background-color: white;
    cursor: text;
     width: 100%;
    padding: 20px;
box-shadow: none;
    overflow: auto;
    border-spacing: 8px;
  border-style: 1px solid;
}
    </style>
  
     <div class="row-fluid">
     
    <div class="span12">
        <h1>Upload Job</h1 >


        </div>
    </div>

    
    <div class="row-fluid">
     
    <div class="span6">
        <form id="uploadimage" action="fileUpload.php" method="post" enctype="multipart/form-data">
   <input type="text" id="nameJob" name="nameJob" placeholder="Job Title" value=""/><br />
            <input type="text" id="keyword" name="keyword" placeholder="Type in keywords seperated by space" value=""/><br /><br/>
            <input type="file" name="classnotes" value="" /><br />
   <p><input type="submit" name="submit" value="Submit" /></p>
</form>


<div id='succ' hidden><div class="alert alert-success">
    <strong>Success!</strong> Job listed successfully
</div></div>


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
                    console.log(result);
                      $('#succ').show();
                    
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