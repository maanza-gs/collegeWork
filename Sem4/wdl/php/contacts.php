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
?>

<html>
    <body>
        <form action="bill.php">
            Enter First Name: <input type="text" name="fname">&nbsp&nbsp&nbsp&nbsp
            Enter Last Name: <input type="text" name="lname"><br><br>
            Enter Address Line 1: <input type="text" name="addl1"><br><br>
            Enter Address Line 2: <input type="text" name="addl2"><br><br>
            Enter Phone Number: <input type="text" name="phno"><br><br>
            <button type="submit" name="submit">Next</button>
        </form>

        <form action="cart.php">
            <button type="submit">Back</button>
        </form>
    </body>        
</html>