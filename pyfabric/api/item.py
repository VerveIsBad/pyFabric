class ItemGroup:
	MISC = ItemGroup('MISC')

	def __init__(self, group: str = None):
		pass


class Settings:
	def __init__(self, group: ItemGroup = None, maxcount: int = None):
		if group is None: group = ItemGroup.MISC
		if maxcount is None: maxcount = 64


class Item:
	def __init__(self, settings: Settings):
		self.settings = settings

