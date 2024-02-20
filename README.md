# Django E-Commerce API

## Overview

This is a Django-based backend API project serves as the foundation for a basic e-commerce platform. It provides RESTful API endpoints for managing products and cart items.

## Features

- **Product Management**: Retrieve all product details, as well as a specific.
- **Cart Management**: Add products to the shopping cart, view cart items, and remove items from the cart.

## Setup

1. **Clone the Repository**: `git clone [git@github.com:Pro-Ace-grammer/E-commerce_API.git]`
2. **Install Dependencies**: `pip install -r requirements.txt`
3. **Run Migrations**: `python manage.py makemigrations`,`python manage.py migrate`
4. **Start the Development Server**: `python manage.py runserver`

## API Endpoints

- **GET /products**: Retrieve a list of all products.
- **GET /products/<id>**: Retrieve details of a specific product.
- **POST /cart**: Add a product to the cart.
- **GET /cart**: Retrieve cart items.
- **DELETE /cart/<id>**: Remove a specific item from the cart.

## Technologies Used

- Django
- Django Rest Framework
- SQLite

## Folder Structure

- **/products**: Contains Django app for API endpoints.
- **/media**: Directory for storing uploaded product images.


## Acknowledgements

Special thanks to [karkhana.io](https://www.karkhana.io) for providing me with the opportunity to work on this assignment.