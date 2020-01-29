# Whatsapp_Notes_Extractor

To all the students out there,You all like me must have gone thorugh the problem of various study notes at the end of each semester/Exams which we want to get rid off at times. 100's and 100's of these notes, circulated via WhatsApp are just lying in our phone Memories eating up space like a Monkey eating Bananas. 
I felt an urge to do something which could just clean these notes from my phone and put them in a different place so that I could Deleted them all together without checking through each and every WhatsApp Image. So, Here I am; by training a CNN model which can predict these notes, extract them from my WhatsApp Images directory and put them in a different folder for me to delete it.

Something Like this:

![](https://github.com/PiyushB001/Whatsapp_Notes_Extractor/blob/master/background_work/Image.jpeg)

Images in red circles are notes which you may wanna delete or extract them to a folder (in case you are a maggu :P) and blue circles are important ones which shouldn't be messed up with.

# Requirements:
[Numpy](www.numpy.org)

[Keras:  preferred running over tensorflow](https://keras.io/)

Please make sure you have Tensorflow/CNTK, or Theano over which keras could actually work. 
I personnally prefer using Tensorflow.

pip install tensorflow (Incase you need it.)

# Instructions

LINUX

Install dependencies using pip install -r requirements.txt. Connect your Smartphone to your system, mount Internal Storage and copy the absolute path to the WhatsApp folder, to know the absolute path open a terminal in WhatsApp folder and run pwd command. Run the extract_Linux.py script by python extract_Linux.py and paste the copied path when asked to. The script will create a new folder named notes in your WhatsApp Image folder and move the study notes images to it.

WINDOWS

Due to some Compability issues with windows path style of the smartphone; Running this script on Windows is a bit complex task.

Install dependencies using pip install -r requirements.txt. Connect your Smartphone to your system and Mount Internal Storage. Navigate to the WhatsApp folder and copy the WhatsApp Images directory. Paste the directory inside the Repository Directory you Downloaded on your System. Open your terminal(if Requirements are installed from the Windows Command Prompt, else open the Prompt on which you installed the Requirements. for Example Anaconda Prompt). In the Prompt run the extract_win.py script by python extract_win.py. The script will create a new folder named notes in your WhatsApp Image folder inside the Repository and move the study notes images to it. You can then replace this WhatsApp Image folder with your phone WhatsApp Image folder.

This model has been trained on about 1200 images and keras' Data Augmentation pipelines have been used to increase this dataset. Currently this model is about 80% accurate on my dataset. Please feel free to add your own data and train the model on it to make the model more accurate. To add your own data, create a data folder in background_work folder, create two subfolders 1 and 0 inside data, in 1 put study notes and put all other important images in 0. See background_work folder for more info.

#

Suggestions are Welcome. 


