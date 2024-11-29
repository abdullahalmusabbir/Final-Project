<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create User</title>
    <link rel="stylesheet" href="{% static 'css/create_seller.css' %}">
</head>
<body>
    <header>
        <div class="header-left">
            <h1>FuaaRI</h1>
        </div>
        <nav>
            <ul>
                {% if user.is_authenticated %}
                    Welcome, {{ user.username }}!
                    <a href={% url 'product_list' %}>Products</a>
                    <a href="{% url 'signout' %}">Log Out</a>
                {% else %}
                <a href={% url 'product_list' %}>Products</a>
                    <a href="{% url 'login' %}">Log In</a>
                {% endif %}
            </ul>
        </nav>
    </header>
    <form method="post">
        {% csrf_token %}
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="phone_number">Phone Number:</label>
        <input type="text" id="phone_number" name="phone_number" required>
        <br>
        <label for="is_seller">Register as Seller:</label>
        <input type="checkbox" id="is_seller" name="is_seller" onclick="toggleSellerForm()">
        <br>
        <div id="sellerFields" style="display: none;">
            <label for="business_name">Business Name:</label>
            <input type="text" id="business_name" name="business_name">
            <br>
            <label for="business_location">Business Location:</label>
            <textarea id="business_location" name="business_location"></textarea>
            <br>
            <label for="NID">NID:</label>
            <input type="text" id="NID" name="NID">
        </div>
        <br>
        <button type="submit">Create User</button>
    </form>

    <footer>
        <p>&copy; 2024 D&M IT</p>
    </footer>

    <script>
    function toggleSellerForm() {
        const isSeller = document.getElementById('is_seller').checked;
        const sellerFields = document.getElementById('sellerFields');
        sellerFields.style.display = isSeller ? 'block' : 'none';
    }
    </script>    
</body>
</html>
