<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Ensure file is uploaded
    if (!isset($_FILES['csv_file']) || $_FILES['csv_file']['error'] != 0) {
        die("Error uploading file.");
    }
    
    $file = $_FILES['csv_file']['tmp_name'];
    
    // Get headers from user input
    //$inputHeaders = explode(',', trim($_POST['input_headers']));
    //$outputHeaders = explode(',', trim($_POST['output_headers']));
    //$tableName = trim($_POST['table_name']);
    $lineSkip = trim($_POST['line_skip']);
    $dateHeaders = array("Date_ID","Date","Year");
    $featureHeaders = array("Feature_ID","Number_bars","Number_Points","Number_Lines","Number_Atoms","Number_Axes","Axes_Limits");
    $imageHeaders = array("Image_ID","Image_Name","File_Size_KB","Pixel_Width","Pixel_Height","Book_Title","ISBN","IEEE_Ref","Subject_name","Diagram_Type","Black_White");
    $factHeaders = array("Image_ID","Feature_ID","Date_id","Image","Page");
    
    // Check if input and output headers match in length
//     if (count($inputHeaders) !== count($outputHeaders)) {
//         die("Error: Input headers and output headers must have the same number of elements.");
//     }
    
    // Read the CSV file
    $handle = fopen($file, 'r');
    if (!$handle) {
        die("Error opening the CSV file.");
    }
    $read = fread($handle, filesize($file));
    $lines = explode("\n", $read); 
    //this array has every line of the thing in it
    $count = 0;
    $outputText = "";
    $inputHeaders = "";
    //echo sizeof($lines) . "\n";
   // echo $lines[0],"\n".$lines[1]."\n".$lines[2]."\n";
    foreach($lines as $line){
        //echo "first line of foreach statement\n";
        $elements = "";
        $elements = explode(",",$line);
        $dateInsert = "";
        $featureInsert = "";
        $imageInsert = "";
        $factInsert = "";
        if($count == 0){
            $inputHeaders = $elements;
        }
        if($count >= $lineSkip){
            //turning the row into an associative array
            //$values[] = NULL;
            $values[] = array_combine($inputHeaders, $elements);
            //echo print_r($values[0]) . '\n';
            //echo print_r($values[1]) . '\n';
            

            //making the date insert statements
//             echo print_r($inputHeaders);
//             echo "\n";
//             echo print_r($elements);
//             echo "<br>";
//             echo print_r($values);
//             echo "<br/><br>";
//             echo ($values[0]['key']);
            $dateInsert = 'INSERT INTO "DimDate" ("Date_ID", "Date", "Year") VALUES (';
            //$dateInsert .= $elements['key'] . ",";
            //echo $count;
            $dateInsert .= $values[$count-1]['key'] . ",";
            $dateInsert .= '"' . $values[$count-1]['Date'] .'"' . ",";
            $date = explode("-", $values[$count-1]['Date']);
            $dateInsert .= $date[$count-1] . ");";
            
            //making the image insert statements
            $imageInsert = 'INSERT INTO "DimImage" ("Image_ID","Image_Name","File_Size_KB","Pixel_Width","Pixel_Height","Book_Title","ISBN","IEEE_Ref","Subject_Name","Diagram_Type","Black_White") VALUES (';
            $imageInsert .= !empty($values[$count-1]['key']) ? $values[$count-1]['key'] . "," : 'NULL,';
            $imageInsert .= !empty($values[$count-1]['Image_Name']) ? '"' . $values[$count-1]['Image_Name'] .'"' . "," : "NULL,";
            $imageInsert .= !empty($values[$count-1]['File_Size_KB']) ? $values[$count-1]['File_Size_KB'] . "," : "NULL,";
            $imageInsert .= !empty($values[$count-1]['Pixel_Width']) ? $values[$count-1]['Pixel_Width'] . "," : "NULL,";
            $imageInsert .= !empty($values[$count-1]['Pixel_Height']) ? $values[$count-1]['Pixel_Height'] . "," : "NULL,";
            $imageInsert .= !empty($values[$count-1]['Book_Title']) ? '"' . $values[$count-1]['Book_Title'] . '"' . "," : "NULL,";
            $imageInsert .= !empty($values[$count-1]['ISBN']) ? '"' . $values[$count-1]['ISBN'] .'"' . "," : 'NULL,';
            $imageInsert .= !empty($values[$count-1]['IEEE_Ref']) ? '"' . $values[$count-1]['IEEE_Ref'] . '"' . "," : 'NULL,';
            $imageInsert .= !empty($values[$count-1]['Subject_Name']) ? '"' . $values[$count-1]['Subject_Name'] .'"' . "," : 'NULL,';
            $imageInsert .= !empty($values[$count-1]['Diagram_Type']) ? '"' . $values[$count-1]['Diagram_Type'] .'"' . "," : "NULL,";
            $imageInsert .= !empty($values[$count-1]['Black_White']) ? $values[$count-1]['Black_White'] == 'TRUE' ? '1)' : '0);' : "NULL);";
            
            //making the features insert statement
            $featureInsert = 'INSERT INTO "DimFeartures" ("Feature_ID","Number_Bars","Number_Points","Number_Lines","Number_Atoms","Axes_limits") VALUES (';
            $featureInsert .= !empty($values[$count-1]['key']) ? $values[$count-1]['key'] . "," : 'NULL,';
            $featureInsert .= !empty($values[$count-1]['Number_Bars']) ? $values[$count-1]['Number_Bars'] . "," : 'NULL,';
            $featureInsert .= !empty($values[$count-1]['Number_Points']) ? $values[$count-1]['Number_Points'] . "," : 'NULL,';
            $featureInsert .= !empty($values[$count-1]['Number_Lines']) ? $values[$count-1]['Number_Lines'] . "," : 'NULL,';
            $featureInsert .= !empty($values[$count-1]['Number_Atoms']) ? $values[$count-1]['Number_Atoms'] . "," : 'NULL,';
            $featureInsert .= !empty($values[$count-1]['Number_Axes_Limits']) ? $values[$count-1]['Number_Axes_Limits'] . "," : 'NULL);';
            
            //making the fact table insert
            $factInsert = 'INSERT INTO "FactDiagram" ("Image_ID","Feature_ID","Date_ID","Image","Page") VALUES (';
            $factInsert .= !empty($values[$count-1]['key']) ? $values[$count-1]['key'] . "," : 'NULL,';
            $factInsert .= !empty($values[$count-1]['key']) ? $values[$count-1]['key'] . "," : 'NULL,';
            $factInsert .= !empty($values[$count-1]['key']) ? $values[$count-1]['key'] . "," : 'NULL,';
            $factInsert .= !empty($values[$count-1]['Image']) ? $values[$count-1]['Image'] . "," : 'NULL,';
            $factInsert .= !empty($values[$count-1]['Page']) ? $values[$count-1]['Page'] . "," : 'NULL);';
            
            $outputText .= $dateInsert . "\n" . $imageInsert ."\n". $featureInsert ."\n". $factInsert ."\n";
        }
        $count++;
    }
    echo $outputText;
    
    //$inputHeaders = explode(",", $lines);
    
    // Get the first row as the actual headers in the CSV if requested
//     if($inputHeaders.equals("BLANK")){
//         $csvHeaders = fgetcsv($handle);
//         if (!$csvHeaders) {
//             die("Error: CSV file is empty or headers are not valid.");
//         }
//     }
    
    // Ensure all input headers exist in the CSV file
//     $headerMap = array_flip($csvHeaders); // Map header names to their index
//     foreach ($inputHeaders as $header) {
//         if (!isset($headerMap[$header])) {
//             die("Error: Input header '$header' not found in the CSV file.");
//         }
//     }
    
    // Begin building SQL statements
//     $sqlStatements = "";
//     $count = 0;
//     while ($row = fgetcsv($handle)){
//         if($count <= $lineSkip){
//             $values = [];
//         }
//         $count++;
//     }
    
    //echo $dateHeaders + "\n" + $featureHeaders + "\n" + $imageHeaders + "\n" + $factHeaders;
//     while (($row = fgetcsv($handle)) !== false) {
//         $values = [];
        
//         // Map input headers to output headers and collect values
//         foreach ($inputHeaders as $i => $inputHeader) {
//             $value = trim($row[$headerMap[$inputHeader]]);
//             $values[] = ($value === '') ? 'NULL' : "'" . pg_escape_string($value) . "'";
//         }
        
//         // Generate the SQL insert statement
//         $sql = "INSERT INTO $tableName (" . implode(', ', $outputHeaders) . ") VALUES (" . implode(', ', $values) . ");";
//         $sqlStatements[] = $sql;
//     }
    
    fclose($handle);
    
    // Output the SQL statements
    header('Content-Type: text/plain');
//     foreach ($sqlStatements as $statement) {
//         echo $statement . "\n";
//     }
} else {
    echo "Invalid request method.";
}
?>
