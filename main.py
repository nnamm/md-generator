"""Generate a template md-file for new blog post.

Create the following file in the specified directory.

content
|
|__posts
   |
   |_001_YYMMDD.md (include the front matter)

Todo:
    Self practice of unit testing with pytest.
    (want to get used to Python development)
"""

import configparser
import datetime
import pathlib
import string
import subprocess


class FrontMatter:
    """Front matter class.

    Handle the data needed for front matter.
    """

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.now = datetime.datetime.now()
        self.new_post_number = self.get_new_post_number()

    def get_new_post_number(self) -> str:
        """Get new post number function.

        Get the latest post file number from the existing post
        files (in ascending order).

        Args:
            none.

        Returns:
            new_post_number (str): new post number (zero padding).
        """
        p = pathlib.Path(self.config["path"]["posts"])
        latest_posts_number = sum(f.is_file() for f in p.iterdir() if f.suffix == ".md")

        new_post_number = latest_posts_number + 1
        if new_post_number >= 1000:
            return str(new_post_number).zfill(4)
        return str(new_post_number).zfill(3)

    @property
    def new_post_file_fullpath(self) -> str:
        """File fullpath property getter method.

        Example: /Users/hoge/fuga/content/posts/001_210601.md
        """
        return (
            f"{self.config['path']['posts']}"
            f"{self.new_post_number}_{self.now.strftime('%y%m%d')}.md"
        )

    @property
    def timestamp(self) -> str:
        """Timestamp property getter method.

        Example: 210110 10:05:45
        """
        return self.now.strftime("%y-%m-%d %H:%M:%S")

    @property
    def slug(self) -> str:
        """Slug property getter method.

        Example: 001-
        """
        return f"{self.new_post_number}-"

    @property
    def author(self) -> str:
        """Author property getter method.

        Example: Takashi Hanamura
        """
        return self.config["consts"]["author"]

    @property
    def lang(self) -> str:
        """Lang property getter method.

        Example: ja
        """
        return self.config["consts"]["lang"]

    @property
    def status(self) -> str:
        """Status property getter method.

        Example: Published
        """
        return self.config["consts"]["status"]

    @property
    def post_url(self) -> str:
        """Post_url property getter method.

        Example: posts/001-
        """
        return f"{self.config['post_url']['prefix']}{self.new_post_number}-"

    @property
    def image_url(self) -> str:
        """Image_url property getter method.

        Example: ../../images/posts/001-210110-0.jpg
        """
        return (
            f"{self.config['image_url']['prefix']}{self.new_post_number}_"
            f"{self.now.strftime('%y%m%d')}-0.jpg"
        )


def generate_md_file() -> str:
    """Generate a markdown file.

    Generate a markdown file based on FrontMatter class & template file.

    Args:
        none.

    Returns:
        md_file_fullpath (str): Full path of generated markdown file.
    """
    fm = FrontMatter()
    with open("template/front_matter.txt") as temp:
        t = string.Template(temp.read())
        template = t.substitute(
            date=fm.timestamp,
            slug=fm.slug,
            author=fm.author,
            lang=fm.lang,
            status=fm.status,
            url=fm.post_url,
            image=fm.image_url,
        )
        md_file_fullpath = fm.new_post_file_fullpath
        with open(md_file_fullpath, "w") as new_md_file:
            new_md_file.write(template)
    return md_file_fullpath


def main() -> None:
    """Prepare to write a new post."""
    config = configparser.ConfigParser()
    config.read("config.ini")
    app = config["app"]["editor"]
    work_dir = config["path"]["content"]
    md_file_path = generate_md_file()

    # Open working dir & generated markdown file for macOS
    subprocess.run(["open", work_dir], check=True)
    subprocess.run(["open", app, md_file_path], check=True)


if __name__ == "__main__":
    main()
