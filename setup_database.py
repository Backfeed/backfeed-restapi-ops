#!/usr/bin/python2.7
import sys
import os

from backfeed_protocol import utils

if len(sys.argv) <= 1:
    raise Exception('You need to provide a filename')

sqlite_db = sys.argv[1]

print 'setting up database',sqlite_db
utils.setup_database(sqlite_db)
