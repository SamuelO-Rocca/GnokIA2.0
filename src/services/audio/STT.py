import speech_recognition as sr
import logging
import os

AUDIO_FILE = "audio_data.mp3"
WAY_AUDIO = os.path.join(os.getcwd(), "src/services/audio/mp3_files")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def capture_audio():
    recognizer = sr.Recognizer()
    recognizer.pause_threshold = 3.0
    with sr.Microphone() as source:
        logging.info("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration = 0.5)
        logging.info("Recording...")

        try:
            audio = recognizer.listen(source, phrase_time_limit=60)
            logging.info("Finished recording.")
            return audio
        except Exception as e:
            logging.error(f"Error during recording: {e}")
            return None
    

def processing_audio_to_text(audio_data, language="pt-BR"):
    if audio_data is None:
        logging.error("No audio data to process.")
        return None
    
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio_data, language=language)
        logging.info(f"Recognized text: {text}")
        return text
    except sr.UnknownValueError:
        logging.warning("Could not understand audio.")
        return None
    except sr.RequestError as e:
        logging.error(f"Could not acess the speech recognition service: {e}")
        return None
    except Exception as e:
        logging.error(f"Error during process audio to text: {e}")
        return None