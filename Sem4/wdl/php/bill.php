<?php
$servername = '10.1.67.156';
$username = "msc20pw19";
$password = "msc20pw";
$db = "msc20pw19";
$conn = mysqli_connect($servername, $username, $password, $db);

if ($conn === false) {
    die("Connection failed: " . mysqli_connect_error());
  }
    $fname = $_REQUEST['fname'];
    $lname = $_REQUEST['lname'];
    $addl1 = $_REQUEST['addl1'];
    $addl2 = $_REQUEST['addl2'];
    $phno = $_REQUEST['phno'];
 
    $sql = "INSERT INTO CART CUSTOMER('$fname','$lname', '$addl1', '$addl2', '$phno');";
    $result = mysqli_query($conn, $sql);
    header("Location: final.php");
?>