#!/usr/bin/env python

from random import randint


class Product:
	"""
	An acme Product
	"""

	def __init__(self,
				name: str,
				price: int = 10,
				weight: int = 20,
				flammability: float = 0.5):
		"""
		Creates a new Product

		Args:
			name (str): Name of the Product
			price (int, optional): Defaults to 10.
			weight (int, optional): Defaults to 20.
			flammability (float, optional): Defaults to 0.5.
		"""

		self.identifier = randint(1000000, 9999999)
		self.name = name
		self.price = price
		self.weight = weight
		self.flammability = flammability

	def stealability(self) -> str:
		"""
		Calculates the stealability of the Product

		Returns:
			str: The stealability of the Product
		"""

		sab = self.price / self.weight
		if sab < .5:
			return('Not so stealable...')
		elif sab < 1:
			return('Kinda stealable.')
		else:
			return('Very stealable!')

	def explode(self) -> str:
		"""
		Explodes the Product

		Returns:
			str: The result of the explosion
		"""

		volatility = self.flammability * self.weight
		if volatility < 10:
			return('...fizzle.')
		elif volatility < 50:
			return('...boom!')
		else:
			return('...BABOOM!!')


class BoxingGlove(Product):
	"""
	An acme Boxing Glove
	"""

	def __init__(self, 
				name: str, 
				price: int = 10,
				weight: int = 10,
				flammability: float = 0.5):

		super().__init__(name=name,
						price=price,
						weight=weight,
						flammability=flammability)

	def explode(self) -> str:
		"""
		Explodes the BoxingGlove

		Returns:
			str: The result of the explosion
		"""

		return('...it\'s a glove.')

	def punch(self) -> str:
		"""
		Punches with the BoxingGlove

		Returns:
			str: The result of the punch
		"""

		if self.weight < 5:
			return('That tickles.')
		elif self.weight < 15:
			return('Hey that hurt!')
		else:
			return('OUCH!')



