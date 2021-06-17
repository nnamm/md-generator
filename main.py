"""
Generate a template md-file for new blog post.

Create the following file in the specified directory. 
content
|__posts
   |_001_YYMMDD.md(include the front matter)
"""

import configparser
import datetime
import pathlib
import string


class FrontMatter:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
        self.now = datetime.datetime.now()
        self.new_post_number: str = self.get_new_post_number()

    def get_new_post_number(self) -> str:
        p = pathlib.Path(self.config["path"]["content"])
        latest_posts_number = sum(f.is_file() for f in p.iterdir() if f.suffix == ".md")

        new_post_number = latest_posts_number + 1
        if new_post_number >= 1000:
            return str(new_post_number).zfill(4)
        return str(new_post_number).zfill(3)

    @property
    def new_post_file_fullpath(self) -> str:
        return (
            f"{self.config['path']['content']}"
            f"{self.new_post_number}_{self.now.strftime('%y%m%d')}.md"
        )

    @property
    def timestamp(self) -> str:
        return self.now.strftime("%y-%m-%d %H:%M:%S")

    @property
    def slug(self) -> str:
        return f"{self.new_post_number}-"

    @property
    def author(self) -> str:
        return self.config["consts"]["author"]

    @property
    def lang(self) -> str:
        return self.config["consts"]["lang"]

    @property
    def status(self) -> str:
        return self.config["consts"]["status"]

    @property
    def post_url(self) -> str:
        return f"{self.config['post_url']['prefix']}{self.new_post_number}-"

    @property
    def image_url(self) -> str:
        return (
            f"{self.config['image_url']['prefix']}{self.new_post_number}_"
            f"{self.now.strftime('%y%m%d')}-0.jpg"
        )


def generate_md_file():
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
    generate_md_file()


if __name__ == "__main__":
    main()
