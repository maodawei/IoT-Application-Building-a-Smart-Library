# Refernce: Week10 Practical material
# Reference: https://pypi.org/project/SpeechRecognition/
# Reference: https://www.geeksforgeeks.org/speech-recognition-in-python-using-google-speech-api/
# Note this example requires PyAudio because it uses the Microphone class

# pip3 install SpeechRecognition
# sudo apt-get install portaudio19-dev python-all-dev python3-all-dev
# pip3 install pyaudio
# pip3 install google-api-python-client
# sudo apt-get install flac
# python3 01_microphoneGoogle.py

# import speech_recognition as sr
# import subprocess

# MIC_NAME = "Microsoft® LifeCam HD-3000: USB Audio (hw:1,0)"


class voice_recognition:
    @staticmethod
    def getTextFromVoice():
        """
        In order to search book details such as ISBN, Title or Author through user's voice google speech_recogntion package
        is presented. By calling this method system waits for the user to say something. Google speech_recognition
        translate the voice to text and returns the text value. 

        Parameters:

        Returns:
            Converted voice to text
        """
        # # Set the device ID of the mic that we specifically want to use to avoid ambiguity
        # for i, microphone_name in enumerate(sr.Microphone.list_microphone_names()):
        #     if(microphone_name == MIC_NAME):
        #         device_id = i
        #         break

        # # obtain audio from the microphone
        # r = sr.Recognizer()
        # with sr.Microphone(device_index = device_id) as source:
        #     # clear console of errors
        #     subprocess.run("clear")

        #     # wait for a second to let the recognizer adjust the
        #     # energy threshold based on the surrounding noise level
        #     r.adjust_for_ambient_noise(source)

        #     print("Say your part of the book details to search for...")
        #     try:
        #         audio = r.listen(source, timeout = 1.5)
        #     except sr.WaitTimeoutError:
        #         return None

        # # recognize speech using Google Speech Recognition
        # text = None
        # try:
        #     # for testing purposes, we're just using the default API key
        #     # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        #     # instead of `r.recognize_google(audio)`
        #     text = r.recognize_google(audio)
        # except(sr.UnknownValueError, sr.RequestError):
        #     pass
        # finally:
        #     return text