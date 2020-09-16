# Welcome to the HackMIT 2020 Beginner Workshop!

<img src="https://i.ibb.co/dgdbd2K/with-rails.png" alt="with-rails" width="100%" border="0" />

## Important Notes
* If you plan on attending the workshop, please make sure to complete [**Pre-Workshop Setup**](#pre-workshop-setup) before the event!
* If you want to submit to the **Beginner** track at HackMIT, you must have attended at least one of the beginner workshops!

## Overview
The HackMIT 2020 Beginner Workshop will be a crash course into the basics of creating a web app. In three 1 hour sessions, we will teach you the basics of creating a webpage, writing a backend, using databases, calling 3rd party APIs, and how to tie them all together. 

**Topics**

The breakdown of topics for each workshop:
1. Friday, 12:00 AM: Workshop 1
    * Intro to using Git
    * Creating a frontend with HTML/CSS
2. Saturday, 10:00 PM: Workshop 2
    * Creating a backend with Flask
    * Connecting it all with Javascript
3. Saturday, 11:15 PM: Workshop 3
    * Using databases
    * Intro to APIs

**Prerequisites**: 
* You should have some fundamental coding knowledge, on the level of AP Computer Science or a college introduction CS course is more than enough.
* You should have some familiarity with Python. Python fundamentals will not be taught
* Finish all the steps of **Pre-Workshop Setup** (below) before the event


**Workshop Structure and Resources**
* The slides for the workshop can be found at [go.hackmit.org/beginner-slides](https://go.hackmit.org/beginner-slides)
* This repository will be used as your starting off point. You will build your app off of here
* We will also provide a repository of the final code from each of the workshops for your future reference

# Pre-Workshop Setup
#### 1. Setup Github
Make sure you have github installed on your computer.

[Setup Instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

You can test this by opening your terminal (or git bash in the case of Windows) and typing: 
`git --version`
You should see a printout similar to
`$ git version 2.17.1`

#### 2. Navigating the Terminal (or Command Prompt)
If you are not familiar with using your Terminal (or Git Bash in the case of Windows), here are some good [starter instructions](https://www.macworld.com/article/2042378/master-the-command-line-navigating-files-and-folders.html).
At the very minimum, you will need to know how to:
* navigate your filesystem with `cd`
* show current files in directory with `ls`
* run basic commands like `python <python file>`

#### 3. Setup SSH Key (optional)
There are two ways to link to Github repositories: HTTP and SSH. Using HTTP requires no setup but will require you to enter your username and password each time you want to push changes online. SSH gets around this. 

[Setup an SSH Key](https://docs.github.com/en/enterprise/2.15/user/articles/adding-a-new-ssh-key-to-your-github-account) on your computer

Adding an ssh key to your computer allows you to interface with git easier, but is not required. If you're stuck on this, move on!

#### 4. Clone this Repo

Click the big green "Clone" button on the right. Choose either "Clone with SSH" if you have it set up or "Clone with HTTPS" otherwise and copy the link

Run `git clone <link>` in your terminal under a directory of your choice

#### 5. Setup Python3
[Setup Instructions](https://www.python.org/downloads/)

You can test by running in your terminal
`python --version`

Make sure you have Python 3.x installed!

**Note**: If you have python 3 installed but `python --version` gives you a Python 2.x version, make sure `python3 --version` gives you a Python 3.x version. Substitute all future calls to `python` with `python3`

#### 6. Pip
[Setup Instructions](https://pip.pypa.io/en/stable/installing/)

In your terminal, run: `pip --version` or `pip3 --version` and make sure you get a printout. Make sure to use the pip version that corresponds to your python 3 version:

Example output: `pip 19.2.3 from /home/<path to python>/python3.8/site-packages/pip (python 3.8)`


#### 7. Install Requirements File
In your terminal, navigate to the root directory of this repository. 

Run `pip install -r requirements.txt` in the command line to install all of the requirements contained in this file.

#### 8. Install Postman
Postman is an application that allows you to easily format requests to API endpoints. We will be using it to debug our backend endpoints, and it may be useful for any future backend development.

[Setup Instructions](https://www.postman.com/downloads/)

#### 9. Check that everything is installed
In the root directory of the repo, run:

`python run.py`

It should run without errors. Navigate to `localhost:5000` in a web browser. You should see "Hello World" printed on the page. This means you have succesfully completed setup. See you at the workshop!

## Troubleshooting

If you are having trouble setting up, or have any questions about the workshop, feel free to email **help@hackmit.org** or join our [Event Slack](https://join.slack.com/t/hackmit2020/shared_invite/zt-gjlojqk6-vwId_VUJpCS3ZcAmxr_3sQ) and use the *#beginner* channel.
