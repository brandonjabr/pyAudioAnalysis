## Installation
 * Install dependencies:
 ```
pip install numpy matplotlib scipy sklearn hmmlearn simplejson eyed3 pydub
```
 * Clone the source of this library: 
 ```
git clone https://github.com/brandonjabr/pyAudioAnalysis.git
```

* Finally, add the directory containing the repository to your `PYTHONPATH` variable, ie. if pyAudioAnalysis is in ~/git, run:
```
echo "export PYTHONPATH=~/git:$PYTHONPATH" >> ~/.profile
```

## Use Case: Recognize Set of Spoken Words

Download and extract the speech commands dataset to the *wav* folder:

```
cd wav
wget http://download.tensorflow.org/data/speech_commands_v0.01.tar.gz
tar xvf speech_commands_v0.01.tar.gz
rm -f speech_commands_v0.01.tar.gz
```

Make sure the dataset folder is titled *speech_commands*

Now run ```python trainSpeechCommands.py``` to train an SVM model on the audio samples found in my-recordings. I recorded a few samples of myself saying a small set of words (yes, no, one, two, three) using a standard microphone. 

Currently the model only has 3 highlight samples to train on, far more samples need to be collected before the model shows any reasonable performance. More samples will be uploaded to this repository soon.


## Use Case: Recognize Sports Highlights

Run ```python trainGOALS.py``` to train an SVM model on the audio from the Spain vs. Portugal match in the 2018 World Cup.

Currently the model only has 3 highlight samples to train on, far more samples need to be collected before the model shows any reasonable performance. More samples will be uploaded to this repository soon.
