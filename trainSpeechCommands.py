from pyAudioAnalysis import audioTrainTest as aT
aT.featureAndTrain(["/home/brandonjabr/pyAudio/pyAudioAnalysis/wav/speech_commands/_background_noise_","/home/brandonjabr/pyAudio/pyAudioAnalysis/wav/speech_commands/one","/home/brandonjabr/pyAudio/pyAudioAnalysis/wav/speech_commands/two","/home/brandonjabr/pyAudio/pyAudioAnalysis/wav/speech_commands/three","/home/brandonjabr/pyAudio/pyAudioAnalysis/wav/speech_commands/four","/home/brandonjabr/pyAudio/pyAudioAnalysis/wav/speech_commands/five","/home/brandonjabr/pyAudio/pyAudioAnalysis/wav/speech_commands/six","/home/brandonjabr/pyAudio/pyAudioAnalysis/wav/speech_commands/seven","/home/brandonjabr/pyAudio/pyAudioAnalysis/wav/speech_commands/eight","/home/brandonjabr/pyAudio/pyAudioAnalysis/wav/speech_commands/nine","/home/brandonjabr/pyAudio/pyAudioAnalysis/wav/speech_commands/yes","/home/brandonjabr/pyAudio/pyAudioAnalysis/wav/speech_commands/no"], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
aT.fileClassification("/home/brandonjabr/pyAudio/pyAudioAnalysis/my-recordings/yes/1529689771.331.wav", "svmSMtemp","svm")