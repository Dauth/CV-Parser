<?php

include 'db.php';

$gaSql['link'] = pg_connect(
    " host=".$gaSql['server'].
    " dbname=".$gaSql['db'].
    " user=".$gaSql['user'].
    " password=".$gaSql['password']
) or die('Could not connect: ' . pg_last_error());   

$select_query = sprintf("SELECT * FROM resume",pg_escape_string(1));
$result = pg_query($gaSql['link'] , $select_query);

if (!$result) 
{
  echo "An error occurred.\n";
  exit;
}

while ($row = pg_fetch_row($result)) 
{
        $row[0] = str_replace("'"," ",$row[0]);

  echo "<a class='loadQuestionLink' href='".$row[2]."' data-count='".$row[0]."'><li class='customStack'>".$row[3]."</li></a>";
}
echo "<br/><br/>";
pg_close( $gaSql['link'] );

?>
