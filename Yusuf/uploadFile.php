<?php

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

          $mainString = "f";
          if ($content) 
          {
              $result = move_uploaded_file($_FILES['classnotes']['tmp_name'], "data/$name.pdf");
              
              $docObj = new Filetotext("data/$name.pdf");
              $mainString = $docObj->convertToText();
			
              $mainJSON = array();
              
            
              
              array_push($mainJSON,$mainString);
              
         
              

        $contentName = $name;
              $name = $_POST['nameSeeker'];
              $hp = $_POST['hpSeeker'];
              $email = $_POST['emailSeeker'];

              echo exec('python CreateNewResume.py "'.$name.'" "'.$hp.'" "'.$email.'" "'.$contentName.'" '.json_encode($mainJSON));
              echo "this is from php";
              echo json_encode($mainJSON);
              $myfile = fopen("1.json", "w");
              fwrite($myfile, json_encode($mainJSON));
              fclose($myfile);
                echo pg_last_error();
              
              echo $mainString;
          }
              
         
   } #endIF
   }
?>


