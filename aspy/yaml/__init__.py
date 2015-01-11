from __future__ import absolute_import
from __future__ import unicode_literals

import yaml

from aspy.yaml.ordereddict import OrderedDict

# Adapted from http://stackoverflow.com/a/21912744/812183


class OrderedLoader(yaml.loader.Loader):
    pass


OrderedLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    lambda loader, node: OrderedDict(loader.construct_pairs(node)),
)


class OrderedDumper(yaml.dumper.SafeDumper):
    pass


OrderedDumper.add_representer(
    OrderedDict,
    lambda dumper, data: dumper.represent_mapping(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        data.items(),
    ),
)


def ordered_load(stream):
    """yaml.load which respects order for dictionaries in the yaml file.

    :param stream: string or streamlike object.
    """
    return yaml.load(stream, Loader=OrderedLoader)


def ordered_dump(obj, **kwargs):
    """yaml.dump which respects order for dictionaries in the yaml object.

    :param obj: Yaml dumpable object
    """
    return yaml.dump(obj, Dumper=OrderedDumper, **kwargs)
