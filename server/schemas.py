from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models import Customer, Item, Review

class ReviewSchema(SQLAlchemySchema):
    class Meta:
        model = Review
        load_instance = True
        include_fk = False

    id = auto_field()
    comment = auto_field()
    customer = fields.Nested(lambda: CustomerSchema(exclude=("reviews", "items")), dump_only=True)
    item = fields.Nested(lambda: ItemSchema(exclude=("reviews", "customers")), dump_only=True)


class CustomerSchema(SQLAlchemySchema):
    class Meta:
        model = Customer
        load_instance = True
        include_fk = False

    id = auto_field()
    name = auto_field()
    reviews = fields.Nested(ReviewSchema, many=True, exclude=("customer", "item"), dump_only=True)
    items = fields.Nested(lambda: ItemSchema(exclude=("reviews", "customers")), many=True, dump_only=True)


class ItemSchema(SQLAlchemySchema):
    class Meta:
        model = Item
        load_instance = True
        include_fk = False

    id = auto_field()
    name = auto_field()
    price = auto_field()
    reviews = fields.Nested(ReviewSchema, many=True, exclude=("item", "customer"), dump_only=True)
    customers = fields.Nested(lambda: CustomerSchema(exclude=("items", "reviews")), many=True, dump_only=True)
