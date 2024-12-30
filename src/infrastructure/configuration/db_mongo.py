from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from contextlib import contextmanager
from src.infrastructure.configuration.settings import CONNECTION_NOSQL


class MongoDB:
    def __init__(self, connection_url: str = CONNECTION_NOSQL):
        self._connection_url = connection_url
        self._client = None

    def connect(self):
        """Establish a connection to MongoDB."""
        if not self._client:
            self._client = MongoClient(self._connection_url, server_api=ServerApi('1'))
        return self._client

    @contextmanager
    def session(self):
        client = self.connect()
        try:
            # Test connection
            client.admin.command('ping')
            yield client
        except Exception as e:
            print(f"MongoDB Error: {e}")
            raise e
        finally:
            client.close()


if __name__ == "__main__":
    mongo = MongoDB()

    with mongo.session() as client:
        db = client.get_database("wefood")
        print(f"Collections in: {db.list_collection_names()}")
        for item in db.get_collection("wefood").find({}):
            print(item)
