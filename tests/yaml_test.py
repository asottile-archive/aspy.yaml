from __future__ import absolute_import
from __future__ import unicode_literals

import aspy.yaml


def test_ordered_load():
    ret = aspy.yaml.ordered_load(
        'a: herp\n'
        'c: derp\n'
        'd: darp\n'
        'b: harp\n'
    )
    # Original behavior
    assert ret == {'a': 'herp', 'b': 'harp', 'c': 'derp', 'd': 'darp'}
    # Ordered behavior
    assert (
        list(ret.items()) ==
        [('a', 'herp'), ('c', 'derp'), ('d', 'darp'), ('b', 'harp')]
    )


def test_ordered_dump():
    ret = aspy.yaml.ordered_dump(
        aspy.yaml.OrderedDict(
            (('a', 'herp'), ('c', 'derp'), ('b', 'harp'), ('d', 'darp'))
        ),
        default_flow_style=False,
        indent=4,
    )
    assert ret == (
        'a: herp\n'
        'c: derp\n'
        'b: harp\n'
        'd: darp\n'
    )
