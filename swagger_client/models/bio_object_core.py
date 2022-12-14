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

class BioObjectCore(NamedObjectCore):
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
        'taxon': 'object'
    }
    if hasattr(NamedObjectCore, "swagger_types"):
        swagger_types.update(NamedObjectCore.swagger_types)

    attribute_map = {
        'taxon': 'taxon'
    }
    if hasattr(NamedObjectCore, "attribute_map"):
        attribute_map.update(NamedObjectCore.attribute_map)

    def __init__(self, taxon=None, *args, **kwargs):  # noqa: E501
        """BioObjectCore - a model defined in Swagger"""  # noqa: E501
        self._taxon = None
        self.discriminator = None
        if taxon is not None:
            self.taxon = taxon
        NamedObjectCore.__init__(self, *args, **kwargs)

    @property
    def taxon(self):
        """Gets the taxon of this BioObjectCore.  # noqa: E501

        Taxon to which the object belongs  # noqa: E501

        :return: The taxon of this BioObjectCore.  # noqa: E501
        :rtype: object
        """
        return self._taxon

    @taxon.setter
    def taxon(self, taxon):
        """Sets the taxon of this BioObjectCore.

        Taxon to which the object belongs  # noqa: E501

        :param taxon: The taxon of this BioObjectCore.  # noqa: E501
        :type: object
        """

        self._taxon = taxon

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
        if issubclass(BioObjectCore, dict):
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
        if not isinstance(other, BioObjectCore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
