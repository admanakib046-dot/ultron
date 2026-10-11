import importlib
import pkgutil
import plugin


class PluginManager:

    def __init__(self):
        self.plugins = {}

    # ----------------------------
    # Register Plugin
    # ----------------------------

    def register(self, plugin):
        self.plugins[plugin.name()] = plugin

    # ----------------------------
    # Execute Plugin
    # ----------------------------

    def execute(self, name, intent):

        plugin = self.plugins.get(name)

        if plugin is None:
            return f"Plugin '{name}' not found."

        return plugin.execute(intent)

    # ----------------------------
    # Plugin List
    # ----------------------------

    def list_plugins(self):

        info = []

        for plugin in self.plugins.values():

            status = "Enabled"

            if hasattr(plugin, "enabled") and not plugin.enabled():
                status = "Disabled"

            version = plugin.version() if hasattr(plugin, "version") else "1.0"
            author = plugin.author() if hasattr(plugin, "author") else "Ultron"
            description = (
                plugin.description()
                if hasattr(plugin, "description")
                else ""
            )

            info.append(
                f"""
{plugin.name()}
 Version : {version}
 Author  : {author}
 Status  : {status}
 {description}
"""
            )

        return info

    # ----------------------------
    # Auto Load Plugins
    # ----------------------------

    def load_plugins(self, services):

        for _, module_name, _ in pkgutil.iter_modules(plugin.__path__):

            if not module_name.endswith("_plugin"):
                continue

            module = importlib.import_module(
                f"plugin.{module_name}"
            )

            for obj in module.__dict__.values():

                if isinstance(obj, type):

                    if obj.__name__.endswith("Plugin"):

                        if obj.__name__ == "Plugin":
                            continue

                        instance = obj(services)

                        self.register(instance)