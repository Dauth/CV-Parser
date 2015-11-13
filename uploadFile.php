<?php

ini_set('max_execution_time', 300);

include 'db.php';
require("class.filetotext.php");




 $gaSql['link'] = pg_connect(
        " host=".$gaSql['server'].
        " dbname=".$gaSql['db'].
        " user=".$gaSql['user'].
        " password=".$gaSql['password']
    ) or die('Could not connect: ' . pg_last_error());   


   	
   if (is_uploaded_file($_FILES['classnotes']['tmp_name'])) {

      if ($_FILES['classnotes']['type'] != "application/pdf") {
          
      } else {
          
          $name  = uniqid(true);

            $content = file_get_contents($_FILES['classnotes']['tmp_name']);

          if ($content) 
          {
              $result = move_uploaded_file($_FILES['classnotes']['tmp_name'], "data/$name.pdf");
            

			exec('pdftotext.exe data/'.$name.'.pdf -table');
                exec('python garyconvert.py "'.$name.'"');

          
              
            
              
             
              
         
              

        $contentName = $name;
              $name = $_POST['nameSeeker'];
              $hp = $_POST['hpSeeker'];
              $email = $_POST['emailSeeker'];

              echo exec('python CreateNewResume.py "'.$name.'" "'.$hp.'" "'.$email.'" "'.$contentName.'"');
            
              echo pg_last_error();
              
          }
              
         
   } #endIF
   }
?>


