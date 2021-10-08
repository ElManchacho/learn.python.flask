import random
from flask import render_template, request
import json

orders = './json/orders.json'
cars = './json/cars.json'

def index():
     return render_template('index.php')

def orders_list():
    return render_template('orders_list.php')

def cars_list():
    return render_template('cars_list.php')

def new_order():
    return render_template('new_order.php')

def new_car():
    return render_template('new_car.php')

