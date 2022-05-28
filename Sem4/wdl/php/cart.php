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
    <head>
        <style>
            *{
                margin: 10px;
                padding: 10px;
                font-family:'Arial', 'sans-serif';
            }

            .container{
                display: flex;
            }

            .products{
                display: flex;
            }

            .product{
                display: block;
                padding: 0;
            }

            .product img{
                width: 150px;
                height: 150px;
            }

            .products label{
                padding: 0;
            }
        </style>
    </head>
    <body>
        <div class=container>
            <div class="container1">
                <h3>Milk</h3>
                <div class="products">
                    <div class="product">
                        <img src="./images/Organic Milk.jpg">
                        <div class="labels">
                            <p>Whole Milk <br>$2.79</p>
                        </div>
                        <form action="addtocart.php" method="post">
                            <input type="hidden" name="pname" value="Whole Milk">
                            <input type="hidden" name="price" value="$2.79">
                            <input type="radio" name="qty">1
                            <input type="radio" name="qty">2
                            <input type="radio" name="qty">3
                            <input type="radio" name="qty">4
                            <input type="radio" name="qty">5<br>
                            <button type="submit" name="submit">Add to Cart</button>
                        </form>
                    </div>
                    <div class="product">
                        <img src="./images/Oat Milk.jpg">
                        <div class="labels">
                            <p>Oat Milk <br>$2.79</p>
                        </div>
                        <form action="addtocart.php"  method="post">
                            <input type="hidden" name="pname" value="Oat Milk">
                            <input type="hidden" name="price" value="$2.79">
                            <input type="radio" name="qty">1
                            <input type="radio" name="qty">2
                            <input type="radio" name="qty">3
                            <input type="radio" name="qty">4
                            <input type="radio" name="qty">5<br>
                            <button type="submit" name="submit">Add to Cart</button>
                        </form>
                    </div>
                    <div class="product">
                        <img src="./images/Skim Milk.jpg">
                        <div class="labels">
                            <p>Skim Milk <br>$2.79</p>
                        </div>
                        <form action="addtocart.php"  method="post">
                            <input type="hidden" name="pname" value="Skim Milk">
                            <input type="hidden" name="price" value="$2.79">
                            <input type="radio" name="qty">1
                            <input type="radio" name="qty">2
                            <input type="radio" name="qty">3
                            <input type="radio" name="qty">4
                            <input type="radio" name="qty">5<br>
                            <button type="submit" name="submit">Add to Cart</button>
                        </form>
                    </div>
                </div>

                <form action="contacts.php">
                    <button type="submit" name="submit">Next</button>
                </form>
            </div>
            <div class = "container2">
                <h3>Your Cart</h3>
                <?php
                    $sql = "SELECT pname, qty, price FROM cart";
                    $result = mysqli_query($conn, $sql);
                    if (mysqli_num_rows($result) > 0) {
                        while($row = mysqli_fetch_assoc($result)) {
                          echo "Product name: " . $row['pname']. "<br> Price: " . $row['price']. "<br>Quantity " . $row['qty' ]. "<br><br><br>";
                        }
                      } else {
                        echo '<p>Your Cart is Empty</p>';
                      }
                ?>
            </div>
        </div>
    </body>
</html>