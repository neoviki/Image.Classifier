## CIFAR-10 Image Recognition Application using Convolutional Neural Networks

A simple and intuitive application that recognizes images from various everyday object categories using a Convolutional Neural Network (CNN). The model is trained on the CIFAR-10 dataset and features a user-friendly PyTkinter GUI for interaction.


![alt text](demo.gif)

## Features

    1. Image recognition powered by a Convolutional Neural Network trained with the Adam Optimizer.
    2. Utilizes the CIFAR-10 dataset, which contains 60,000 labeled images across 10 object classes.
    3. Built with a PyTkinter interface for ease of use and interaction.
    4. The neural network is implemented using PyTorch for efficient training and evaluation.

## Install Dependencies 
```bash
chmod +x install.dependencies.sh
./install.dependencies.sh
```

## Run the application
```bash
chmod +x run.app.sh
./run.app.sh
```
## PARAM SETTINGS

Config Name | Batch Size | LR | Momentum | Notes
Baseline | 64 | 0.0001 | 0.9 | Your current setup
Faster Converge | 128 | 0.001 | 0.9 | Faster training, test for stability
Adaptive LR | 64 | 0.01 → decay | 0.9 | Use StepLR, ReduceLROnPlateau, etc.
Adam Optimizer | 64 | 0.001 | – | Try Adam instead of SGD

