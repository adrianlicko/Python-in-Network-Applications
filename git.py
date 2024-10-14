import os

repository_url = "https://github.com/adrianlicko/PSA.git"

def clone_repo(repo_url, path):
  os.chdir(path)
  os.system("git clone " + repo_url)
  return

def add_file(fileName, path):
  os.chdir(path)
  os.system("git add " + fileName)
  return

def add_all_files(path):
  os.chdir(path)
  os.system("git add .")
  return

def commit_changes(commitMessage, path):
  os.chdir(path)
  os.system("git commit -m \"" + commitMessage + "\"")
  return

def push_git(path):
  os.chdir(path)
  os.system("git push")
  return
