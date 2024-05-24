Git & GitHub has steadily risen from being just a preferred skill to a must-have skill for multiple job roles today. In this article, I will talk about the Top 20 Git Commands that you will be using frequently while you are working with Git.

Following are the Git commands which are being covered:

- git config
- git init
- git clone
- git add
- git commit
- git diff
- git reset
- git status
- git rm
- git log
- git show
- git tag
- git branch
- git checkout
- git merge
- git remote
- git push
- git pull
- git stash

So, let’s get started now!!

# git config

## **Usage:** git config -global user.name “[name]”

## **Usage:** git config -global user.email “[email address]”

This command sets the author name and email address respectively to be used with your commits.

![](https://miro.medium.com/v2/resize:fit:962/1*8HUmCSPeXDzPg7SXt07QQA.png)

# git init

## **Usage:** git init [repository name]

This command is used to start a new repository.

![](https://miro.medium.com/v2/resize:fit:962/1*dWnCmhEhNO9fKt1ThV0v8A.png)

# git clone

## **Usage:** git clone [url]

This command is used to obtain a repository from an existing URL.

![](https://miro.medium.com/v2/resize:fit:962/1*6_iTS0qstfFe_jNbeRlxeg.png)

# git add

## **Usage:** git add [file]

This command adds one or more files to the staging area.

![](https://miro.medium.com/v2/resize:fit:962/1*P2An1Y9NCCjFKYqOotfKxQ.png)

## **Usage:** git add *

This command adds one or more to the staging area.

![](https://miro.medium.com/v2/resize:fit:653/1*j4vMw9vJlJmk_pzK-BgRAQ.png)

# git commit

## **Usage: git commit -m “[ Type in the commit message]”**

This command records or snapshots the file permanently in the version history.

![](https://miro.medium.com/v2/resize:fit:962/1*4x8GCtmoUsOvYgyoQ9CDTQ.png)

## **Usage: git commit -a**

This command commits any files you’ve added with the git add command and also commits any files you’ve changed since then.

![](https://miro.medium.com/v2/resize:fit:962/1*icxzIA5Ues4vDIB5GxsxiA.png)

# git diff

## **Usage: git diff**

This command shows the file differences which are not yet staged.

![](https://miro.medium.com/v2/resize:fit:962/1*fqcP_Pi7d6-fnKWPAiOMMA.png)

## **Usage: git diff –staged**

This command shows the differences between the files in the staging area and the latest version present.

![](https://miro.medium.com/v2/resize:fit:962/1*zHonL5EOX7aL0LGRok4-3A.png)

## **Usage: git diff [first branch] [second branch]**

This command shows the differences between the two branches mentioned.

![](https://miro.medium.com/v2/resize:fit:962/1*EC4MWS3sYPbhSABz7xX-1A.png)

# git reset

## **Usage: git reset [file]**

This command unstages the file, but it preserves the file contents.

![](https://miro.medium.com/v2/resize:fit:962/1*CgAYvTIhGV5ZiL6G6DmN9Q.png)

## **Usage: git reset [commit]**

This command undoes all the commits after the specified commit and preserves the changes locally.

![](https://miro.medium.com/v2/resize:fit:962/1*UxIbcPVz39tcze8g5zo74Q.png)

## **Usage: git reset -hard [commit]**

This command discards all history and goes back to the specified commit.

![](https://miro.medium.com/v2/resize:fit:962/1*gTFoK5XixfM0DwHq4MxK6g.png)

# git status

## **Usage: git status**

This command lists all the files that have to be committed.

![](https://miro.medium.com/v2/resize:fit:962/1*bhEGTSceXgD2xycgGay3LQ.png)

# git rm

## **Usage: git rm [file]**

This command deletes the file from your working directory and stages the deletion.

![](https://miro.medium.com/v2/resize:fit:962/1*fYV7NUwxT0FH4_-2ES7Rdw.png)

# git log

## **Usage: git log**

This command is used to list the version history for the current branch.

![](https://miro.medium.com/v2/resize:fit:1050/1*M7Cm4njeG2kl57Rd0vLArg.png)

## **Usage: git log -follow[file]**

This command lists version history for a file, including the renaming of files also.

![](https://miro.medium.com/v2/resize:fit:1050/1*sPCu7_bId1onE50MnJVD9w.png)

# git show

## **Usage: git show [commit]**

This command shows the metadata and content changes of the specified commit.

![](https://miro.medium.com/v2/resize:fit:1050/1*2qHgXNTI-CE1GFrXmVTRhg.png)

# git tag

## **Usage: git tag [commitID]**

This command is used to give tags to the specified commit.

![](https://miro.medium.com/v2/resize:fit:962/1*bHm5DY-1Gthri6351oqunQ.png)

# git branch

## **Usage: git branch**

This command lists all the local branches in the current repository.

![](https://miro.medium.com/v2/resize:fit:678/1*4xRndU8pT95BzNr4qBizYA.png)

## **Usage: git branch [branch name]**

This command creates a new branch.

![](https://miro.medium.com/v2/resize:fit:962/1*9m0DaShOc5RcvPmwPg8h8g.png)

## **Usage: git branch -d [branch name]**

This command deletes the feature branch.

![](https://miro.medium.com/v2/resize:fit:962/1*lIWOaErZzOk3uvT4aak9_A.png)

# git checkout

## **Usage: git checkout [branch name]**

This command is used to switch from one branch to another.

![](https://miro.medium.com/v2/resize:fit:962/1*jRGfXP4IPICYHXtmmJ4RHQ.png)

## **Usage: git checkout -b [branch name]**

This command creates a new branch and also switches to it.

![](https://miro.medium.com/v2/resize:fit:962/1*4nn_D7_tT1kuPvWi88UdSw.png)

# git merge

## **Usage: git merge [branch name]**

This command merges the specified branch’s history into the current branch.

![](https://miro.medium.com/v2/resize:fit:572/1*QGsQYNhDzEzvjUlXI0FuZQ.png)

# git remote

## **Usage: git remote add [variable name] [Remote Server Link]**

This command is used to connect your local repository to the remote server.

![](https://miro.medium.com/v2/resize:fit:962/1*kVQ77mdtHApIpFPk1gbkPw.png)

# git push

## **Usage: git push [variable name] master**

This command sends the committed changes of master branch to your remote repository.

![](https://miro.medium.com/v2/resize:fit:962/1*1-O8X8_uaq5ggfGgFZyIag.png)

## **Usage: git push -all [variable name]**

This command pushes all branches to your remote repository.

![](https://miro.medium.com/v2/resize:fit:962/1*QPaNxQ8azYk0ZOFKsIUK1g.png)

## **Usage: git push [variable name] :[branch name]**

This command sends the branch commits to your remote repository.

![](https://miro.medium.com/v2/resize:fit:962/1*bxaHFcGizwJYtDjmYJkvQw.png)

# git pull

## **Usage: git pull [Repository Link]**

This command fetches and merges changes on the remote server to your working directory.

![](https://miro.medium.com/v2/resize:fit:962/1*rvRYOyOJQP8LkqktyUlhgg.png)

# git stash

## **Usage: git stash save**

This command temporarily stores all the modified tracked files.

![](https://miro.medium.com/v2/resize:fit:962/1*5UAQr_erBnC6Fnda2rS0sw.png)

## **Usage: git stash pop**

This command restores the most recently stashed files.

![](https://miro.medium.com/v2/resize:fit:962/1*zuzuEL9VzL8Xt7yAoKp72A.png)

## **Usage: git stash list**

This command lists all stashed changesets.

![](https://miro.medium.com/v2/resize:fit:962/1*lqr8ZdO78ztoeomIBDFYBA.png)

## **Usage: git stash drop**

This command discards the most recently stashed changeset.

![](https://miro.medium.com/v2/resize:fit:962/1*ZbCSi45lki09YdPCueuf-w.png)

This brings us to the end of the article