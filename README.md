SoundLocAndRecClassification
===============

# Sounds used
[UrbanSound8k Dataset](https://urbansounddataset.weebly.com/urbansound8k.html) for main training and testing of recognition code.  
Self recorded sounds which are not referenced.


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
