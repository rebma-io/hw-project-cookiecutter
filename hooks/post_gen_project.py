"""Cleanup updates if unneeded

This just does a quick cleanup of the updates directory if the user chose not to create
one. Unfortunately, there's not a cleaner way to do this in cookiecutter.
"""
import os
import shutil

from pathlib import Path

cwd = Path(os.getcwd())

parent_dir = cwd.parent.absolute()

def remove_path(filepath: Path) -> None:
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

blog_desired = "{{ cookiecutter.create_blog }}" in ("y", "yes")
changelog_desired = "{{ cookiecutter.create_changelog }}" in ("y", "yes")
action_desired = "{{ cookiecutter.create_github_action }}" in ("y", "yes")

if not blog_desired:
    blog_path = os.path.join(
        parent_dir,
        "{{ cookiecutter.project_slug }}",
        "docs",
        "updates",
    )
    remove_path(blog_path)

if not changelog_desired:
    changelog_path = os.path.join(
        parent_dir,
        "{{ cookiecutter.project_slug }}",
        "docs",
        "CHANGELOG.md",
    )
    remove_path(changelog_path)

if not action_desired:
    action_path = os.path.join(
        parent_dir,
        "{{ cookiecutter.project_slug }}",
        ".github",
    )
    remove_path(action_path)
