from __future__ import print_function, division

from collections import Iterable

from functools import partial
from operator import attrgetter

from nose.tools import assert_equal, assert_true

import numpy as np
from pandas import DataFrame
from ..metadatadataframe import MetadataDataFrame

def load_dump(obj):
    from cPickle import dumps, loads
    return loads(dumps(obj))

def assert_attr_equal(attr):
    lift_attr = partial(map, attrgetter(attr))

    def attr_assert(*a):
        assert(len(a) == 2)
        if isinstance(lift_attr(a)[0], Iterable):
            assert_true(np.all(np.equal(*lift_attr(a))))
        else:
            assert_equal(*lift_attr(a))
    attr_assert.func_name = 'assert_{}_equal'.format(attr)

    return attr_assert

all_attr_asserts = map(
    assert_attr_equal,
    [
        'values',
        'columns',
        'index',
        'metadata',
        'name',
    ]
)

try:
    from watty.utils.iterator import map_apply
except:
    map_apply = lambda fs, *args, **kwargs: [f(*args, **kwargs) for f in fs]

def assert_all_attr_equal(*a):
    assert(len(a) == 2)
    map_apply(all_attr_asserts, *a)

class test_MetadataDataFrame_pickling(object):
    def setup(self):
        self.mdf = MetadataDataFrame(
            data=np.arange(16),
            index=None,
            columns=['col'],
            metadata=12,
            dtype=np.int64,
            copy=False,
        )

    def test_id_test(self):
        assert_all_attr_equal(
            self.mdf,
            self.mdf
        )
    def test_dump_load(self):
        assert_all_attr_equal(
            self.mdf,
            load_dump(self.mdf)
        )
