# coding: utf-8

"""
    Example API

    Example API spec

    The version of the OpenAPI document: v1
    Contact: example@example-team.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.get_examples500_response import GetExamples500Response

class TestGetExamples500Response(unittest.TestCase):
    """GetExamples500Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetExamples500Response:
        """Test GetExamples500Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetExamples500Response`
        """
        model = GetExamples500Response()
        if include_optional:
            return GetExamples500Response(
                message = 'Results found',
                items = [{"ParentId":"f59e24c1-8d57-4ad3-b6e7-8577fc117269","ParentName":"Example parent name 1"},{"ParentId":"128583d9-2517-43c2-a9f0-1ad4cad687cd","ParentName":"Example parent name 2"}],
                count = ''
            )
        else:
            return GetExamples500Response(
        )
        """

    def testGetExamples500Response(self):
        """Test GetExamples500Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
