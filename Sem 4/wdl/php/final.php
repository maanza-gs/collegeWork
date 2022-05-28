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

<?php
    echo("<h3>Your Cart</h3>");
    $sql = "SELECT pname, qty, price FROM cart";
    $result = mysqli_query($conn, $sql);
    if (mysqli_num_rows($result) > 0) {
        while($row = mysqli_fetch_assoc($result)) {
          echo "Product name: " . $row['pname']. "<br> Price: $" . $row['price']. "<br>Quantity " . $row['qty' ]. "<br>Total: $".$row['price']*$row['qty']."<br><br><br>";
        }
      }

    echo("<h3>Billing Address</h3>");
    $sql = "SELECT * FROM customer";
    $result = mysqli_query($conn, $sql);
    if (mysqli_num_rows($result) > 0) {
        while($row = mysqli_fetch_assoc($result)) {
          echo "First name: " . $row['fname']."&nbsp&nbspLast name: " . $row['lname']."<br> Address Line 1: " . $row['addl1']. "<br>Address Line 2 " . $row['addl2' ]. "<br>Phone Number: " . $row['phno']."<br><br><br>";
        }
      }
?>