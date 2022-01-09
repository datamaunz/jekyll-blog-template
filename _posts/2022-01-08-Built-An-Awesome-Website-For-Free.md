---
layout: post
title: Build an awesome website for free
subtitle: Tutorial
categories: Website
tags: [Github, website]
---

## Welcome to this tutorial!

<a href="https://youtu.be/TRIys0HLJuU" title="Link Title"><img src="/assets/images/post_images/website_tutorial/youtube_cover_image.png" alt="Link to video version of tutorial" /></a>


### Why a Github page?

Today we will be building this amazing website. It is 100% free and 100% yours. You won’t have to pay for a domain, a template or for hosting. All you need is a Github account, which comes for free as well. Having a Github account is anyway kind of necessary if you want to break into tech. 

So, no matter whether or not you need a website, you have come to the right place because you should definitely create a Github account. And when doing so, why not making the world a bit more beautiful by adding your wonderful site?

### Examples for the type of website

Here are two examples for the kind of website you will be building: 
- [tea-berlin](https://tea-berlin.github.io/) and 
- [bruno-danelon](https://bruno-danelon.github.io/). 

The website template comes from [jeffreytse](https://github.com/jeffreytse/jekyll-theme-yat) and got simplified by [datamaunz](https://github.com/datamaunz/jekyll-blog-template) for the sake of this tutorial.

### Features of your website

This website will allow you to blog about the things that you care about and you can show the world who you are. Your visitors can toggle between light & dark mode and they can pick their preferred language for viewing your site. If you are missing your preferred language in the menu, no worries! The tutorial will show you how to further customise the options.

Besides automatic translations, the site will archive your posts automatically by date. Furthermore, it will classify your posts through categories of your choice. In addition to that, you can use tags to make it easier for your users to find the right articles.And most amazingly, it looks absolutely stunning; it is ultra fast and 100% free. 

What are you waiting for?! Build your own website and show the world who you are.

## Let's get started!
### Create a free Github account

![Sign up](/assets/images/post_images/website_tutorial/sign_up.png)

First, we have to create a Github account. Go to [GitHub](https://github.com) and hit the sign-up button in the upper right corner. Enter an email address, a password, and a username. As mentioned before, you will not have to pay for your website, not even for the domain, because Github provides you with a subdomain, which will be constructed from your username. This is why the choice of your username is kind of important. I will go with *tea-berlin*. You should use yours. 

Now we are being asked whether we want to receive product updates and announcements and we'll have to solve a quick puzzle to verify that we are humans. You'll receive a verification code that you need to enter via email, we skip the personalisation. And: Done!

Congratulations! You have a Github account!

### Fork the repo containing the template

![skip intro](/assets/images/post_images/website_tutorial/skip_introduction.png)

Here you can introduce yourself to those visiting your account. You should definitely do that! But for now we will skip it because we want to learn how to create our amazing website. Click “Dismiss This”, open a new tab and go to [jekyll-blog-template](https://github.com/datamaunz/jekyll-blog-template).

![fork repo](/assets/images/post_images/website_tutorial/fork_datamaunz_repo.png)

Now we are on the Github account of Datamaunz. And more precisely, we are seeing the repository called *Jekyll blog template*. 

It contains various folders and files. But no worries. In order to transfer all these files into our own Github account, we just have to go to the upper right corner and click on “Fork”.

Now a fork is being created. This fork is a copy of the original repository that will appear in our own account.

### Rename the repo such that Github will treat it as a website

![go to settings after forking](/assets/images/post_images/website_tutorial/go_to_settings_adter_forking.png)

As you can see, we are now in our own Github account; and more precisely. We are in our own repository called “Jekyll blog template”.

To make this our website, we have to change the name of this repository. To do so, go to settings.

By convention, Github repositories that are named by the name of the Github account followed by *.github.io* will be treated as websites by Github. In our case, this is *tea-berlin.github.io*

![rename repo](/assets/images/post_images/website_tutorial/rename_repo.png)

Change the entry for *repository name* accordingly and hit *rename*.


If you have followed the Tutorial up to this point, your repository should now have the name that you have selected as username for your Github account and this name should be followed by *.github.io*. This is also the address to your website. Open a new tab and enter the name of your repository. In my case, this is tea-berlin.github.io. It might take a few minutes until the changes will have propagated. BAEHM! We have our own website! 

![view website 1](/assets/images/post_images/website_tutorial/view_website_1.png)

And users can pick their favorite language to view your site. Later we will see how to customise the choices in this menu.

Let’s go back to our repository and scroll down to the ReadMe Page. It shows all the steps required to customise your page. You only have to follow the links to access the respective files. Note, you could also access the files directly. But we will be using the links to make it as easy to follow as possible.

![readme instrutions](/assets/images/post_images/website_tutorial/readme_instructions.png)

### Thank Jeffreytse for creating this template

First, let’s thank the creator of this amazing template, Jeffreytse, by following the first link. The link brings us to the original repository from where Datamaunz has forked its repository in order to simplify it by creating a Readme etc. to make it easier for people like us. However, the actual work comes from Jeffreytse. You can show your appreciation by giving a star for this repository.

![star for jeffreytse](/assets/images/post_images/website_tutorial/star_for_jeffreytse.png)

### Customize heading and subheading

Now, let’s go back to our own repository and personalize the contents.

In its current version, our website says *your awesome title* and *your awesome subheading*. 

To change the values for heading and subheading, go to _data/defaults.yml (by following the link in the readme instructions or by opening the file via the file system in your repo). 

![defaults_yml file](/assets/images/post_images/website_tutorial/defaults_yml.png)

Click on the little pencil icon. This will put the interface into editing mode. Note, this is not how experienced developers use Github. They would do the changes via an Editor like VS Code or Pycharm, commit the changes to some branch and merge them into the main branch. You should definitely do that in the future as well. However, for our current purpose it is okay to use this graphical user interface (even though less efficient). You will learn in another lesson how to use Github more efficiently. 

![click pencil icon for editing](/assets/images/post_images/website_tutorial/hit_pencil_icon.png)

For heading, we will pass the value; “Tech Expert Academy”. You might want to put your own name there; or the name of your project; or whatever you think represents your intentions best. Make sure to put this value into quotation marks. The result should read; "heading"; "colon"; "quotation mark"; your new heading; "quotation mark”. 

Now that we are in editing mode, let's change the values for heading and subheading. Before the change, the file should contain the following entries:
```Yaml
home:
  heading: "your awesome title"
  subheading: "your awesome subheading"
  banner: "your awesome url"
```
I will change it as shown below but you should pick values that represent your website (and thus yourself, your project or your cause) best. Make sure not to mess up the syntax:
```Yaml
home:
  heading: "Tech Expert Academy"
  subheading: "Land a tech job in just 6 months"
  banner: "your awesome url"
```
Now, scroll down to the bottom of the page and smash the Commit button.

![commit changes](/assets/images/post_images/website_tutorial/Commit_button.png)

Congratulations, you have committed your first changes! This is huge. Github is a version control system. Changes are documented in the form of such commits. This means, based on your history of commits, you can restore earlier versions of your repository. This comes in handy when you (or someone else) have messed up.

### Customize menu for automatic translations

Let’s make some more changes to our website. Go back to your root repository and scroll down to the Readme file. 

The second change is about the menu for automated translations. You do not have to make any changes here if you are satisfied with the default options. In case you want to make changes, this is how you can do it.

Go to *_data/translate_langs.yml* (either by navigating your file system or by using the link in the ReadMe instructions).

![translate_lang](/assets/images/post_images/website_tutorial/translate_lang.png)

Each language option is represented by one bullet point taking up three lines. One line for language, one for image, and one for text. 

```Yaml
# Translate languges
# langs refer to https://cloud.google.com/translate/docs/languages

- lang: en
  img: https://cdn.countryflags.com/thumbs/united-states-of-america/flag-400.png
  text: English

- lang: fr
  img: https://cdn.countryflags.com/thumbs/france/flag-400.png
  text: French

- lang: zh-CN
  img: https://cdn.countryflags.com/thumbs/china/flag-400.png
  text: Chinese(Simple)

...
```

The first bullet block represents the language that is being displayed as first option in the menu, the second as second etc. If you want to change the order in which the languages appear, just switch to editing mode (the pencil icon), copy the bullet block that you want to move to a different place and paste it to the desired position. 

To remove a language, just delete the respective bullet block.

To add a new language, you need to provide:
- *lang:* followed by an abbrevation of the language (the [following languages and their abbreviations](https://cloud.google.com/translate/docs/languages) are supported
- *img:* a link to a country flag image that will appear in the language menu (links to [country flags](https://www.countryflags.com/) can be found here)
- *text:* the name of the language which will be uised as label in the menu

Don't forget to hit the commit button at the bottom of the page to not lose your changes.

### Customize the banner image
#### Add a new image

Go back to the root repository and head down to the Readme file. The third intervention concerns the banner image. The default image is great and you do not have to change it. In case you wanted to change the image, go to *assets/images/banners/*. The banners folder contains two files: 
- datacamp_certificate_dummy.jpg and 
- home.jpeg

![banners folder](/assets/images/post_images/website_tutorial/banners_folder.png)

home.jpeg is the image that is currently being used as your background banner. Again, no need to change the banner of your website. But if you wanted, you could drop another file into the banner folder. I will do that and add balloon-image.jpg. You should pick whatever image you want. To do so, click *Add file* and select *Upload files*. Now you can drag and drop the image into the folder.

![drop image](/assets/images/post_images/website_tutorial/drop_image.png)

Scroll down and commit the changes. 

#### Link to new image

Head back to the root repository and scroll down to the ReadMe instructions. The second intervention needed for changing the image requires us to make a change in *index.html*. Open index.html by following the link or by navigating your file system.

![index html](/assets/images/post_images/website_tutorial/index_html.png)

The file contains an entry called banner. The value for this entry is the path to *home.jpeg* that we have spotted in the banners folder. Change this path such that it points to the image that you want to use for your website. To do so, click the little pencil button to edit the file. Now replace home.jpeg by the name of your new file.


```HTML
---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Home
banner: "assets/images/banners/home.jpg"
---
```

I will use balloon-image.jpg. You should use the image you have uploaded (or pass a url to an image that is stored somewhere else):

```HTML
---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Home
banner: "assets/images/banners/balloon-image.jpg"
---
```

Scroll down and commit the changes. Done!

### Further customizations

Head back to the root repository. And scroll down to the Readme instructions.

This time, we need to edit some entries in a file called *_config.yml*. Open the file and scroll down a bit.

![config_yml](/assets/images/post_images/website_tutorial/config_yml.png)

We want to change:  *Title* (which will appear in the upper left corner of your website), *Email*, *Author* (name is being used on your blog posts), *Copyright* (appears on the footer of your site), *Description* (appears as description on, e.g., Google when showing your site), and potentially the favicon. You should pass what works best for you, I will make the following changes for my site (note that the code below only shows the entries without comments etc.):

```YAML
title: Tech Expert Academy
email: berlin@techexpertacademy.com
author: TEA
copyright: "Unpublished Work (cleft) {currentYear} {author}"
description: >- # this means to ignore newlines until "baseurl:"
  We offer high quality courses that help you become a tech professional in record time. We also help you to find a job at a great company. You only pay tuition when you get hired.
```

Scroll down, commit the changes and: Done!

### Customize your About page
#### Markdown

Back to the root repository scrolling down to the ReadMe instructions. Only the customisation of the About page is left. We can do this by using Markdown syntax.

Markdown is an easy to use language for creating formatted text. Trust me, if you are not using it already, you will be using it a lot in the future. It is a good investment of your time to get familiar with the basic syntax. There are plenty of good resources online. The Readme instructions link to a good [guide](https://www.markdownguide.org/basic-syntax/). 

Open the guide in a new tab. The syntax is straight forward. For example: to create different levels for headings you can use hashes in front of the line you want to treat as heading. One hash gives you the largest heading size. Two hashes will give you the second largest size. Just scroll a bit through the guide and you will see, that you can do most of the things you usually use for text formatting: Making text bold or italic, creating tables, inserting links, inserting images etc. The text of this tutorial is written in markdown.

The best way to learn is practice! So, let’s get our hands dirty.

#### About.md

Follow the link to about.md (or open the file via your file system) and go to editing mode by clicking the little pencil icon.

```
---
layout: about
title: About
---

## About

Hi, nice to meet you.
```

Currently, the file only says: About Hi nice to meet you. The entries on top of the text page indicate meta information. They are demarcated by three dashes at the top and the bottom. Inside of them we have two variables:
- *layout* refers to the layout used for the about page that is being defined in the *_layouts* folder. Let's not touch it here and leave it as it is
- *title* defines the title that appears on your website's about page.

Everything that follows underneath this header can be formatted by using markdown syntax.

Use the about page to tell the world about yourself, your project or your cause. For communication purposes, it is good practice to break down messages into: 
- *Why?*, 
- *How?* and 
- *What?* 

We will be using these categories as headers by applying three hashes (but do what works best for you). Also, do not forget to tell visitors under Contacts how they can get in touch. This is how the file looks for me after editing:

```
---
layout: about
title: About
---

## Welcome to Tech Expert Academy

### Why

While companies are desperately looking for tech talent, many people are either unemployed or they work in unfullfilling jobs. We want to be the match maker between these two parties. 

### How

We partner with fast growing companies. By knowing their needs in the near future, we know how to best prepare our students to fill these roles. 

### What

At TEA students take a three months intensive training for careers such as Data Engineering, Cloud Solutions etc. They learn at their own pace and have a personal coach checking in with them each week. After the three months period is over, coaches and mentors help to land a job. The classes are free and will be paid back through income share agreements if the student successfully lands a job.

### Contact

You are interested? Check out our [website](https://techexpertacademy.com). If you like what we are doing, [send us](https://www.techexpertacademy.com/#contact-form-main) a link to your GitHub Page and we’ll get back to you soon. Follow us on [LinkedIn](https://de.linkedin.com/company/tech-expert-academy?trk=public_profile_topcard-current-company).
```

And as always: Scroll down and commit the changes. Wonderful! We are almost there.

## Write your first post

Now, back to our root repository and down to our Readme instructions. The last step is about how to add blog posts. 

Follow the link to the *_posts* folder or scroll up and open the _posts folder directly. 

![posts folder](/assets/images/post_images/website_tutorial/posts_folder.png)

We have already two posts in our folder. Look at their names: They follow the same scheme. First, we see a date (year-month-day) followed by a name and the markdown extension:

> year-month-day-postname.md

You have to name your posts according to this convention. Otherwise, they will not be treated as posts. 

> Tip: If you want to work on posts before publishing on your site, add a character like *_* in front of the date and it will not show up on your site. As soon as you want it to be published, remove the character.

Let's open *2021-12-25-my-second-post.md*. When viewing it in editing mode it looks as follows:

```
---
layout: post
title: Introduction to Python
subtitle: Each post also has a subtitle
categories: Python
tags: [Python, intro, certificate]
---

## Introduction to Python

This post is meant to summarize some of the key concepts I have learned in the course *Introduction to Python*


![datacamp certification](/assets/images/banners/datacamp_certificate_dummy.jpg)
```

As you can tell, the file starts with a header demarcated by three dashes at top and bottom containing meta information. Every post you write needs to define these key value pairs.

Let's copy this header. We will need it for our new post. 

Head back to the _posts folder. Click on *Add file* and select *Create new file*.

![add new post to folder](/assets/images/post_images/website_tutorial/add_file_post.png)

Enter a name by following the naming convention for posts.

> year-month-day-postname.md

I will call mine:
- *2022-01-03-my-first-post-this-year.md* 

You should take what works best for you. Let's paste the header at the top of the file and customize the key value pairs. 

- The first entry is **layout**. It defines which layout will be applied to this file when being rendered. This needs to be set to post. 
- The second entry is **title**. This title will be displayed on links to your post and on top of your post's page.
- The third entry is **subtitle**, which will pe displayed underneath your title on the post's page. I will pass; "Quick summary";
- The fourth entry is **categories**. If you want to use multiple categories, you can put the collection into square brackets. Order matters here (going from higher to lower categories from left to right). I will stick to one single category.
- The fifth entry is **tags**. Put the tags that are relevant to your post into square brackets and separate them by commas.

The actual content of the post goes below the header. You can use all the markdown magic you want. I will use an ordered list to summarize the steps of building this site. This is how my file looks after editing:

```
---
layout: post
title: How I've built my website
subtitle: quick summary
categories: Website
tags: [Github, website]
---

1. I created a GitHub account
2. I forked a repository from https://github.com/datamaunz
3. I renamed the forked repository tea-berlin.github.io
4. I edited the files as described in the README.md
5. Now I am writing my first post by following the advice that I got from the README file
```

Scroll down and commit the changes. Done! You first post is going live! Note that it can take a few minutes until the post shows up on your site. If it takes suspiciously long, check the file name and the header (also the file needs to be inside of the *_posts* folder).

## Further Cleanup
### Delete *.github* folder

Let's clean things up a bit further. You do not have to follow these steps but it does not hurt either.

![delete .github folder](/assets/images/post_images/website_tutorial/delete_dot_github_folder.png)


Do you see the *.github* folder at the top of your repository? We don't need it. Open the *.github* folder. In the upper right corner, you find a button showing *...*
Click the button and select *delete directory*. Scroll down and commit the changes. 

Excellent!

### Remove footer info

If you want to cut the information on the footer down to the copyright info, you can do the following. Go to _includes/views/footer.html and click on the little pencil icon to edit the page. 

Delete the lines 15, 16, 17, and 18 so that the following remains:

```HTML
<footer class="site-footer h-card">
  <data class="u-url" href="{{ "/" | relative_url }}"></data>

  <div class="wrapper">
    <div class="site-footer-inner">
        {%- assign currentYear = 'now' | date: "%Y" -%}
        {%- assign copyright = site.copyright
            | replace: '{currentYear}', currentYear
            | replace: '{author}', site.author
            | replace: '(c)', '&copy;'
            | replace: '(p)', '℗'
            | replace: '(cleft)', '<span class="copyleft">&copy;</span>'
        -%}
      <div>{{ copyright }}</div>
    </div>
  </div>
</footer>
```

Scroll down and commit the changes.

## What to do next?

Fantastic! You have finished the tutorial. Just wait a bit until the changes have updated on your website and you are done. Congratulations!

If you liked the tutorial, give us a thumbs up and subscribe to the channel.

Also; please put the website you have built into the comments. If you like what we are doing a Tech Expert Academy, feel free to reach out via our website at techexpertacademy.com. We are always looking for talented students; coaches; and for companies who are looking for talent.

Note; the combination of a Jekyll blog and Github works best when edited via a proper editor. There are plenty of tutorials that you can use to flex your skills. The main idea here was to help you create a website to showcase yourself and your work. From now on, the sky is the limit. 

Good luck!