import speech_recognition as sr
import logging
import os

AUDIO_FILE = "audio_data.mp3"
WAY_AUDIO = os.path.join(os.getcwd(), "src/services/audio/mp3_files")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def capture_audio(flag_recording):
    recorgnizer = sr.Recognizer()
    with sr.Microphone() as source:
        logging.info("Listening...")
        recorgnizer.adjust_for_ambient_noise(source, duration = 0.5)
        buffer_frames = []
        sample_rate = 44100
        sample_width = 2

        logging.info("Recording...")


        try:
            while flag_recording():
                frame = source.stream.read(source.CHUNK)
                buffer_frames.append(frame)
        except Exception as e:
            logging.error(f"Error during recording: {e}")
            return None
        logging.info("Finished recording.")


        full_audio = b''.join(buffer_frames)
        audio_data = sr.AudioData(
            frame_data = full_audio,
            sample_rate = sample_rate,
            sample_width = sample_width
        )
        return audio_data
    
def processing_audio_to_text(audio_data, language="pt-BR", second_language="en-US"):
    if audio_data is None:
        logging.error("No audio data to process.")
        return None
    
    recorgnizer = sr.Recognizer()
    try:
        text = recorgnizer.recognize_google(audio_data, language=language or second_language)
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