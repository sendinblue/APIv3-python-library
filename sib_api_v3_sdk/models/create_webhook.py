# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   | 406  | Error. Not Acceptable  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CreateWebhook(object):
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
        'url': 'str',
        'description': 'str',
        'events': 'list[str]',
        'type': 'str',
        'domain': 'str'
    }

    attribute_map = {
        'url': 'url',
        'description': 'description',
        'events': 'events',
        'type': 'type',
        'domain': 'domain'
    }

    def __init__(self, url=None, description=None, events=None, type='transactional', domain=None):  # noqa: E501
        """CreateWebhook - a model defined in Swagger"""  # noqa: E501

        self._url = None
        self._description = None
        self._events = None
        self._type = None
        self._domain = None
        self.discriminator = None

        self.url = url
        if description is not None:
            self.description = description
        self.events = events
        if type is not None:
            self.type = type
        if domain is not None:
            self.domain = domain

    @property
    def url(self):
        """Gets the url of this CreateWebhook.  # noqa: E501

        URL of the webhook  # noqa: E501

        :return: The url of this CreateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CreateWebhook.

        URL of the webhook  # noqa: E501

        :param url: The url of this CreateWebhook.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def description(self):
        """Gets the description of this CreateWebhook.  # noqa: E501

        Description of the webhook  # noqa: E501

        :return: The description of this CreateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateWebhook.

        Description of the webhook  # noqa: E501

        :param description: The description of this CreateWebhook.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def events(self):
        """Gets the events of this CreateWebhook.  # noqa: E501

        - Events triggering the webhook. Possible values for **Transactional** type webhook: #### `sent` OR `request`, `delivered`, `hardBounce`, `softBounce`, `blocked`, `spam`, `invalid`, `deferred`, `click`, `opened`, `uniqueOpened` and `unsubscribed` - Possible values for **Marketing** type webhook: #### `spam`, `opened`, `click`, `hardBounce`, `softBounce`, `unsubscribed`, `listAddition` & `delivered` - Possible values for **Inbound** type webhook: #### `inboundEmailProcessed`   # noqa: E501

        :return: The events of this CreateWebhook.  # noqa: E501
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this CreateWebhook.

        - Events triggering the webhook. Possible values for **Transactional** type webhook: #### `sent` OR `request`, `delivered`, `hardBounce`, `softBounce`, `blocked`, `spam`, `invalid`, `deferred`, `click`, `opened`, `uniqueOpened` and `unsubscribed` - Possible values for **Marketing** type webhook: #### `spam`, `opened`, `click`, `hardBounce`, `softBounce`, `unsubscribed`, `listAddition` & `delivered` - Possible values for **Inbound** type webhook: #### `inboundEmailProcessed`   # noqa: E501

        :param events: The events of this CreateWebhook.  # noqa: E501
        :type: list[str]
        """
        if events is None:
            raise ValueError("Invalid value for `events`, must not be `None`")  # noqa: E501
        allowed_values = ["sent", "hardBounce", "softBounce", "blocked", "spam", "delivered", "request", "click", "invalid", "deferred", "opened", "uniqueOpened", "unsubscribed", "listAddition", "contactUpdated", "contactDeleted", "inboundEmailProcessed"]  # noqa: E501
        if not set(events).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `events` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(events) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._events = events

    @property
    def type(self):
        """Gets the type of this CreateWebhook.  # noqa: E501

        Type of the webhook  # noqa: E501

        :return: The type of this CreateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateWebhook.

        Type of the webhook  # noqa: E501

        :param type: The type of this CreateWebhook.  # noqa: E501
        :type: str
        """
        allowed_values = ["transactional", "marketing", "inbound"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def domain(self):
        """Gets the domain of this CreateWebhook.  # noqa: E501

        Inbound domain of webhook, required in case of event type `inbound`  # noqa: E501

        :return: The domain of this CreateWebhook.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CreateWebhook.

        Inbound domain of webhook, required in case of event type `inbound`  # noqa: E501

        :param domain: The domain of this CreateWebhook.  # noqa: E501
        :type: str
        """

        self._domain = domain

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
        if issubclass(CreateWebhook, dict):
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
        if not isinstance(other, CreateWebhook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
