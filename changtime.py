#! /usr/bin/env python
#coding=utf-8

import time

print "CST",time.strftime("%Y-%m-%d %A %X %Z", time.localtime())

print "UTC",time.strftime("%Y-%m-%d %A %X %Z", time.gmtime())

from datetime import datetime
import pytz

tz_est = pytz.timezone('US/Eastern')
tz_us = pytz.timezone('America/Los_Angeles')
dt_est = datetime.now(tz_est)
dt_us = datetime.now(tz_us)
print dt_est.tzinfo,dt_est
print dt_us.tzinfo,dt_us
