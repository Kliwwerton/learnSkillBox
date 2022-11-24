# coding -*- UTF-8 -*-

# Нужно собрать сведения об операционной системе и версии Pyтона

import platform
import sys

info = 'OS info is \n{} \n\nPython version is {} {}'.format(platform.uname(), sys.version, platform.architecture())

print(info)


