# DEPRECATED

In python>=3.6 and pyyaml>=5.1 this library is unnecessary and can be replaced
with the following code:

```python
import functools

import yaml

Loader = getattr(yaml, 'CSafeLoader', yaml.SafeLoader)
ordered_load = functools.partial(yaml.load, Loader=Loader)
Dumper = getattr(yaml, 'CSafeDumper', yaml.SafeDumper)
ordered_dump = functools.partial(yaml.dump, Dumper=Dumper, sort_keys=False)
```
___

[![Build Status](https://asottile.visualstudio.com/asottile/_apis/build/status/asottile.aspy.yaml?branchName=master)](https://asottile.visualstudio.com/asottile/_build/latest?definitionId=4&branchName=master)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/asottile/asottile/4/master.svg)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=4&branchName=master)

aspy.yaml
=========

Some extensions to pyyaml.

## Installation

`pip install aspy.yaml`

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
