import common
import schema
import requirements
from icecream import ic

the_schema = schema.Schema(
    [{
        "lotNumber": schema.And(schema.Use(int), requirements.is_valid_lot_number),
        "postalCode": schema.And(
            schema.Use(str), requirements.is_valid_postal_code
        ),
        "ownerName": schema.And(schema.Use(str), requirements.is_valid_owner_name),
    }]
)


class TestValidData:

    def test_is_valid_should_return_true(self):

        # arrange
        data = common.load_data(common.DataFile.Valid)

        # act
        actual = the_schema.is_valid(data)

        # assert
        assert actual == True

    def test_validate_should_not_throw_errors(self):

        # arrange
        data = common.load_data(common.DataFile.Valid)
        error = None

        # act
        try:
            actual = the_schema.validate(data)
            ic(actual)

        except schema.SchemaError as e:
            error = e
            ic(error)

        # assert
        assert error == None


class TestInvalidData:

    def test_is_valid_should_return_false(self):

        # arrange
        data = common.load_data(common.DataFile.Invalid)

        # act
        actual = the_schema.is_valid(data)

        # assert
        assert actual == False

    def test_validate_should_throw_errors(self):

        # arrange
        data = common.load_data(common.DataFile.Invalid)
        error = None

        # act
        try:
            actual = the_schema.validate(data)
            ic(actual)

        except schema.SchemaError as e:
            error = e
            ic(error)

        # assert
        assert isinstance(error, schema.SchemaError)
