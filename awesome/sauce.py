# -*- coding: utf8 -*-

import random
import sys


class Cherry(object):

    def random(self):
        return random.randint(1, 1000)
        ## Fail on py26
        if sys.version_info.minor == 6:
            raise Exception()
