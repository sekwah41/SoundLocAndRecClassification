SoundLocAndRecClassification
===============

# Sounds used
[UrbanSound8k Dataset](https://urbansounddataset.weebly.com/urbansound8k.html) for main training and testing of recognition code.  
Self recorded sounds which are not referenced.
https://www.kaggle.com/datasets/chrisfilo/urbansound8k


# Running gpu accelerated
I've added this section as I wanted to tinker with this again after some time but found it a LOT harder to get it properly running again due to needing specific versions of different libraries and packages.

Luckily this isn't too crazily optimised for with the GPU though at least on my setup it will cut the time down to about a quarter.
That being said, this project isn't designed solely for efficiency, otherwise id have stored the pre-processed data in another folder to skip processed sounds, so there is definitely a lot that can be improved.

This can be quite frustrating due to many reasons where it will seemingly randomly not accept the GPU.
If you are struggling to set up GPU acceleration I would suggest following the instructions here

https://www.tensorflow.org/install/docker

From my understanding as long as you have nvidia drivers installed you should be fine to run this.
So you should only need to make sure you have docker, and [nvidia-docker](https://github.com/NVIDIA/nvidia-docker) installed.
https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

Most of the instructions seem to be mostly based for ubuntu so if you want the easist time it may be best to use that.

Then these commands should allow you to get a environment that has tensorflow and jupyter installed with GPU acceleration.

On arch https://aur.archlinux.org/packages/nvidia-docker will help.

```bash
# These notes are just for myself as well as anyone who may be less experienced with docker for easier setup
# If you want to use the latest switch the version number with latest, though for re-visiting this project in the future I've set a specific number to add less compatability issues.
docker pull tensorflow/tensorflow:2.12.0-gpu-jupyter

# Use this to run the project with GPU support
docker run --name soundloc --net="host" --gpus all -v $PWD:/soundloc -w /soundloc -it -p 8888:8888 tensorflow/tensorflow:2.12.0-gpu-jupyter bash

# To get back into the existing container as it'll stop when you exit
docker start -ia soundloc

# If you want to attack another terminal e.g. installing packages or whatever while jupyter is running
docker exec -it soundloc bash

# You can run this to check if it is working
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

# AS the user inside docker is root youll need to run, if anyone knows a better way to do this please let me know
jupyter notebook --allow-root

```

```bash
# Update this via `pip freeze > requirements.txt`
# Though you may want to filter out most of the packages that are not explicitly needed for this project or are already provided
# Though this may clash/have issues if you have updated the tensorflow docker image e.g. above 2.12.0
python3 -m pip install --upgrade pip
apt update
apt upgrade
apt-get install -y libsndfile1 graphviz
pip install -r requirements.txt

# The main libraries that should be needed or work as of writing this are
pip install pandas wavefile matplotlib==3.7.1 librosa resampy seaborn pydot graphviz
```

As its quite easy to reset to the start by deleting the container, it should be quite easy to generate a proper requirements.txt.


# Split longer sounds into shorter samples
`ffmpeg -i somefile.mp3 -f segment -segment_time (seconds) -c copy out%03d.mp3`

# Structure of samples
/resources/UrbanSounds8k/

/resources/CustomSounds/{class_string}

# Sources
This code is partially based on [this article](https://medium.com/@mikesmales/sound-classification-using-deep-learning-8bc2aa1990b7)
It follows the same main process and uses some snippets from it to save time but is re-purposed for this project.

# What is needd to run this project?
For this section of the project you will need Jupyter notebook and a series of modules such as TensorFlow.
You can find a list of modules listed at the start of the notebook at `src/Sound Recognition.ipynb`

# Why Jupyter?
If you haven't used jupyter before you really should for tasks that use a lot of data.
You do not need to run the whole program every time and you can still open sockets and integrate it as a normal program.
You can also output the final python file with any extra notes removed if you really need to use it without Jupyter.
