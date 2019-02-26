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


class GetCampaignOverview(object):
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
        'name': 'str',
        'subject': 'str',
        'type': 'str',
        'status': 'str',
        'scheduled_at': 'datetime',
        'ab_testing': 'bool',
        'subject_a': 'str',
        'subject_b': 'str',
        'split_rule': 'int',
        'winner_criteria': 'str',
        'winner_delay': 'int',
        'send_at_best_time': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'subject': 'subject',
        'type': 'type',
        'status': 'status',
        'scheduled_at': 'scheduledAt',
        'ab_testing': 'abTesting',
        'subject_a': 'subjectA',
        'subject_b': 'subjectB',
        'split_rule': 'splitRule',
        'winner_criteria': 'winnerCriteria',
        'winner_delay': 'winnerDelay',
        'send_at_best_time': 'sendAtBestTime'
    }

    def __init__(self, id=None, name=None, subject=None, type=None, status=None, scheduled_at=None, ab_testing=None, subject_a=None, subject_b=None, split_rule=None, winner_criteria=None, winner_delay=None, send_at_best_time=None):  # noqa: E501
        """GetCampaignOverview - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._subject = None
        self._type = None
        self._status = None
        self._scheduled_at = None
        self._ab_testing = None
        self._subject_a = None
        self._subject_b = None
        self._split_rule = None
        self._winner_criteria = None
        self._winner_delay = None
        self._send_at_best_time = None
        self.discriminator = None

        self.id = id
        self.name = name
        if subject is not None:
            self.subject = subject
        self.type = type
        self.status = status
        if scheduled_at is not None:
            self.scheduled_at = scheduled_at
        if ab_testing is not None:
            self.ab_testing = ab_testing
        if subject_a is not None:
            self.subject_a = subject_a
        if subject_b is not None:
            self.subject_b = subject_b
        if split_rule is not None:
            self.split_rule = split_rule
        if winner_criteria is not None:
            self.winner_criteria = winner_criteria
        if winner_delay is not None:
            self.winner_delay = winner_delay
        if send_at_best_time is not None:
            self.send_at_best_time = send_at_best_time

    @property
    def id(self):
        """Gets the id of this GetCampaignOverview.  # noqa: E501

        ID of the campaign  # noqa: E501

        :return: The id of this GetCampaignOverview.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetCampaignOverview.

        ID of the campaign  # noqa: E501

        :param id: The id of this GetCampaignOverview.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetCampaignOverview.  # noqa: E501

        Name of the campaign  # noqa: E501

        :return: The name of this GetCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetCampaignOverview.

        Name of the campaign  # noqa: E501

        :param name: The name of this GetCampaignOverview.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def subject(self):
        """Gets the subject of this GetCampaignOverview.  # noqa: E501

        Subject of the campaign. Only available if `abTesting` flag of the campaign is `false`  # noqa: E501

        :return: The subject of this GetCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this GetCampaignOverview.

        Subject of the campaign. Only available if `abTesting` flag of the campaign is `false`  # noqa: E501

        :param subject: The subject of this GetCampaignOverview.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def type(self):
        """Gets the type of this GetCampaignOverview.  # noqa: E501

        Type of campaign  # noqa: E501

        :return: The type of this GetCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetCampaignOverview.

        Type of campaign  # noqa: E501

        :param type: The type of this GetCampaignOverview.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["classic", "trigger"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def status(self):
        """Gets the status of this GetCampaignOverview.  # noqa: E501

        Status of the campaign  # noqa: E501

        :return: The status of this GetCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetCampaignOverview.

        Status of the campaign  # noqa: E501

        :param status: The status of this GetCampaignOverview.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["draft", "sent", "archive", "queued", "suspended", "in_process"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def scheduled_at(self):
        """Gets the scheduled_at of this GetCampaignOverview.  # noqa: E501

        UTC date-time on which campaign is scheduled (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :return: The scheduled_at of this GetCampaignOverview.  # noqa: E501
        :rtype: datetime
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """Sets the scheduled_at of this GetCampaignOverview.

        UTC date-time on which campaign is scheduled (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501

        :param scheduled_at: The scheduled_at of this GetCampaignOverview.  # noqa: E501
        :type: datetime
        """

        self._scheduled_at = scheduled_at

    @property
    def ab_testing(self):
        """Gets the ab_testing of this GetCampaignOverview.  # noqa: E501

        Status of A/B Test for the campaign. abTesting = false means it is disabled, & abTesting = true means it is enabled.  # noqa: E501

        :return: The ab_testing of this GetCampaignOverview.  # noqa: E501
        :rtype: bool
        """
        return self._ab_testing

    @ab_testing.setter
    def ab_testing(self, ab_testing):
        """Sets the ab_testing of this GetCampaignOverview.

        Status of A/B Test for the campaign. abTesting = false means it is disabled, & abTesting = true means it is enabled.  # noqa: E501

        :param ab_testing: The ab_testing of this GetCampaignOverview.  # noqa: E501
        :type: bool
        """

        self._ab_testing = ab_testing

    @property
    def subject_a(self):
        """Gets the subject_a of this GetCampaignOverview.  # noqa: E501

        Subject A of the ab-test campaign. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :return: The subject_a of this GetCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._subject_a

    @subject_a.setter
    def subject_a(self, subject_a):
        """Sets the subject_a of this GetCampaignOverview.

        Subject A of the ab-test campaign. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :param subject_a: The subject_a of this GetCampaignOverview.  # noqa: E501
        :type: str
        """

        self._subject_a = subject_a

    @property
    def subject_b(self):
        """Gets the subject_b of this GetCampaignOverview.  # noqa: E501

        Subject B of the ab-test campaign. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :return: The subject_b of this GetCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._subject_b

    @subject_b.setter
    def subject_b(self, subject_b):
        """Sets the subject_b of this GetCampaignOverview.

        Subject B of the ab-test campaign. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :param subject_b: The subject_b of this GetCampaignOverview.  # noqa: E501
        :type: str
        """

        self._subject_b = subject_b

    @property
    def split_rule(self):
        """Gets the split_rule of this GetCampaignOverview.  # noqa: E501

        The size of your ab-test groups. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :return: The split_rule of this GetCampaignOverview.  # noqa: E501
        :rtype: int
        """
        return self._split_rule

    @split_rule.setter
    def split_rule(self, split_rule):
        """Sets the split_rule of this GetCampaignOverview.

        The size of your ab-test groups. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :param split_rule: The split_rule of this GetCampaignOverview.  # noqa: E501
        :type: int
        """

        self._split_rule = split_rule

    @property
    def winner_criteria(self):
        """Gets the winner_criteria of this GetCampaignOverview.  # noqa: E501

        Criteria for the winning version. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :return: The winner_criteria of this GetCampaignOverview.  # noqa: E501
        :rtype: str
        """
        return self._winner_criteria

    @winner_criteria.setter
    def winner_criteria(self, winner_criteria):
        """Sets the winner_criteria of this GetCampaignOverview.

        Criteria for the winning version. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :param winner_criteria: The winner_criteria of this GetCampaignOverview.  # noqa: E501
        :type: str
        """

        self._winner_criteria = winner_criteria

    @property
    def winner_delay(self):
        """Gets the winner_delay of this GetCampaignOverview.  # noqa: E501

        The duration of the test in hours at the end of which the winning version will be sent. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :return: The winner_delay of this GetCampaignOverview.  # noqa: E501
        :rtype: int
        """
        return self._winner_delay

    @winner_delay.setter
    def winner_delay(self, winner_delay):
        """Sets the winner_delay of this GetCampaignOverview.

        The duration of the test in hours at the end of which the winning version will be sent. Only available if `abTesting` flag of the campaign is `true`  # noqa: E501

        :param winner_delay: The winner_delay of this GetCampaignOverview.  # noqa: E501
        :type: int
        """

        self._winner_delay = winner_delay

    @property
    def send_at_best_time(self):
        """Gets the send_at_best_time of this GetCampaignOverview.  # noqa: E501

        It is true if you have chosen to send your campaign at best time, otherwise it is false  # noqa: E501

        :return: The send_at_best_time of this GetCampaignOverview.  # noqa: E501
        :rtype: bool
        """
        return self._send_at_best_time

    @send_at_best_time.setter
    def send_at_best_time(self, send_at_best_time):
        """Sets the send_at_best_time of this GetCampaignOverview.

        It is true if you have chosen to send your campaign at best time, otherwise it is false  # noqa: E501

        :param send_at_best_time: The send_at_best_time of this GetCampaignOverview.  # noqa: E501
        :type: bool
        """

        self._send_at_best_time = send_at_best_time

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
        if not isinstance(other, GetCampaignOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
