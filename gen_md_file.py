"""
新規ブログ記事の雛形Markdownファイルを作るスクリプト
所定のディレクトリに、以下のディレクトリを作成する
...blog/
      |__001
           |_img/
           |_001_YYMMDD.md（フロントマター含）
"""

import configparser
import datetime
import pathlib
import string


def create_front_matter_info(work_dir: str) -> dict:
    """ フロントマター用のデータを作成する
    Args:
        work_dir: 所定のディレクトリパス
    Returns:
        dict: フロントマターに設定する情報
    """

    fm_dict = {
        "new_dir_name": "",  # 新記事を格納するディレクトリ名（作業用）
        "new_dir_path": "",  # 上記を含めたフルパス
        "created_date_long": "",  # 記事作成日時ロング版（スクリプト実行日時）
        "created_date_short": "",  # 上記のショート版
        "eye_path": "",  # アイキャッチの画像のパス
        "slug_str": "",  # スラッグ
        "post_type": "blog",  # ポストタイプはblog
    }

    # 新記事のディレクトリ名（ゼロパディング）とフルバス
    p = pathlib.Path(work_dir)
    dir_list = [p.name for p in p.iterdir() if p.is_dir()]
    dir_list.sort()
    latest_dir = int(dir_list[-1])
    fm_dict["new_dir_name"] = str(latest_dir + 1).zfill(3)
    fm_dict["new_dir_path"] = work_dir + fm_dict["new_dir_name"]

    # 新記事の作成日時（long: YYYY-MM-DD HH:MM:SS / short: YYYYMMDD）
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    fm_dict["created_date_long"] = dt
    fm_dict["created_date_short"] = (dt[2:10]).replace("-", "")

    # アイキャッチの画像パス
    fm_dict["eye_path"] = f'/ec/blog/ec_blog_{fm_dict["new_dir_name"]}.jpg'

    # スラッグ
    fm_dict["slug_str"] = f'{fm_dict["new_dir_name"]}-{fm_dict["created_date_short"]}-'

    return fm_dict


def generate_blog_file(params: dict):
    """ 新記事のディレクトリとファイルを作成する
    Args:
        params: フロントマターに設定する情報
    """

    dir_name = params["new_dir_name"]
    dir_path = params["new_dir_path"]
    l_date = params["created_date_long"]
    s_date = params["created_date_short"]
    img_path = params["eye_path"]
    slug = params["slug_str"]
    post_type = params["post_type"]

    # ディレクトリを作成
    pathlib.Path(dir_path + "/img/").mkdir(parents=True)

    # mdファイルにテンプレートからフロントマターを設定
    md_full_path = f"{dir_path}/{dir_name}_{s_date}.md"
    with open("template/front_matter.txt") as fm:
        t = string.Template(fm.read())
        template = t.substitute(date=l_date, image=img_path, slug=slug, type=post_type)
        with open(md_full_path, "w") as new_md:
            new_md.write(template)

    # macOSのAutomatorと連携するために引数としてファイルパスを出力
    print(md_full_path)


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini")
    blog_path = config["path"]["blog"]

    generate_blog_file(create_front_matter_info(blog_path))
