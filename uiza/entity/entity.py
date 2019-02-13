try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from uiza.base.decorators import validate_schema
from uiza.base.base import UizaBase
from uiza.entity.handle_errors import EntitiesErrors
from mappers.entity import CreateEntitySchema, ListEntitySchema
from utility.utility import set_url
from settings.config import settings


class Entity(UizaBase):

    def __init__(self, connection, **kwargs):
        """

        :param connection:
        :param kwargs:
        """
        super(Entity, self).__init__(connection, **kwargs)
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.entity.type,
            api_version=settings.uiza_api.entity.version,
            api_sub_url=settings.uiza_api.entity.sub_url
        )

    @validate_schema(schema=CreateEntitySchema())
    def create(self, data):
        """

        :param kwargs:
        :return:
        """
        result = self.connection.post(data=data)

        return result

    @validate_schema(schema=ListEntitySchema())
    def get_entities(self, params):
        query = ''
        if params:
            query = '?{}'.format(urlencode(params))
        data = self.connection.get(query=query)

        return data


    def search_entity(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        keyword = kwargs.get('keyword')
        if not keyword:
            raise ValueError(EntitiesErrors.ERR_UIZA_ENTITY_SEARCH_KEYWORD)

        self.connection.url = '{}/search'.format(self.connection.url)
        query = ''
        if kwargs:
            query = '?{}'.format(urlencode(kwargs))
        data = self.connection.get(query=query)

        return data

    def publish_entity(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        if 'id' not in kwargs.keys():
            raise ValueError(EntitiesErrors.ERR_UIZA_ENTITY_PUBLISH_ID)

        self.connection.url = '{}/publish'.format(self.connection.url)
        data = self.connection.post(data=kwargs)

        return data

    def get_status_publish_entity(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        id = kwargs.get('id')
        if not id:
            raise ValueError(EntitiesErrors.ERR_UIZA_ENTITY_GET_STATUS_PUBLISH_ID)

        self.connection.url = '{}/publish/status'.format(self.connection.url)
        query = '?{}'.format(urlencode({'id': id}))
        data = self.connection.get(query=query)

        return data

    def get_aws_upload_key(self):
        """

        :return:
        """
        aws_sub_url = 'admin/app/config/aws'
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.entity.type,
            api_version=settings.uiza_api.entity.version,
            api_sub_url=aws_sub_url
        )

        data = self.connection.get()

        return data
