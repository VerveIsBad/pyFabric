class Identifier:
	def __init__(self, mod: str, name: str = None):
		if name is None:
			self.identifier = mod
		else:
			self.identifier = mod + ':' + name
