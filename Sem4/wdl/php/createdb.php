<?php
$servername = '10.1.67.156';
$username = "msc20pw19";
$password = "msc20pw";
$db = "msc20pw19";
$conn = mysqli_connect($servername, $username, $password, $db);
if(!$conn)
{
    echo("Connection failed. Try again later");
}

$query = 'create table carts(pname varchar(50) primary key, price int, qty int);';
$result = mysqli_query($conn, $squery);
?>

