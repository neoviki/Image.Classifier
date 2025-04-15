#!/bin/bash
if [[ ! -d model ]]; then
    mkdir model
fi
cd src
python3 CIFAR10_Image_Recognizer.py
