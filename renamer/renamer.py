import os
import shutil
import cmd
import imghdr

try:
    import termcolor
except ImportError:
    termcolor = None


class Rename(cmd.Cmd):
    def __init__(self):
        super(Rename, self).__init__()
        self.path = "."
        self.mode = "pictures"
        self.sc = 1
        self.intro = f"""
{'Welcome':*^80}
{'Renamer program for organizing pictures and tv series':=^80}
Renamer version 2.1, Copyright (C) 2015 Parham Alvani (parham.alvani@gmail.com)
Renamer comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
This is free software, and you are welcome to redistribute it
under certain conditions; type `show c' for details.
"""

    def do_rename(self, _: str):
        print(f"{'Renaming start':=^80}".format(""))
        print(f"Mode: {self.mode:<80}")
        print(f"Path: {self.path:<80}")
        print(f"Sequence Counter: {self.sc:<80}")

        if self.mode == "pictures":
            index = self.sc
            for file in sorted(os.listdir(self.path)):
                if not os.path.isdir(file):
                    extension = imghdr.what(file)
                else:
                    extension = None
                if extension:
                    name = f"{index}.{extension}"
                    index += 1
                    if os.path.exists(os.path.join(self.path, name)):
                        result = input(
                            f"{os.path.join(self.path, name)} is exists,"
                            "do you wish to continue ? (Yes / No)"
                        )
                        if result != "Yes":
                            break
                    shutil.move(
                        os.path.join(self.path, file),
                        os.path.join(self.path, name),
                    )
                    print(
                        f"mv {os.path.join(self.path, file)}"
                        f"{os.path.join(self.path, name)}"
                    )

        if self.mode == "tv-series":
            series = input("TV-Series Name: ")
            season = input("TV-Series Season#: ")
            index = self.sc
            for file in sorted(os.listdir(self.path)):
                extension = os.path.splitext(file)[1]
                if extension.lower() == ".mkv":
                    name = (
                        f"Episode {index}/"
                        f"{series} S{season:0>2}E{index:0>2}.mkv"
                    )
                    os.mkdir(os.path.join(self.path, f"Episode {index}"))
                    index += 1
                    shutil.move(
                        os.path.join(self.path, file),
                        os.path.join(self.path, name),
                    )
                    print(
                        f"mv {os.path.join(self.path, file)}"
                        f"{os.path.join(self.path, name)}"
                    )

        print("{0:=^80}".format("Renaming end"))

    def do_shell(self, line: str):
        os.system(line)

    def do_quit(self, _: str):
        print("Thank you for using Renamer")
        return True

    def do_mode(self, line: str):
        if line.lower() == "pictures":
            self.mode = "pictures"
        elif line.lower() == "tv-series":
            self.mode = "tv-series"
        else:
            print(f"*** Unknown mode: {line}")

    def do_path(self, line: str):
        if os.path.isdir(line):
            self.path = line
        else:
            print(f"*** Invalid path: {line}")

    def do_sc(self, line: str):
        try:
            self.sc = int(line)
        except ValueError as exception:
            self.sc = 1
            print(f"*** Invalid number: {str(exception)}")

    @property
    def prompt(self):
        prompt = f"Renamer at {self.path} > [{self.mode}] > "
        if termcolor:
            prompt = termcolor.colored(prompt, color="red", attrs=["bold"])
        return prompt

    do_EOF = do_quit


cli = Rename()
cli.cmdloop()
