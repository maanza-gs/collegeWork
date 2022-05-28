<?php
$servername = '10.1.67.156';
$username = "msc20pw19";
$password = "msc20pw";
$db = "msc20pw19";

$conn = mysqli_connect($servername, $username, $password, $db);

if ($conn === false) {
    die("Connection failed: " . mysqli_connect_error());
  }

//$name = $_REQUEST['pname'];
//$price = $_REQUEST['price'];
//$qty = $_REQUEST['qty'];
 
//$sql = "INSERT INTO CART(pname, qty, price) VALUES('$name',$qty,$price);";
$query = 'insert into cart values("'.$_POST['pname'].'", "'.$_POST['qty'].'", "'.$_POST['qty'].'");';
$result = mysqli_query($conn, $squery);
header("Location: cart.php");

?>