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
          
          $name  = uniqid(true);

            $content = file_get_contents($_FILES['classnotes']['tmp_name']);

          if ($content) {
			$parser = new \Smalot\PdfParser\Parser();
			$pdf    = $parser->parseContent($content);
			$pages  = $pdf->getPages();
			
              $mainJSON = array();
              $mainString = "";
              
			foreach ($pages as $page) {
                $mainString = $mainString." ".$page->getText();
                
                  
                

			}
              
              array_push($mainJSON,$mainString);
              
         $result = move_uploaded_file($_FILES['classnotes']['tmp_name'], "uploads/$name.pdf");
              

                  
                  //http://stackoverflow.com/questions/14047979/executing-python-script-in-php-and-exchanging-data-between-the-two
                  //Asked by : Neta Meta, http://stackoverflow.com/users/1589336/neta-meta
                  //Edited by : Lee Taylor, http://stackoverflow.com/users/933198/lee-taylor
                  //Answered by : Tom van der Woerdt, http://stackoverflow.com/users/377037/tom-van-der-woerdt
                  
                  // This is the data you want to pass to Python
        $contentName = $name;
              $name = 'Omar';
              $hp = '3333';
              $email = 'aaada@fsdfsdf.com';
              
              
              $result = exec('python CreateNewResume.py '.$name.' '.$hp.' '.$email.' '.$contentName.' '.json_encode($mainJSON));

// Decode the result
$resultData = json_decode($result, true);

// This will contain: array('status' => 'Yes!')
var_dump($resultData);
              
                echo pg_last_error();
              
              echo $mainString;
          }
              
         
      } #endIF
   } #endIF

?>


