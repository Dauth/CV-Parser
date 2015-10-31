<?php

if(!$_POST['page'])
{
	if(file_exists('overview.php'))
	{
		echo file_get_contents('overview.php');
	}
}

$page = $_POST['page'];

if(file_exists(substr($page,1,strlen($page)).'.php'))
echo file_get_contents(substr($page,1,strlen($page)).'.php');

?>
