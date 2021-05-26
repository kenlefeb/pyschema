import common
import schema
import pytest
import json

class TestCommon:

    @pytest.mark.parametrize(
        "type,expected",
        [
            (common.DataFile.Valid, "./data/valid.json"), 
            (common.DataFile.Invalid, "./data/invalid.json")
        ],
    )
    def test_get_filename(self, type, expected):

        # arrange

        # act
        actual = common.get_filename(type)

        # assert
        assert actual == expected


    @pytest.mark.parametrize(
        "type,filename",
        [
            (common.DataFile.Valid, "./data/valid.json"), 
            (common.DataFile.Invalid, "./data/invalid.json")
        ],
    )
    def test_load_data(self, type, filename):

        # arrange
        expected = {}
        with open(filename) as file:
            expected = json.loads(file.read())

        # act
        actual = common.load_data(type)

        # assert
        assert actual == expected
