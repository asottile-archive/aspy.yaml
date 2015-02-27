[![Build Status](https://travis-ci.org/asottile/aspy.yaml.svg?branch=master)](https://travis-ci.org/asottile/aspy.yaml)
[![Coverage Status](https://img.shields.io/coveralls/asottile/aspy.yaml.svg?branch=master)](https://coveralls.io/r/asottile/aspy.yaml)
[![Build status](https://ci.appveyor.com/api/projects/status/8ta4jqydro93c61u/branch/master?svg=true)](https://ci.appveyor.com/project/asottile/aspy/branch/master)

aspy.yaml
==========

Some extensions to pyyaml.


### aspy.yaml.ordered_load

yaml.load which respects order for dictionaries in the yaml file.

```python
>>> from aspy.yaml import ordered_load
>>> ordered_load(
        'foo: bar\n'
        'bar: baz\n'
        'herp: derp\n'
    )
OrderedDict([('foo', 'bar'), ('bar', 'baz'), ('herp', 'derp')])
```

### aspy.yaml.ordered_dump

yaml.dump which respects order for dictionaries in the yaml file.

```python
>>> from aspy.yaml import ordered_dump
>>> print(ordered_dump(
        OrderedDict((('a', '1'), ('b', '2'), ('c', '3'), ('d', '4'))),
        default_flow_style=False,
    ))
a: '1'
b: '2'
c: '3'
d: '4'
```
