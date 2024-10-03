import signal
from threading import Thread
from Modules.Osint_Menu import main_menu  
from Modules.Utilities import Helpers
import pygame

# Inicia mi Progama
if __name__ == "__main__":
    #  Ctrl+C
    signal.signal(signal.SIGINT, Helpers.control_De_salida)
    #Music
    music_file = Helpers.get_music_file_path('Adiccion.mp3') 
    music_thread = Thread(target=Helpers.play_music, args=(music_file,))
    music_thread.start()
    # Mostrar el menú principal
    main_menu()
    pygame.mixer.music.stop()
    music_thread.join()
