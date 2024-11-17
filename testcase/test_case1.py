
import pytest
import logging


class Test_test1:
    @pytest.mark.smoking
    def test_case1(self):
        logging.info('test_case1')
        print('test_case1')
        assert 1 == 1

    @pytest.mark.smoking
    def test_case3(self):
        logging.info('test_case3')
        assert 1 == 1

    @pytest.mark.other
    def test_case2(self):
        logging.info('test_case2')
        assert 1 == 1