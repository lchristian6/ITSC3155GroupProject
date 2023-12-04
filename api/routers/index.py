from . import (orders, order_details, customers, payments, reviews, resourceManagement,
               Promotion, pizzas)


def load_routes(app):
    app.include_router(customers.router)
    app.include_router(reviews.router)
    app.include_router(payments.router)
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(resourceManagement.router)
    app.include_router(Promotion.router)
    app.include_router(pizzas.router)


