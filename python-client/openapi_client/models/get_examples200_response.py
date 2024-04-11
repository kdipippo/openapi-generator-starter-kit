# coding: utf-8

"""
    Example API

    Example API spec

    The version of the OpenAPI document: v1
    Contact: example@example-team.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.example_parent_model import ExampleParentModel
from typing import Optional, Set
from typing_extensions import Self

class GetExamples200Response(BaseModel):
    """
    GetExamples200Response
    """ # noqa: E501
    message: Optional[Annotated[str, Field(min_length=1, strict=True)]] = Field(default=None, description="Message response string.", alias="Message")
    items: Optional[List[ExampleParentModel]] = Field(default=None, description="Array of objects returned.", alias="Items")
    count: Optional[StrictStr] = Field(default=None, description="Count of objects returned, null if error occured.", alias="Count")
    __properties: ClassVar[List[str]] = ["Message", "Items", "Count"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GetExamples200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Items'] = _items
        # set to None if count (nullable) is None
        # and model_fields_set contains the field
        if self.count is None and "count" in self.model_fields_set:
            _dict['Count'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetExamples200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Message": obj.get("Message"),
            "Items": [ExampleParentModel.from_dict(_item) for _item in obj["Items"]] if obj.get("Items") is not None else None,
            "Count": obj.get("Count")
        })
        return _obj


