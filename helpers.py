import click

import click
import sqlite3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define SQLAlchemy model for products
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String)

# Initialize SQLite database
engine = create_engine('sqlite:///e_commerce.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

@click.group()
def cli():
    """E-Commerce CLI for managing products and orders."""
    pass

@cli.command()
@click.argument('name')
@click.argument('price', type=int)
@click.option('--description', default='', help='Product description')
def add_product(name, price, description):
    """Add a new product to the catalog."""
    product = Product(name=name, price=price, description=description)
    session.add(product)
    session.commit()
    click.echo(f"Product '{name}' added successfully!")

@cli.command()
def list_products():
    """List all available products."""
    products = session.query(Product).all()
    for product in products:
        click.echo(f"{product.id}: {product.name} (${product.price})")

# Add more commands for other features (shopping cart, orders, etc.)

if __name__ == '__main__':
    cli()



def exit_program():
    print("Goodbye!")
    exit()


def get_input(prompt):
    return input(prompt)


# @click.group()
# def cli():
#     """E-commerce CLI tool."""
#     pass

# @cli.command()
# @click.argument('product_id')
# @click.argument('quantity', type=int)
# def add_to_cart(product_id, quantity):
#     """Add items to the cart."""
#     # Implement logic to add product_id with specified quantity to the cart
#     click.echo(f"Added {quantity} units of product {product_id} to the cart.")

# @cli.command()
# @click.argument('product_id')
# @click.argument('new_quantity', type=int)
# def update_quantity(product_id, new_quantity):
#     """Update quantities in the cart."""
#     # Implement logic to update product_id with new_quantity in the cart
#     click.echo(f"Updated quantity of product {product_id} to {new_quantity}.")

# @cli.command()
# def calculate_total():
#     """Calculate total price."""
#     # Implement logic to calculate total price based on cart contents
#     total_price = 42.0  # Replace with actual calculation
#     click.echo(f"Total price: ${total_price:.2f}")

# if __name__ == "__main__":
#     cli()
