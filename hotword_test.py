import hotword
import snowboydecoder

def my_callback_func():
    snowboydecoder.play_audio_file()
    print("Haru detected!")

hotword_detection = hotword.hotword()
hotword_detection.start_detection(my_callback_func)
hotword_detection.terminate_detection()
