import common
import jsonschema
import requirements
from icecream import ic

the_schema = common.load_data(common.DataFile.Schema)


class TestValidData:
    def test_validate_should_not_throw_errors(self):

        # arrange
        data = common.load_data(common.DataFile.Valid)
        error = None

        for item in data:
            # act
            try:
                jsonschema.validate(instance=item, schema=the_schema)

            except jsonschema.ValidationError as e:
                error = e
                ic(error)

            # assert
            assert error == None


class TestInvalidData:
    def test_validate_should_throw_errors(self):

        # arrange
        data = common.load_data(common.DataFile.Invalid)
        error = None

        for item in data:
            # act
            try:
                jsonschema.validate(instance=item, schema=the_schema)

            except jsonschema.ValidationError as e:
                error = e
                ic(error)

            # assert
            assert isinstance(error, jsonschema.ValidationError)
