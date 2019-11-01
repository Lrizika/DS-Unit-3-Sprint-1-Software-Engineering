#!/usr/bin/env python

import unittest
import io
import sys
from acme import Product
from acme_report import generate_products, inventory_report, ADJECTIVES, NOUNS


def cap_stdout(func: callable, *args, **kwargs) -> str:
	"""
	Capture stdout for a function

	Args:
		func (callable): Function to call

	Returns:
		str: Captured output
	"""

	capture = io.StringIO()
	sys.stdout = capture  # Catch output to stdout
	func(*args, **kwargs)  # Call the function
	sys.stdout = sys.__stdout__  # Release output to stdout
	return(capture.getvalue())  # Return any captured output


class AcmeProductTests(unittest.TestCase):
	"""Making sure Acme products are the tops!"""
	def test_default_product_price(self):
		"""Test default product price being 10."""
		prod = Product('Test Product')
		self.assertEqual(prod.price, 10)

	def test_default_product_weight(self):
		"""Test default product weight being 10."""
		prod = Product('Test Product')
		self.assertEqual(prod.weight, 20)

	def test_constructed_product_funcs(self):
		"""Test a product having correct method results."""
		prod = Product('Test Product', price=2, weight=300, flammability=0.1)
		self.assertEqual(prod.stealability(), 'Not so stealable...')
		self.assertEqual(prod.explode(), '...boom!')


class AcmeReportTests(unittest.TestCase):
	"""Making sure Acme reports are the tops!"""
	def test_default_num_products(self):
		"""Test default product list being of length 30."""
		prods = generate_products()
		self.assertEqual(len(prods), 30)

	def test_legal_names(self):
		"""Test default product list containing legal names."""
		prods = generate_products()
		for prod in prods:
			words = prod.name.split(' ')
			self.assertEqual(len(words), 2)
			self.assertIn(words[0], ADJECTIVES)
			self.assertIn(words[1], NOUNS)

	def test_report(self):
		"""Test a product report having correct output."""
		prods = [Product('Test the First'),
				Product('Test the Second')]
		report = cap_stdout(inventory_report, prods)
		expected_report = """
ACME CORPORATION OFFICIAL INVENTORY REPORT
Unique product names: 2
Average price: 10.0
Average weight: 20.0
Average flammability: 0.5

"""
		self.assertEqual(report, expected_report)


if __name__ == '__main__':
	unittest.main()

