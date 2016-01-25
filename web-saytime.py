#!/usr/bin/env python3
# datetime.py by Bill Weinman <http://bw.org/contact/>
# Copyright (c) 2010 The BearHeart Group, LLC
# CGI/SSI version for bw.org
#

import time, saytime, serb

t = time.localtime()
#returns time struct object

print("Content-type: text/html\n")
print(
    "U Batajnici, sada je priblizno " +
    saytime.saytime_t(t).words() +
    ", na " +
    serb.day() +
    str(t.tm_mday) + "og " +
    serb.mth() +
    time.strftime(' %Y. godine.')
)


