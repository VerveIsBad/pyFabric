from . import util
from . import item


to_register = []


def register(register_key: str, identifier, util.Identifier, item: item.Item):
	to_register.append({
		'key': register_key,
		'id': identifier,
		'item': item
	})
