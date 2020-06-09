import os
import glob
from subprocess import call


def isSVN(dir):
    """
    Checks if the given directory is a working subversion copy.
    :param dir: directory to check.
    :return: returns 'True' if is is a working copy, 'False' otherwise.
    """
    print "Searching {0}".format(dir)
    command = 'svn status --depth=empty %s' % dir
    #command = call(["svn", "status", dir])

    if os.system(command) is None:
        print "{0} is a working svn copy".format(dir)


if __name__ == '__main__':
    currentDir = os.getcwd()

    # Get immediate sub directories in current dir INCLUDING TRUNK.
    subDirs = glob.glob('*/*/')
    print subDirs

    for dir in subDirs:
        isSVN(dir)
