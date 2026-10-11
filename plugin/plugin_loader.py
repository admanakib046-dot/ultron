import os
import importlib
import inspect

from plugin.plugin import Plugin


class PluginLoader:

    def load(self, services):

        plugins = []

        folder = os.path.dirname(__file__)

        for file in os.listdir(folder):

            if not file.endswith(".py"):
                continue

            if file.startswith("_"):
                continue

            if file in (
                "plugin.py",
                "plugin_loader.py",
                "plugin_manager.py",
            ):
                continue

            module_name = file[:-3]

            module = importlib.import_module(
                f"plugin.{module_name}"
            )

            for _, obj in inspect.getmembers(module):

                if inspect.isclass(obj):

                    if issubclass(obj, Plugin):

                        if obj is Plugin:
                            continue

                        plugins.append(
                            obj(services)
                        )

        return plugins