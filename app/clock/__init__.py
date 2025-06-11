import pygame

def play_audio(audio_path):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    input("Press Enter to stop the audio...")
    pygame.mixer.music.stop()

if __name__ == "__main__":
    audio_path = "jarvis/application/clock/alarm_sound/zilly-pop-17767.mp3"
    play_audio(audio_path)
