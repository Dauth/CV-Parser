<?php
$item='example';
$result = exec('python CreateNewJob.py '.$item.'');

echo $result;

?>