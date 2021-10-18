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
                type_ = "blob"
                with open(full, "rb") as f:
                    old = data.hash_object(f.read())
            elif entry.is_dir(follow_symlinks=False):
                type_ = "tree"
                old = write_tree(full)
            entries.append((entry.name, old, type_))
    tree = "".join(f"{type_} {old} {name}\n" for name, old, type_ in sorted(entries))
    return data.hash_object(tree.encode(), "tree")


def _iter_tree_entries(old):
    if not old:
        return
    tree = data.get_object(old, "tree")
    for entry in tree.decode().splitlines():
        type_, old, name = entry.split(" ", 2)
        yield type_, old, name


def get_tree(old, base_path=""):
    result = {}
    for type_, old, name in _iter_tree_entries(old):
        if "/" in name or name in ("..", "."):
            raise ValueError(f"name: {name} is incorrect")
        path = base_path + name
        if type_ == "blob":
            result[path] = old
        elif type_ == "tree":
            result.update(get_tree(old, f"{path}/"))
        else:
            raise ValueError(f"Unknown tree entry {type_}")
    return result


def _empty_current_directory():
    for root, dirnames, filenames in os.walk(".", topdown=False):
        for filename in filenames:
            path = os.path.relpath(f"{root}/{filename}")
            if is_ignored(path) or not os.path.isfile(path):
                continue
            os.remove(path)
        for dirname in dirnames:
            path = os.path.relpath(f"{root}/{dirname}")
            if is_ignored(path):
                continue
            try:
                os.rmdir(path)
            except (FileNotFoundError, OSError):
                # Deletion might fail if the directory contains ignored files
                # so it is okay
                pass


def read_tree(tree_old):
    _empty_current_directory()
    for path, old in get_tree(tree_old, base_path="./").items():
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "wb") as f:
            f.write(data.get_object(old))


def is_ignored(path):
    return ".joegit" in path.split("/")
