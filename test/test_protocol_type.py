import unittest
import datetime

import mountebank_api
from mountebank_api.models.protocol_type import ProtocolType  # noqa: E501
from mountebank_api.rest import ApiException

class TestProtocolType(unittest.TestCase):
    """ProtocolType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProtocolType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mountebank_api.models.protocol_type.ProtocolType()  # noqa: E501
        if include_optional :
            return ProtocolType(
            )
        else :
            return ProtocolType(
        )

    def testProtocolType(self):
        """Test ProtocolType"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
