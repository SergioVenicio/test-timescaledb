from itertools import product
from datetime import datetime
from random import choice
import psycopg2

from models.models import Product, Timeline
from repositories.product import ProductRepository
from repositories.timeline import TimelineRepository


ACTIONS = [
    'CREATE',
    'UPDATE',
    'DELETE',
    'REQUEST_UPDATE',
    'REQUEST_DELETE',
]
CONNECTION = "postgres://psql:password@127.0.0.1:5432/product_timeline"

psql_conn = psycopg2.connect(CONNECTION)

product_repository = ProductRepository(psql_conn)
timeline_repository = TimelineRepository(psql_conn)

product = Product(id=None, description='test', org='test')
product.id = product_repository.insert_row(product)
for _ in range(100000):
    action = choice(ACTIONS)
    timeline = Timeline(time=datetime.now(), product_id=product.id, action=action)
    timeline_repository.insert_row(timeline)
