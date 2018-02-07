# Weakly Supervised Semantic Segmentation for Join Key Local Structure Localization and Classification of Aurora Image
By Chuang Niu, Jun Zhang, Qian Wang, and Jimin Liang

## Introduction
A weakly supervised semantic segmentation method for joint KLS localization and classification of aurora image is implememted in this project.
The related paper is submitted to TGRS.
More details will be descibed.

This project is based on:
* [selective search](https://github.com/BradNeuberg/selective_search_py)
* [fast-rcnn](https://github.com/rbgirshick/fast-rcnn)

These codes are not directly uesd by this project, but you must make sure that they can run normally before implementation of this project.


## Install

### Prereq
Cmake, C++ compiler, Boost>=1.63 are required in addition to Python.

* Linux: `apt install cmake make gcc`
  Due to outdated Boost for many Linux distros, consider using Anaconda/[Miniconda Python](https://conda.io/miniconda.html) to get Boost
  ```sh
  conda install boost

  cmake -DBOOST_INCLUDEDIR=$HOME/miniconda3/include -DBOOST_LIBRARYDIR=$HOME/miniconda3/lib ..
  ```
  assuming your Anaconda install is under `$HOME/miniconda3` (the default)
* Mac: `brew install cmake make gcc boost boost-python`


### Setup
1.  Get the code.
    ```sh
    git clone https://github.com/niuchuangnn/Aurora-ASI-KLS
    cd Aurora-ASI-KLS
    pip install -e .
    cmake .
    make

    cd &KLS_ROOT/fast-rcnn/caffe-fast-rcnn
    make all
    make pycaffe
    cd &KLS_ROOT/fast-rcnn/lib
    make
    ```
2.  Download the region detection [model](https://1drv.ms/u/s!ArnlNXPnKNAKjQWsM4hsLuvu8cNW)
    ```sh
    cd $KLS_ROOT/Data
    mkdir -p region_classification/output
    ```
    Put the downloaded model into this folder.

3. Run demo.

```
cd $KLS_ROOT/src/demo
python demo.py
```
You will see:
```
classification time: 1.2338631897
segmentation time: 1.77530801296
```
![arc](https://github.com/niuchuangnn/Aurora-ASI-KLS/blob/master/Data/demo_examples/a_r.png)
![drapery](https://github.com/niuchuangnn/Aurora-ASI-KLS/blob/master/Data/demo_examples/D_r.png)
![radial](https://github.com/niuchuangnn/Aurora-ASI-KLS/blob/master/Data/demo_examples/R_r.png)
![hot-spot](https://github.com/niuchuangnn/Aurora-ASI-KLS/blob/master/Data/demo_examples/HS_r.png)

## Notes
Tested on Linux, but should work on other operating systems.
Start a [GitHub Issue](https://github.com/niuchuangnn/Aurora-ASI-KLS/issues) if it doesn't work for you.
