"""md-generator - Unit test cases."""

import pytest

import md_generator as md


@pytest.fixture(name="conf1", scope="class")
def fixture_conf1():
    """Instance of loaded config_test1.ini."""
    return md.FrontMatter("./tests/config_test1.ini")


@pytest.fixture(name="conf2", scope="class")
def fixture_conf2():
    """Instance of loaded config_test2.ini."""
    return md.FrontMatter("./tests/config_test2.ini")


@pytest.fixture(name="conf3", scope="class")
def fixture_conf3():
    """Instance of loaded config_test3.ini."""
    return md.FrontMatter("./tests/config_test3.ini")


def test_get_new_post_number1(conf1):
    """Case1. No post files."""
    assert conf1.get_new_post_number() == "001"


def test_get_new_post_number2(conf2):
    """Case2. Already exist 3-post files."""
    assert conf2.get_new_post_number() == "004"


def test_get_new_post_number3(conf3):
    """Case3. Already exist 99-post files."""
    assert conf3.get_new_post_number() == "100"


def test_new_post_file_fullpath(conf2):
    """Case4. Property"""
    now_str = conf2.now.strftime("%y%m%d")
    assert conf2.new_post_file_fullpath == (
        f"./tests/test_nnamm.work2/content/posts/004_{now_str}.md"
    )


def test_slug(conf2):
    """Case5. Property"""
    assert conf2.slug == "004-"


def test_author(conf2):
    """Case6. Property"""
    assert conf2.author == "Test_Takashi"


def test_lang(conf2):
    """Case7. Property"""
    assert conf2.lang == "ja"


def test_status(conf2):
    """Case8. Property"""
    assert conf2.status == "published"


def test_post_url(conf2):
    """Case9. Property"""
    assert conf2.post_url == "posts/004-"


def test_image_url(conf2):
    """Case10. Property"""
    now_str = conf2.now.strftime("%y%m%d")
    assert conf2.image_url == f"../../images/posts/004_{now_str}-0.jpg"
