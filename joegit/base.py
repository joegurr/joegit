import os

from . import data


def write_tree(directory="."):
    entries = []
    with os.scandir(directory) as it:
        for entry in it:
            full = f"{directory}/{entry.name}"
            if is_ignored(full):
                continue
            if entry.is_file(follow_symlinks=False):
                type = "blob"
                with open(full, "rb") as f:
                    old = data.hash_object(f.read())
            elif entry.is_dir(follow_symlinks=False):
                type_ = "tree"
                old = write_tree(full)
            entries.append((entry.name, old, type))
    tree = "".join(f"{type_} {old} {name}\n" for name, old, type_ in sorted(entries))
    return data.hash_object(tree.encode(), "tree")


def is_ignored(path):
    return ".joegit" in path.split("/")
