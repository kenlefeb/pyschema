import common
import requirements
from icecream import ic
from jschon import Catalogue, Evaluator, JSON, JSONSchema, OutputFormat, URI, JSONSchemaError

catalog = Catalogue.create_default_catalogue('2020-12')

the_schema = JSONSchema({
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "$id": "https://t2c.clev.frb.org/payment-poc.schema.json",
    "title": "ThunderCats HOA Search API",
    "description": "A property record",
    "type": "object",
    "properties": {
        "lotNumber": {
            "description": "The Lot Number for the property",
            "type": "string",
            "pattern": "[0-9]",
            "minLength": 1,
            "maxLength": 2
        },
        "postalCode": {
            "description": "The Postal Code for the property",
            "type": "string",
            "pattern": "[a-z0-9]",
            "minLength": 1,
            "maxLength": 4
        },
        "ownerName": {
            "description": "The property's owner's full name",
            "type": "string",
            "minLength": 1,
            "maxLength": 128
        }
    },
    "required": [
        "lotNumber",
        "postalCode",
        "ownerName"
    ]
}).validate()


class TestValidData:

    def test_evaluate_should_return_valid_scope(self):

        # arrange
        data = JSON(common.load_data(common.DataFile.Valid))

        for item in data:
            # act
            actual = the_schema.evaluate(item)
            ic(actual)

            # assert
            assert actual.valid


class TestInvalidData:

    def test_validate_should_return_invalid_scope(self):

        # arrange
        data = JSON(common.load_data(common.DataFile.Invalid))

        for item in data:
            # act
            actual = the_schema.evaluate(item)
            ic(actual)

            for error in actual.collect_errors():
                ic(error)

            # assert
            assert actual.valid == False
