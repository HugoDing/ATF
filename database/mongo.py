# -*- coding=utf-8 -*-

"""
About database.mongo
    This module contains all the APIs about MongoDB.
     
Description of classes
    MongoDB:
        Methods to operate MongoDB

Description of methods
    _get_database: Get a Mongo database

"""

__authors__ = [
    '"Hugo Ding" <huicong.ding@spirent.com>',
]

__version__ = "V0.1"

__all__ = ["MongoDB"]

# ChangeLog:
# Version   Date         Description                                   Author
# ------------------------------------------------------------------------------
# V0.1      2014-10-31   First version                                 Hugo
# ------------------------------------------------------------------------------

import copy

import pymongo

from utility.config_parser import get_config
from data.template import testcase_template


class MongoDB(object):
    def __init__(self):
        self._db_host = get_config("mongo", "host")
        self._port = int(get_config("mongo", "port"))
        self._db_name = get_config("mongo", "db")
        self.client = pymongo.MongoClient(self._db_host, self._port)

    def _get_database(self, db_name):
        """
        :summary: Return a database instance
        :param db_name: Name of database
        :return: Database instance
        """
        db = self.client[db_name]
        return db

    def _get_collection(self, collection_name, db_name="atf"):
        """
        :summary: Get the collection of db_name
        :param collection_name: Collection name
        :param db_name: Database name
        :return: Collection you want
        """
        db = self._get_database(db_name)
        collection = db[collection_name]
        return collection

    def post_data(
            self, type_="testcase",
            project="velocity", module=None, case=None, description=None,
            data_driven=False, data=None):
        collection = self._get_collection(type_)
        testcase = copy.deepcopy(testcase_template)
        

if __name__ == "__main__":
    mg = MongoDB()
    print mg._get_collection("testcase")