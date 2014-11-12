# -*- coding=utf-8 -*-

"""
About database.mongo
    This module contains all the APIs about MongoDB.
     
Description of classes
    MongoDB:

Description of methods
    create_database: Create a Mongo database, also it's not necessary.

"""

__authors__ = [
    '"Hugo Ding" <huicong.ding@spirent.com>',
	]

__version__ = "V0.1"

__all__ = []

# ChangeLog:
# Version   Date         Description                                   Author
# ------------------------------------------------------------------------------
# V0.1      2014-10-31   First version                                 Hugo
# ------------------------------------------------------------------------------

import pymongo


class MongoDB(object):
    def __init__(self):
        self._db_host = "localhost"
        self._port = 27017

    def create_database(self, db_name):
        client = pymongo.MongoClient(self._db_host, self._port)
        exec("client.%s" % db_name)

if __name__ == "__main__":
    pass