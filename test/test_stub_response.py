import unittest
import datetime

import mountebank_api
from mountebank_api.models.stub_response import StubResponse  # noqa: E501
from mountebank_api.rest import ApiException

class TestStubResponse(unittest.TestCase):
    """StubResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StubResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mountebank_api.models.stub_response.StubResponse()  # noqa: E501
        if include_optional :
            return StubResponse(
                _is = mountebank_api.models.http_response.HttpResponse(
                    status_code = 56, 
                    headers = mountebank_api.models.headers.headers(), 
                    body = '', 
                    _mode = 'text', ), 
                proxy = mountebank_api.models.proxy_response.ProxyResponse(
                    to = '', 
                    mode = 'proxyOnce', 
                    predicate_generators = [
                        mountebank_api.models.predicate_generator.PredicateGenerator(
                            matches = {
                                'key' : True
                                }, 
                            case_sensitive = True, )
                        ], 
                    inject_headers = {
                        'key' : ''
                        }, )
            )
        else :
            return StubResponse(
        )

    def testStubResponse(self):
        """Test StubResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
