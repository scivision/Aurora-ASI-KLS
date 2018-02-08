# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------
install_requires = ['numpy','cython','easydict']
import numpy as np
from setuptools import setup,find_packages
from distutils.extension import Extension
from Cython.Distutils import build_ext

cmdclass = {}
ext_modules = [
    Extension(
        "utils.cython_bbox",
        ["utils/bbox.pyx"],
        extra_compile_args=["-Wno-cpp", "-Wno-unused-function"],
    ),
    Extension(
        "utils.cython_nms",
        ["utils/nms.pyx"],
        extra_compile_args=["-Wno-cpp", "-Wno-unused-function"],
    )
]
cmdclass.update({'build_ext': build_ext})

setup(
    name='fast_rcnn',
    packages=find_packages(),
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    include_dirs=[np.get_include()],
    install_requires=install_requires,
)
