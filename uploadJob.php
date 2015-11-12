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


          if ($content)
          {
              $result = move_uploaded_file($_FILES['classnotes']['tmp_name'], "data/$name.pdf");



                exec('pdftotext.exe data/'.$name.'.pdf -table');
                exec('python garyconvert.py "'.$name.'"');




echo $name;
        $contentName = $name;
              $name = $_POST['nameJob'];
              echo $name;
              $keyword = $_POST['keyword'];
              $keyword = str_replace(",", "\n", $keyword);
              $myfile = fopen("2.txt", "w") or die("Unable to open file!");
fwrite($myfile, $keyword);
fclose($myfile);

                exec('python garyconvertKeyword.py');

              echo $keyword;
              exec('python CreateNewJob.py "'.$name.'" "'.$contentName.'" "'.$keyword.'"');
              echo "this is from php";
              echo json_encode($mainJSON);



              echo json_encode($mainJSON);

                echo pg_last_error();

          }
              
         
   } #endIF
   }
?>


