import inspect
import pprint
import re  # noqa: F401

from mountebank_api.configuration import Configuration


class Imposter(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'port': 'int',
        'protocol': 'ProtocolType',
        'name': 'str',
        'record_requests': 'bool',
        'number_of_requests': 'int',
        'key': 'str',
        'cert': 'str',
        'mutual_auth': 'bool',
        'default_response': 'HttpResponse',
        'stubs': 'list[Stub]',
    }

    attribute_map = {
        'port': 'port',
        'protocol': 'protocol',
        'name': 'name',
        'record_requests': 'recordRequests',
        'number_of_requests': 'numberOfRequests',
        'key': 'key',
        'cert': 'cert',
        'mutual_auth': 'mutualAuth',
        'default_response': 'defaultResponse',
        'stubs': 'stubs',
    }

    def __init__(self, port=None, protocol=None, name=None, record_requests=None, number_of_requests=None, key=None, cert=None, mutual_auth=None, default_response=None, stubs=None, local_vars_configuration=None):  # noqa: E501
        """Imposter - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._port = None
        self._protocol = None
        self._name = None
        self._record_requests = None
        self._number_of_requests = None
        self._key = None
        self._cert = None
        self._mutual_auth = None
        self._default_response = None
        self._stubs = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if protocol is not None:
            self.protocol = protocol
        if name is not None:
            self.name = name
        if record_requests is not None:
            self.record_requests = record_requests
        if number_of_requests is not None:
            self.number_of_requests = number_of_requests
        if key is not None:
            self.key = key
        if cert is not None:
            self.cert = cert
        if mutual_auth is not None:
            self.mutual_auth = mutual_auth
        if default_response is not None:
            self.default_response = default_response
        if stubs is not None:
            self.stubs = stubs

    @property
    def port(self):
        """Gets the port of this Imposter.  # noqa: E501


        :return: The port of this Imposter.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this Imposter.


        :param port: The port of this Imposter.  # noqa: E501
        :type port: int
        """

        self._port = port

    @property
    def protocol(self):
        """Gets the protocol of this Imposter.  # noqa: E501


        :return: The protocol of this Imposter.  # noqa: E501
        :rtype: ProtocolType
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this Imposter.


        :param protocol: The protocol of this Imposter.  # noqa: E501
        :type protocol: ProtocolType
        """

        self._protocol = protocol

    @property
    def name(self):
        """Gets the name of this Imposter.  # noqa: E501


        :return: The name of this Imposter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Imposter.


        :param name: The name of this Imposter.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def record_requests(self):
        """Gets the record_requests of this Imposter.  # noqa: E501


        :return: The record_requests of this Imposter.  # noqa: E501
        :rtype: bool
        """
        return self._record_requests

    @record_requests.setter
    def record_requests(self, record_requests):
        """Sets the record_requests of this Imposter.


        :param record_requests: The record_requests of this Imposter.  # noqa: E501
        :type record_requests: bool
        """

        self._record_requests = record_requests

    @property
    def number_of_requests(self):
        """Gets the number_of_requests of this Imposter.  # noqa: E501


        :return: The number_of_requests of this Imposter.  # noqa: E501
        :rtype: int
        """
        return self._number_of_requests

    @number_of_requests.setter
    def number_of_requests(self, number_of_requests):
        """Sets the number_of_requests of this Imposter.


        :param number_of_requests: The number_of_requests of this Imposter.  # noqa: E501
        :type number_of_requests: int
        """

        self._number_of_requests = number_of_requests

    @property
    def key(self):
        """Gets the key of this Imposter.  # noqa: E501


        :return: The key of this Imposter.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Imposter.


        :param key: The key of this Imposter.  # noqa: E501
        :type key: str
        """

        self._key = key

    @property
    def cert(self):
        """Gets the cert of this Imposter.  # noqa: E501


        :return: The cert of this Imposter.  # noqa: E501
        :rtype: str
        """
        return self._cert

    @cert.setter
    def cert(self, cert):
        """Sets the cert of this Imposter.


        :param cert: The cert of this Imposter.  # noqa: E501
        :type cert: str
        """

        self._cert = cert

    @property
    def mutual_auth(self):
        """Gets the mutual_auth of this Imposter.  # noqa: E501


        :return: The mutual_auth of this Imposter.  # noqa: E501
        :rtype: bool
        """
        return self._mutual_auth

    @mutual_auth.setter
    def mutual_auth(self, mutual_auth):
        """Sets the mutual_auth of this Imposter.


        :param mutual_auth: The mutual_auth of this Imposter.  # noqa: E501
        :type mutual_auth: bool
        """

        self._mutual_auth = mutual_auth

    @property
    def default_response(self):
        """Gets the default_response of this Imposter.  # noqa: E501


        :return: The default_response of this Imposter.  # noqa: E501
        :rtype: HttpResponse
        """
        return self._default_response

    @default_response.setter
    def default_response(self, default_response):
        """Sets the default_response of this Imposter.


        :param default_response: The default_response of this Imposter.  # noqa: E501
        :type default_response: HttpResponse
        """

        self._default_response = default_response

    @property
    def stubs(self):
        """Gets the stubs of this Imposter.  # noqa: E501


        :return: The stubs of this Imposter.  # noqa: E501
        :rtype: list[Stub]
        """
        return self._stubs

    @stubs.setter
    def stubs(self, stubs):
        """Sets the stubs of this Imposter.


        :param stubs: The stubs of this Imposter.  # noqa: E501
        :type stubs: list[Stub]
        """

        self._stubs = stubs

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Imposter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Imposter):
            return True

        return self.to_dict() != other.to_dict()
