#!/usr/bin/env python

from acme import Product
from random import randint, choice, random


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_product() -> Product:
	"""
	Generates a random acme.Product
	
	Returns:
		Product
	"""

	name = f'{choice(ADJECTIVES)} {choice(NOUNS)}'
	price = randint(5, 100)
	weight = randint(5, 100)
	flammability = random() * 2.5

	return(Product(	name=name,
					price=price,
					weight=weight,
					flammability=flammability))


def generate_products(count: int = 30) -> list:
	"""
	Generates a list of random acme.Product instances

	Args:
		count (int, optional): Number of Products to generate. Defaults to 30.
	
	Returns:
		list: List of Products
	"""

	products = [generate_product() for i in range(count)]
	return(products)


def inventory_report(products: list) -> None:
	"""
	Prints a report on a list of Products
	
	Args:
		products (list): List of Products to report on
	"""

	names = set()
	prices = []
	weights = []
	flammabilities = []
	for product in products:
		names |= {product.name}
		prices.append(product.price)
		weights.append(product.weight)
		flammabilities.append(product.flammability)

	uniques = len(names)
	avg_price = sum(prices)/len(prices)
	avg_weight = sum(weights)/len(weights)
	avg_flammability = sum(flammabilities)/len(flammabilities)
	print(f"""
ACME CORPORATION OFFICIAL INVENTORY REPORT
Unique product names: {uniques}
Average price: {avg_price:.4}
Average weight: {avg_weight:.4}
Average flammability: {avg_flammability:.6}
""")


if __name__ == '__main__':
    inventory_report(generate_products())
