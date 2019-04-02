from arctic import Arctic
from sysdata.mongodb.mongo_connection import mongo_defaults

"""
IMPORTANT NOTE: Make sure you have a mongodb running eg mongod --dbpath /home/yourusername/pysystemtrade/data/futures/arctic

This connection won't fail if mongo missing, but will hang

"""



class articConnection(object):
    """
    All of our ARCTIC mongo connections use this class (not static data which goes directly via mongo DB)

    """
    def __init__(self, collection_name, database_name= None, host = None, port=None):

        database_name, host, _port_not_used = mongo_defaults(db=database_name, host=host, port=port)

        # Arctic doesn't accept a port

        store = Arctic(host)
        library_name = database_name+"."+collection_name
        store.initialize_library(library_name) # will this fail if already exists??
        library = store[library_name]

        self.database_name = database_name
        self.collection_name = collection_name
        self.host = host

        self.store = store
        self.library_name = library_name
        self.library = library

    def __repr__(self):
        return "Arctic connection: host %s, db name %s, collection %s" % \
               self.host, self.database_name, self.collection_name
