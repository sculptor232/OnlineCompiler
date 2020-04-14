import os
from subprocess import getstatusoutput


def compiler(dirPath, string):

    filePath = os.path.join(dirPath, "Demo.js")


    with open(filePath, "w+") as fp:
        fp.write(string)


    cmd = f"node {filePath}"

    print(cmd, string)
    exitcode, data = getstatusoutput(cmd)



    return exitcode == 0, data
