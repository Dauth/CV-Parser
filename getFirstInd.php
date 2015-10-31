<?php

include 'vendor/autoload.php';
include 'db.php';

 $gaSql['link'] = pg_connect(
        " host=".$gaSql['server'].
        " dbname=".$gaSql['db'].
        " user=".$gaSql['user'].
        " password=".$gaSql['password']
    ) or die('Could not connect: ' . pg_last_error());   


   	$id = htmlspecialchars($_GET["id"]);

  $batches = array();
              
              $select_query = sprintf("SELECT firstextract_data FROM firstextract WHERE firstextract_id = '%s'",pg_escape_string($id));
   	$select = pg_query($gaSql['link'] , $select_query);


while ($row = pg_fetch_row($select)) 
    {
     
         echo $row[0];
      }
    

                
                echo pg_last_error();
              
          
              
         

?>


