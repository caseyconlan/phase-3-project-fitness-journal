# Phase 3 CLI Project Template

## Learning Goals

- Discuss the basic directory structure of a CLI.
- Outline the first steps in building a CLI.

***

## Introduction

You now have a basic idea of what constitutes a CLI, but you (understandably!)
likely don't have the best idea of where to start. Fork and clone this lesson
for a template for your CLI. Take a look at the directory structure before we
begin:

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py
    ├── db
    │   ├── models.py
    │   └── seed.py
    ├── debug.py
    └── helpers.py
```

> **Note: You may already know some or all of the material covered in this
> lesson. We hope that having it all in one place will help you in designing
> and developing your project, regardless of where you're starting off.**

***

# Fitness Journal
The Fitness Journal is a command-line application that allows users to track their fitness activities, log their food intake, and monitor their BMI (Body Mass Index). It provides a simple and convenient way to keep a record of your fitness journey.

## Description
The Fitness Journal is designed to help individuals maintain a healthy and active lifestyle by providing a platform to track their fitness progress. It allows users to log various aspects of their fitness routine, including exercise activities, food intake, and BMI measurements. The program offers features such as user registration and login, enabling each user to have a personalized and secure journal.

With the Fitness Journal, users can record details about their daily exercise routines, such as the type of exercise, duration, repetitions, and sets. They can also log their food consumption by entering information about the food items consumed, including the type of food and its calorie count. Additionally, users can input their height and weight to calculate their BMI automatically, helping them monitor their overall health and progress.

The program provides a user-friendly interface where users can easily navigate through the menu options to perform various journaling tasks. It also offers summaries of fitness and food logs, giving users insights into their progress and enabling them to make informed decisions regarding their health and fitness goals.

## Features
User Registration: New users can create an account by providing a unique username and password.
User Login: Existing users can log in using their username and password.
Fitness Log: Users can record their daily fitness activities, including exercise type, duration, and notes.
Food Log: Users can log the food they consume each day, including the type of food and its calorie count.
BMI Calculation: Users can enter their height and weight to calculate their BMI automatically.
Journal Entry: Users can add additional notes or journal entries to track their progress and thoughts.
Summaries: Users can view summaries of their fitness and food logs, including total calories burned and consumed for a specific date.

## Installation

Clone the repository to your local machine:
git clone https://github.com/your_username/fitness-journal.git

Navigate to the project directory:
cd fitness-journal

Create a virtual environment:
python -m venv venv
Activate the virtual environment:

For Windows:
venv\Scripts\activate

For macOS and Linux:
source venv/bin/activate

Install the required dependencies:
pip install -r requirements.txt

Run the application:
python lib.cli

## Usage
Upon running the application, you will be presented with a menu of options to register a new user, log in, and perform various fitness journal operations. Use the arrow keys to navigate the menu and press Enter to select an option.

Follow the on-screen prompts to enter the required information for each operation, such as recording fitness activities, logging food intake, and entering height and weight for BMI calculation.

Enjoy using the Fitness Journal to track your fitness progress and stay motivated!

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.

Before submitting a pull request, please ensure that your code adheres to the project's coding style and conventions.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Where Do I Start?

This project will likely be one of the biggest projects you've undertaken so
far. Your first task should be creating a Git repository to keep track of your
work and roll back any undesired changes.

### Removing Existing Git Configuration

If you're using this template, start off by removing the existing metadata for
Github and Canvas. Run the following command to carry this out:

```console
$ rm -rf .git .canvas
```

The `rm` command removes files from your computer's memory. The `-r` flag tells
the console to remove _recursively_, which allows the command to remove
directories and the files within them. `-f` removes them permanently.

`.git` contains this directory's configuration to track changes and push to
Github (you want to track and push _your own_ changes instead), and `.canvas`
contains the metadata to create a Canvas page from your Git repo. You don't have
the permissions to edit our Canvas course, so it's not worth keeping around.

### Creating Your Own Git Repo

First things first- rename this directory! Once you have an idea for a name,
move one level up with `cd ..` and run `mv python-p3-cli-project-template
<new-directory-name>` to change its name.

> **Note: `mv` actually stands for "move", but your computer interprets this
> rename as a move from a directory with the old name to a directory with
> a new name.**

`cd` back into your new directory and run `git init` to create a local git
repository. Add all of your local files to version control with `git add --all`,
then commit them with `git commit -m'initial commit`. (You can change the
message here- this one is just a common choice.)

Navigate to [GitHub](github.com). In the upper-right corner of the page, click
on the "+" dropdown menu, then select "New repository". Enter the name of your
local repo, choose whether you would like it to be public or private, make sure
"Initialize this repository with a README" is unchecked (you already have one),
then click "Create repository".

Head back to the command line and enter `git remote add <project name> <github
url>`. This will map the remote repository to your local repository. Finally,
push your first commit with `git push -u origin main`.

Your project is now version-controlled locally and online. This will allow you
to create different versions of your project and pick up your work on a
different machine if the need arises.

***

## Generating Your Pipenv

You might have noticed in the file structure- there's already a Pipfile! That
being said, we haven't put much in there- just Python version 3.8 and ipdb.

Install any dependencies you know you'll need for your project, like SQLAlchemy
and Alembic, before you begin. You can do this straight from the command line:

```console
$ pipenv install sqlalchemy alembic
```

From here, you should run your second commit:

```console
$ git add Pipfile Pipfile.lock
$ git commit -m'add sqlalchemy and alembic to pipenv'
$ git push
```

Now that your environment is set up, run `pipenv shell` to enter it.

***

## Generating Your Database

Once you're in your environment, you can start development wherever you'd like.
We think it's easiest to start with setting up your database.

`cd` into the `lib/db` directory, then run `alembic init migrations` to set up
Alembic. Modify line 58 in `alembic.ini` to point to the database you intend to
create, then replace line 21 in `migrations/env.py` with the following:

```py
from models import Base
target_metadata = Base.metadata
```

We haven't created our `Base` or any models just yet, but we know where they're
going to be. Navigate to `models.py` and start creating those models. Remember
to regularly run `alembic revision --autogenerate -m'<descriptive message>'` and
`alembic upgrade head` to track your modifications to the database and create
checkpoints in case you ever need to roll those modifications back.

If you want to seed your database, now would be a great time to write out your
`seed.py` script and run it to generate some test data. You may want to use
Pipenv to install Faker to save you some time.

***

## Generating Your CLI

A CLI is, simply put, an interactive script. You can run it with `python cli.py`
or include the shebang and make it executable with `chmod +x`. It will ask for
input, do some work, and accomplish some sort of task by the end.

Past that, CLIs can be whatever you'd like. An inventory navigator? A checkout
station for a restaurant? A choose-your-adventure video game? Absolutely!

Here's what all of these things have in common (if done well): a number of
`import` statements (usually _a lot_ of import statements), an `if __name__ ==
"__main__"` block, and a number of function calls inside of that block. These
functions should be kept in other modules (ideally not _just_ `helpers.py`)

There will likely be some `print()` statements in your CLI script to let the
user know what's going on, but most of these can be placed in functions in
other modules that are grouped with others that carry out similar tasks. You'll
see some variable definitions, object initializations, and control flow
operators (especially `if/else` blocks and `while` loops) as well. When your
project is done, your `cli.py` file might look like this:

```py
from helpers import (
    function_1, function_2,
    function_3, function_4,
    function_5, function_6,
    function_7, function_8,
    function_9, function_10
)

if __name__ == '__main__':
    print('Welcome to my CLI!')
    function_1()
    x = 0
    while not x:
        x = function_2(x)
    if x < 0:
        y = function_3(x)
    else:
        y = function_4(x)
    z = function_5(y)
    z = function_6(z)
    z = function_7(z)
    z = function_8(z)
    function_9(z)
    function_10(x, y, z)
    print('Thanks for using my CLI')

```

***

## Updating Your README.md

`README.md` is a Markdown file that describes your project. These files can be
used in many different ways- you may have noticed that we use them to generate
entire Canvas lessons- but they're most commonly used as homepages for online
Git repositories. **When you develop something that you want other people to
use, you need to have a README.**

Markdown is not a language that we cover in Flatiron's Software Engineering
curriculum, but it's not a particularly difficult language to learn (if you've
ever left a comment on Reddit, you might already know the basics). Refer to the
cheat sheet in this lesson's resources for a basic guide to Markdown.

## Conclusion

A lot of work goes into a good CLI, but it all relies on concepts that you've
practiced quite a bit by now. Hopefully this template and guide will get you
off to a good start with your Phase 3 Project.

Happy coding!

***

## Resources

- [Setting up a respository - Atlassian](https://www.atlassian.com/git/tutorials/setting-up-a-repository)
- [Create a repo- GitHub Docs](https://docs.github.com/en/get-started/quickstart/create-a-repo)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
- [Calculating BMI](https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_2.html#:~:text=Formula%3A%20weight%20(lb)%20%2F,a%20conversion%20factor%20of%20703.)
- [Python Best Practices] - Beginner's Step-by-Step Guide Coding Course - Penguin Randomhouse Publishing

