<?php

include '../vendor/autoload.php';
include 'db.php';

 $gaSql['link'] = pg_connect(
        " host=".$gaSql['server'].
        " dbname=".$gaSql['db'].
        " user=".$gaSql['user'].
        " password=".$gaSql['password']
    ) or die('Could not connect: ' . pg_last_error());   


   	

   if (is_uploaded_file($_FILES['classnotes']['tmp_name'])) {

      if ($_FILES['classnotes']['type'] != "application/pdf") {
         echo "<p>Class notes must be uploaded in PDF format.</p>";
      } else {
          
            $content = file_get_contents($_FILES['classnotes']['tmp_name']);

          if ($content) {
			
              $mainJSON = array();
              $mainString = "";
              
			foreach ($pages as $page) {
                $mainString = $mainString." ".$page->getText();
                
                  
                

			}
              
              array_push($mainJSON,$mainString);
              
           
                
                $contentName = uniqid();
               $name = "Jobssfodummies";
              $keyWords = "vava";
              
              
              $result = exec('python CreateNewJob.py '.$name.' '.$contentName.' '.$keyWords.' '.json_encode($mainJSON));

                echo pg_last_error();
              
              echo $mainString;
          }
              
         
      } #endIF
   } #endIF

?>


