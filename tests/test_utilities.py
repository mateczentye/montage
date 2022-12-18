import pytest
import montage.utilities as util

@pytest.mark.utilities
def test_format_check():
    with pytest.raises(TypeError):
        util.format_check(123)


@pytest.mark.utilities
def test_format_check2():
    with pytest.raises(TypeError):
        util.format_check('str.jpeg', 123)


@pytest.mark.utilities
def test_format_check3():
    with pytest.raises(ValueError):
        util.format_check('jpeg', ['.jpeg', 12])


@pytest.mark.utilities
def test_format_check4():
    check = util.format_check('str.picture')
    assert check is False


@pytest.mark.utilities
def test_format_check5():
    check = util.format_check('str.jpeg')
    assert check is True


@pytest.mark.utilities
def test_loop_check1():
    with pytest.raises(TypeError):
        util.loop_check('str')


@pytest.mark.utilities
def test_loop_check2():
    test = ['str.jpeg', 'str.not_a_pic', 'asd.png', 'gf.gif']
    check = util.loop_check(test)
    assert len(check) == len(test)


@pytest.mark.utilities
def test_loop_check3():
    test = ['str.jpeg', 'str.not_a_pic', 'asd.png', 'gf.gif']
    check = util.loop_check(test)
    assert check[1] == '.'
