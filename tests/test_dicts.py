from utils import dicts


def test_get_val(dict_array):
    assert dicts.get_val(dict_array, "vcs") == "mercurial"
    assert dicts.get_val(dict_array, "key") == "value"
    assert dicts.get_val(dict_array, "vcs", "git") == "mercurial"
    assert dicts.get_val(dict_array, "another_key") == "git"
    assert dicts.get_val({}, "vcs", "git") == "git"
    assert dicts.get_val({}, "vcs", "bazaar") == "bazaar"
