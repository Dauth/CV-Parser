<?php

include '../vendor/autoload.php';
include 'db.php';

 $gaSql['link'] = pg_connect(
        " host=".$gaSql['server'].
        " dbname=".$gaSql['db'].
        " user=".$gaSql['user'].
        " password=".$gaSql['password']
    ) or die('Could not connect: ' . pg_last_error());   


   	

  $batches = array();
              
              $select_query = sprintf("SELECT firstextract_id FROM firstextract WHERE firstextract_isprocessed = '%s'",pg_escape_string('f'));
   	$select = pg_query($gaSql['link'] , $select_query);


while ($row = pg_fetch_row($select)) 
    {
     
          array_push($batches, $row[0]);
      }
    
echo json_encode($batches);


                
                echo pg_last_error();
              
          
              
         

?>


