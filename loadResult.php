<?php

include 'db.php';

$gaSql['link'] = pg_connect(
    " host=".$gaSql['server'].
    " dbname=".$gaSql['db'].
    " user=".$gaSql['user'].
    " password=".$gaSql['password']
) or die('Could not connect: ' . pg_last_error());   

error_reporting(E_ERROR | E_PARSE);

$jobInQn = $_POST['job'];
$select_query = sprintf("SELECT * FROM resulttwo",pg_escape_string(1));
$result = pg_query($gaSql['link'] , $select_query);

function sortByOrder($a, $b) {
    return -($a[1] - $b[1]);
}


if (!$result) 
{
  echo "An error occurred.\n";
  exit;
}
$major = array();
while ($row = pg_fetch_row($result)) 
{
    $a = json_decode($row[0]);
    foreach($a as $key => $val) {
         if($key==$jobInQn)
         {
             $major = array_merge($major,$val);
         }// This will show jsut the value f each key like "var1" will print 9
                       // And then goes print 16,16,8 ...
    }
    
  //echo "<a class='loadQuestionLink' href='".$row[2]."' data-count='".$row[0]."'><li class='customStack'>".$row[3]."</li></a>";
}
//echo count($major);
usort($major, 'sortByOrder');
$retta = array();
$counta = 1;
foreach($major as $key) {
    $select_query2 = sprintf("SELECT * FROM resume WHERE resume_contentname='%s'",pg_escape_string($key[0]));
    $result2 = pg_query($gaSql['link'] , $select_query2);

    while ($row2 = pg_fetch_row($result2)) 
    {
          echo "<a class='loadQuestionLink2' data-once='false' href='#myModal' data-opena='".$row2[2]."'><li class='customStack'>".$counta.". ".$row2[3]."<div style='float-right'>Score : ".$key[1]."</div></li></a>";

    }
    $counta = $counta+1;
    array_push($retta,$key[0]);
}
pg_close( $gaSql['link'] );

?>
