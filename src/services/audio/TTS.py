import textwrap
import re
import asyncio
import os
import subprocess
import edge_tts
import platform

if platform.system() == "Windows":
    from playsound import playsound

class TTS:
    async def synthesize_text_to_speech_async(self, text):
        voice = "pt-BR-AntonioNeural"
        blocks = textwrap.wrap(text, width=1000, break_long_words=False)
        for i, block in enumerate(blocks):
            file_arquive = f"response_{i}.mp3"
            communicate = edge_tts.Communicate(block, voice=voice, rate="-5%", pitch="-2Hz", volume="+5dB")
            await communicate.save(file_arquive)
            if platform.system() == "Windows":
                playsound(file_arquive)
            else:
                subprocess.run(["mpg123", "-q", file_arquive])
            os.remove(file_arquive)
            await asyncio.sleep(0.5)

    def synthesize_text_to_speech(self, text):
        asyncio.run(self.synthesize_text_to_speech_async(text))

    def clear_text_tts(self, text):
        text = re.sub(r"[\u200B-\u200F\uFEFF]", "", text)
        text = re.sub(r"<\s*/?\s*[^>]*>", "", text)
        text = re.sub(r"\[\s*/?\s*[^\]]*\]", "", text)
        text = re.sub(r"[*_#`~^]", "", text)
        text = re.sub(r"\s{2,}", " ", text).strip()
        emoji_pattern = re.compile(
            "["
            "\U0001F600-\U0001F64F"
            "\U0001F300-\U0001F5FF"
            "\U0001F680-\U0001F6FF"
            "\U0001F1E0-\U0001F1FF"
            "]+", flags=re.UNICODE
        )
        text = emoji_pattern.sub(r"", text)
        return text