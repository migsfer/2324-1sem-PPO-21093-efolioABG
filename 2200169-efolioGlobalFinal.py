#!/usr/bin/python
'''========================================================================
Name        : 2200169_efolioGlobal.py
Author      : bmfernandes
Description : BrunoMiguelFernandes_2200169_efolioA
Date        : 28.02.2024

NOTAS       : versão Final, foram acrescentadas 2 funcionalidades Carregar/Guardar eventos 
            para ficheiro, e sons com o modulo pygame

python 2200169_efolioGlobal.py
============================================================================
'''
import os
import sys
import re
from copy import deepcopy
from random import randint
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame


class Jogador:
    def __init__(self, Nome, Pos, Marcou=0, Min_J=0, Seg_J=0):
        self.Nome = Nome
        self.Pos = Pos
        self.Marcou = Marcou
        self.Min_J = Min_J
        self.Seg_J = Seg_J

    def __str__(self):
        return f"{self.Pos:<8}{self.Nome:<24}\t{self.Marcou:>02d}\t[{self.Min_J:>02d}:{self.Seg_J:>02d}] "


class Equipa(Jogador):
    def __init__(self, Nome_Equipa, Lst_Jgdrs):
        super().__init__(None, None)
        self.Nome_Equipa = Nome_Equipa
        self.Lst_Jgdrs = Lst_Jgdrs

    def __str__(self):
        return f"{self.Nome_Equipa}"

    # sobrecarga de operador add
    def __add__(self, jogador):
        self.Lst_Jgdrs.append(jogador)
        return self


class InfoJogo:
    def __init__(self, Nome_Eq_Casa, Nome_Eq_Fora, GameType, Marcadr_Casa=0, Marcadr_Fora=0):
        self.Nome_Eq_Casa = Nome_Eq_Casa
        self.Nome_Eq_Fora = Nome_Eq_Fora
        self.GameType = GameType
        self.Marcadr_Casa = Marcadr_Casa
        self.Marcadr_Fora = Marcadr_Fora

    # polimorfismo
    def ShowinfoJogo(self):
        return f"{self.GameType:<4}:{self.Nome_Eq_Casa:<24}\t{self.Marcadr_Casa:>02d} - {self.Marcadr_Fora:>02d}\t{self.Nome_Eq_Fora:>24}] "


class InfoJogoFut(InfoJogo):
    def __init__(self, Nome_Eq_Casa, Nome_Eq_Fora, GameType, Marcadr_Casa, Marcadr_Fora, EquipaCasa, EquipaFora, Lst_Evnts):
        super().__init__(Nome_Eq_Casa, Nome_Eq_Fora, GameType, Marcadr_Casa, Marcadr_Fora)
        self.EquipaCasa = EquipaCasa
        self.EquipaFora = EquipaFora
        self.Lst_evnts = Lst_Evnts

    # polimorfismo
    def ShowInfoJogo(self):
        for it in range(5+len(self.EquipaCasa.Lst_Jgdrs)+len(self.EquipaFora.Lst_Jgdrs)):
            print("===", end='')
        print()
        print(self.GameType)
        print(self.Nome_Eq_Casa, "\t\t\t", self.Marcadr_Casa, "\t -\t ", self.Marcadr_Fora, "\t\t", self.Nome_Eq_Fora)
        for it in range(5+len(self.EquipaCasa.Lst_Jgdrs)+len(self.EquipaFora.Lst_Jgdrs)):
            print("===", end='')
        print()
        print("Titulares:")
        for i in range(max(len(self.EquipaCasa.Lst_Jgdrs), len(self.EquipaFora.Lst_Jgdrs))):
            if i == 11:
                for it in range(5+len(self.EquipaCasa.Lst_Jgdrs)+len(self.EquipaFora.Lst_Jgdrs)):
                    print("___", end='')
                print()
                print("Suplentes:")
            if i < len(self.EquipaCasa.Lst_Jgdrs):
                print("|| Jog{} - {}".format(i+1, self.EquipaCasa.Lst_Jgdrs[i]), end='')
            else:
                print("\t\t\t\t\t", end='\t')
            if i < len(self.EquipaFora.Lst_Jgdrs):
                print("|| Jog{} - {} ||".format(i+1+len(self.EquipaCasa.Lst_Jgdrs), self.EquipaFora.Lst_Jgdrs[i]))
        for it in range(5+len(self.EquipaCasa.Lst_Jgdrs)+len(self.EquipaFora.Lst_Jgdrs)):
            print("===", end='')
        print()
        # for evnt in self.Lst_evnts:
        #    print(evnt)

    def PlaySoundback(self):
        backnr = randint(1, 2).__str__()
        soundname = os.path.join(sys.path[0], 'soundGlobal', 'football-back'+backnr+'.mp3')
        pygame.mixer.music.load(soundname)
        pygame.mixer.music.play(-1)  # -1 plays the music in a loop

    def PlaySoundEvent(self, evnt):
        self.evnt = evnt
        print(self.evnt)
        soundname = pygame.mixer.Sound(os.path.join(sys.path[0], 'soundGlobal', 'football-'+self.evnt+'.mp3'))
        pygame.mixer.Sound.play(soundname)

    def PlaySoundSTOP(self):
        pygame.mixer.music.stop()
        pygame.mixer.stop()
        pygame.quit()


class InfoJogoBas(InfoJogo):
    def __init__(self, Nome_Eq_Casa, Nome_Eq_Fora, GameType, Marcadr_Casa, Marcadr_Fora, EquipaCasa, EquipaFora, Lst_Evnts):
        super().__init__(Nome_Eq_Casa, Nome_Eq_Fora, GameType, Marcadr_Casa, Marcadr_Fora)
        self.EquipaCasa = EquipaCasa
        self.EquipaFora = EquipaFora
        self.Lst_evnts = Lst_Evnts
        # print("Jogo Bas Created")

    # polimorfismo
    def ShowInfoJogo(self):
        for it in range((len(self.EquipaCasa.Lst_Jgdrs)+len(self.EquipaFora.Lst_Jgdrs))*2 + 20):
            print("==", end='')
        print()
        print(self.GameType)
        print(self.Nome_Eq_Casa, "\t\t\t", self.Marcadr_Casa, "\t -\t ", self.Marcadr_Fora, "\t\t", self.Nome_Eq_Fora)
        for it in range((len(self.EquipaCasa.Lst_Jgdrs)+len(self.EquipaFora.Lst_Jgdrs))*2 + 20):
            print("==", end='')
        print()
        print("Titulares:")
        for i in range(max(len(self.EquipaCasa.Lst_Jgdrs), len(self.EquipaFora.Lst_Jgdrs))):
            if i == 5:
                for it in range((len(self.EquipaCasa.Lst_Jgdrs)+len(self.EquipaFora.Lst_Jgdrs))*2 + 20):
                    print("__", end='')
                print()
                print("Suplentes:")
            if i < len(self.EquipaCasa.Lst_Jgdrs):
                print(f"|| Jog{i+1} - {self.EquipaCasa.Lst_Jgdrs[i]}", end='')
            else:
                print("\t\t\t\t\t", end='\t')
            if i < len(self.EquipaFora.Lst_Jgdrs):
                print("|| Jog{} - {} ||".format(i+1+len(self.EquipaCasa.Lst_Jgdrs), self.EquipaFora.Lst_Jgdrs[i]))
        for it in range((len(self.EquipaCasa.Lst_Jgdrs)+len(self.EquipaFora.Lst_Jgdrs))*2 + 20):
            print("==", end='')
        print()
        # for evnt in self.Lst_evnts:
        #     print(evnt)

    def PlaySoundback(self):
        backnr = randint(1, 3).__str__()
        soundname = os.path.join(sys.path[0], 'soundGlobal', 'basketball-back'+backnr+'.mp3')
        pygame.mixer.music.load(soundname)
        pygame.mixer.music.play(-1)  # -1 plays the music in a loop

    def PlaySoundEvent(self, evnt):
        self.evnt = evnt
        print(self.evnt)
        soundname = pygame.mixer.Sound(os.path.join(sys.path[0], 'soundGlobal', 'basketball-'+self.evnt+'.mp3'))
        pygame.mixer.Sound.play(soundname)

    def PlaySoundSTOP(self):
        pygame.mixer.music.stop()
        pygame.mixer.stop()
        pygame.quit()


def menusave():
    choice = ''

    choice = input("Pretende Guardar os Jogos das Ligas de Futebol e Basquetebol(S) ? ou Descartar os eventos desta sessão(N) ?").lower()
    while choice not in ['s', 'n']:
        choice = input("Guardar os Jogos das Ligas de Futebol e Basquetebol(S) ?").lower()

    print("\n")
    return choice


def menuload():
    choice = ''
    print("****************************************************************************************")
    print("****************************************************************************************")
    print("10porto \nInformação de Jogos das Ligas de Futebol e Basquetebol:")
    print("****************************************************************************************")
    print("****************************************************************************************\n\n")

    choice = input("Pretende Carregar os Jogos das Ligas de Futebol e Basquetebol(L) ? ou Iniciar sem Carregar dados(N) ?").lower()
    while choice not in ['l', 'n']:
        choice = input("Carregar(L) os Jogos das Ligas ou iniciar sem carregar(N) ?").lower()

    print("\n")
    return choice


def menu():
    choice = ''
    print("\n\n")
    print("1. Inserir Jogo da Liga de Futebol ")
    print("2. Inserir Jogo da Liga de Basquetebol")
    print("3. Mostrar Jogos ocorridos da Liga de Futebol")
    print("4. Mostrar Jogos ocorridos da Liga de Basquetebol")
    print("\nQ. Quit.\n")

    while choice not in ['1', '2', '3', '4', 'q', 'Q']:
        choice = input("Enter your choice:[1-4] ").lower()
    return choice


def loadEqps(filename):
    equipasDB = []

    with open(filename, 'r') as myfile:
        lines = myfile.readlines()
        i = 0
        while i < len(lines):
            equipaNome = lines[i].strip()
            i += 1
            equipasDB.append(Equipa(equipaNome, []))
            while i < len(lines) and lines[i].strip() != "":
                jogadorLine = lines[i].strip().split(',')
                playah = Jogador(jogadorLine[0], jogadorLine[1])
                equipasDB[-1] = equipasDB[-1] + playah
                i += 1
            i += 1

    return equipasDB


def user_choice_int(prompt, len_Lst):
    lim_min = 0
    choice = 'N/A'

    while choice.isdigit() is False or (int(choice) not in range(lim_min+1, len_Lst+1)):
        choice = input(prompt)
        if choice.isdigit() is False:
            print("NOT A NUMBER")
        elif choice.isdigit() is True:
            if int(choice) not in range(lim_min+1, len_Lst+1):
                print("NOT IN RANGE[", lim_min+1, "-", len_Lst, "]")
                choice = 'N/A'
    return int(choice)


def InsereJogoFute(LstEquipasFut):
    choice = ''
    LstEvnts = []
    index = 0
    indexSub = 0

    print(len(LstEquipasFut))
    print("Escolha o Nr. das Equipas que vão jogar:")
    print("Equipa que joga em Casa: ")
    print("Nr.")
    for i in range(len(LstEquipasFut)):
        print(i+1, "\tEquipa: ", LstEquipasFut[i])
    print("\nEscolha o Nr. da Equipa que joga em Casa:")
    choice = user_choice_int("InsereJogoFut-> ", len(LstEquipasFut))
    EquipaCasa = deepcopy(LstEquipasFut[choice-1])
    print(EquipaCasa)
    while (EquipaCasa.Nome_Equipa == LstEquipasFut[choice-1].Nome_Equipa):
        print("\nEquipa que joga Fora: ")
        choice = user_choice_int("InsereJogoFut-> ", len(LstEquipasFut))
        EquipaFora = deepcopy(LstEquipasFut[choice-1])
        print(EquipaFora)
        if EquipaCasa.Nome_Equipa == LstEquipasFut[choice-1].Nome_Equipa:
            print("**Equipa Fora não pode ser igual á equipa da Casa **")

    JogoFut = InfoJogoFut(EquipaCasa.Nome_Equipa, EquipaFora.Nome_Equipa, "Fut", 0, 0, EquipaCasa, EquipaFora, [])
    # Initialize pygame
    pygame.init()
    JogoFut.PlaySoundback()

    while True:
        index = 0
        print("\033[H\033[J", end="")  # clear screen
        JogoFut.ShowInfoJogo()
        if len(LstEvnts) > 0:
            print("Evento Inserido:  ", LstEvnts[-1], " Inválido !!!")
            LstEvnts.clear()
        print("Inserir eventos do Jogo de Futebol('q' para concluir eventos do jogo): ")
        choice = input("-> ")
        LstEvnts.append(choice)
        if choice.lower() == 'q':
            break

        if re.match(r"^Jog[0-9][0-9]?,[0-9][0-9]?$", choice):
            print("golo-\U000026bd")
            index = int(choice.split('g')[-1].split(',')[0]) - 1
            if index >= 0 and index < 11:
                if "\U0001f7e5" not in JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaCasa.Lst_Jgdrs[index].Marcou += 1
                    JogoFut.Marcadr_Casa += 1
                    JogoFut.Nome_Eq_Casa += "\U000026bd"
                    JogoFut.Lst_evnts.append(choice)
                    LstEvnts.clear()
                    JogoFut.PlaySoundEvent("g2")
            elif index >= 18 and index < 29:
                index -= 18
                if "\U0001f7e5" not in JogoFut.EquipaFora.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaFora.Lst_Jgdrs[index].Marcou += 1
                    JogoFut.Marcadr_Fora += 1
                    JogoFut.Nome_Eq_Fora = "\U000026bd" + JogoFut.Nome_Eq_Fora
                    JogoFut.Lst_evnts.append(choice)
                    LstEvnts.clear()
                    JogoFut.PlaySoundEvent("g2")

        if re.match(r"^Jog[0-9][0-9]?,Jog[1-3][0-9]?,[0-9][0-9]?$", choice):
            print("sub-\U0001f504")
            indexSub = int(choice.split('g')[-1].split(',')[0]) - 1
            index = int(choice.split(',')[0].split('g')[-1]) - 1
            if index >= 0 and index < 11 and indexSub >= 11:
                if "\U0001f504" not in JogoFut.EquipaCasa.Lst_Jgdrs[indexSub].Nome and "\U0001f7e5" not in JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome += "\U0001f504"
                    JogoFut.EquipaCasa.Lst_Jgdrs[index], JogoFut.EquipaCasa.Lst_Jgdrs[indexSub] = JogoFut.EquipaCasa.Lst_Jgdrs[indexSub], JogoFut.EquipaCasa.Lst_Jgdrs[index]
                    JogoFut.Lst_evnts.append(choice)
                    LstEvnts.clear()
                    JogoFut.PlaySoundEvent("s1")
            elif index >= 18 and index < 29 and indexSub >= 29:
                index -= 18
                indexSub -= 18
                if "\U0001f504" not in JogoFut.EquipaFora.Lst_Jgdrs[indexSub].Nome and "\U0001f7e5" not in JogoFut.EquipaFora.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaFora.Lst_Jgdrs[index].Nome += "\U0001f504"
                    JogoFut.EquipaFora.Lst_Jgdrs[index], JogoFut.EquipaFora.Lst_Jgdrs[indexSub] = JogoFut.EquipaFora.Lst_Jgdrs[indexSub], JogoFut.EquipaFora.Lst_Jgdrs[index]
                    JogoFut.Lst_evnts.append(choice)
                    LstEvnts.clear()
                    JogoFut.PlaySoundEvent("s1")

        if re.match(r"^Jog[0-9][0-9]?,\*,[0-9][0-9]?$", choice):
            print("amarelo-\U0001f7e8")
            index = int(choice.split('g')[-1].split(',')[0]) - 1
            if index >= 0 and index < 11:
                if "\U0001f7e8" in JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome and "\U0001f7e5" not in JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome += "\U0001f7e5"
                    JogoFut.Lst_evnts.append(choice)
                    LstEvnts.clear()
                    JogoFut.PlaySoundEvent("w3")
                elif not any(x in JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome for x in ["\U0001f504", "\U0001f7e5"]):
                    JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome += "\U0001f7e8"
                    JogoFut.Lst_evnts.append(choice)
                    LstEvnts.clear()
                    JogoFut.PlaySoundEvent("w2")
            elif index >= 18 and index < 29:
                index -= 18
                if "\U0001f7e8" in JogoFut.EquipaFora.Lst_Jgdrs[index].Nome and "\U0001f7e5" not in JogoFut.EquipaFora.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaFora.Lst_Jgdrs[index].Nome += "\U0001f7e5"
                    JogoFut.Lst_evnts.append(choice)
                    LstEvnts.clear()
                    JogoFut.PlaySoundEvent("w3")
                elif not any(x in JogoFut.EquipaFora.Lst_Jgdrs[index].Nome for x in ["\U0001f504", "\U0001f7e5"]):
                    JogoFut.EquipaFora.Lst_Jgdrs[index].Nome += "\U0001f7e8"
                    JogoFut.Lst_evnts.append(choice)
                    LstEvnts.clear()
                    JogoFut.PlaySoundEvent("w2")

        if re.match(r"^Jog[0-9][0-9]?,\*\*,[0-9][0-9]?$", choice):
            print("vermelho-\U0001f7e5")
            index = int(choice.split('g')[-1].split(',')[0]) - 1
            if index >= 0 and index < 11:
                if "\U0001f7e5" not in JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome += "\U0001f7e5"
                    JogoFut.Lst_evnts.append(choice)
                    LstEvnts.clear()
                    JogoFut.PlaySoundEvent("w3")
            elif index >= 18 and index < 29:
                index -= 18
                if "\U0001f7e5" not in JogoFut.EquipaFora.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaFora.Lst_Jgdrs[index].Nome += "\U0001f7e5"
                    JogoFut.Lst_evnts.append(choice)
                    LstEvnts.clear()
                    JogoFut.PlaySoundEvent("w3")

        if re.match(r"^Jog[0-9][0-9],\#,[1-9][1-9]?$", choice):
            print("own3d-\U0001f945")
            index = int(choice.split('g')[-1].split(',')[0]) - 1
            if index >= 0 and index < 11:
                if "\U0001f7e5" not in JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaCasa.Lst_Jgdrs[index].Marcou += 1
                    JogoFut.Marcadr_Fora += 1
                    JogoFut.Nome_Eq_Fora = "\U0001f945" + JogoFut.Nome_Eq_Fora
                    JogoFut.Lst_evnts.append(choice)
                    LstEvnts.clear()
                    JogoFut.PlaySoundEvent("o3")
            elif index >= 18 and index < 29:
                index -= 18
                if "\U0001f7e5" not in JogoFut.EquipaFora.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaFora.Lst_Jgdrs[index].Marcou += 1
                    JogoFut.Marcadr_Casa += 1
                    JogoFut.Nome_Eq_Casa += "\U0001f945"
                    JogoFut.Lst_evnts.append(choice)
                    LstEvnts.clear()
                    JogoFut.PlaySoundEvent("o3")
    JogoFut.PlaySoundSTOP()
    return JogoFut



def InsereJogoBasq(LstEquipasBas):
    choice = ''
    LstEvnts = []
    index = 0
    pontos = 0
    maxpnts = 0
    minutos = 0
    segs = 0

    print(len(LstEquipasBas))
    print("Escolha o Nr. das Equipas que vão jogar:")
    print("Equipa que joga em Casa: ")
    print("Nr.")
    for i in range(len(LstEquipasBas)):
        print(i+1, "\tEquipa: ", LstEquipasBas[i])
    print("\nEscolha o Nr. da Equipa que joga em Casa:")
    choice = user_choice_int("InsereJogoBas-> ", len(LstEquipasBas))
    EquipaCasa = deepcopy(LstEquipasBas[choice-1])
    print(EquipaCasa)
    while (EquipaCasa.Nome_Equipa == LstEquipasBas[choice-1].Nome_Equipa):
        print("\nEquipa que joga Fora: ")
        choice = user_choice_int("InsereJogoBas-> ", len(LstEquipasBas))
        EquipaFora = deepcopy(LstEquipasBas[choice-1])
        print(EquipaFora)
        if EquipaCasa.Nome_Equipa == LstEquipasBas[choice-1].Nome_Equipa:
            print("**Equipa Fora não pode ser igual á equipa da Casa **")

    JogoBas = InfoJogoBas(EquipaCasa.Nome_Equipa, EquipaFora.Nome_Equipa, "Bas", 0, 0, EquipaCasa, EquipaFora, [])
    # Initialize pygame
    pygame.init()
    JogoBas.PlaySoundback()

    while True:
        index = 0
        print("\033[H\033[J", end="")  # clear screen
        JogoBas.ShowInfoJogo()
        if len(LstEvnts) > 0:
            print("Evento Inserido:  ", LstEvnts[-1], " Inválido !!!")
            LstEvnts.clear()
        print("Inserir eventos do Jogo de Basquetebol('q' para concluir eventos do jogo): ")
        choice = input("-> ")
        LstEvnts.append(choice)
        if choice.lower() == 'q':
            break

        if re.match(r"^Jog[0-9][0-9]?,[0-9][0-9]?$", choice):
            print("pontos-\U0001f3c0")
            index = int(choice.split('g')[-1].split(',')[0]) - 1
            pontos = int(choice.split(',')[-1])
            maxpnts = 0
            i = 0
            if index >= 0 and index < 12:
                JogoBas.EquipaCasa.Lst_Jgdrs[index].Marcou += pontos
                JogoBas.Marcadr_Casa += pontos
                for i in range(len(JogoBas.EquipaCasa.Lst_Jgdrs)):
                    if "\U0001f3c0" in JogoBas.EquipaCasa.Lst_Jgdrs[i].Nome:
                        JogoBas.EquipaCasa.Lst_Jgdrs[i].Nome = JogoBas.EquipaCasa.Lst_Jgdrs[i].Nome[:-1]
                    if JogoBas.EquipaCasa.Lst_Jgdrs[i].Marcou > maxpnts:
                        maxpnts = JogoBas.EquipaCasa.Lst_Jgdrs[i].Marcou
                        index = i
                JogoBas.EquipaCasa.Lst_Jgdrs[index].Nome += "\U0001f3c0"
                JogoBas.Lst_evnts.append(choice)
                LstEvnts.clear()
                JogoBas.PlaySoundEvent("s3")
            elif index >= 12 and index < 24:
                index -= 12
                JogoBas.EquipaFora.Lst_Jgdrs[index].Marcou += pontos
                JogoBas.Marcadr_Fora += pontos
                for i in range(len(JogoBas.EquipaFora.Lst_Jgdrs)):
                    if "\U0001f3c0" in JogoBas.EquipaFora.Lst_Jgdrs[i].Nome:
                        JogoBas.EquipaFora.Lst_Jgdrs[i].Nome = JogoBas.EquipaFora.Lst_Jgdrs[i].Nome[:-1]
                    if JogoBas.EquipaFora.Lst_Jgdrs[i].Marcou > maxpnts:
                        maxpnts = JogoBas.EquipaFora.Lst_Jgdrs[i].Marcou
                        index = i
                JogoBas.EquipaFora.Lst_Jgdrs[index].Nome += "\U0001f3c0"
                JogoBas.Lst_evnts.append(choice)
                LstEvnts.clear()
                JogoBas.PlaySoundEvent("s3")

        if re.match(r"^Jog[0-9][0-9]?,[0-9][0-9]?:[0-9][0-9]?$", choice):
            print("played-\U0001f552")
            index = int(choice.split(',')[0].split('g')[-1]) - 1
            minutos = int(choice.split(',')[-1].split(':')[0])
            segs = int(choice.split(',')[-1].split(':')[-1])
            if index >= 0 and index < 12 and (0 <= segs < 60) and (0 <= minutos <= 20):
                if "\U0001f552" not in JogoBas.EquipaCasa.Lst_Jgdrs[index].Nome:
                    JogoBas.EquipaCasa.Lst_Jgdrs[index].Nome = "\U0001f552" + JogoBas.EquipaCasa.Lst_Jgdrs[index].Nome
                JogoBas.EquipaCasa.Lst_Jgdrs[index].Min_J = minutos
                JogoBas.EquipaCasa.Lst_Jgdrs[index].Seg_J = segs
                JogoBas.Lst_evnts.append(choice)
                LstEvnts.clear()
                JogoBas.PlaySoundEvent("p2")
            elif index >= 12 and index < 24 and (0 <= segs < 60) and (0 <= minutos <= 20):
                index -= 12
                if "\U0001f552" not in JogoBas.EquipaFora.Lst_Jgdrs[index].Nome:
                    JogoBas.EquipaFora.Lst_Jgdrs[index].Nome = "\U0001f552" + JogoBas.EquipaFora.Lst_Jgdrs[index].Nome
                JogoBas.EquipaFora.Lst_Jgdrs[index].Min_J = minutos
                JogoBas.EquipaFora.Lst_Jgdrs[index].Seg_J = segs
                JogoBas.Lst_evnts.append(choice)
                LstEvnts.clear()
                JogoBas.PlaySoundEvent("p2")
    JogoBas.PlaySoundSTOP()
    return JogoBas


def AddEvntsFut(LstEquipasFut, LstEvntsFut):

    LstEvnts = []
    index = 0
    indexSub = 0

    for i in range(len(LstEquipasFut)):
        if LstEvntsFut[0].split(',')[0] in LstEquipasFut[i].Nome_Equipa:
            EquipaCasa = deepcopy(LstEquipasFut[i])
            # print(EquipaCasa)
        elif LstEvntsFut[0].split(',')[-1] in LstEquipasFut[i].Nome_Equipa:
            EquipaFora = deepcopy(LstEquipasFut[i])
            # print(EquipaFora)


    JogoFut = InfoJogoFut(EquipaCasa.Nome_Equipa, EquipaFora.Nome_Equipa, "Fut", 0, 0, EquipaCasa, EquipaFora, [])

    for event in LstEvntsFut[1:]:
        if re.match(r"^Jog[0-9][0-9]?,[0-9][0-9]?$", event):
            # print("golo-\U000026bd")
            index = int(event.split('g')[-1].split(',')[0]) - 1
            if index >= 0 and index < 11:
                if "\U0001f7e5" not in JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaCasa.Lst_Jgdrs[index].Marcou += 1
                    JogoFut.Marcadr_Casa += 1
                    JogoFut.Nome_Eq_Casa += "\U000026bd"
                    JogoFut.Lst_evnts.append(event)
                    LstEvnts.clear()
            elif index >= 18 and index < 29:
                index -= 18
                if "\U0001f7e5" not in JogoFut.EquipaFora.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaFora.Lst_Jgdrs[index].Marcou += 1
                    JogoFut.Marcadr_Fora += 1
                    JogoFut.Nome_Eq_Fora = "\U000026bd" + JogoFut.Nome_Eq_Fora
                    JogoFut.Lst_evnts.append(event)
                    LstEvnts.clear()

        if re.match(r"^Jog[0-9][0-9]?,Jog[1-3][0-9]?,[0-9][0-9]?$", event):
            # print("sub-\U0001f504")
            indexSub = int(event.split('g')[-1].split(',')[0]) - 1
            index = int(event.split(',')[0].split('g')[-1]) - 1
            if index >= 0 and index < 11 and indexSub >= 11:
                if "\U0001f504" not in JogoFut.EquipaCasa.Lst_Jgdrs[indexSub].Nome and "\U0001f7e5" not in JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome += "\U0001f504"
                    JogoFut.EquipaCasa.Lst_Jgdrs[index], JogoFut.EquipaCasa.Lst_Jgdrs[indexSub] = JogoFut.EquipaCasa.Lst_Jgdrs[indexSub], JogoFut.EquipaCasa.Lst_Jgdrs[index]
                    JogoFut.Lst_evnts.append(event)
                    LstEvnts.clear()
            elif index >= 18 and index < 29 and indexSub >= 29:
                index -= 18
                indexSub -= 18
                if "\U0001f504" not in JogoFut.EquipaFora.Lst_Jgdrs[indexSub].Nome and "\U0001f7e5" not in JogoFut.EquipaFora.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaFora.Lst_Jgdrs[index].Nome += "\U0001f504"
                    JogoFut.EquipaFora.Lst_Jgdrs[index], JogoFut.EquipaFora.Lst_Jgdrs[indexSub] = JogoFut.EquipaFora.Lst_Jgdrs[indexSub], JogoFut.EquipaFora.Lst_Jgdrs[index]
                    JogoFut.Lst_evnts.append(event)
                    LstEvnts.clear()

        if re.match(r"^Jog[0-9][0-9]?,\*,[0-9][0-9]?$", event):
            # print("amarelo-\U0001f7e8")
            index = int(event.split('g')[-1].split(',')[0]) - 1
            if index >= 0 and index < 11:
                if "\U0001f7e8" in JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome and "\U0001f7e5" not in JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome += "\U0001f7e5"
                    JogoFut.Lst_evnts.append(event)
                    LstEvnts.clear()
                elif not any(x in JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome for x in ["\U0001f504", "\U0001f7e5"]):
                    JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome += "\U0001f7e8"
                    JogoFut.Lst_evnts.append(event)
                    LstEvnts.clear()
            elif index >= 18 and index < 29:
                index -= 18
                if "\U0001f7e8" in JogoFut.EquipaFora.Lst_Jgdrs[index].Nome and "\U0001f7e5" not in JogoFut.EquipaFora.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaFora.Lst_Jgdrs[index].Nome += "\U0001f7e5"
                    JogoFut.Lst_evnts.append(event)
                    LstEvnts.clear()
                elif not any(x in JogoFut.EquipaFora.Lst_Jgdrs[index].Nome for x in ["\U0001f504", "\U0001f7e5"]):
                    JogoFut.EquipaFora.Lst_Jgdrs[index].Nome += "\U0001f7e8"
                    JogoFut.Lst_evnts.append(event)
                    LstEvnts.clear()

        if re.match(r"^Jog[0-9][0-9]?,\*\*,[0-9][0-9]?$", event):
            # print("vermelho-\U0001f7e5")
            index = int(event.split('g')[-1].split(',')[0]) - 1
            if index >= 0 and index < 11:
                if "\U0001f7e5" not in JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome += "\U0001f7e5"
                    JogoFut.Lst_evnts.append(event)
                    LstEvnts.clear()
            elif index >= 18 and index < 29:
                index -= 18
                if "\U0001f7e5" not in JogoFut.EquipaFora.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaFora.Lst_Jgdrs[index].Nome += "\U0001f7e5"
                    JogoFut.Lst_evnts.append(event)
                    LstEvnts.clear()

        if re.match(r"^Jog[0-9][0-9],\#,[1-9][1-9]?$", event):
            # print("own3d-\U0001f945")
            index = int(event.split('g')[-1].split(',')[0]) - 1
            if index >= 0 and index < 11:
                if "\U0001f7e5" not in JogoFut.EquipaCasa.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaCasa.Lst_Jgdrs[index].Marcou += 1
                    JogoFut.Marcadr_Fora += 1
                    JogoFut.Nome_Eq_Fora = "\U0001f945" + JogoFut.Nome_Eq_Fora
                    JogoFut.Lst_evnts.append(event)
                    LstEvnts.clear()
            elif index >= 18 and index < 29:
                index -= 18
                if "\U0001f7e5" not in JogoFut.EquipaFora.Lst_Jgdrs[index].Nome:
                    JogoFut.EquipaFora.Lst_Jgdrs[index].Marcou += 1
                    JogoFut.Marcadr_Casa += 1
                    JogoFut.Nome_Eq_Casa += "\U0001f945"
                    JogoFut.Lst_evnts.append(event)
                    LstEvnts.clear()
    return JogoFut


def AddEvntsBas(LstEquipasBas, LstEvntsBas):

    LstEvnts = []
    index = 0
    pontos = 0
    maxpnts = 0
    minutos = 0
    segs = 0

    for i in range(len(LstEquipasBas)):
        if LstEvntsBas[0].split(',')[0] in LstEquipasBas[i].Nome_Equipa:
            EquipaCasa = deepcopy(LstEquipasBas[i])
            # print(EquipaCasa)
        elif LstEvntsBas[0].split(',')[-1] in LstEquipasBas[i].Nome_Equipa:
            EquipaFora = deepcopy(LstEquipasBas[i])
            # print(EquipaFora)

    JogoBas = InfoJogoBas(EquipaCasa.Nome_Equipa, EquipaFora.Nome_Equipa, "Bas", 0, 0, EquipaCasa, EquipaFora, [])

    for event in LstEvntsBas[1:]:
        if re.match(r"^Jog[0-9][0-9]?,[0-9][0-9]?$", event):
            # print("pontos-\U0001f3c0")
            index = int(event.split('g')[-1].split(',')[0]) - 1
            pontos = int(event.split(',')[-1])
            maxpnts = 0
            i = 0
            if index >= 0 and index < 12:
                JogoBas.EquipaCasa.Lst_Jgdrs[index].Marcou += pontos
                JogoBas.Marcadr_Casa += pontos
                for i in range(len(JogoBas.EquipaCasa.Lst_Jgdrs)):
                    if "\U0001f3c0" in JogoBas.EquipaCasa.Lst_Jgdrs[i].Nome:
                        JogoBas.EquipaCasa.Lst_Jgdrs[i].Nome = JogoBas.EquipaCasa.Lst_Jgdrs[i].Nome[:-1]
                    if JogoBas.EquipaCasa.Lst_Jgdrs[i].Marcou > maxpnts:
                        maxpnts = JogoBas.EquipaCasa.Lst_Jgdrs[i].Marcou
                        index = i
                JogoBas.EquipaCasa.Lst_Jgdrs[index].Nome += "\U0001f3c0"
                JogoBas.Lst_evnts.append(event)
                LstEvnts.clear()
            elif index >= 12 and index < 24:
                index -= 12
                JogoBas.EquipaFora.Lst_Jgdrs[index].Marcou += pontos
                JogoBas.Marcadr_Fora += pontos
                for i in range(len(JogoBas.EquipaFora.Lst_Jgdrs)):
                    if "\U0001f3c0" in JogoBas.EquipaFora.Lst_Jgdrs[i].Nome:
                        JogoBas.EquipaFora.Lst_Jgdrs[i].Nome = JogoBas.EquipaFora.Lst_Jgdrs[i].Nome[:-1]
                    if JogoBas.EquipaFora.Lst_Jgdrs[i].Marcou > maxpnts:
                        maxpnts = JogoBas.EquipaFora.Lst_Jgdrs[i].Marcou
                        index = i
                JogoBas.EquipaFora.Lst_Jgdrs[index].Nome += "\U0001f3c0"
                JogoBas.Lst_evnts.append(event)
                LstEvnts.clear()

        if re.match(r"^Jog[0-9][0-9]?,[0-9][0-9]?:[0-9][0-9]?$", event):
            # print("played-\U0001f552")
            index = int(event.split(',')[0].split('g')[-1]) - 1
            minutos = int(event.split(',')[-1].split(':')[0])
            segs = int(event.split(',')[-1].split(':')[-1])
            if index >= 0 and index < 12 and (0 <= segs < 60) and (0 <= minutos <= 20):
                if "\U0001f552" not in JogoBas.EquipaCasa.Lst_Jgdrs[index].Nome:
                    JogoBas.EquipaCasa.Lst_Jgdrs[index].Nome = "\U0001f552" + JogoBas.EquipaCasa.Lst_Jgdrs[index].Nome
                JogoBas.EquipaCasa.Lst_Jgdrs[index].Min_J = minutos
                JogoBas.EquipaCasa.Lst_Jgdrs[index].Seg_J = segs
                JogoBas.Lst_evnts.append(event)
                LstEvnts.clear()
            elif index >= 12 and index < 24 and (0 <= segs < 60) and (0 <= minutos <= 20):
                index -= 12
                if "\U0001f552" not in JogoBas.EquipaFora.Lst_Jgdrs[index].Nome:
                    JogoBas.EquipaFora.Lst_Jgdrs[index].Nome = "\U0001f552" + JogoBas.EquipaFora.Lst_Jgdrs[index].Nome
                JogoBas.EquipaFora.Lst_Jgdrs[index].Min_J = minutos
                JogoBas.EquipaFora.Lst_Jgdrs[index].Seg_J = segs
                JogoBas.Lst_evnts.append(event)
                LstEvnts.clear()
    return JogoBas

def main():
    choice = ''

    fnEquipasFut = "EquipasFut.db"
    fnEquipasBas = "EquipasBas.db"
    fnEvntsFut = "EvntsFut.sav"
    fnEvntsBas = "EvntsBas.sav"

    LstEquipasFut = loadEqps(os.path.join(sys.path[0], fnEquipasFut))
    LstEquipasBas = loadEqps(os.path.join(sys.path[0], fnEquipasBas))
    LstEvntsFut = []
    LstEvntsBas = []

    JogosLigaFut = []
    JogosLigaBas = []

    choice = menuload()
    if choice == 'l':
        print("Loading .....")
        if not os.path.isfile(os.path.join(sys.path[0], fnEvntsFut)):
            print("Ficheiro", fnEvntsFut, " does not exist")
        elif os.path.isfile(os.path.join(sys.path[0], fnEvntsFut)):
            with open(os.path.join(sys.path[0], fnEvntsFut), mode='r') as myfile:
                for line in myfile:
                    if line.strip() != '-':
                        # print(line.strip())
                        LstEvntsFut.append(line.strip())
                    elif line.strip() == '-':
                        JogosLigaFut.append(AddEvntsFut(LstEquipasFut, LstEvntsFut))
                        LstEvntsFut.clear()
            myfile.close()

        if not os.path.isfile(os.path.join(sys.path[0], fnEvntsBas)):
            print("Ficheiro", fnEvntsBas, " does not exist")
        elif os.path.isfile(os.path.join(sys.path[0], fnEvntsBas)):
            with open(os.path.join(sys.path[0], fnEvntsBas), mode='r') as myfile:
                for line in myfile:
                    if line.strip() != '-':
                        # print(line.strip())
                        LstEvntsBas.append(line.strip())
                    elif line.strip() == '-':
                        JogosLigaBas.append(AddEvntsBas(LstEquipasBas, LstEvntsBas))
                        LstEvntsBas.clear()
            myfile.close()
        # JogosLigaBas.append(AddEvntsBas(LstEquipasBas, LstEvntsBas))
    else:
        print("")

    while True:
        choice = menu()
        if choice == '1':
            print("You selected Option 1.")
            print("\033[H\033[J", end="")  # clear screen
            JogosLigaFut.append(InsereJogoFute(LstEquipasFut))
            JogosLigaFut[-1].ShowInfoJogo()
        elif choice == '2':
            print("You selected Option 2.")
            print("\033[H\033[J", end="")  # clear screen
            JogosLigaBas.append(InsereJogoBasq(LstEquipasBas))
            JogosLigaBas[-1].ShowInfoJogo()
        elif choice == '3':
            print("You selected Option 3.")
            # print("\033[H\033[J", end="")  # clear screen
            print('\n'*200)
            for jogo in JogosLigaFut:
                jogo.ShowInfoJogo()
        elif choice == '4':
            print("You selected Option 4.")
            # print("\033[H\033[J", end="")  # clear screen
            print('\n'*200)
            for jogo in JogosLigaBas:
                jogo.ShowInfoJogo()
        elif choice == 'q':
            # print("\033[H\033[J", end="")  # clear screen
            print("Exiting the program...")
            choice = menusave()
            if choice == 's':
                print("Saving...")
                with open(os.path.join(sys.path[0], fnEvntsFut), mode='w') as myfile:
                    for jogo in JogosLigaFut:
                        myfile.write(jogo.Nome_Eq_Casa.replace("\U000026bd", '').replace("\U0001f945", '')+","+jogo.Nome_Eq_Fora.replace("\U000026bd", '').replace("\U0001f945", '')+'\n')
                        for line in jogo.Lst_evnts:
                            myfile.write(line+'\n')
                        myfile.write("-"+'\n')
                myfile.close()
                with open(os.path.join(sys.path[0], fnEvntsBas), mode='w') as myfile:
                    for jogo in JogosLigaBas:
                        myfile.write(jogo.Nome_Eq_Casa+","+jogo.Nome_Eq_Fora+'\n')
                        for line in jogo.Lst_evnts:
                            myfile.write(line+'\n')
                        myfile.write("-"+'\n')
                myfile.close()

            return
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
