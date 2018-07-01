# Computer-Vision-Python-openCV-and-DL
Computer Vision and Deep Learning.
Easy way to implement Deep Learning For Image Classification is to use _pre trained_ network . Training a Neural Network from scratch is difficult , as it requires one to resort to expensive GPU's and can be time consuming. 
The # trick in using pre-trained network # is to download the weights of these trained network and use these weights to classify the image. 
The normal training process requires me to do both the forward pass f(x)--->b and do the back propagation , which is basically taking the partial derivatives and adjust the weights so that the mapping between the input and the output is learnt by the network. This process of learning the mapping is stored as weights.
So if I can get hold of the pretrained weights then it becomes very easy to classify the images as I just need the forward pass f(x)--->b and get rid of the lengthy back propagation part, making state of art classification as simple as running a few lines of code on a CPU based machine.
# Various Pre trained available :
VGG16
VGG19
ResNet50
Inception V3
Xception
# VGG networks
These networks were first introduced by Simonyan and Zisserman in 2014 in their paper Very Deep Convolutional Network for large Scale Image Recognition.. The VGG family of the Network are characterised by 3 * 3 convolution layers stacked over one another , increasing depth.Reducing the volume size is done by the max-pooling. Finally we have two fully connected layers with 4096 nodes and then followed by an softmax classifier.
Drawbacks of VGG model is that these models are very difficult to train and the network weight themselves are very large 533 MB for VGG16 and 574 MB VGG19.

# ResNet 
Introduced by He et. al. in their 2015 Deep Residual Learning for Image Recognition , the ResNet architechture has a extremelly deep network and can be trained using standard SGD (Standard Gradient Descent) through the use of residual network.The ResNet50 has 50 weights and inspite of its massive size has lower weights size of 102 MB . This occurs due to use of global average pooling _instead of_ the fully connected layer.

# Inception V3
The Inception model was first intorduced by Szegedy et al. in their paper "Going Deeper with Convolutions". The goal of the inception module is to act as _multi level features extractor_ by computing 1 * 1 , 3 * 3 , 5 * 5 convolutions within the same module of the network - the results of these filters are stacked along the channel dimension before being fed into the next layer in the network.The weight of the Inception V3 model is the lowest of the all the models named above and comes at 96MB.
# Xception 
This model was developed by Francois Chollet et. al in his 2016 paper Xception; Deep Learning with Depthwise Separable Convolutions. This model is an extension of the previous model where the inception module (having 1 * 1 , 3 * 3, 5 * 5 convolutions in a module) is replaced with _depthwise separable_ convnolutions. The weights for the Xception module comes at 91 MB and is the least in the list.

# Squeeze Net (not available in Keras):
this is extemely small network. having a squeeze and expand module. Where the squeeze module has 1 * 1 and expand module has 1 * 1 , 3 * 3 convolutions. The size of weights of the squeezenet architecture is 4.9 MB.

Final Note : I downloaded the xception architecture weights weighing 92 MB from the internet and using it classified a image to that of an 'koala' in 15 seconds ( including the downloading time.) These weights need to be downloaded only once and the images can be classified in 5 seconds since then.
