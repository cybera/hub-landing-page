#!/bin/bash

DIR=$(dirname "$0")

cd $DIR

branch="template-callysto"
if [[ -n $1 ]]; then
  branch="template-${1}"
fi

if [[ $(git status -s) ]]
then
    echo "The working directory is dirty. Please commit any pending changes."
    exit 1;
fi

echo "Deleting old publication"
rm -rf _site
mkdir _site
git worktree prune
rm -rf .git/worktrees/_site

echo "Checking out $branch branch into public"
git worktree add -B $branch _site origin/$branch

echo "Removing existing files"
rm -rf _site/*

echo "Generating site"
jekyll build

echo "Updating $1 branch"
cd _site && git add --all && git commit -m "Publishing to template (ansible.sh)" && git push
