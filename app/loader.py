import errno
import os
import yaml

class Loader(object):
    def __init__(self, path=None):
        self._validate_config_path(path)
        self.path = path

    def _validate_config_path(self, path):
        if not os.path.isfile(path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path)

    def load(self):
        fd = open(self.path, 'rb')
        res = yaml.safe_load(fd)

        fd.close()
        return res

class LoaderFactory(object):
    def get_database_config(self):
        return Loader("{}/app/config/database.yml".format(os.path.abspath(os.getcwd())))