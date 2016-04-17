import sys
import os

from restapi import protocol;

if __name__ == '__main__':
	sqlite_db = sys.argv[1]
	if not os.path.exists(sqlite_db):
		protocol.setup_database(sqlite_db)
