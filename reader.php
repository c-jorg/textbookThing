
<html>
	<head>
		<script src='script.js'></script>
	</head>
	<p>csv file location</p>
	<input type='text' id='file'>
	<br/><br/>
	<p>starting at line</p>
	<input type='text' id='start'>
	<p>order of columns you want use same name as next input seperate by spaces</p>
	<input type='text' id='outputOrder'>
	<br/><br/>
	<p>order  of columns in the csv file add all columns in csv seperate by spaces</p>
	<input type='text' id='inputOrder'>
	<br/><br/>
	<input type='button' value='submit' id='submit' onclick='readCsv()'>
	<br/><br/>
	
	<div id='output'></div>
</html>

