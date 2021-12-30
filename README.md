## Purpose

Template to build a versatile blog forked from [jeffreytse](https://github.com/jeffreytse/jekyll-theme-yat)

## Personalize the website

1. Go to [_data/defaults.yml](_data/defaults.yml) and change the values for
    - heading
    - subheading
2. Go to [_data/translate_langs.yml](_data/translate_langs.yml) to customize the options for automatic translations by adding or removing entries.
3. To change the background image
    1. upload the file (ideally *.jpeg*) to [assets/images/banners/](assets/images/banners/)
    2. change the entry for *banner* in [index.html](index.html) such that it points to your image of choice
4. Go to [_config.yml](_config.yml) and change the values for
    1. title
    2. email
    3. author
    4. copyright
    5. description
    6. favicon
5. Got to [about.md](about.md) and tell the world who you are
    1. To do so, look up the markdown syntax in some [guide](https://www.markdownguide.org/basic-syntax/)
6. Go to [_posts](_posts) and add you first post
    1. the file needs to have a markdown extension (*.md*)
    2. the file name needs to follow the format year-month-day-filename.md (e.g. 2021-12-24-filename.md)
    3. in the head of the file, you need to provide values to the following entries (the value for layout needs to be post):
        1. layout: post
        2. title: Markdown Guide
        3. subtitle: Resources to work with Markdown
        4. categories: markdown
        5. tags: [guide, markdown]
    4. Write the content of the post in markdown



## License

This theme is licensed under the [MIT license](https://opensource.org/licenses/mit-license.php) © JeffreyTse.

<!-- External links -->

[jekyll]: https://jekyllrb.com/
[yat-git-repo]: https://github.com/jeffreytse/jekyll-theme-yat/
[yat-live-demo]: https://jeffreytse.github.io/jekyll-theme-yat/
[jekyll-spaceship]: https://github.com/jeffreytse/jekyll-spaceship
[jekyll-seo-tag]: https://github.com/jekyll/jekyll-seo-tag
[jekyll-sitemap]: https://github.com/jekyll/jekyll-sitemap
[jekyll-feed]: https://github.com/jekyll/jekyll-feed
[highlight-js]: https://github.com/highlightjs/highlight.js
