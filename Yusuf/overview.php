<?php

header('Content-Type: text/html; charset=UTF-8');

?>

<html>
<style type="text/css">
#modalLoad
{
  height: 30%;
  width: auto;
  padding-top: 40%;
  margin: auto;
}
.close 
{
    cursor: pointer;
    float:right;
    display:inline-block;
    padding:2px 5px;
}
#fromGraph
{
    z-index: 99999;
}
 #fade {
        display: none; /* Hidden as default */
        background: #000;
        position: fixed; left: 0; top: 0;
        width: 100%; height: 100%;
        opacity: .80;
        z-index: 9998;
        }
        .modalTable{
          table-layout: fixed;
          width: 100%;
          color: white;
          border-spacing: 10px;
border-collapse: separate;
        }
        #myModal {
        overflow-y:auto;
        max-height:90%;
        position: fixed;
        color: white;
        display: none; /* Hidden as default */
        float: left;
        top: 10px; 
        z-index: 99998;
        padding: 25px;
        }
button
{
    width: 100%;
    border-radius: 50%;
}
    .centered-text {
    text-align:center
}   
    
    <!--http://stackoverflow.com/questions/9184141/how-do-you-get-centered-content-using-twitter-bootstrap    -->
    
.no-sort::after { display: none!important; opacity: 0!important;}

.no-sort { pointer-events: none!important; cursor: default!important; opacity: 0!important;}

#selectAll, #unselectAll
{
    cursor: pointer;
    color: blue;
}
.indSumm
{
    cursor: pointer;
    z-index: 10001;
}
#eventSelectNotif, #typeNotification
{
    width: 100% !important;
}
select
{
    width: 150px;
}
td
{
    text-align:center !important;
}
td.highlight {
        background-color: #efefef;
        border-style: 2px solid white !important    ;
    }
.copy
{
    cursor: pointer;
}
.carousel-indicators li { visibility: hidden !important; }
textarea
{
    font-family: 'Dosis', sans-serif;
    text-align: justify;
    resize: none;
    height: 150px;
  width:100%;
}
    .btn-style{
	border : solid 0px #ffffff;
	border-radius : 3px;
	moz-border-radius : 3px;
	font-size : 20px;
	color : #ffffff;
	padding : 7px 12px;
	background-color : #0a66c9;

}
textarea[disabled]
{
    background-color: rgba(236, 240, 241,0.3);
    border-style: none;
    cursor: default;
    box-shadow: none;
}
.searchFields
{
    width: 80%;
    padding-left: 10px;
    padding-right: 10px;
  border-radius:10px;
  border-style: none;
}
.searchFieldsSelect
{
    max-width: 80px;
}
.searchFields:focus
{
    outline:none;
}
.searchContainer
{
    padding: 20px;
}
.centerWrapper
{
    text-align:center;
}
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

.classnotes::-webkit-file-upload-button {
  visibility: hidden;
}
.classnotes::before {
  content: 'Choose file';
  display: inline-block;
  background: -webkit-linear-gradient(top, #f9f9f9, #e3e3e3);
  border: 1px solid #999;
  border-radius: 3px;
  padding: 5px 8px;
  outline: none;
  white-space: nowrap;
  -webkit-user-select: none;
  cursor: pointer;
  text-shadow: 1px 1px #fff;
  font-weight: 700;
  font-size: 10pt;
}
.classnotes:hover::before {
  border-color: black;
}
.classnotes:active::before {
  background: -webkit-linear-gradient(top, #e3e3e3, #f9f9f9);
}
</style>
    <div class="row-fluid">
     
    <div class="span12">
        <h1>Apply Now !</h1 >


        </div>
    </div>

    <div class="row-fluid">
     
    <div class="span6">
        <form id="uploadimage" action="fileUpload.php" method="post" enctype="multipart/form-data">
   <input type="text" id="nameSeeker" name="nameSeeker" placeholder="Your name" value=""/><br />
            <input type="text" name="emailSeeker" id="emailSeeker" placeholder="Your email" value=""/><br />
            <input  type="text" id="hpSeeker" name="hpSeeker" placeholder="Your HP" value=""/><br />
            <input type="file" id="actual" name="classnotes" value="" hidden/><br />
             

            
   <p><input type="submit" name="Submit" value="Submit" id="realsub" hidden/></p>
</form><div class="classnotes"> </div><br/><div id="fileNama"></div><br/>   <input type="button" id="fakebtn" name="btn" class="btn-style" value="Submit" />

<br/><br/>
<div id='succ' hidden><div class="alert alert-success">
<strong>Awesome!</strong> We'll get back to you shortly.
</div></div>

        </div>
        <div class="span6 centered-text">

    <img src="images/biz.png" alt="" width="60%">


        </div>
    </div>
    

    <script type="text/javascript">
        
         $( '#uploadimage' ).submit( function( e ) 
    {
             e.preventDefault();
        $.ajax({
                  url: 'uploadFile.php',
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
        
        $('body').on('click', '.classnotes', function (e) {
        $('#actual').trigger('click');
            

        });
        
         $('body').on('click', '#fakebtn', function (e) {
        $('#realsub').trigger('click');
            

        });
        
        //http://stackoverflow.com/questions/2189615/how-to-get-file-name-when-user-select-a-file-via-input-type-file
        $('body').on('change', '#actual', function (e) {
               $('#fileNama').html($(this).val().replace(/.*[\/\\]/, ''));
        });
        
        
        
        
        
        
        
        
        
        
        
        
        

          
    </script>
    
</html>