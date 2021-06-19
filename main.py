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
        """provisional comment"""
        p = pathlib.Path(self.config["path"]["content"])
        latest_posts_number = sum(f.is_file() for f in p.iterdir() if f.suffix == ".md")

        new_post_number = latest_posts_number + 1
        if new_post_number >= 1000:
            return str(new_post_number).zfill(4)
        return str(new_post_number).zfill(3)

    @property
    def new_post_file_fullpath(self) -> str:
        """provisional comment"""
        return (
            f"{self.config['path']['content']}"
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


def generate_md_file():
    """Generate a md-file based on FrontMatter class & template file."""
    fm = FrontMatter()
    md_file_fullpath = fm.new_post_file_fullpath
    with open("template/front_matter.txt") as f:
        t = string.Template(f.read())
        template = t.substitute(
            date=fm.timestamp,
            slug=fm.slug,
            author=fm.author,
            lang=fm.lang,
            status=fm.status,
            url=fm.post_url,
            image=fm.image_url,
        )
        with open(md_file_fullpath, "w") as new_md:
            new_md.write(template)

    # Output file path as an arg to work with masOS Automator.
    print(md_file_fullpath)


def main():
    """main process"""
    generate_md_file()


if __name__ == "__main__":
    main()
