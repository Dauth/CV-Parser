<?php

include 'db.php';

$gaSql['link'] = pg_connect(
    " host=".$gaSql['server'].
    " dbname=".$gaSql['db'].
    " user=".$gaSql['user'].
    " password=".$gaSql['password']
) or die('Could not connect: ' . pg_last_error());   

   	$id = $_POST["id"];


$select_query = sprintf("SELECT * FROM result WHERE result_job=%d",pg_escape_string(intval($id)));
$result = pg_query($gaSql['link'] , $select_query);

while ($row = pg_fetch_row($result)) 
{
    $row[1] = substr($row[1],1,strlen($row[1])-2);
    $ex = explode(",",$row[1]);
    foreach($ex as $i)
    {
        $select_query2 = sprintf("SELECT * FROM firstextract WHERE firstextract_id=%d",pg_escape_string(intval($i)));
$result2 = pg_query($gaSql['link'] , $select_query2);
        while ($row2 = pg_fetch_row($result2)) 
        {
       echo "<a class='loadQuestionLink' data-once='false' href='#myModal' data-pdf='".$row2[2]."'><li class='customStack'>".$row2[2]."</li></a>";
        }
    }
}
echo "<br/><br/>";
pg_close( $gaSql['link'] );

?>
