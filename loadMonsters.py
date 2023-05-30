#!/bin/python3
import urllib.request
import os
import json
import re

source_version = "v2.3"
source_filename = "monsterData"
source_extension = "js"
source_filename_full = source_filename + "." + source_version + "." + source_extension
source_url_path = "https://github.com/mjcadz/sfrpgtools/raw/master/app/static/js/"
source_url = source_url_path + source_filename_full
filePrefix = "var monsterData = "
fileJSCommentRegex = ",\n\s*?\/\*(.|\n|\r)+?\*\/"


def main():
    urllib.request.urlretrieve(source_url, source_filename_full) # downloads file
    f = open(source_filename_full, "r")
    file_contents = f.read()
    f.close()
    file_contents = file_contents.rstrip()
    # print(file_contents)
    if len(file_contents) == 0:
        print("File empty");
        return 1
    # print(file_contents[-1])
    # print(file_contents[0:len(filePrefix)+1])
    if file_contents[-1] != ";" or file_contents[0:len(filePrefix)] != filePrefix:
        print("File formatting has changed");
        return 1
    file_contents = file_contents[len(filePrefix):-1]
    file_contents = re.sub(fileJSCommentRegex, "", file_contents)
    # print(file_contents)
    data = json.loads(file_contents)
    for name in data:
        s = convertMonster(name, data[name])
        f = open(os.path.join("Bestiary", name + ".md"), "w")
        f.write(s)
        f.close()
    return 0

def convertMonster(name, stats):
    return '''
# {}

- [cr::{}]
- [combatType::{}]
- [alignment::{}]
- [size::{}]
- [type::{}]
- [subtype::{}]
- [environment::{}]
- [climate::{}]
- [planet::{}]
- [organization::{}]
- [source::{}]
- [page::{}]
'''.format(
        name,
        stats["cr"],
        stats["combatType"],
        stats["alignment"],
        stats["size"],
        stats["type"],
        stats["subtype"],
        stats["environment"],
        stats["climate"],
        stats["planet"],
        stats["organization"],
        stats["source"],
        stats["page"]
    )

if __name__ == "__main__":
    main()

