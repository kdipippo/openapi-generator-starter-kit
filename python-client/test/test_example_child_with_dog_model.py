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

from openapi_client.models.example_child_with_dog_model import ExampleChildWithDogModel

class TestExampleChildWithDogModel(unittest.TestCase):
    """ExampleChildWithDogModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExampleChildWithDogModel:
        """Test ExampleChildWithDogModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExampleChildWithDogModel`
        """
        model = ExampleChildWithDogModel()
        if include_optional:
            return ExampleChildWithDogModel(
                model_type = 'ExampleChildWithDog',
                child_id = '5c06345b-eb66-4f31-84ed-42847b630133',
                child_name = 'Example child name 1',
                dog_name = 'Bones'
            )
        else:
            return ExampleChildWithDogModel(
        )
        """

    def testExampleChildWithDogModel(self):
        """Test ExampleChildWithDogModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
