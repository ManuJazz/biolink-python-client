# coding: utf-8

"""
    BioLink API

    API integration layer for linked biological objects.   __Source:__ https://github.com/biolink/biolink-api/  # noqa: E501

    OpenAPI spec version: 1.1.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.named_object_core import NamedObjectCore  # noqa: F401,E501

class RelationRef(NamedObjectCore):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'inverse': 'bool'
    }
    if hasattr(NamedObjectCore, "swagger_types"):
        swagger_types.update(NamedObjectCore.swagger_types)

    attribute_map = {
        'inverse': 'inverse'
    }
    if hasattr(NamedObjectCore, "attribute_map"):
        attribute_map.update(NamedObjectCore.attribute_map)

    def __init__(self, inverse=False, *args, **kwargs):  # noqa: E501
        """RelationRef - a model defined in Swagger"""  # noqa: E501
        self._inverse = None
        self.discriminator = None
        if inverse is not None:
            self.inverse = inverse
        NamedObjectCore.__init__(self, *args, **kwargs)

    @property
    def inverse(self):
        """Gets the inverse of this RelationRef.  # noqa: E501

        is relation inverted  # noqa: E501

        :return: The inverse of this RelationRef.  # noqa: E501
        :rtype: bool
        """
        return self._inverse

    @inverse.setter
    def inverse(self, inverse):
        """Sets the inverse of this RelationRef.

        is relation inverted  # noqa: E501

        :param inverse: The inverse of this RelationRef.  # noqa: E501
        :type: bool
        """

        self._inverse = inverse

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RelationRef, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RelationRef):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
