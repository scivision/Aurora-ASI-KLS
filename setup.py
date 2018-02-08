#!/usr/bin/env python
import zipfile
import subprocess
import urllib.request
from pathlib import Path
from setuptools import setup, find_packages, Extension
#
sURL = 'https://cs.brown.edu/~pff/segment/segment.zip'


# %% get "segment" C code

def dlex(url:str, outdir:Path=None) -> Path:
    """download and extract Zip file"""

    if not outdir:
        outdir = Path(url.split('/')[-1]).stem

    outdir = Path(outdir).expanduser()
    outdir.mkdir(parents=True, exist_ok=True)

    zipfn = outdir/url.split('/')[-1]


    try:
        zipfile.ZipFile(zipfn)
    except (FileNotFoundError,zipfile.BadZipfile):
        print('downloading',url)
        urllib.request.urlretrieve(url, zipfn)

    print('extracting',zipfn,'to',outdir)
    with zipfile.ZipFile(zipfn) as z:
        z.extractall(outdir)

    return outdir

dlex(sURL,'.')

#%%

# FIXME include Boost Python via conda
segmod = Extension('segment',
                    sources = ['selective_search/segment_py.cpp'])

setup(name='aurora_kls',
      packages = find_packages(),
      description = 'Auroral segmentation',
      python_requires='>=3.6',)
      #ext_modules=[segmod])