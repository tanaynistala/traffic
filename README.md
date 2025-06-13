# MATH123 Final Project - Traffic Analysis

## Introduction

In this work, we address the issue of traffic congestion in urban environments. To do so, we collect publicaly available data from cited datasets below, preprocess and clean the data, and then cluster the data by city before passing it as input to a neural network which learns to predict the congestion based on various features. The chosen neural network is a Long Short Term (LSTM) Network meant to encapsulate the temporal nature of traffic patterns in addition to the other features. The inference goal is to be able to predict future traffic conditions based on the state of the system in advance. Furthermore, to analyze the performance of the LSTM network, we evaluated the disparity between predicted and actual.

## Current Implementation

We used TensorFlow Keras alongside a WindowGenerator class we customized to our purposes to format the traffic dataset's temporal component to train the LSTM. Evaluation of the model's performance with the test set (and not just during training against the validation set) was conducted visually and furthermore, we looked into monitoring the predictions against the map of the towns in question.

## Future Work and Extension

Given the trained LSTM (which could always be trained for longer with better computational resources than the 3060 that we used as students), this project could be extended to consider the predictions made by the model and then use them in a feedback loop to recommend optimizations. That is, for urban planning or for general improved planning by individual members of the community, optimization algorithms could be implemented that take predicted traffic conditions as input and then suggest changes to traffic signals, lanes, signage, or other interventions and environmental conditions. The goal of this would be to minimize congestions over time based on actionable and dynamic insight.

Another aspect of future work is to augment the amount of data per city. This could either be done by including more years or by using augmentation tricks such as for example considering different intersections from different angles in a similar wasy as to how reflections are for example employed with images in CV tasks. The reason that this is vital to our project when we already have a fairly large dataset is that the clustering step breaks the dataset down before the neural network is trained, which means each of the clusters is rather small in size which can minimize training efficacy.  

## Resources

* [Dataset](https://www.research-collection.ethz.ch/handle/20.500.11850/437802)
* [Mini Dataset](https://www.kaggle.com/datasets/fedesoriano/traffic-prediction-dataset/data)

## Installation

```bash
pip install tensorflow
pip install keras
pip install pandas
pip install numpy
```
