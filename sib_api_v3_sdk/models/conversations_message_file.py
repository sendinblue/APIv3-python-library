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


class ConversationsMessageFile(object):
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
        'filename': 'str',
        'size': 'int',
        'is_image': 'bool',
        'url': 'str',
        'image_info': 'ConversationsMessageFileImageInfo'
    }

    attribute_map = {
        'filename': 'filename',
        'size': 'size',
        'is_image': 'isImage',
        'url': 'url',
        'image_info': 'imageInfo'
    }

    def __init__(self, filename=None, size=None, is_image=None, url=None, image_info=None):  # noqa: E501
        """ConversationsMessageFile - a model defined in Swagger"""  # noqa: E501

        self._filename = None
        self._size = None
        self._is_image = None
        self._url = None
        self._image_info = None
        self.discriminator = None

        if filename is not None:
            self.filename = filename
        if size is not None:
            self.size = size
        if is_image is not None:
            self.is_image = is_image
        if url is not None:
            self.url = url
        if image_info is not None:
            self.image_info = image_info

    @property
    def filename(self):
        """Gets the filename of this ConversationsMessageFile.  # noqa: E501

        Name of the file  # noqa: E501

        :return: The filename of this ConversationsMessageFile.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this ConversationsMessageFile.

        Name of the file  # noqa: E501

        :param filename: The filename of this ConversationsMessageFile.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def size(self):
        """Gets the size of this ConversationsMessageFile.  # noqa: E501

        Size in bytes  # noqa: E501

        :return: The size of this ConversationsMessageFile.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ConversationsMessageFile.

        Size in bytes  # noqa: E501

        :param size: The size of this ConversationsMessageFile.  # noqa: E501
        :type: int
        """
        if size is not None and size < 0:  # noqa: E501
            raise ValueError("Invalid value for `size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._size = size

    @property
    def is_image(self):
        """Gets the is_image of this ConversationsMessageFile.  # noqa: E501

        Whether the file is an image  # noqa: E501

        :return: The is_image of this ConversationsMessageFile.  # noqa: E501
        :rtype: bool
        """
        return self._is_image

    @is_image.setter
    def is_image(self, is_image):
        """Sets the is_image of this ConversationsMessageFile.

        Whether the file is an image  # noqa: E501

        :param is_image: The is_image of this ConversationsMessageFile.  # noqa: E501
        :type: bool
        """

        self._is_image = is_image

    @property
    def url(self):
        """Gets the url of this ConversationsMessageFile.  # noqa: E501

        URL of the file  # noqa: E501

        :return: The url of this ConversationsMessageFile.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ConversationsMessageFile.

        URL of the file  # noqa: E501

        :param url: The url of this ConversationsMessageFile.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def image_info(self):
        """Gets the image_info of this ConversationsMessageFile.  # noqa: E501


        :return: The image_info of this ConversationsMessageFile.  # noqa: E501
        :rtype: ConversationsMessageFileImageInfo
        """
        return self._image_info

    @image_info.setter
    def image_info(self, image_info):
        """Sets the image_info of this ConversationsMessageFile.


        :param image_info: The image_info of this ConversationsMessageFile.  # noqa: E501
        :type: ConversationsMessageFileImageInfo
        """

        self._image_info = image_info

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
        if issubclass(ConversationsMessageFile, dict):
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
        if not isinstance(other, ConversationsMessageFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
