from . import orders, order_details, recipes, dishes, resources, customers

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    dishes.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    customers.Base.metadata.create_all(engine)
