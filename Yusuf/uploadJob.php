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

          $mainString = "Page1Praveen Deorani
Research Scholar at National University of Singapore
Experience
Research Scholar at National University of Singapore
January 2011 - Present (4 years 10 months)
Research Associate at Indian Institute of Technology, Kanpur
May 2010 - October 2010 (6 months)
PublicationsRole of spin mixing conductance in spin pumping: Enhancement of spin pumping efficiency in Ta/Cu/Py
structures
Applied Physics Letters November 18, 2013
Authors: Praveen Deorani, Hyunsoo Yang
Nonreciprocity engineering in magnetostatic spin waves
Current Applied Physics March 14, 2014
Authors: Praveen Deorani, Jae Hyun Kwon, Hyunsoo Yang
Observation of inverse spin Hall effect in bismuth selenide
Physical Review B September 3, 2014
Authors: Praveen Deorani, Jaesung Son, Karan Banerjee, Nikesh Koirala, Matthew Brahlek, Seongshik Oh,
Hyunsoo Yang
Angular and temperature dependence of current induced spin-orbit effective fields in Ta/CoFeB/MgO
nanowires
Scientific Reports March 12, 2014
Authors: Xuepeng Qiu, Praveen Deorani, Kulothunga sagaran, Ki-Seung Lee, Kyung-Jin Lee, Hyun-Woo Lee,
Hyunsoo Yang
Investigation of the temperature-dependence of ferromagnetic resonance and spin waves in CoFeAlSi
Applied Physics Letters June 2, 2014
Authors: Li Ming Loong, Jae Hyun Kwon, Praveen Deorani, Chris Nga Tung Yu, Atsufumi Hirohata, Hyunsoo
Yang
Attenuation characteristics of spin-pumping signal due to traveling spin waves
Physical Review B March 12, 2012
Authors: Praveen Deorani, Sankha Subhra Mujherjee, Jae Hyun Kwon, Hyunsoo Yang
Characterization of magnetostatic surface spin waves in magnetic thin films: evaluation for
microelectronic applications
Applied Physics A January 19, 2013
Authors: Jae Hyun Kwon, Sankha Subhra Mukherjee, Praveen Deorani, Masamitsu Hayashi, Hyunsoo Yang";
          if ($content) 
          {
              $result = move_uploaded_file($_FILES['classnotes']['tmp_name'], "data/$name.pdf");
              
              $docObj = new Filetotext("data/$name.pdf");
            //  $mainString = $docObj->convertToText();
			
              $mainJSON = array();
              
            
              
              array_push($mainJSON,$mainString);
              
         
              
echo $name;
        $contentName = $name;
              $name = $_POST['nameJob'];
              echo $name;
              $keyword = $_POST['keyword'];

              exec('python CreateNewJob.py "'.$name.'" "'.$contentName.'" "'.$keyword.'" '.json_encode($mainJSON));
              
              echo json_encode($mainJSON);
              
                echo pg_last_error();
              
          }
              
         
   } #endIF
   }
?>


