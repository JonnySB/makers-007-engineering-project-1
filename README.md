# Flask HTML Web & Database Project Starter

This is a starter project for you to use to start your Flask HTML web & database
projects.

It contains quite a lot of example code. You can use this to see how the various
parts of the project work, or you can delete it and start from scratch.

There are two videos to support:

- [A demonstration of setting up the project](https://www.youtube.com/watch?v=YStsRfMVx44&t=0s)
- [A walkthrough of the project codebase](https://www.youtube.com/watch?v=YStsRfMVx44&t=314s)

## Setup

```shell
# Clone the repository to your local machine
; git clone https://github.com/JonnySB/makers-007-engineering-project-1.git

; cd makers-007-engineering-project-1

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell

# Install the virtual browser we will use for testing
; playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
; createdb MAKERS_BNB
; createdb MAKERS_BNB_test

# Open lib/database_connection.py and change the database names
; open lib/database_connection.py

# Seed the development database (ensure you have run `pipenv shell` first)
; python seed_dev_database.py

# Run the tests (with extra logging)
; pytest -sv

# Run the app
; python app.py
# Now visit http://localhost:5001/emoji in your browser
```

If you would like to remove the example code:

```shell
; ./remove_example_code.sh
```

# Guide for using Git/GitHub

## 1.  Add all your files, commit and push to your branch.

When in the branch you're working in, and you're happy with all your changes, use the following:
```shell
```shell
git add .
git commit -m "Your commit message"
git push
```

## 2. Checkout to main and pull any changes from main

Switch to the main branch and pull any changes from there:
```
git checkout main

git pull origin main
```

For example:
```shell
➜  makers-007-engineering-project-1 git:(story-2-list-spaces) git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
➜  makers-007-engineering-project-1 git:(main) git pull
remote: Enumerating objects: 66, done.
remote: Counting objects: 100% (62/62), done.
remote: Compressing objects: 100% (28/28), done.
remote: Total 42 (delta 23), reused 33 (delta 14), pack-reused 0
Unpacking objects: 100% (42/42), 9.66 KiB | 309.00 KiB/s, done.
From https://github.com/JonnySB/makers-007-engineering-project-1
   e548da6..086f6bf  branch_user_story1 -> origin/branch_user_story1
   f245360..eb5efea  story_7            -> origin/story_7
Already up to date.
```

## 3. Checkout to your branch and merge it with the main branch

Switch to your branch and merge it with the main branch.
```shell
git checkout your-branch-name

git fetch
git merge origin/main
```

For example:
```shell
➜  makers-007-engineering-project-1 git:(main) git checkout story-2-list-spaces
Switched to branch 'story-2-list-spaces'
Your branch is up to date with 'origin/story-2-list-spaces'.
➜  makers-007-engineering-project-1 git:(story-2-list-spaces) git fetch
➜  makers-007-engineering-project-1 git:(story-2-list-spaces) git merge origin/main
Merge made by the 'ort' strategy.
 lib/booking.py        | 15 +++++++++++++--
 lib/users.py          | 12 ++++++++++++
 tests/test_booking.py | 19 +++++++++++++++++++
 3 files changed, 44 insertions(+), 2 deletions(-)
 create mode 100644 lib/users.py
 create mode 100644 tests/test_booking.py
```

## 4. Retest all your code with the new changes from main

Once you've merged your branch with the main, open your virtual environment and retest all your code with **pytest** and also **checking the html pages are working appropriately**.

For example:
```shell
➜  makers-007-engineering-project-1 git:(story-2-list-spaces) pipenv shell
Launching subshell in virtual environment...
 . /Users/mattwshepherd/.local/share/virtualenvs/makers-007-engineering-project-1-Tkx7Kyu9/bin/activate
➜  makers-007-engineering-project-1 git:(story-2-list-spaces)  . /Users/mattwshepherd/.local/share/virtualenvs/makers-007
-engineering-project-1-Tkx7Kyu9/bin/activate
(makers-007-engineering-project-1) ➜  makers-007-engineering-project-1 git:(story-2-list-spaces) pytest
================================================== test session starts ==================================================
platform darwin -- Python 3.11.2, pytest-7.4.3, pluggy-1.3.0
rootdir: /Users/mattwshepherd/Documents/MakersCode/06_engineering_project_1/makers-007-engineering-project-1
plugins: xprocess-0.23.0, playwright-0.4.3, base-url-2.0.0
collected 8 items

tests/test_app.py .                                                                                               [ 12%]
tests/test_booking.py ..                                                                                          [ 37%]
tests/test_database_connection.py .                                                                               [ 50%]
tests/test_space.py ...                                                                                           [ 87%]
tests/test_space_repository.py .                                                                                  [100%]

=================================================== 8 passed in 1.90s ==================================================
➜  makers-007-engineering-project-1 git:(story-2-list-spaces)  . /Users/mattwshepherd/.local/share/virtualenvs/makers-007
-engineering-project-1-Tkx7Kyu9/bin/activate
(makers-007-engineering-project-1) ➜  makers-007-engineering-project-1 git:(story-2-list-spaces) python app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5001
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 114-236-802
127.0.0.1 - - [10/Jan/2024 10:54:48] "GET /spaces?vscodeBrowserReqId=1704884088786 HTTP/1.1" 200 -
^C%
```

If you're happy and there are no changes, exit your virtual environment.

For example:
```shell
(makers-007-engineering-project-1) ➜  makers-007-engineering-project-1 git:(story-2-list-spaces) exit
```

If there were changes, **repeat step 1**.

## 5. Push your final changes

Push your final changes when you're happy.

```shell
git push origin your-branch-name
```

Or if you're in your branch, just use
```shell
git push
```

## 6. Open up a pull request

If you've successfully completed **steps 1-5**, and would like your branch to be merged onto the main branch, open up a **pull request** and ask for your team to review it.

>[!CAUTION] 
>Make sure you do not just merge the changes to main yourself! Ensure everyone has reviewed and approved your code first

If there are any issues with your code, make the appropriate changes and **repeat steps 1-5.**

>[!NOTE]
>If you have opened a pull request, any commits after that will be shown in that pull request so ensure your pull request is reviewed before you continue working on that branch.





<!-- END GENERATED SECTION DO NOT EDIT -->
