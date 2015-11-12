<?php

header('Content-Type: text/html; charset=UTF-8');

?>

<html>
<style type="text/css">

    .outer {
        color: white;
            display: inline-block;
                        margin-bottom: 3px;

            margin-left: 3px;
                        margin-right: 3px;

            padding-top: 1px;
            padding-bottom: 1px;
            padding-left: 7px;
                        padding-right: 7px;
border-radius: 3px;
    border: 1px solid #2c3e50;
            background-color: #2c3e50;
        }
    
        .inner {
            display: inline-block;
                        margin: 3px;


            padding-top: 1px;
            padding-bottom: 1px;
            padding-left: 7px;
                        padding-right: 7px;
border-radius: 3px;
    border: 1px solid #ecf0f1;
            background-color: #ecf0f1;
        }

</style>
        <!-- Modal -->
    <div id="myModal">
        <div class="close-myModal popClose" style="cursor:pointer;float:right;color:white;font-size:200%;padding:20px;"> 
            <i class="fa fa-times"></i>
        </div>
        <div class="modal-content" style="padding:20px;">
            
            
        <div class="row-fluid text-left">
        <div class="span12 text-center">
              <div id="resultContent"></div>  
            </div>
        </div>
        </div></div>
    
    <div class="row-fluid">
     
    <div class="span12">
        <h1>Job Listings</h1 >


        </div>
    </div>

    <div class="row-fluid">
     
    <div class="span6">
        
        <div id="loadQuestions">
<ul>
    
</ul>
<br/>
</div>
        
        </div>
        <div class="span6">
<div id="loadParsed" style="font-size:110%">
            </div>


        </div>
    </div>
    <hr/>
    <div class="row-fluid">
     
    <div class="span12">
        
        <div id="listResumes">
            

</div>
        
        </div>
    </div>
      

    <script type="text/javascript">
                 $('#myModal').hide();

        $.ajax({    //create an ajax request to load_page.php
	        type: "POST",
	        url: "loadJobServer.php",
	        //data: "htmldata="+ s,  //with the page number as a parameter
	        dataType: "html",   //expect html to be returned
	        success: function(msg){

	            if(parseInt(msg)!=0)    //if no errors
	            {
	            	$("#loadQuestions").html(msg).hide().fadeIn('2000');
	                //$('.mainBody').html(msg).hide().fadeIn('2000');    //load the returned html into pageContet
	                //$('#loading').css('visibility','hidden');   //and hide the rotating gif
	            }
	        },
	        error: function()
	        {
	            alert('error');
	        }

    	});
        
        $('body').on('click', '.loadQuestionLink2', function (e) {
             e.preventDefault();
             
              document.body.style.overflow = "hidden";
    
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
             
              $('#resultContent').html("<iframe style='body{margin: 0;}' src=data/"+$(this).attr('data-opena')+".pdf?#zoom=100' type='application/pdf' width=850 height='100%'<param name='view'/></iframe>");

            
        });
        
        $('body').on('click', '.resBtn', function (e) {
             e.preventDefault();
             
              document.body.style.overflow = "hidden";
    
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
             
              $('#resultContent').html("<iframe style='body{margin: 0;}' src=data/"+$(this).attr('data-opena')+".pdf?#zoom=100' type='application/pdf' width=850 height='100%'<param name='view'/></iframe>");

            
        });
        
        $('body').on('click', '.ressecBtn', function (e) {
            
            
               $.ajax({    //create an ajax request to load_page.php
	        type: "POST",
	        url: "loadResult.php",
	        data: "job="+ $(this).attr('data-toSearch'),  //with the page number as a parameter
	        dataType: "html",   //expect html to be returned
	        success: function(msg){

	            if(parseInt(msg)!=0)    //if no errors
	            {
	            	$("#listResumes").html(msg).hide().fadeIn('2000');
	            }
	        },
	        error: function()
	        {
	            alert('error');
	        }

    	});

            
        });
        
         $('body').on('click', '.loadQuestionLink', function (e) {
             jQuery('.loadQuestionLink').each(function() {
                 $(this).children().css("background-color","#ffffff");
});
             $(this).children().css("background-color","#f1c40f");
             
             e.preventDefault();
             var a = $(this).attr('data-count');
             var b = JSON.parse(a);
             var str = " <button href='#listResumes' class='ressecBtn btn btn-large btn-primary' + data-toSearch='" + $(this).attr('href') + "' type='button'>View Matching Resumes</button><hr/>" ;
             var str = str + " <button data-once='false' href='#myModal' class='resBtn btn btn-large btn-primary' + data-opena='" + $(this).attr('href') + "' type='button'>View Job</button><hr/>" ;
             
             str = str + "<h4>Location</h4>";
             

             str = str + "<div class='inner'>" +  b.location.json.address + "</div>" + " "; 
             
             str = str + "<h4>Education</h4>"; 
             
             Object.keys(b.education).forEach(function (key) {
    var vala = b.education[key];
                 str = str + "<p><div class='outer'>" + key + "</div></p>"; 
});
             str = str + "<h4>Experience</h4>"; 
             
             for(j=0;j<b.experience.length;j++)
             {
                 if(b.experience[j]["workDuration"]==null)
                 {
                     str = str + "<div class='outer'>" + b.experience[j]["workPositionOrExp"] + "</div> - ";
                 }
                 else
                 {
                 str = str + "<div class='outer'>" + b.experience[j]["workPositionOrExp"] + "</div><div class='inner'>" +  b.experience[j]["workDuration"] + "</div> - ";
                 }
             }
             str = str + "<h4>Skill(s)</h4>"; 
             
             Object.keys(b.skillSet["py/set"]).forEach(function (key) {
    var vala = b.skillSet["py/set"][key];
                 str = str + "<div class='inner'>" + vala + "</div>" + " "; 
});
             str = str + "<h4>Important Keyword(s)</h4>"; 
             
             Object.keys(b.importantKeywords).forEach(function (key) {
    var vala = b.importantKeywords[key];
                 str = str + "<div class='inner'>" + vala + "</div>" + " "; 
});
             str = str + "<h4>Language(s)</h4>"; 
             
             Object.keys(b.language).forEach(function (key) {
    var vala = b.language[key];
                 str = str + "<div class='inner'>" + vala + "</div>" + " "; 
});
            $("#loadParsed").html(str).hide().fadeIn('2000');

        });
        
        
        
        
        
        
        
        
        
        
        
        
        

          
    </script>
    
</html>