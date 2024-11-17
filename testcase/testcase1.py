
import pytest


class Test_test1:
    @pytest.mark.smoking
    def test_case1(self):
        assert 1 == 1

    @pytest.mark.smoking
    def test_case2(self):
        assert 1 == 2