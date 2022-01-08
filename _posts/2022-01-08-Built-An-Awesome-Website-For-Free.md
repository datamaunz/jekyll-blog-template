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
### 1. Create a free Github account

![Sign up](/assets/images/post_images/website_tutorial/sign_up.png)

First, we have to create a Github account. Go to [GitHub](https://github.com) and hit the sign-up button in the upper right corner. Enter an email address, a password, and a username. As mentioned before, you will not have to pay for your website, not even for the domain, because Github provides you with a subdomain, which will be constructed from your username. This is why the choice of your username is kind of important. I will go with *tea-berlin*. You should use yours. 

Now we are being asked whether we want to receive product updates and announcements and we'll have to solve a quick puzzle to verify that we are humans. You'll receive a verification code that you need to enter via email, we skip the personalisation. And: Done!

Congratulations! You have a Github account!

### 2. Fork the repo with the template

![skip intro](/assets/images/post_images/website_tutorial/skip_introduction.png)

Here you can introduce yourself to those visiting your account. You should definitely do that! But for now we will skip it because we want to learn how to create our amazing website. Click “Dismiss This”, open a new tab and go to [jekyll-blog-template](https://github.com/datamaunz/jekyll-blog-template).

![fork repo](/assets/images/post_images/website_tutorial/fork_datamaunz_repo.png)

Now we are on the Github account of Datamaunz. And more precisely, we are seeing the repository called *Jekyll blog template*. 

It contains various folders and files. But no worries. In order to transfer all these files into our own Github account, we just have to go to the upper right corner and click on “Fork”.

Now a fork is being created. This fork is a copy of the original repository that will appear in our own account. And: Here we go! 

![go to settings after forking](/assets/images/post_images/website_tutorial/go_to_settings_adter_forking.png)

As you can see, we are now in our own Github account; and more precisely. We are in our own repository called “Jekyll blog template”.

To make this our website, we have to change the name of this repository. To do so, go to settings.

By convention, Github repositories that are named by the name of the Github account; followed by "dot", “GitHub”, "dot", "i o", will be treated as websites by Github. In our case, this is "tea", "minus", "Berlin", "dot", “GitHub”, "dot", i o.


Change the entry for "repository name" accordingly; and hit "rename".


If you have followed the Tutorial up to this point, your repository should now have the name that you have selected as username for your Github account; and this name is being followed by; “dot”, “GitHub”, “dot”, “io”. This is also the address to your website. Open a new tab; and enter the name of your repository. In my case, this is “tea”, “minus”, “berlin”, “dot”, Github, “dot”, io.

Hit enter. It might take a few minutes until the changes will have propagated. 

BAEHM! 

We have our own website! 

Isn't that amazing?!

And users can pick their favorite language to view your site. We will later see how to customise the choices in this menu.

Let’s scroll down to the ReadMe Page. It shows all the steps that are required to customise your page. You only have to follow the links to access the respective files. Note; you could also access the files directly. But we will be using the links to make it as easy to follow as possible.


First, let’s thank the creator of this amazing template, Jeffreytse, by following the link. The link brings us to the original repository. We have forked the repo from the Datamounz account. But Datamounz got it from here. Datamounz simplified it a bit and added the Readme to make it easier for people like us. However, the actual work comes from Jeffreytse. You can show your appreciation by clicking the star for this repository.


Now, let’s go back to our own repository and personalize the contents.

When looking at our website, you can see that it currently says; “your awesome title”; and; “your awesome subheading”. 

Go to _data/defaults dot yaml. The goal is to change the values for heading and subheading. In order to do so, you have to click on the little pencil icon. This puts the interface into editing mode. Note; this is not how experienced developers use Github. They would do the changes via an Editor different from Github and commit the changes to some branch and merge them into the main branch that we are currently on. However, for our current purpose it is okay to use this graphical user interface. You will learn in another lesson how to use Github more efficiently. 

For heading, we will pass the value; “Tech Expert Academy”. You might want to put your own name there; or the name of your project; or whatever you think represents your intentions best. Make sure to put this value into quotation marks. The result should read; "heading"; "colon"; "quotation mark"; your new heading; "quotation mark”. 

Now, change the value of subheading in the same fashion. We will pass; "Land a tech job in just 6 months”. 

You should put your own slogan there. Again; use quotation marks and don’t mess up the syntax of the file.


Now; scroll down to the bottom of the page and smash the Commit button.

Congratulations! You have committed your first changes! This is huge. Github is a version control system. Changes are documented in the form of such commits. This means, based on your history of commits, you can restore earlier versions of your repository. This comes in handy when you; or someone else; have messed up.

Now; let’s make some more changes to our website. Go back to your root repository; and scroll down to the Readme file. 

The second change is about the menu for automated translations. You do not have to make any changes here; if you want to keep the current state. But I want to show you nonetheless how to make such changes when needed.

In order to go to the respective file, click on  _data/translate_langs; dot; yaml


As you can see; each language option is represented by one bullet point taking up three lines. One line for language; one for image; and one for text. Links to the respective abbreviations and country flags will be put down in the comments section below.

Instead of adding a new language, we will just move up the entry for Arabic into the second position.


To be able to edit the file; we have to go again to the pencil icon. Now copy and cut the entry and paste it into the second position. 

Scroll down; and commit the changes. 

Now; let’s go back to the root repository and head down to the Readme file. The third intervention concerns the banner image. 

Again; the default image is great and you do not have to change it. But just in case; if you wanted to change the image, click the link assets/images/banners. This will bring you to a folder that should contain two files: datacamp_certificate_dummy.jpg; and home.jpeg



home.jpeg is currently being used as your background banner; as you can see when opening the file. Again, no need to change the banner of your website. But if you wanted, you could drop another file into the banner folder. I will do that and add; balloon minus image.jpg



As always; we scroll down and commit the changes. 

Now; we head back to the root repository. Scroll down to the Readme instructions. The second intervention needed for changing the image requires us to make a change in index.html. Hit the link.


As you can see; there is an entry called banner. The value for this entry is the path to the home.jpeg file that we have spotted in the banners folder. All you have to do is to change this path such that it points to the image that you want to use for your website. 

Click the little pencil button to edit the file. Now replace home.jpeg by the name of your new file.

In my case; the name of the new file is; balloon minus image.jpg

In your case; the name might be different; if you want to change the image at all;

Make sure that you keep the part of the path that points to the banners folder; assets/images/banners;

Scroll down and commit the changes.

Done!


Let’s check how the website looks now. Note that it might take a few minutes until the changes have propagated. 

And; voilà! Looking great! But note; the upper left corner still shows; “your awesome title”;

We want to change that. So head back to the root repository. And scroll down to the Readme instructions.

This time, we need to edit the
Title;
Email;
Author;
Copyright;
Description;
And potentially the favicon

In a file called; _config; dot; yaml;

To open the file, follow the respective link. 


As you can see; all the entries are here.
Title; Email; Author; Copyright; Description; and the favicon.


As always; click at the little pencil icon to edit the file;

Add a value to the title. I will go for; Tech Expert Academy

Then enter an email address. My address is; berlin@techexpertacademy.com

Add a name for the author; my name will be the abbreviation of Tech Expert Academy; which is T; E; A;

For the copyright line; I will just remove the starting year, since we will be starting the blog this year; Do what works best for your blog though.

Now, we only need a description. I will copy the description we have on our website at techexpertacademy.com:

We offer high quality courses that help you become a tech professional in record time. We also help you to find a job at a great company. You only pay tuition when you get hired.

Now; I replace the current description with this new text. Obviously; you should take your own description.

For the moment, I do not want to select a favicon. So; I leave it as it is, scroll down; and commit my changes. Done!


Back to the root repository; I scroll down to the Readme instructions. Only the customisation of the About page is left


According to the Readme instructions; we should now customise our about page. We can do this by using Markdown syntax.

Markdown is an easy to use language for creating formatted text. Trust me, you will be using it a lot in the future. It is a good investment of your time to get familiar with the basic syntax. There are plenty of good resources online. Here in the Readme instructions; you can find a link to a good guide. 


Let’s open the guide in a new tab. 

The syntax is straight forward. For example; to create different levels for headings; you can use hashes. One hash gives you the largest heading size. Two hashes will give you the second largest size; etc

Just scroll a bit through the page and you will see, that you can do most of the things you usually use for text formatting; making text bold or italic; creating tables; inserting links; inserting images; etc.

The best way to learn is practice! So, let’s get our hands dirty.


Follow the link to; about; dot; md.

As you can see; it currently shows; "About"; "Hi nice to meet you".

Let's verify this on the actual website. Clicking at; about; in the menu; brings us to the page. Nothing surprising here. Let's go back to the tab of our repository and improve the content of our page. 

As always; click the little pencil icon to enter the editing mode.

We want to tell the world what our site is about. You can write about yourself; or about your project.




Remember; two hashes will give you the second largest heading.

Instead of ## About; I will write ## Welcome to Tech Expert Academy

For communication purposes; it is good practice to break down messages into; "Why?"; "How?"; and ; "What?"; we will be using these categories as headers by applying three hashes. 



To answer the first question; "Why are we doing what we are doing?"; We will pass;

While companies are desperately looking for tech talent, many people are either unemployed or they work in unfullfilling jobs. We want to be the match maker between these two parties. 

And; "How are we doing that?"

We partner with fast growing companies. By knowing their needs in the near future, we know how to best prepare our students to fill these roles. 

What precisely do we offer?

At Tech Expert Academy students take a three months intensive training for careers such as Data Engineering, Cloud Solutions etc. They learn at their own pace and have a personal coach checking in with them each week. After the three months period is over, coaches and mentors help to land a job. The classes are free and will be paid back through income share agreements if the student successfully lands a job.


Let's add one more section; telling people how to contact us. 





### Contact

You are interested? Check out our [website](https://techexpertacademy.com). If you like what we are doing, [send us](https://www.techexpertacademy.com/#contact-form-main) a link to your GitHub Page and we’ll get back to you soon. Follow us on [LinkedIn](https://de.linkedin.com/company/tech-expert-academy?trk=public_profile_topcard-current-company).

We are using the syntax for links. You can read up on it in the markdown guide or just infer it from what you can see here.

Now; scroll down and commit the changes. 

Wonderful! We are almost there.

Now; back to our root repository and down to our Readme instructions. 

The last step is about how to add blog posts. 

You could follow the link to the _posts folder. Or; you just scroll up and open the _posts folder directly.

We have already two posts in our folder. Look at their names; They follow a particular scheme. First, we see a date. The date consists of; year; minus; month; minus; day. 

This date is being followed by a name and the markdown extension. 

You have to name your posts according to this convention. Otherwise, they will not be treated as posts. 



Let's click at "my second post".

As you can tell; there is a table at the very top. You might have noticed this already in other files as well. This table will not show up on the post itself. Rather, it contains important meta information.

Let's head to the little pencil icon to switch to editing mode.

At the top of the page, we see a header that contains the meta information we were talking about. It is delineated by three dashes at the top and three dashes at the bottom. 

Let's copy this header. We will need it for our new post. 


Head back to the _posts folder. Click on; "Add file"; and select; "Create new file".

Enter a name by following the naming convention that we have discussed before.

Start with the year. 2022. Minus. The month. 01. Minus. The day. 03. Minus. The name that you want to use for the file. I will go with first post this year. Add the markdown extension. .md.

Obviously, you should be using the date of the day you are creating the post.



Now, let's paste the header at the top of the file.

The first entry is layout. It defines which layout will be applied to this file when being rendered. This needs to be set to post. 

The second entry is; title. I will call it; "How I have built my website."

The third entry is; subtitle. I will pass; "Quick summary";

The fourth entry is; categories; I will call it; "Website";

The fifth entry is; tags; Put the tags that are relevant to your post into square brackets and separate them by commas. I will use; "Github" and "Website".

The information in the header look great. Let's move on to write the post.

Let's start with a level 2 header starting with three hashes. 

I will call it; How I've built my website.

Then I will use an ordered list to explain the steps. Ordered lists can be simply created by using ordinal numbers in the following fashion.

1. I created a GitHub account
2. I cloned a repository from github.com/datamounz
3. I renamed the cloned repository tea-berlin.github.io
4. I edited the files as described in the README.md
5. Now I am writing my first post by following the advice that I got from the README file

Scroll down and commit the changes.

Excellent! Let's head over to the website. 

The post is not there yet. As always, it might take some time for the changes to propagate to our site.

In the meantime, we can already look at our other pages. Head to; about.

Beautiful! Looks great!

At the side, we even have a Table of Contents. It automatically picks up the headers and links to the respective segments. By the way; the same happens in our posts.


Let's test whether or not the toggle between light and dark mode works. 

Nice!

What about the automatic translations?

Works also as desired. Great job!


Okay; enough time should have passed for the website to update.

Great! Our new post is online. Let's open the post to see how it looks.


Looking great. Only the duplication of the heading bothers me. 

Let's go back to our repository opening the _posts folder. Open the post we just created. The title is already in the header. We do not need the heading in the content section. 

So let's delete it; 


Scroll down; commit the changes and go back to the root repository.


Let's clean things up a bit further. You do not have to follow these steps; but trust me, it will make things cleaner.

Do you see the dot github folder at the top of your repository? We don't need it. Let's get rid of it.

Open the dot github folder. In the upper right corner, you find a button with three dots. Click the button and select; "delete directory". Scroll down and commit the changes. 

Excellent!

If you want to cut the information on the footer down to the copyright info, you can do the following. Open the _includes folder. Then open the views folder. And open footer.html.


Go to the little pencil icon to edit the page. 

Delete the lines 15; 16; 17; and 18.

Scroll down and commit the changes.


Fantastic! You have finished the tutorial. Just wait a bit until the changes have updated on your website and you are done. Congratulations!

If you liked the tutorial, give us a thumbs up and subscribe to the channel.

Also; please put the website you have built into the comments. If you like what we are doing a Tech Expert Academy, feel free to reach out via our website at techexpertacademy.com. We are always looking for talented students; coaches; and for companies who are looking for talent.

Note; the combination of a Jekyll blog and Github works best when edited via a proper editor. There are plenty of tutorials that you can use to flex your skills. The main idea here was to help you create a website to showcase yourself and your work. From now on, the sky is the limit. 

Good luck!









Balloon-image.jpg







Language adjustments:

https://www.countryflags.com/
https://www.labnol.org/code/19899-google-translate-languages



