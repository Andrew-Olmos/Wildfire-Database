from flask import render_template, url_for, flash, redirect, request, abort, Blueprint

products = Blueprint("products", __name__)


@products.route("/product/<string:asin>", methods=["GET", "POST"])
def product(asin):
    # Implement
    return render_template("product.html", product=product, title="Product")


@products.route("/user/product/<string:asin>", methods=["GET", "POST"])
def user_product(asin):
    # Implement
    return render_template("user_product.html", product=product, title="Product")