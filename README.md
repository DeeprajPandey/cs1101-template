# Problem Set 0

This problem set is ungraded and is set up to help you get acquainted with the submission workflow. Follow the steps and email [course staff](mailto:csphy1101@ashoka.edu.in?subject=[GitHub]%20A0%20Query) if you have any questions.

### Setup

Clone this repository and open the directory. Here, `<USERNAME>` is your GitHub username.

```sh
$ git clone https://github.com/CS1101-Spring2021/pset0-<USERNAME>.git
$ cd pset0-<USERNAME>/
```

Create a new branch and switch to it

```sh
$ git checkout -b submission0
```

### Working on your Solution

There are two commands you will need to work on your submission. To compile, link, and create the executable, use

```sh
$ make addition
```

To delete the obj file and the executable,

```sh
$ make clean
```

### Grading

The pset comes with an autograder with a few public test cases to help you with your solution. There will be more hidden test cases that your program will have to pass for full credit.

To set up the grader, run the following command only _once_.
```sh
$ make init_grader
```

After the autograder has been set up, you can use the following command to check your code with the provided test cases
```sh
$ make grade
```

### Snapshots

Work on your solution on this branch. You can check which files were modified with the status command.

```sh
$ git status
```

Every once in a while, commit your work. <details><summary>Committing is a two-step process.</summary>

<ul>
<li>Add specific files to the staging area. You can specify multiple files too.

```sh
$ git add addition.c
```
  
You can also add all the files which were modified (be careful). It's good practice to specify the files you want committed and write targeted commit messages for your changes

```sh
$ git add .
```
</li>

<li>Commit your changes

The `-m` flag adds a message for your commit. You write your message in double quotes following the flag. For an example of where the message shows up, check this commit [6eaa760](https://github.com/DeeprajPandey/cs1101-template/commit/6eaa760e5603d62d78b00d8e26dc3bcfd5d3e632).

```sh
$ git commit -m "Add print statement"
```
</li>
</ul>
</details>

<details><summary>Push all your commits to the remote repo.</summary>

_Use this command only the first time you push. `--set-upstream` will add a new branch of the same name in the remote repository_

```sh
$ git push --set-upstream origin submission0
```

For every subsequent push, use this

```sh
$ git push
```
</details>

### Gearing for Submission

<details><summary>When you are done with the solution and you have pushed all your commits to the `submission0` branch, merge the submission branch to main.</summary>

<ul>
<li>First ensure that you are on the main branch and that there are no differences between the remote copy and your local copy

```sh
$ git checkout main

$ git pull
```
</li>

<li>Now, merge your submission branch to main

```sh
$ git merge submission0
```
</li>
</ul>
</details>

Push the new changes in main to the remote repo

```sh
$ git push
```
