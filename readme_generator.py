from os import listdir

__README__ = "README_copy.md"

__ignore__ = [
]

__directories__ = [
    "1. Easy Leetcode Questions",
]

__headers__ = {
    "directory": "### ",
    "file": "> * ",
}


def read_file(filename: str = __README__) -> list[str]:
    with open(filename, "r+") as file:
        return file.readlines()


def explore_dir(directory: str, mask: list = [".py"]) -> list:
    yield from (file for file in listdir(directory) if any(map(file.endswith, mask)))


def update_file(filename: str = __README__,
                headers: dict = __headers__,
                dirs: list = __directories__,
                ignore: list = __ignore__) -> None:
    f_cont = read_file(filename)
    for dir in dirs:
        if (mrkdn_dir := f"{headers.get('directory')}{dir}\n") not in f_cont:
            continue
        [f_cont.insert(i, proj_name)
         for i, file in enumerate(explore_dir(dir), start=1+f_cont.index(mrkdn_dir))
         if (proj_name := f"{headers.get('file')}{file}\n") not in f_cont and file not in ignore]

    with open(filename, "w") as updated_file:
        updated_file.write("".join(f_cont))


if __name__ == '__main__':
    update_file()
