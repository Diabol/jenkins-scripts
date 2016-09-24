import requests
import sys
import collections

def main(args):
    #print args
    #print "Downloading json"
    r = requests.get('http://updates.jenkins-ci.org/update-center.actual.json')
    #print "Done"

    plugins = r.json()['plugins']
    plugin_list = []
    for arg in args:
        plugin = plugins[arg]
        plugin_list = plugin_list + get_dependencies(arg, plugins, plugin)

    plugin_version = compile_version(set(plugin_list), plugins)
    plugin_version = collections.OrderedDict(sorted(plugin_version.items()))

    for entry in plugin_version:
        print entry + ":" + plugin_version[entry]


def get_dependencies(name, plugins, plugin):
    dependencies = [name]
    for dependency in plugin['dependencies']:
        if not dependency['optional']:
            dependencies.append(dependency['name'])
            dependencies = dependencies + get_dependencies(name, plugins, plugins[dependency['name']])
    return dependencies


def compile_version(plugin_list, plugins):
    plugin_version = {}
    for plugin in plugin_list:
        plugin_version[plugin] = plugins[plugin]['version']
    return plugin_version


if __name__ == "__main__":
    main(sys.argv[1:])