# coding: utf-8

"""
    Kinde Management API

    Provides endpoints to manage your Kinde Businesses  # noqa: E501

    The version of the OpenAPI document: 1
    Contact: support@kinde.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from kinde_sdk import schemas  # noqa: F401

class User(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        class properties:
            id = schemas.StrSchema
            email = schemas.StrSchema
            last_name = schemas.StrSchema
            first_name = schemas.StrSchema
            is_suspended = schemas.BoolSchema
            picture = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "email": email,
                "last_name": last_name,
                "first_name": first_name,
                "is_suspended": is_suspended,
                "picture": picture,
            }
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["id"]
    ) -> MetaOapg.properties.id: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["email"]
    ) -> MetaOapg.properties.email: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["last_name"]
    ) -> MetaOapg.properties.last_name: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["first_name"]
    ) -> MetaOapg.properties.first_name: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["is_suspended"]
    ) -> MetaOapg.properties.is_suspended: ...
    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["picture"]
    ) -> MetaOapg.properties.picture: ...
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "id",
                "email",
                "last_name",
                "first_name",
                "is_suspended",
                "picture",
            ],
            str,
        ],
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["id"]
    ) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["email"]
    ) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["last_name"]
    ) -> typing.Union[MetaOapg.properties.last_name, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["first_name"]
    ) -> typing.Union[MetaOapg.properties.first_name, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["is_suspended"]
    ) -> typing.Union[MetaOapg.properties.is_suspended, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["picture"]
    ) -> typing.Union[MetaOapg.properties.picture, schemas.Unset]: ...
    @typing.overload
    def get_item_oapg(
        self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal[
                "id",
                "email",
                "last_name",
                "first_name",
                "is_suspended",
                "picture",
            ],
            str,
        ],
    ):
        return super().get_item_oapg(name)
    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        email: typing.Union[
            MetaOapg.properties.email, str, schemas.Unset
        ] = schemas.unset,
        last_name: typing.Union[
            MetaOapg.properties.last_name, str, schemas.Unset
        ] = schemas.unset,
        first_name: typing.Union[
            MetaOapg.properties.first_name, str, schemas.Unset
        ] = schemas.unset,
        is_suspended: typing.Union[
            MetaOapg.properties.is_suspended, bool, schemas.Unset
        ] = schemas.unset,
        picture: typing.Union[
            MetaOapg.properties.picture, str, schemas.Unset
        ] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[
            schemas.AnyTypeSchema,
            dict,
            frozendict.frozendict,
            str,
            date,
            datetime,
            uuid.UUID,
            int,
            float,
            decimal.Decimal,
            None,
            list,
            tuple,
            bytes,
        ],
    ) -> "User":
        return super().__new__(
            cls,
            *_args,
            id=id,
            email=email,
            last_name=last_name,
            first_name=first_name,
            is_suspended=is_suspended,
            picture=picture,
            _configuration=_configuration,
            **kwargs,
        )
