# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst

from __future__ import (absolute_import, division, print_function)


class Suite:

    def named_method(self):
        return 0

    named_method.benchmark_name = 'custom.track_method'


def named_function(self):
    pass


named_function.benchmark_name = 'custom.time_function'
named_function.pretty_name = 'My Custom Function'


def track_custom_pretty_name(self):
    return 42


track_custom_pretty_name.pretty_name = 'this.is/the.answer'
