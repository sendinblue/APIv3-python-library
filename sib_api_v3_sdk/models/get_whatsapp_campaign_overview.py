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


class GetWhatsappCampaignOverview(object):
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
        'id': 'int',
        'campaign_name': 'str',
        'campaign_status': 'str',
        'scheduled_at': 'str',
        'sender_number': 'str',
        'stats': 'WhatsappCampStats',
        'template': 'WhatsappCampTemplate',
        'created_at': 'str',
        'modified_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'campaign_name': 'campaignName',
        'campaign_status': 'campaignStatus',
        'scheduled_at': 'scheduledAt',
        'sender_number': 'senderNumber',
        'stats': 'stats',
        'template': 'template',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt'
    }

    def __init__(self, id=None, campaign_name=None, campaign_status=None, scheduled_at=None, sender_number=None, stats=None, template=None, created_at=None, modified_at=None):  # noqa: E501
        """GetWhatsappCampaignOverview - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._campaign_name = None
        self._campaign_status = None
        self._scheduled_at = None
        self._sender_number = None
        self._stats = None
        self._template = None
        self._created_at = None
        self._modified_at = None
        self.discriminator = None

        self.id = id
        self.campaign_name = campaign_name
        self.campaign_status = campaign_status
        if scheduled_at is not None:
            self.scheduled_at = scheduled_at
        self.sender_number = sender_number
        if stats is not None:
            self.stats = stats
        self.template = template
        self.created_at = created_at
        self.modified_at = modified_at

    @property
    def id(self):
        """Gets the id of this GetWhatsappCampaignOverview.  # noqa: E501

        ID of the Whatsapp Campaign  # noqa: E501

        :return: The id of this GetWhatsappCampaignOverview.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetWhatsappCampaignOverview.

        ID of the Whatsapp Campaign  # noqa: E501

        :param id: The id of this GetWhatsappCampaignOverview.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def campaign_name(self):
        """Gets the campaign_name of this GetWhatsappCampaignOverview.  # noqa: E501

        Name of the Whatsapp Campaign  # noqa: E501

        :return: The campaign_name of this GetWhatsappCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        """Sets the campaign_name of this GetWhatsappCampaignOverview.

        Name of the Whatsapp Campaign  # noqa: E501

        :param campaign_name: The campaign_name of this GetWhatsappCampaignOverview.  # noqa: E501
        :type: str
        """
        if campaign_name is None:
            raise ValueError("Invalid value for `campaign_name`, must not be `None`")  # noqa: E501

        self._campaign_name = campaign_name

    @property
    def campaign_status(self):
        """Gets the campaign_status of this GetWhatsappCampaignOverview.  # noqa: E501

        Status of the Whatsapp Campaign  # noqa: E501

        :return: The campaign_status of this GetWhatsappCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._campaign_status

    @campaign_status.setter
    def campaign_status(self, campaign_status):
        """Sets the campaign_status of this GetWhatsappCampaignOverview.

        Status of the Whatsapp Campaign  # noqa: E501

        :param campaign_status: The campaign_status of this GetWhatsappCampaignOverview.  # noqa: E501
        :type: str
        """
        if campaign_status is None:
            raise ValueError("Invalid value for `campaign_status`, must not be `None`")  # noqa: E501
        allowed_values = ["draft", "scheduled", "pending", "approved", "running", "suspended", "rejected", "sent"]  # noqa: E501
        if campaign_status not in allowed_values:
            raise ValueError(
                "Invalid value for `campaign_status` ({0}), must be one of {1}"  # noqa: E501
                .format(campaign_status, allowed_values)
            )

        self._campaign_status = campaign_status

    @property
    def scheduled_at(self):
        """Gets the scheduled_at of this GetWhatsappCampaignOverview.  # noqa: E501

        UTC date-time on which Whatsapp campaign is scheduled. Should be in YYYY-MM-DDTHH:mm:ss.SSSZ format  # noqa: E501

        :return: The scheduled_at of this GetWhatsappCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """Sets the scheduled_at of this GetWhatsappCampaignOverview.

        UTC date-time on which Whatsapp campaign is scheduled. Should be in YYYY-MM-DDTHH:mm:ss.SSSZ format  # noqa: E501

        :param scheduled_at: The scheduled_at of this GetWhatsappCampaignOverview.  # noqa: E501
        :type: str
        """

        self._scheduled_at = scheduled_at

    @property
    def sender_number(self):
        """Gets the sender_number of this GetWhatsappCampaignOverview.  # noqa: E501

        Sender of the Whatsapp Campaign  # noqa: E501

        :return: The sender_number of this GetWhatsappCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._sender_number

    @sender_number.setter
    def sender_number(self, sender_number):
        """Sets the sender_number of this GetWhatsappCampaignOverview.

        Sender of the Whatsapp Campaign  # noqa: E501

        :param sender_number: The sender_number of this GetWhatsappCampaignOverview.  # noqa: E501
        :type: str
        """
        if sender_number is None:
            raise ValueError("Invalid value for `sender_number`, must not be `None`")  # noqa: E501

        self._sender_number = sender_number

    @property
    def stats(self):
        """Gets the stats of this GetWhatsappCampaignOverview.  # noqa: E501


        :return: The stats of this GetWhatsappCampaignOverview.  # noqa: E501
        :rtype: WhatsappCampStats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """Sets the stats of this GetWhatsappCampaignOverview.


        :param stats: The stats of this GetWhatsappCampaignOverview.  # noqa: E501
        :type: WhatsappCampStats
        """

        self._stats = stats

    @property
    def template(self):
        """Gets the template of this GetWhatsappCampaignOverview.  # noqa: E501


        :return: The template of this GetWhatsappCampaignOverview.  # noqa: E501
        :rtype: WhatsappCampTemplate
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this GetWhatsappCampaignOverview.


        :param template: The template of this GetWhatsappCampaignOverview.  # noqa: E501
        :type: WhatsappCampTemplate
        """
        if template is None:
            raise ValueError("Invalid value for `template`, must not be `None`")  # noqa: E501

        self._template = template

    @property
    def created_at(self):
        """Gets the created_at of this GetWhatsappCampaignOverview.  # noqa: E501

        Creation UTC date-time of the SMS campaign (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :return: The created_at of this GetWhatsappCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetWhatsappCampaignOverview.

        Creation UTC date-time of the SMS campaign (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :param created_at: The created_at of this GetWhatsappCampaignOverview.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this GetWhatsappCampaignOverview.  # noqa: E501

        UTC date-time of last modification of the SMS campaign (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :return: The modified_at of this GetWhatsappCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this GetWhatsappCampaignOverview.

        UTC date-time of last modification of the SMS campaign (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :param modified_at: The modified_at of this GetWhatsappCampaignOverview.  # noqa: E501
        :type: str
        """
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501

        self._modified_at = modified_at

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
        if issubclass(GetWhatsappCampaignOverview, dict):
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
        if not isinstance(other, GetWhatsappCampaignOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other