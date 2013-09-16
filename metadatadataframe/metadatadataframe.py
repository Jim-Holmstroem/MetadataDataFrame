from __future__ import print_function, division

import numpy as np
from pandas import DataFrame

class MetadataDataFrame(DataFrame):
    def __init__(
        self,
        data=None,
        index=None,
        columns=None,
        metadata=None,
        name=None,
        dtype=None,
        copy=False
    ):
        super(MetadataDataFrame, self).__init__(
            data=data,
            index=index,
            columns=columns,
            dtype=dtype,
            copy=copy,
        )
        self.metadata = metadata
        self.name = name

    def __reduce__(self):
        return self.__class__, (
            DataFrame(self),  # NOTE Using that type(data)==DataFrame and the
                              # the rest of the arguments of DataFrame.__init__
                              # to defaults, the constructors acts as a
                              # copy constructor.
            None,
            None,
            self.metadata,
            self.name,
            None,
            False,
        )
