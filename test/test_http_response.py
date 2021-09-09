import unittest
import datetime

import mountebank_api
from mountebank_api.models.http_response import HttpResponse  # noqa: E501
from mountebank_api.rest import ApiException

class TestHttpResponse(unittest.TestCase):
    """HttpResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test HttpResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mountebank_api.models.http_response.HttpResponse()  # noqa: E501
        if include_optional :
            return HttpResponse(
                status_code = 56, 
                headers = mountebank_api.models.headers.headers(), 
                body = '', 
                mode = 'text'
            )
        else :
            return HttpResponse(
        )

    def testHttpResponse(self):
        """Test HttpResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
