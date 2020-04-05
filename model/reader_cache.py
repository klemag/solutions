import pandas as pd
import json


class ReaderCache(type):

    cache = {}

    @staticmethod
    def hash_item(item):
        if isinstance(item, pd.DataFrame) or isinstance(item, pd.Series):
            item = tuple(pd.util.hash_pandas_object(item))
        try:
            return hash(item)
        except TypeError:
            pass

        try:
            return hash(json.dumps(item, separators=(',', ':')))
        except TypeError:
            pass

        try:
            return(hash(str(item)))
        except TypeError:
            pass

        try:
            return hash(tuple(item))
        except TypeError as e:
            raise e

    @classmethod
    def read_csv(cls, *args, **kwargs):
        key = ReaderCache.hash_item(args[0])
        for arg in args[1:]:
            key = (key << 64) ^ ReaderCache.hash_item(arg)
        for arg in sorted(kwargs.keys()):
            key = (key << 64) ^ ReaderCache.hash_item(arg)
            key = (key << 64) ^ ReaderCache.hash_item(kwargs[arg])

        try:
            return cls.cache[key].copy()
        except KeyError:
            df = pd.read_csv(*args, **kwargs)
            cls.cache[key] = df
            return df
