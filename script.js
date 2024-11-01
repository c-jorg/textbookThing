function readCsv(){
	var csvFileLocation = document.getElementById('file');
	var startingLine = document.getElementById('start');
	var outputOrder = document.getElementById('outputOrder');
	var inputOrder = document.getElementById('inputOrder');
	var xmlhttp = new XMLHttpRequest();
	
	xmlhttp.onreadystatechange = function() {
		if(xmlhttp.readyState == 4 && xmlhttp.status == 200){
			document.getElementById('output').innerHTML = xmlhttp.responseText;
		}else {
			document.getElementById('output').innerHTML = "Error ocurred.";
		}
	}
	
	xmlhttp.open('GET', 'readCsv.php?csvFileLocation='+csvFileLocation+'&startingLine='+startingLine+'&outputOrder='+outputOrder+'&inputOrder='+inputOrder, true);
	xmlhttp.send();
}