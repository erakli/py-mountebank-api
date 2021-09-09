

import unittest

import mountebank_api
from mountebank_api.api.imposter_api import ImposterApi  # noqa: E501
from mountebank_api.rest import ApiException


class TestImposterApi(unittest.TestCase):
    """ImposterApi unit test stubs"""

    def setUp(self):
        self.api = mountebank_api.api.imposter_api.ImposterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_imposter(self):
        """Test case for create_imposter

        """
        pass

    def test_delete_imposter(self):
        """Test case for delete_imposter

        """
        pass

    def test_delete_imposters(self):
        """Test case for delete_imposters

        """
        pass

    def test_get_imposter(self):
        """Test case for get_imposter

        """
        pass


if __name__ == '__main__':
    unittest.main()
