As of April 2nd, 2020 I have 106 Git repositories, which is more than any person should. Git is an open-source project developed by the creator of Linux — Linus Torvalds.

Git is a (Version Control System). The idea behind Git is very simple. Instead of having only a single place for code for software. Git offers a remote copy of the code in what’s called a repository and that can contain the full history of all changes at a contributor level. It’s also designed with performance, security, and flexibility.

Git is currently the industry standard. A requirement in any programming environment the level of experience can vary a lot. From a single person to a 50+ team with code reviews. If you are an inexperienced developer wanting to build up valuable skills in software development tools, when it comes to version control, Git should be on your list.

## Ready to learn a practical example of Git?

Before starting I highly recommend using Git on the terminal instead of GUI. My reason is simple — Git UI doesn’t scale well in a collaborative environment. When I hire a new Software Software Engineer the first habit I break is using the GitHub desktop app.

Let’s say you started a new website project

### Step 1 - Example Site

Start by creating new folder named `example-website` with a single file called `index.html`

**index.html**
```
<!doctype html>
<html lang="en">
  <head>
    <title>Hello, world!</title>
  </head>
  <body>
    <h1>Hello, world!</h1>
  </body>
</html>
```

### Step 2 - Github.com

Go to Github.com and setup a new Repo.

![Github Create Repo](/static/blog/1_LxWnYRHysCK6R_ohAfMsdg.png)

### Step 3

From the terminal 
```
cd example-website
git init
```

### Step 3 - Add a remote 

```
git remote add origin git@github.com:terrillo/example-website.git
```

Adding a remote connects your local computer with remote repositories. This process can be repeated across multiple computers. Alternatively, you can clone a repo to your local to get started.

```
git clone https://github.com/terrillo/example-website.git
```

When I first started using Git in 2010 I started using GIT as a way for me to try other people code I searched for on Github.

### Step 4 - Add Files 

The Git process is based around three workflow steps **ADD -> COMMIT -> PUSH**. Each file must be added to a staging environment before you can commit. 

Add a single file
```
git add index.html
```

Add all files
```
git add --all
```

After adding files you can use the status command to see what you have done for.
```
git status
```

Git status response —
```
On branch main
No commits yet
Changes to be committed:
 (use “git rm — cached <file>…” to unstage)
new file: index.html
```

Each file and directory can be easily identified by the green and red statuses.


### Step 5 - Commit

After adding your files. The next step is to commit your work. Each commit is attached to a message.

```
git commit -m “First commit”
```

This message is what you will see when browsing your history. In the beginning, you’ll have nice and beautiful messages. With time your messages started to become more crypt-like, “ugh”, “another bug fix”, and “oops”. It happens to all of us.

```
[main (root-commit) 6581e1b] First commit
 1 file changed, 22 insertions(+)
 create mode 100644 index.html
```

After each commit, you get this motivational message with the number of files changed and lines inserted and deleted.

Before going on to the next step. Git is even better when used with a modern text editor like Atom or VS Code. These editors make Git worth it for personal projects. After changing the title in the index.html Atom highlights that line as a change. A small feature that can have a big impact on your workflow.

```
git add --all
git commit -m “Title change”
```

### Step 6 - Push
This next step is the process of updating your remote repo. Its best to push after every commit but it’s really up to you based on your workflow.


```
git push origin main
```

origin — the remote name

main — the branch name

```
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 1.09 KiB | 1.09 MiB/s, done.
Total 6 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To github.com:terrillo/example-website.git
 * [new branch] main -> main
```

 ## Done 

That’s a really basic introduction to using Git. With this basic setup, you can start backing up all your code remotely with the option to view the complete history of each file.

Thanks for reading