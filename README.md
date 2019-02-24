[![Build Status](https://travis-ci.org/asottile/aspy.yaml.svg?branch=master)](https://travis-ci.org/asottile/aspy.yaml)
[![Coverage Status](https://img.shields.io/coveralls/asottile/aspy.yaml.svg?branch=master)](https://coveralls.io/r/asottile/aspy.yaml)
[![Build Status](https://asottile.visualstudio.com/asottile/_apis/build/status/asottile.aspy.yaml?branchName=master)](https://asottile.visualstudio.com/asottile/_build/latest?definitionId=4&branchName=master)

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
