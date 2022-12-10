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

class SequencePosition(object):
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
        'position': 'int',
        'reference': 'str'
    }

    attribute_map = {
        'position': 'position',
        'reference': 'reference'
    }

    def __init__(self, position=None, reference=None):  # noqa: E501
        """SequencePosition - a model defined in Swagger"""  # noqa: E501
        self._position = None
        self._reference = None
        self.discriminator = None
        if position is not None:
            self.position = position
        if reference is not None:
            self.reference = reference

    @property
    def position(self):
        """Gets the position of this SequencePosition.  # noqa: E501


        :return: The position of this SequencePosition.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this SequencePosition.


        :param position: The position of this SequencePosition.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def reference(self):
        """Gets the reference of this SequencePosition.  # noqa: E501


        :return: The reference of this SequencePosition.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SequencePosition.


        :param reference: The reference of this SequencePosition.  # noqa: E501
        :type: str
        """

        self._reference = reference

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
        if issubclass(SequencePosition, dict):
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
        if not isinstance(other, SequencePosition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other