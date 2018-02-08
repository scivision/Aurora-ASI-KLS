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
GPU is required.

### Prereq
Cmake, C++ compiler, Boost>=1.63 are required in addition to Python.

* Linux: `apt install cmake make gcc`
  Due to outdated Boost for many Linux distros, consider using Anaconda/[Miniconda Python](https://conda.io/miniconda.html) to get Boost
  ```sh
  conda install boost
  ```
* Mac: `brew install cmake make gcc boost boost-python`

All operating systems with Anaconda/Miniconda:
```sh
conda install caffe
```

### Setup
1.  Get the code.
    ```sh
    git clone https://github.com/niuchuangnn/Aurora-ASI-KLS
    cd Aurora-ASI-KLS
    pip install -e .
    ```
    Following steps are under this `Aurora-ASI-KLS` directory.
2.  Build selective_python code
    ```sh
    cd selective_search/lib

    cmake -DBOOST_INCLUDEDIR=$HOME/miniconda3/include -DBOOST_LIBRARYDIR=$HOME/miniconda3/lib ..
    make
    ```
    assuming your Anaconda install is under `$HOME/miniconda3` (the default)
3.  Build fast-rcnn
    ```sh
    cd fast-rcnn/lib
    pip install - e.
    ```
4.  Download the region detection [model](https://1drv.ms/u/s!ArnlNXPnKNAKjQWsM4hsLuvu8cNW)
    ```sh
    mkdir -p Data/region_classification/output
    ```
    Put the downloaded model into the `.../output` folder.

## Uaage
```
python demo.py
```
You will see:
```
classification time: 1.234
segmentation time: 1.775
```
![arc](https://github.com/niuchuangnn/Aurora-ASI-KLS/blob/master/Data/demo_examples/a_r.png)
![drapery](https://github.com/niuchuangnn/Aurora-ASI-KLS/blob/master/Data/demo_examples/D_r.png)
![radial](https://github.com/niuchuangnn/Aurora-ASI-KLS/blob/master/Data/demo_examples/R_r.png)
![hot-spot](https://github.com/niuchuangnn/Aurora-ASI-KLS/blob/master/Data/demo_examples/HS_r.png)

## Notes

* Tested on Linux, but should work on other operating systems.
* Windows may be difficult due to large number of prereqs--use [Windows Subsystem for Linux](https://www.scivision.co/install-windows-subsystem-for-linux/)
* Start a [GitHub Issue](https://github.com/niuchuangnn/Aurora-ASI-KLS/issues) if it doesn't work for you.
