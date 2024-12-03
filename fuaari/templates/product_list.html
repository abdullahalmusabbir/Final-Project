<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product List</title>
    <link rel="stylesheet" href="{% static 'css/list.css' %}"> <!-- Link to your CSS -->
</head>
<body>
    <header>
        <div class="header-left">
            <h1>FuaaRI</h1>
        </div>
        <nav class="header-right">
            <ul>
                {% if user.is_authenticated %}
                    Welcome, {{ user.username }}!
                    {% if user.seller %}
                        <a href="{% url 'deshboard' %}">Dashboard</a>
                    {% endif %}
                    <a href="{% url 'signout' %}">Log Out</a>
                {% else %}
                    <a href="{% url 'login' %}">Log In</a>
                    <a href="{% url 'signup' %}">Sign Up</a>
                {% endif %}
            </ul>
        </nav>
    </header> 
    <form method="get" action="{% url 'product_list' %}">
        <input type="text" name="q" placeholder="Search for products..." value="{{ request.GET.q }}">
        <button type="submit">Search</button>
    </form>

    <!-- Filtering options -->
    <aside class="filter-sidebar">
        <h3>Filter by Category</h3>
            {% for category in categories %}
                <a href="{% url 'product_list' %}?category={{ category }}">{{ category }}</a>
            {% endfor %}
    </aside>


    <ul>
        {% for a in products %}
            <li>
                <img src="{{ a.images.url }}" width="200"> <br>
                {{ a.name }}<br>
                {{ a.description }}<br>
                {{ a.price }}<br>
                {% if user.is_authenticated %}
                    <a href="{% url 'create_order' a.id user.id %}">Order</a>
                    <a href="{% url 'create_reviews' a.id user.id %}">Reviews</a>
                {% else %}
                    <p>Login to Order or Review</p>
                {% endif %}
            </li>
        {% endfor %}
    </ul>

    <footer>
        <p>&copy; 2024 D&M IT</p>
    </footer>
</body>
</html>
