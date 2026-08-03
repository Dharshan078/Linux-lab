# Git Add a folder to Github repo
## Step 1: Need to configure git email and user name using
    `git config --global user.email "sivadahrshanxxx@gmail.com"`
    `git config --global user.name "dharshanxxx"`

## Step 2: Initialize Git
It creates a hidden .git file to start tracking changes
`git init`

## Step 3: Add files to next commit
`git add .`

## Step 4: Add commit
Commit is like saving a checkpoint
`git commit -m "first commit"`

## Step 5: Connect to github repo
`git remote add origin https://github.com/Dharshan078/Linux-lab`
- remote -> Another repo
- add -> add a new one
- origin -> Conventional name for the main remote

## Step 6: Push the commit to the github repo
`git branch -m main`
**main** -> it pushes to the main branch
`git push -u origin main`
pushes to origin **repo** and **main** branch
