import uiza
from uiza import Connection
from uiza.api_resources.base.base import UizaBase
from uiza.settings.config import settings
from uiza.utility.utility import set_url
from uiza.exceptions import ClientException


class Live(UizaBase):

    def __init__(self):
        self.connection = Connection(workspace_api_domain=uiza.workspace_api_domain, api_key=uiza.api_key)
        self.connection.url = set_url(
            workspace_api_domain=self.connection.workspace_api_domain,
            api_type=settings.uiza_api.livestreaming.type,
            api_version=settings.uiza_api.livestreaming.version,
            api_sub_url=settings.uiza_api.livestreaming.sub_url
        )

    def list(self, **params):
        """
        Override method list of Uizabase
        :param params:
        """
        raise ClientException('Livestreaming list method not found')

    def delete(self, id):
        """
        Override method delete of Uizabase
        :param id:
        """
        raise ClientException('Livestreaming delete method not found')

    def start_feed(self, id):
        """
        Start a live event
        :param id: identifier of event.
        """
        self.connection.url = '{}/feed'.format(self.connection.url)
        result = self.connection.post(dict(id=id, appId=uiza.app_id))

        return result

    def stop_feed(self, id):
        """
        Stop a live event
        :param id: identifier of event.
        """
        self.connection.url = '{}/feed'.format(self.connection.url)
        result = self.connection.put(dict(id=id, appId=uiza.app_id))

        return result

    def get_view(self, id):
        """
        Get a live view status
        :param id: event id has been created
        """
        self.connection.url = '{}/tracking/current-view'.format(self.connection.url)
        query = self.url_encode(params={'id': id, 'appId': uiza.app_id})
        result = self.connection.get(query=query)

        return result

    def list_recorded(self, id=None):
        """
        List of recorded file after streamed
        """
        self.connection.url = '{}/dvr'.format(self.connection.url)
        params = dict(appId=uiza.app_id)
        params.update(dict(id=id)) if id else params
        query = self.url_encode(params=params)
        result = self.connection.get(query=query)

        return result

    def convert_into_vod(self, id):
        """
        Convert recorded file into VOD entity
        :param id: identifier of record (get from list record)
        """
        self.connection.url = '{}/dvr/convert-to-vod'.format(self.connection.url)
        result = self.connection.post(dict(id=id, appId=uiza.app_id))

        return result

    def delete_recorded(self, id):
        """
        Delete a recorded file
        :param id: identifier of record (get from list record)
        """
        self.connection.url = '{}/dvr'.format(self.connection.url)
        result = self.connection.delete(dict(id=id, appId=uiza.app_id))

        return result
