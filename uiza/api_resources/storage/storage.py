import uiza
from uiza import Connection
from uiza.api_resources.base.base import UizaBase
from uiza.settings.config import settings
from uiza.utility.utility import set_url
from uiza.exceptions import ClientException


class Storage(UizaBase):

    def __init__(self):
        self.connection = Connection(workspace_api_domain=uiza.workspace_api_domain, api_key=uiza.api_key)
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.storage.type,
            api_version=settings.uiza_api.storage.version,
            api_sub_url=settings.uiza_api.storage.sub_url
        )

    def list(self, **params):
        """
        Override method list of Uizabase
        :param params:
        :return: Raise error when get method list
        """
        raise ClientException('Storage list method not found')
