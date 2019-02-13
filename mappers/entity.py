from marshmallow import fields

from mappers.base import BaseSchema
from uiza.entity.handle_errors import EntitiesErrors


class CreateEntitySchema(BaseSchema):
    name = fields.Str(required=True, error_messages={'required': EntitiesErrors.ERR_UIZA_ENTITY_CREATE_NAME})
    url = fields.Str(required=True, error_messages={'required': EntitiesErrors.ERR_UIZA_ENTITY_CREATE_URL})
    inputType = fields.Str(required=True,
                           validate=lambda x: x in ['http', 's3', 'ftp', 's3-uiza'],
                           error_messages={'required': EntitiesErrors.ERR_UIZA_ENTITY_CREATE_URL})
    description = fields.Str()
    metadataId = fields.List(fields.Str())
    shortDescription = fields.Str(validate=lambda x: len(x) <= 250)
    poster = fields.Str()
    thumbnail = fields.Str()
    metadataIds = fields.List(fields.Str())
    extendMetadata = fields.Dict()
    embedMetadata = fields.Dict()

    class Meta:
        strict = True


class ListEntitySchema(BaseSchema):
    metadataId = fields.List(fields.Str())
    publishToCdn = fields.Str(validate=lambda x: x in ['queue', 'not-ready', 'success', 'failed'],
                              error_messages={'validator_failed': EntitiesErrors.ERR_UIZA_ENTITY_LIST_PUBLIST_TO_CDN})

    class Meta:
        strict = True


class SearchEntitySchema(BaseSchema):
    keyword = fields.Str(required=True, error_messages={'required': EntitiesErrors.ERR_UIZA_ENTITY_SEARCH_KEYWORD})

    class Meta:
        strict = True
