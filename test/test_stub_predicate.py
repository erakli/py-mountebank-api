import unittest
import datetime

import mountebank_api
from mountebank_api.models.stub_predicate import StubPredicate  # noqa: E501
from mountebank_api.rest import ApiException

class TestStubPredicate(unittest.TestCase):
    """StubPredicate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StubPredicate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mountebank_api.models.stub_predicate.StubPredicate()  # noqa: E501
        if include_optional :
            return StubPredicate(
                equals = mountebank_api.models.predicate.Predicate(), 
                deep_equals = mountebank_api.models.predicate.Predicate(), 
                contains = mountebank_api.models.predicate.Predicate(), 
                starts_with = mountebank_api.models.predicate.Predicate(), 
                ends_with = mountebank_api.models.predicate.Predicate(), 
                matches = mountebank_api.models.predicate.Predicate(), 
                exists = mountebank_api.models.predicate.Predicate(), 
                _not = mountebank_api.models.predicate.Predicate(), 
                _or = mountebank_api.models.predicate.Predicate(), 
                _and = mountebank_api.models.predicate.Predicate(), 
                case_sensitive = True, 
                _except = ''
            )
        else :
            return StubPredicate(
        )

    def testStubPredicate(self):
        """Test StubPredicate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
