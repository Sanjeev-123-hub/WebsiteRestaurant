# Ex.07 Restaurant Website
## Date:18-10-2025

## AIM:
To develop a static Restaurant website to display the food items and services provided by them.

## DESIGN STEPS:

### Step 1:
Requirement collection.

### Step 2:
Creating the layout using HTML and CSS.

### Step 3:
Updating the sample content.

### Step 4:
Choose the appropriate style and color scheme.

### Step 5:
Validate the layout in various browsers.

### Step 6:
Validate the HTML code.

### Step 7:
Publish the website in the given URL.

## PROGRAM:
```
index.html:
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Little Lemon - Home</title>
  <link rel="stylesheet" href="{% static 'restaurantapp/index.css' %}">
</head>
<body>
  <header>
    <h1>LITTLE LEMON</h1>
    <nav>
      <ul>
        <li><a href="index.html" class="active">Home</a></li>
        <li><a href="menu.html">Menu</a></li>
        <li><a href="admin.html">Administration</a></li>
        <li><a href="contact.html">Contact Us</a></li>
      </ul>
    </nav>
  </header>

  <section class="banner">
    <h2 >30% Off This Weekend</h2>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse at congue massa.</p>
  </section>

  <section class="cards">
    <div class="card">
      <img src="{% static 'restaurantapp/rest1.jpg' %}" alt="New Menu">
      <h3>Our New Menu</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse at congue massa.</p>
    </div>

    <div class="card">
      <img src="{% static 'restaurantapp/rest2.jpg' %}" alt="Book a Table">
      <h3>Book a table</h3>
      <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse at congue massa.</p>
    </div>

    <div class="card">
      <img src="{% static 'restaurantapp/rest3.jpg' %}" alt="Opening Hours">
      <h3>Opening Hours</h3>
      <p>Mon - Fri: 2pm - 10pm<br>Sat: 2pm - 11pm<br>Sun: 2pm - 9pm</p>
    </div>
  </section>

  <footer>
    <p>Designed and Developed by <b>Sangeeth</b></p>
  </footer>
</body>
</html>

admin.html:
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Little Lemon - Administration</title>
  <link rel="stylesheet" href="{% static 'restaurantapp/admin.css' %}">
</head>
<body>
  <header>
    <h1>LITTLE LEMON</h1>
    <nav>
      <ul>
        <li><a href="index">Home</a></li>
        <li><a href="menu">Menu</a></li>
        <li><a href="admin" class="active">Administration</a></li>
        <li><a href="contact">Contact Us</a></li>
      </ul>
    </nav>
  </header>

  <section class="admin-section">
    <h2>Our Administration Team</h2>
    <div class="admin-grid">
      <div class="admin-card">
        <img src="{% static 'restaurantapp/image1.jpg' %}" alt="Admin 1">
        <h3>Mr. Arjun</h3>
        <p>Manager</p>
      </div>
      <div class="admin-card">
        <img src="{% static 'restaurantapp/images.jpg' %}" alt="Admin 2">
        <h3>Ms. Priya</h3>
        <p>Chef</p>
      </div>
      <div class="admin-card">
        <img src="{% static 'restaurantapp/image2.jpg' %}" alt="Admin 3">
        <h3>Mr. Rahul</h3>
        <p>Assistant Chef</p>
      </div>
      <div class="admin-card">
        <img src="{% static 'restaurantapp/image3.jpg' %}" alt="Admin 4">
        <h3>Ms. Kavya</h3>
        <p>Receptionist</p>
      </div>
      <div class="admin-card">
        <img src="{% static 'restaurantapp/images6.jpg' %}" alt="Admin 5">
        <h3>Mr. Manoj</h3>
        <p>Waiter</p>
      </div>
      <div class="admin-card">
        <img src="{% static 'restaurantapp/images5.jpg' %}" alt="Admin 6">
        <h3>Ms. Sneha</h3>
        <p>Cashier</p>
      </div>
    </div>
  </section>

  <footer>
    <p>Designed and Developed by <b>Sangeeth</b></p>
  </footer>
</body>
</html>

menu.html:
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Little Lemon - Menu</title>
  <link rel="stylesheet" href="{% static 'restaurantapp/menu.css' %}">
</head>
<body>
  <header>
    <h1>LITTLE LEMON</h1>
    <nav>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="menu.html" class="active">Menu</a></li>
        <li><a href="admin.html">Administration</a></li>
        <li><a href="contact.html">Contact Us</a></li>
      </ul>
    </nav>
  </header>

  <section class="menu-section">
    <h2>Our Delicious Menu</h2>
    <div class="menu-grid">
      <div class="item">Pizza</div>
      <div class="item">Burger</div>
      <div class="item">Pasta</div>
      <div class="item">Fried Rice</div>
      <div class="item">Noodles</div>
      <div class="item">Grilled Chicken</div>
      <div class="item">Sandwich</div>
      <div class="item">French Fries</div>
      <div class="item">Ice Cream</div>
      <div class="item">Milkshake</div>
      <div class="item">Juices</div>
      <div class="item">Cupcakes</div>
    </div>
  </section>

  <footer>
    <p>Designed and Developed by <b>Sangeeth</b></p>
  </footer>
</body>
</html>

contact.html:
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Little Lemon - Menu</title>
  <link rel="stylesheet" href="{% static 'restaurantapp/menu.css' %}">
</head>
<body>
  <header>
    <h1>LITTLE LEMON</h1>
    <nav>
      <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="menu.html" class="active">Menu</a></li>
        <li><a href="admin.html">Administration</a></li>
        <li><a href="contact.html">Contact Us</a></li>
      </ul>
    </nav>
  </header>

  <section class="menu-section">
    <h2>Our Delicious Menu</h2>
    <div class="menu-grid">
      <div class="item">Pizza</div>
      <div class="item">Burger</div>
      <div class="item">Pasta</div>
      <div class="item">Fried Rice</div>
      <div class="item">Noodles</div>
      <div class="item">Grilled Chicken</div>
      <div class="item">Sandwich</div>
      <div class="item">French Fries</div>
      <div class="item">Ice Cream</div>
      <div class="item">Milkshake</div>
      <div class="item">Juices</div>
      <div class="item">Cupcakes</div>
    </div>
  </section>

  <footer>
    <p>Designed and Developed by <b>Sangeeth</b></p>
  </footer>
</body>
</html>

report.html:
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Report - TastyBites</title>
  <link rel="stylesheet" href="{% static 'restaurantapp/style.css' %}">
</head>
<body>
  <header>
    <nav class="navbar">
      <h1 class="logo">TastyBites</h1>
      <ul class="nav-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="menu.html">Menu</a></li>
        <li><a href="admin.html">Administration</a></li>
        <li><a href="contact.html">Contact Us</a></li>
        <li><a href="report.html" class="active">Report</a></li>
      </ul>
    </nav>
  </header>

  <section class="report">
    <h2>Website Report</h2>
    <p><b>Color Scheme:</b> 
      - Banner & Navbar: Deep Red (#b71c1c)  
      - Text: White  
      - Background: Light Beige (#fff7f0)
    </p>
    <p>No external libraries or frameworks were used. All HTML & CSS are handwritten.</p>
  </section>

  <footer>
    <p>Designed by Sangeeth © 2025</p>
  </footer>
</body>
</html>

index.css:
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #fff7f2;
  color: #333;
}

header {
  text-align: center;
  background-color: #fff;
  padding: 10px 0;
}

header h1 {
  font-size: 28px;
  color: #2e4f46;
  letter-spacing: 2px;
}

nav ul {
  list-style: none;
  background-color: #3c3c3c;
  display: flex;
  justify-content: center;
  padding: 10px;
  margin: 0;
}

nav ul li {
  margin: 0 10px;
}

nav ul li a {
  text-decoration: none;
  color: white;
  font-weight: bold;
  padding: 6px 15px;
  border-radius: 5px;
}

nav ul li a:hover,
.active {
  background-color: #555;
}

.banner {
  background: url('./bg.jpg') no-repeat center center/cover;
  width: 100%;
  height: 120px;
  text-align: center;
  padding: 80px 20px;
  color: white;
}

.banner h2 {
  font-size: 32px;
  margin-bottom: 10px;
}

.cards {
  display: flex;
  justify-content: center;
  gap: 20px;
  padding: 30px;
}

.card {
  background: #fff3e0;
  width: 280px;
  border-radius: 10px;
  padding: 10px;
  text-align: center;
}

.card img {
  width: 100%;
  border-radius: 10px;
}

footer {
  text-align: center;
  padding: 10px;
  background-color: #fff;
  color: #3c3c3c;
  font-size: 14px;
}

admin.css:
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #fff7f2;
}

header {
  text-align: center;
  background-color: #fff;
  padding: 10px 0;
}

header h1 {
  color: #2e4f46;
  font-size: 28px;
}

nav ul {
  list-style: none;
  background-color: #3c3c3c;
  display: flex;
  justify-content: center;
  padding: 10px;
  margin: 0;
}

nav ul li {
  margin: 0 10px;
}

nav ul li a {
  text-decoration: none;
  color: white;
  font-weight: bold;
  padding: 6px 15px;
  border-radius: 5px;
}

nav ul li a:hover,
.active {
  background-color: #555;
}

.admin-section {
  text-align: center;
  padding: 30px;
}

.admin-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
}

.admin-card {
  background: #fff3e0;
  border-radius: 10px;
  width: 180px;
  padding: 10px;
  height: 550px;
  border: 1px solid #ddd;
}

.admin-card img {
  width: 100%;
  height: 500px;
  border-radius: 10px;
}

footer {
  text-align: center;
  padding: 10px;
  background-color: #fff;
  color: #3c3c3c;
}

menu.css:
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #fff7f2;
}

header {
  text-align: center;
  background-color: #fff;
  padding: 10px 0;
}

header h1 {
  color: #2e4f46;
  font-size: 28px;
}

nav ul {
  list-style: none;
  background-color: #3c3c3c;
  display: flex;
  justify-content: center;
  padding: 10px;
  margin: 0;
}

nav ul li {
  margin: 0 10px;
}

nav ul li a {
  text-decoration: none;
  color: white;
  font-weight: bold;
  padding: 6px 15px;
  border-radius: 5px;
}

nav ul li a:hover,
.active {
  background-color: #555;
}

.menu-section {
  text-align: center;
  padding: 30px;
}

.menu-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 20px;
  max-width: 800px;
  margin: auto;
}

.item {
  background: #fff3e0;
  padding: 20px;
  border-radius: 10px;
  border: 1px solid #ddd;
  font-weight: bold;
}

footer {
  text-align: center;
  padding: 10px;
  background-color: #fff;
  color: #3c3c3c;
}

contact.css:
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #fff7f2;
}

header {
  text-align: center;
  background-color: #fff;
  padding: 10px 0;
}

header h1 {
  color: #2e4f46;
  font-size: 28px;
}

nav ul {
  list-style: none;
  background-color: #3c3c3c;
  display: flex;
  justify-content: center;
  padding: 10px;
  margin: 0;
}

nav ul li {
  margin: 0 10px;
}

nav ul li a {
  text-decoration: none;
  color: white;
  font-weight: bold;
  padding: 6px 15px;
  border-radius: 5px;
}

nav ul li a:hover,
.active {
  background-color: #555;
}

.contact {
  text-align: center;
  padding: 40px;
  background: #fff3e0;
  margin: 40px auto;
  width: 60%;
  border-radius: 10px;
  border: 1px solid #ddd;
}

footer {
  text-align: center;
  padding: 10px;
  background-color: #fff;
  color: #3c3c3c;
}
```

## OUTPUT:
![alt text](<Screenshot 2025-10-21 160011.png>) ![alt text](<Screenshot 2025-10-21 160040.png>) ![alt text](<Screenshot 2025-10-21 160059.png>) ![alt text](<Screenshot 2025-10-21 160123.png>) ![alt text](<Screenshot 2025-10-21 161214.png>)

## RESULT:
The program for designing software company website using HTML and CSS is completed successfully.
