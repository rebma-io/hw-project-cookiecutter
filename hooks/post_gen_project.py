"""Cleanup blog if unneeded

This just does a quick cleanup of the blog directory if the user chose not to create
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

if not blog_desired:
    blog_path = os.path.join(
        parent_dir,
        "{{ cookiecutter.project_slug }}",
        "docs",
        "blog",
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