import pytest


@pytest.fixture
def list_array():
    return [1, 2, 3, 4]


@pytest.fixture
def dict_array():
    return {'key': 'value',
            'vcs': 'mercurial',
            }
