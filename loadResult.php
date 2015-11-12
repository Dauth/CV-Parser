<?php

ini_set('max_execution_time', 300);

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
}

$uniqueArray = array();
$majorFiltered = array();

foreach($major as $key) 
{
    if (in_array($key[0], $uniqueArray)) 
    {
        
    }
    else
    {
        array_push($majorFiltered,$key);
        array_push($uniqueArray,$key[0]);
    }    
}

usort($majorFiltered, 'sortByOrder');
$retta = array();
$counta = 1;
foreach($majorFiltered as $key) {

    $matchedKeyWords = array();
    $select_query3= sprintf("SELECT * FROM matchbox");
    $result3 = pg_query($gaSql['link'] , $select_query3);
    
    while ($row3 = pg_fetch_row($result3))
    {
        $js = json_decode($row3[0],true);
        if($js['job']['contentId']===$jobInQn)
        {
            for($y=0;$y<count($js['matches']['py/set']);$y++)
            {
                if($js['matches']['py/set'][$y]['resume']['contentId']==$key[0])
                {

                    for($z=0;$z<count($js['matches']['py/set'][$y]['matchedKeywords']);$z++)
                    {
                       array_push($matchedKeyWords,$js['matches']['py/set'][$y]['matchedKeywords'][$z]);
                    }
                }
            }
        }
    }
    
    $matchedKeyWords = array_unique($matchedKeyWords);
    
    $select_query2 = sprintf("SELECT * FROM resume WHERE resume_contentname='%s'",pg_escape_string($key[0]));
    $result2 = pg_query($gaSql['link'] , $select_query2);

    while ($row2 = pg_fetch_row($result2)) 
    {
          echo "<a class='loadQuestionLink2' data-once='false' href='#myModal' data-opena='".$row2[2]."'><li class='customStack'><h2>".$counta.". ".$row2[3]."</h2><h4><div style='float-right'>Score : ".$key[1]."</div></h4>";
        echo "<div><h4>Matching Keywords</h4>";
          for($w=0;$w<count($matchedKeyWords);$w++)
          {
                echo "<div class='outer'>".$matchedKeyWords[$w]."</div>";
          }
        echo "</div>";
          echo "</li></a>";
    }
    $counta = $counta+1;
    array_push($retta,$key[0]);
}

pg_close( $gaSql['link'] );

?>
