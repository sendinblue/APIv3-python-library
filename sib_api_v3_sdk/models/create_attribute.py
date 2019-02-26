# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from sib_api_v3_sdk.models.create_attribute_enumeration import CreateAttributeEnumeration  # noqa: F401,E501


class CreateAttribute(object):
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
        'value': 'str',
        'enumeration': 'list[CreateAttributeEnumeration]',
        'type': 'str'
    }

    attribute_map = {
        'value': 'value',
        'enumeration': 'enumeration',
        'type': 'type'
    }

    def __init__(self, value=None, enumeration=None, type=None):  # noqa: E501
        """CreateAttribute - a model defined in Swagger"""  # noqa: E501

        self._value = None
        self._enumeration = None
        self._type = None
        self.discriminator = None

        if value is not None:
            self.value = value
        if enumeration is not None:
            self.enumeration = enumeration
        if type is not None:
            self.type = type

    @property
    def value(self):
        """Gets the value of this CreateAttribute.  # noqa: E501

        Value of the attribute. Use only if the attribute's category is 'calculated' or 'global'  # noqa: E501

        :return: The value of this CreateAttribute.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CreateAttribute.

        Value of the attribute. Use only if the attribute's category is 'calculated' or 'global'  # noqa: E501

        :param value: The value of this CreateAttribute.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def enumeration(self):
        """Gets the enumeration of this CreateAttribute.  # noqa: E501

        List of values and labels that the attribute can take. Use only if the attribute's category is \"category\". For example, `[{\"value\":1, \"label\":\"male\"}, {\"value\":2, \"label\":\"female\"}]`  # noqa: E501

        :return: The enumeration of this CreateAttribute.  # noqa: E501
        :rtype: list[CreateAttributeEnumeration]
        """
        return self._enumeration

    @enumeration.setter
    def enumeration(self, enumeration):
        """Sets the enumeration of this CreateAttribute.

        List of values and labels that the attribute can take. Use only if the attribute's category is \"category\". For example, `[{\"value\":1, \"label\":\"male\"}, {\"value\":2, \"label\":\"female\"}]`  # noqa: E501

        :param enumeration: The enumeration of this CreateAttribute.  # noqa: E501
        :type: list[CreateAttributeEnumeration]
        """

        self._enumeration = enumeration

    @property
    def type(self):
        """Gets the type of this CreateAttribute.  # noqa: E501

        Type of the attribute. Use only if the attribute's category is 'normal', 'category' or 'transactional' ( type 'boolean' is only available if the category is 'normal' attribute, type 'id' is only available if the category is 'transactional' attribute & type 'category' is only available if the category is 'category' attribute )  # noqa: E501

        :return: The type of this CreateAttribute.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateAttribute.

        Type of the attribute. Use only if the attribute's category is 'normal', 'category' or 'transactional' ( type 'boolean' is only available if the category is 'normal' attribute, type 'id' is only available if the category is 'transactional' attribute & type 'category' is only available if the category is 'category' attribute )  # noqa: E501

        :param type: The type of this CreateAttribute.  # noqa: E501
        :type: str
        """
        allowed_values = ["text", "date", "float", "boolean", "id", "category"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
