api_config = {
    "uiza_api": {
        "user": {
            "type": "api/public",
            "version": "v3",
            "sub_url": "admin/user"
        },
        "entity": {
            "type": "api/public",
            "version": "v3",
            "sub_url": "media/entity"
        }
    }
}


class Settings(object):
    dict = None  # type: dict

    def __init__(self, d):
        self.dict = d
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
                setattr(self, a, [Settings(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, Settings(b) if isinstance(b, dict) else b)


settings = Settings(api_config)
