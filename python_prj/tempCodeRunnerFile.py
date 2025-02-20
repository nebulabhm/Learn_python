from __future__ import print_function, unicode_literals
from os import listdir, walk, mkdir, remove, chmod, makedirs
from os.path import isfile, isdir, join, basename, exists
from zipfile import ZipFile
from shutil import rmtree
from stat import S_IWRITE
from time import sleep