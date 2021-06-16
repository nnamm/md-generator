""" md-generator のユニットテストケース """
import os
import unittest

import main as md

TEST_ANS_DICT = {
    "new_dir_name": "006",
    "new_dir_path": "/Users/nnamm/Develop/MyProject/_test/006",
    "created_date_long": "2020-04-29 15:00:00",
    "created_date_short": "200429",
    "eye_path": "/ec/blog/ec_blog_006.jpg",
    "slug_str": "006-200429-",
    "post_type": "blog",
}
TEST_ANS_LIST = ["006_200429.md", "img"]


class GeneratorMdTest(unittest.TestCase):
    """ テストクラス """

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_create_front_matter_info(self):
        """ フロントマター情報の確認 """

        self.assertDictEqual(
            md.create_front_matter_info("/Users/nnamm/Develop/MyProject/_test/"),
            TEST_ANS_DICT,
        )

    def test_generate_blog_file(self):
        """ ディレクトリとファイル生成の確認 """

        # まずディレクトリとファイルを作成
        md.generate_blog_file(TEST_ANS_DICT)

        # ディレクトリとファイルが正しく作成されているか確認（詳細な中身は目視確認とする）
        path = "/Users/nnamm/Develop/MyProject/_test/006/"
        files_list = os.listdir(path)
        files_list.sort()
        self.assertListEqual(files_list, TEST_ANS_LIST)
