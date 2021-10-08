from flask import Flask
import views

app = Flask(__name__)

app.add_url_rule('/index', view_func=views.index)

app.add_url_rule('/orders_list', view_func=views.orders_list)

app.add_url_rule('/cars_list', view_func=views.cars_list)

app.add_url_rule('/new_order', view_func=views.new_order)

app.add_url_rule('/new_car', view_func=views.new_car)

app.add_url_rule('/create_order', view_func=views.create_order)

app.add_url_rule('/create_car', view_func=views.create_car)

if __name__ == '__main__':
  app.run(debug=True) 