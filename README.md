# Blog

## Built By [Tom Chege](https://github.com/emdeechege/)

## Description
an application that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.


## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like to:
* View the blog posts submitted.
* Comment on blog posts.
* View the most recent posts
* Alerted when a new post is made by joining a subscription.
* comment on the different pitches and leave feedback.

## Blogger Abilities
These are the behaviours/features that the application implements for use by the writter/Blogger

Bloggers would like to:
* Sign in to the blog
* Create a blog from the application
* Delete comments that I find insulting or degrading
* Update or delete blogs I have created.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Writer/Blogger Authentication | **On demand** | Access Admin dashboard |
| Display blogs by most recent | **Home page** | Clickable links to open all blogs |
| Display profile | **Click profile page** | Redirected to a page with your profile |
| Display single blogs | **On link click** | Blog is displayed with comment ready function plus any comments already stored |
| To add a blog  | **Through Admin dashboard** | Redirected to the new blog form collection form|
| To edit a blog  | **Through Admin dashboard** | Redirected to the  blog form collection form and editing happens|
| To delete a blog/comments  | **Through Admin dashboard and on displays** | Bad comments and posts can be deleted|
| To subscribe  | **On button click** | Users can subscribe on click|


## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
* Requirements.txt

### Cloning
* In your terminal:

        $ git clone https://github.com/emdeechege/peech/
        $ cd peech

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Flask and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ chmod +x start.sh
        $ ./start.sh

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test

## Technologies Used
* Python3.6
* Flask

## License

Copyright (c) 2018 emdeechege

------------

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
