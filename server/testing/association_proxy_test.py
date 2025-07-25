from app import app
from models import *

def test_has_association_proxy(test_client):
    '''has association proxy to items'''
    c = Customer(name='Test Customer')
    i = Item(name='Test Item', price=9.99)
    db.session.add_all([c, i])
    db.session.commit()

    r = Review(comment='great!', customer=c, item=i)
    db.session.add(r)
    db.session.commit()

    assert hasattr(c, 'items')
    assert i in c.items
