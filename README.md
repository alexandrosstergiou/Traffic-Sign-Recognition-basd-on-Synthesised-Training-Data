# The Driver's Assistant: Utilising Synthetic Data Generation and Deep Learning for Traffic Sign Classification

The full thesis will be available on my website.

## Abstract
A main concern of road sign recognition systems has been the use of a large dataset obtained through research and manually finding sufficient data in order to conduct the necessary experiments and optimally, create a model with high accuracy rates. The purpose of this dissertation is the introduction of a traffic sign recognition system , which is based on synthetic data generation methods (SGTD), that is not bound to a specific set of road signs as occurring in a country or region, but can gen- erate training examples given a defined set of templates. This work can significantly decrease the time spent by researches or system developers in order to acquire data and allows the reallocation of the main project focus on the construction of the pre- dictive model. Although, the training dataset is synthetically created, the variations in visual appearance between examples, such as differences in illumination and ro- tation, are reflected on each image to best represent road signs in real world settings and have been implemented using Computer Vision methods. The main classifier that the system is based on is a Convolutional Neural Network (CNN) that can achieve close to state-of-the art accuracy results when trained on actual data.

## Installation
Git is required to download and install the repo. You can open Terminal (for Linux and Mac) or cmd (for Windows) and follow these commands:
```sh
$ sudo apt-get update
$ sudo apt-get install git
$ clone https://github.com/alexandrosstergiou/The-Drivers-Assistant-Traffic-Sign-Recognition
```

Note that the synthetic dataset SGTSD will need aprox. 10Gb and the sample set used for training will be close to 1Gb.
Please allow sufficient storing space when running the genertor on a system.

## License
MIT
**This system was made for the puroses of my MSc thesis and thus is a part of University of Essex. For commercial purposes / non private usage, the university will need to be contacted.

## Contact
Alexandros Stergiou

asterga at essex.ac.uk

Any queries or suggestions are much appreciated!
