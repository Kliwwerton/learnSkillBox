# coding -*- UTF-8 -*-

# Нужно собрать сведения об операционной системе и версии Пайтона

import platform
import sys

info = 'OS info is \n{} \n\n Python version is {}  {}'.format(platform.uname(), sys.version, platform.architecture())

print(info)

with open('os_info.txt', 'w') as ff:
    ff.write(info)
