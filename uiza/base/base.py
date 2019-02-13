try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from uiza.base.handle_errors import ClientBaseErrors


class UizaBase(object):

    data_validated = None

    def __init__(self, connection, **kwargs):
        """

        :param connection:
        :param kwargs:
        """
        self.connection = connection

    def create(self, **data):
        """

        :param data:
        :return:
        """
        result = self.connection.post(data=data)

        return result

    def update(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        if 'id' not in kwargs.keys():
            raise ValueError(ClientBaseErrors.ERR_ID_NOT_FOUND)

        data = self.connection.put(data=kwargs)

        return data

    def get_list(self, **params):
        """

        :param params:
        :return:
        """
        query = ''
        if params:
            query = '?{}'.format(urlencode(params))
        data = self.connection.get(query=query)

        return data

    def retrieve(self, **kwargs):
        """

        :param id:
        :return:
        """
        id = kwargs.get('id')
        if not id:
            raise ValueError(ClientBaseErrors.ERR_ID_NOT_FOUND)

        query = '?{}'.format(urlencode({'id': id}))
        data = self.connection.get(query=query)

        return data

    def delete(self, **kwargs):
        """

        :return:
        """
        id = kwargs.get('id')
        if not id:
            raise ValueError(ClientBaseErrors.ERR_ID_NOT_FOUND)

        data = self.connection.delete(dict(id=id))

        return data
