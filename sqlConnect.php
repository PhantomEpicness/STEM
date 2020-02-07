 <?php
$servername = "localhost";
$username = "school";
$password = "password";
$dbname = "school";
//require 'errorHandler.php';
// Create connection
$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$sql = "SELECT * FROM students";
$result = mysqli_query($conn, $sql);
echo $sql;
if (mysqli_num_rows($result) > 0) {
    // output data of each row
    while($row = mysqli_fetch_assoc($result)) {
        echo $row;
            while($row = mysqli_fetch_array($result)){
                echo $row;
                echo $results;
                echo $table;
            }
    }
} else {
    echo "0 results";
}

mysqli_close($conn);
?>
