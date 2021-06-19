# Generate a markdown file for blog posts include front matter.

A tool for writing blog posts for my site that uses a static site generator. It generates a new article (Markdown) 
including front matter.

My website: [nnamm.work : portfolio note](https://nnamm.work)  
Static site generator, powered by Python: [Pelican](https://blog.getpelican.com/)

## Function

Generate a markdown file in specified directory according to certain rules (config.ini & front_matter.txt). The file 
name starts with 3-4 character number, which is determined by the tool. 

```
content
|
|__posts
   |
   |_001_YYMMDD.md (include the front matter)
```

## Other

This tool was developed to be used in conjunction with Automator on macOS. It is a very self-designed tool :)
