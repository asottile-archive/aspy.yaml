from __future__ import absolute_import
from __future__ import unicode_literals

import sys

import aspy.yaml
import pytest


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


def test_ordered_load_merge():
    ret = aspy.yaml.ordered_load(
        'a: &b\n'
        '  c: d\n'
        '  e: f\n'
        'g:\n'
        '  <<: *b\n'
        '  h: i\n'
    )
    assert list(ret['a'].items()) == [('c', 'd'), ('e', 'f')]
    assert list(ret['g'].items()) == [('c', 'd'), ('e', 'f'), ('h', 'i')]


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


@pytest.mark.xfail(sys.version_info < (3, 6), reason='py36+')
def test_ordered_dump_plain_dict_py36_plus():
    ret = aspy.yaml.ordered_dump({'z': 1, 'a': 2, 'c': 3, 'b': 4, 'd': -1})
    assert ret == (
        'z: 1\n'
        'a: 2\n'
        'c: 3\n'
        'b: 4\n'
        'd: -1\n'
    )
