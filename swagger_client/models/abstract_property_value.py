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

class AbstractPropertyValue(object):
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
        'val': 'str',
        'pred': 'str',
        'xrefs': 'list[str]'
    }

    attribute_map = {
        'val': 'val',
        'pred': 'pred',
        'xrefs': 'xrefs'
    }

    def __init__(self, val=None, pred=None, xrefs=None):  # noqa: E501
        """AbstractPropertyValue - a model defined in Swagger"""  # noqa: E501
        self._val = None
        self._pred = None
        self._xrefs = None
        self.discriminator = None
        if val is not None:
            self.val = val
        if pred is not None:
            self.pred = pred
        if xrefs is not None:
            self.xrefs = xrefs

    @property
    def val(self):
        """Gets the val of this AbstractPropertyValue.  # noqa: E501

        value part  # noqa: E501

        :return: The val of this AbstractPropertyValue.  # noqa: E501
        :rtype: str
        """
        return self._val

    @val.setter
    def val(self, val):
        """Sets the val of this AbstractPropertyValue.

        value part  # noqa: E501

        :param val: The val of this AbstractPropertyValue.  # noqa: E501
        :type: str
        """

        self._val = val

    @property
    def pred(self):
        """Gets the pred of this AbstractPropertyValue.  # noqa: E501

        predicate (attribute) part  # noqa: E501

        :return: The pred of this AbstractPropertyValue.  # noqa: E501
        :rtype: str
        """
        return self._pred

    @pred.setter
    def pred(self, pred):
        """Sets the pred of this AbstractPropertyValue.

        predicate (attribute) part  # noqa: E501

        :param pred: The pred of this AbstractPropertyValue.  # noqa: E501
        :type: str
        """

        self._pred = pred

    @property
    def xrefs(self):
        """Gets the xrefs of this AbstractPropertyValue.  # noqa: E501

        Xrefs provenance for property-value  # noqa: E501

        :return: The xrefs of this AbstractPropertyValue.  # noqa: E501
        :rtype: list[str]
        """
        return self._xrefs

    @xrefs.setter
    def xrefs(self, xrefs):
        """Sets the xrefs of this AbstractPropertyValue.

        Xrefs provenance for property-value  # noqa: E501

        :param xrefs: The xrefs of this AbstractPropertyValue.  # noqa: E501
        :type: list[str]
        """

        self._xrefs = xrefs

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
        if issubclass(AbstractPropertyValue, dict):
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
        if not isinstance(other, AbstractPropertyValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
