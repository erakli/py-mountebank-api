import unittest
import datetime

import mountebank_api
from mountebank_api.models.predicate_generator import PredicateGenerator  # noqa: E501
from mountebank_api.rest import ApiException

class TestPredicateGenerator(unittest.TestCase):
    """PredicateGenerator unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PredicateGenerator
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mountebank_api.models.predicate_generator.PredicateGenerator()  # noqa: E501
        if include_optional :
            return PredicateGenerator(
                matches = {
                    'key' : True
                    }, 
                case_sensitive = True
            )
        else :
            return PredicateGenerator(
        )

    def testPredicateGenerator(self):
        """Test PredicateGenerator"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
