Contributing guidelines
=======================

We are glad that you chose this organization to give your time to and contribute. Thank you for your interest in contributing to OpenWISP.

Settings things up
------------------

Please follow up the instructions in the README of the repository to which you want to contribute to, so that you can set up the project.

Finding Something to Work
-------------------------

Visit any repository and then to try to explore the project's codebase. Use it and give us your opinion about any change that might be helpful to you as well as to us. If you find any bug or error or something that is worth mentioning please create an **issue** regarding that bug or error.

If you are unable to find anything on your own to be worked upon, don't worry we got your back. Visit that project's **Issues** tab and explore those issues that might interests you, comment on the issue thread and we'll help you get along with that.

If neither of the above works for you, please post your views on our `gitter channel. <https://gitter.im/openwisp/general>`_

Steps to Submit your Code or Changes
------------------------------------

Our main development branch is master it's our central development branch. Your code should be pushed from a different branch and then it is merged into master after proper review from the project maintainers.

1. Create a new branch for your development and a self-descriptive branch name.
    
    git pull origin master
    git checkout master
    git checkout -b your-branch-name

2. Commit and push code of your branch:

- Commits should be descriptive in nature, the message should be self-explanatory.
- Please make sure your code is following our coding style or our project's style. Code should be well formatted.
- Before committing and pushing the changes , test the code on your local machine first.
- After pushing your branch code, make a Pull Request of that corresponding change of yours which should contain a descriptive meassage and mention the issue number too(if there is one). Example- "Fixes #123".

    git commit -m "your message here"
    git push <remote name> <branch name>

3. After pushing the code make your Pull Request:

- From your forked repository of the project select your branch and click "New Pull Request". Check if everythind is accordingly and write a descriptive meassage for the PR.
- After submitting your PR, check back again whether your PR has passed our required tests. If the tests fails check what the eroor is andask for help if you don't understand what the error is.
- If the tests are passed maintainers will review the PR and will ask you to change anything as and when required.
- Once everything is fine with us we'll merge your Pull Request.

Thanks for contributing to our organization :) .
