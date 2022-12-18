import pytest
import matplotlib
import os
import sys
sys.path.insert(0,'..')
from montage.montager import montager


@pytest.mark.exe
def test_montager_intype():
    with pytest.raises(TypeError):
        montager('string')


@pytest.mark.exe
def test_path_type():
    with pytest.raises(TypeError):
        montager(['1', '2'], 20)


@pytest.mark.exe
def test_path_exists():
    with pytest.raises(FileExistsError):
        montager(['1', '2'], 'not_a_path')


@pytest.mark.exe
def test_array_fill():
    with pytest.raises(ValueError):
        montager([], './')


@pytest.mark.exe
def test_array_elements():
    with pytest.raises(ValueError):
        montager(['str', 'str', 20], './')


@pytest.mark.exe
def test_result():
    cwd = os.getcwd()
    test_file_path = cwd + '/tests/test_figs/'
    file = 'test.jpeg'
    fig = montager(
        name_array=[[file, file, file], [file, file, file]], 
        dir=test_file_path
    )
    assert isinstance(fig, matplotlib.figure.Figure) 
