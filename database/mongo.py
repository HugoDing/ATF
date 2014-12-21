# -*- coding=utf-8 -*-

"""
About database.mongo
    This module contains all the APIs about MongoDB.
     
Description of classes
    MongoDB:
        Methods to operate MongoDB

Description of methods
    _get_database: Get a Mongo database
    _get_collection: Get a Mongo database collection
    post_data: Post JSON data to MongoDB
    find_data: Find data from MongoDB

"""

__authors__ = [
    '"Hugo Ding" <huicong.ding@spirent.com>',
]

__version__ = "V0.2"

__all__ = ["MongoDB"]

# ChangeLog:
# Version   Date         Description                                   Author
# ------------------------------------------------------------------------------
# V0.1      2014-10-31   First version                                 Hugo
# V0.2      2014-11-23   Add methods to post and get testcase
#                        data from MongoDB.                            Hugo
# ------------------------------------------------------------------------------

import copy

import pymongo

from utility.config_parser import get_config
from data.template import testcase_template
from logging_report.logging_ import print_log


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
        """
        :summary: Post data to MongoDB.
        :param type_: The type of data, could be testcase or suite
        :param project: Project name
        :param module: Module name or component name
        :param case: Name of testcase
        :param description: Description of this data
        :param data_driven: Use data driven or not
        :param data: Real test data
        :return: The Object ID of this data in MongoDB
        """
        if self.find_data(type_, project, module, case):
            print_log("The data of testcase %s has already existed." % module)
            return -1

        if type_ == "testcase":
            collection = self._get_collection(type_)
            testcase = copy.deepcopy(testcase_template)

            if project != "velocity":
                testcase["project"] = project
            testcase["module"] = module
            testcase["case"] = case
            testcase["description"] = description
            testcase["data_driven"] = data_driven
            testcase["data"] = data

            return collection.insert(testcase)

    def find_data(
            self, type_="testcase",
            project="web", module=None, case=None):
        collection = self._get_collection(type_)

        data = collection.find_one(
            {"project": project, "module": module, "case": case}
        )

        if data:
            print_log(
                "The data of testcase %s has been found." % case,
                "debug"
            )
            return data["data"]
        else:
            print_log(
                "The data of testcase %s.%s hasn't been found!"
                % (module, case),
                "warn"
            )
            return False


if __name__ == "__main__":
    mg = MongoDB()
    print mg.find_data(module="login_demo", case="ValidLogin")