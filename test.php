<?php
$test = "something";
$test2 = "";
$string = !empty($test) ? 'its not empty,' : "NULL,";
$string .= !empty($test2) ? "its not empty," : "NULL,";
echo $string;
?>