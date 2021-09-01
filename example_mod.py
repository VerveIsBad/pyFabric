from pyfabric import api


class ExampleMod(api.Mod):
	POTATO = api.item.Item(api.item.Settings(group = api.item.group.MISC, maxcount = 1))

	def initialize():
		api.registry.register(api.registry.ITEM, api.util.Identifier("example_mod", "potato"), POTATO)


mod = ExampleMod()
mod.compile_self(output_dir = './example_mod/')
