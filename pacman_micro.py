class SongPlayer:
    def __init__(self) -> None:
        self.playsong_x = 0
        self.playsong_y = 0
        self.power_up_ost = []
        self.pacman_intro_ost = []
        self.pacman_bg_ost = []
        self.sfx_ost = []
        # MUSICA 1 - POWER-UP
        # COMECO DAS NOTAS
        self.power_up_ost.append(587)
        self.power_up_ost.append(880)
        self.power_up_ost.append(784)
        self.power_up_ost.append(740)
        self.power_up_ost.append(659)
        self.power_up_ost.append(0) # Pausas = 0
        self.power_up_ost.append(587)
        self.power_up_ost.append(880)
        self.power_up_ost.append(784)
        self.power_up_ost.append(740)
        self.power_up_ost.append(587)
        self.power_up_ost.append(0)
        self.power_up_ost.append(587)
        self.power_up_ost.append(659)
        self.power_up_ost.append(740)
        self.power_up_ost.append(784)
        self.power_up_ost.append(880)
        self.power_up_ost.append(0)
        self.power_up_ost.append(587)
        self.power_up_ost.append(587)
        self.power_up_ost.append(523)
        self.power_up_ost.append(523)
        self.power_up_ost.append(440)
        self.power_up_ost.append(392)
        self.power_up_ost.append(440)
        # COMECO DOS TEMPOS
        self.power_up_ost.append(music.beat(BeatFraction.HALF))
        self.power_up_ost.append(music.beat(BeatFraction.HALF))
        self.power_up_ost.append(music.beat(BeatFraction.QUARTER))
        self.power_up_ost.append(music.beat(BeatFraction.HALF))
        self.power_up_ost.append(music.beat(BeatFraction.DOUBLE))
        self.power_up_ost.append(music.beat(BeatFraction.QUARTER))
        self.power_up_ost.append(music.beat(BeatFraction.HALF))
        self.power_up_ost.append(music.beat(BeatFraction.HALF))
        self.power_up_ost.append(music.beat(BeatFraction.QUARTER))
        self.power_up_ost.append(music.beat(BeatFraction.HALF))
        self.power_up_ost.append(music.beat(BeatFraction.DOUBLE))
        self.power_up_ost.append(music.beat(BeatFraction.WHOLE))
        self.power_up_ost.append(music.beat(BeatFraction.HALF))
        self.power_up_ost.append(music.beat(BeatFraction.HALF))
        self.power_up_ost.append(music.beat(BeatFraction.QUARTER))
        self.power_up_ost.append(music.beat(BeatFraction.HALF))
        self.power_up_ost.append(music.beat(BeatFraction.DOUBLE))
        self.power_up_ost.append(music.beat(BeatFraction.QUARTER))
        self.power_up_ost.append(music.beat(BeatFraction.HALF))
        self.power_up_ost.append(music.beat(BeatFraction.QUARTER))
        self.power_up_ost.append(music.beat(BeatFraction.HALF))
        self.power_up_ost.append(music.beat(BeatFraction.QUARTER))
        self.power_up_ost.append(music.beat(BeatFraction.QUARTER))
        self.power_up_ost.append(music.beat(BeatFraction.QUARTER))
        self.power_up_ost.append(music.beat(BeatFraction.DOUBLE))

        # Tema de Introdução do Pac-Man
        # COMECO DAS NOTAS
        self.pacman_intro_ost.append(247)
        self.pacman_intro_ost.append(494)
        self.pacman_intro_ost.append(370)
        self.pacman_intro_ost.append(311)
        self.pacman_intro_ost.append(494)
        self.pacman_intro_ost.append(370)
        self.pacman_intro_ost.append(370)
        self.pacman_intro_ost.append(311)
        # BEAT 3
        self.pacman_intro_ost.append(262)
        self.pacman_intro_ost.append(523)
        self.pacman_intro_ost.append(392)
        self.pacman_intro_ost.append(330)
        self.pacman_intro_ost.append(523)
        self.pacman_intro_ost.append(392)
        self.pacman_intro_ost.append(330)
        self.pacman_intro_ost.append(247)
        self.pacman_intro_ost.append(494)
        self.pacman_intro_ost.append(370)
        self.pacman_intro_ost.append(311)
        self.pacman_intro_ost.append(494)
        self.pacman_intro_ost.append(370)
        self.pacman_intro_ost.append(370)
        self.pacman_intro_ost.append(311)
        # 3A PARTE
        self.pacman_intro_ost.append(311)
        self.pacman_intro_ost.append(330)
        self.pacman_intro_ost.append(349)
        self.pacman_intro_ost.append(349)
        self.pacman_intro_ost.append(370)
        self.pacman_intro_ost.append(392)
        self.pacman_intro_ost.append(392)
        self.pacman_intro_ost.append(415)
        self.pacman_intro_ost.append(440)
        self.pacman_intro_ost.append(494)

        # COMECO DOS TEMPOS
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.EIGHTH))
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.EIGHTH))
        self.pacman_intro_ost.append(music.beat(BeatFraction.HALF))
        # BEAT 3
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.EIGHTH))
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.HALF))
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.EIGHTH))
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.EIGHTH))
        self.pacman_intro_ost.append(music.beat(BeatFraction.HALF))
        # 3A PARTE
        self.pacman_intro_ost.append(music.beat(BeatFraction.EIGHTH))
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.EIGHTH))
        self.pacman_intro_ost.append(music.beat(BeatFraction.EIGHTH))
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.EIGHTH))
        self.pacman_intro_ost.append(music.beat(BeatFraction.EIGHTH))
        self.pacman_intro_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_intro_ost.append(music.beat(BeatFraction.HALF))

        # Pac-Man Background Theme
        # COMECO DAS NOTAS
        self.pacman_bg_ost.append(494)
        self.pacman_bg_ost.append(494)
        self.pacman_bg_ost.append(466)
        self.pacman_bg_ost.append(370)
        self.pacman_bg_ost.append(330)
        self.pacman_bg_ost.append(370)
        self.pacman_bg_ost.append(0)  # Pausa
        self.pacman_bg_ost.append(494)
        self.pacman_bg_ost.append(0)  # Pausa
        self.pacman_bg_ost.append(659)
        self.pacman_bg_ost.append(0)  # Pausa
        self.pacman_bg_ost.append(988)
        self.pacman_bg_ost.append(880)
        self.pacman_bg_ost.append(880)
        self.pacman_bg_ost.append(831)
        self.pacman_bg_ost.append(932)
        self.pacman_bg_ost.append(880)
        self.pacman_bg_ost.append(831)
        self.pacman_bg_ost.append(880)
        self.pacman_bg_ost.append(831)
        self.pacman_bg_ost.append(740)
        self.pacman_bg_ost.append(0)  # Pausa
        self.pacman_bg_ost.append(622)
        self.pacman_bg_ost.append(0)  # Pausa
        self.pacman_bg_ost.append(494)
        self.pacman_bg_ost.append(523)
        self.pacman_bg_ost.append(587)
        self.pacman_bg_ost.append(659)
        self.pacman_bg_ost.append(698)
        self.pacman_bg_ost.append(784)
        self.pacman_bg_ost.append(698)
        self.pacman_bg_ost.append(659)
        self.pacman_bg_ost.append(587)
        self.pacman_bg_ost.append(554)
        self.pacman_bg_ost.append(622)
        self.pacman_bg_ost.append(698)
        self.pacman_bg_ost.append(740)
        self.pacman_bg_ost.append(831)
        self.pacman_bg_ost.append(740)
        self.pacman_bg_ost.append(698)
        self.pacman_bg_ost.append(622)
        self.pacman_bg_ost.append(523)
        self.pacman_bg_ost.append(523)
        self.pacman_bg_ost.append(587)
        self.pacman_bg_ost.append(659)
        self.pacman_bg_ost.append(698)
        self.pacman_bg_ost.append(784)
        self.pacman_bg_ost.append(0)  # Pausa
        self.pacman_bg_ost.append(698)
        self.pacman_bg_ost.append(659)
        self.pacman_bg_ost.append(587)
        self.pacman_bg_ost.append(262)
        self.pacman_bg_ost.append(262)
        self.pacman_bg_ost.append(587)
        self.pacman_bg_ost.append(262)
        self.pacman_bg_ost.append(587)
        self.pacman_bg_ost.append(262)
        self.pacman_bg_ost.append(587)
        self.pacman_bg_ost.append(262)
        self.pacman_bg_ost.append(587)
        self.pacman_bg_ost.append(262)
        self.pacman_bg_ost.append(1176)  # Pausa

        # COMECO DOS TEMPOS
        pself.acman_bg_ost.append(music.beat(BeatFraction.HALF))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.append(music.beat(BeatFraction.HALF))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.append(music.beat(BeatFraction.HALF))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.append(music.beat(BeatFraction.HALF))
        self.pacman_bg_ost.append(music.beat(BeatFraction.HALF))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.append(music.beat(BeatFraction.HALF))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.append(music.beat(BeatFraction.HALF))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.appendmusic.beat(BeatFraction.HALF))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.append(music.beat(BeatFraction.HALF))
        self.pacman_bg_ost.append(music.beat(BeatFraction.QUARTER))
        self.pacman_bg_ost.append(music.beat(BeatFraction.HALF))
        self.pacman_bg_ost.append(music.beat(BeatFraction.HALF))
        self.pacman_bg_ost.append(music.beat(BeatFraction.HALF))
        self.pacman_bg_ost.append(music.beat(BeatFraction.HALF))

        # SFX 1:
        # INICIO NOTAS
        self.sfx_ost.append(523)
        self.sfx_ost.append(659)
        self.sfx_ost.append(784)
        # INICIO TEMPO
        self.sfx_ost.append(music.beat(BeatFraction.QUARTER))
        self.sfx_ost.append(music.beat(BeatFraction.QUARTER))
        self.sfx_ost.append(music.beat(BeatFraction.QUARTER))

    def play_song(self, list: List[]):
        while (5 * self.playsong_y + self.playsong_x) < len(list) and not (self.stop_ost()):
            music.play(music.tone_playable(list[5 * self.playsong_y + self.playsong_x],
                    list[5 * self.playsong_y + (self.playsong_x + 1)]),
                music.PlaybackMode.UNTIL_DONE)
            self.playsong_x = 0
            self.playsong_y += 1
    def stop_ost(self):
        if stop_intro or (stop_background or stop_power_up):
            return True
        else:
            return False

def incrementa_pontuacao(pacman: Pacman, comida: Comida):
    global pontuacao, power_up
    if pacman.x == comida.x and pacman.y == comida.y:
        music.stop_all_sounds()
        SongPlayer.play_song(SongPlayer.comida_sfx)
        pontuacao = pontuacao + 1
        if pontuacao >= 3:
            music.stop_all_sounds()
            power_up = True

class UI_Manager:
    def __init__(self) -> None:
        self.animacao_menu: List[Image] = []
        self.animacao_menu.append(images.create_image("""
                . # # # .
                # # # . .
                # # . . .
                # # # . .
                . # # # .
                """))
        self.animacao_menu.append(images.create_image("""
                . # # # .
                # # # # #
                # # # . .
                # # # # #
                . # # # .
                """))
        self.animacao_menu.append(images.create_image("""
                . # # # .
                # # # # #
                # # # # #
                # # # # #
                . # # # .
                """))
        self.animacao_menu.append(images.create_image("""
                . # # # .
                # # # # #
                # # # . .
                # # # # #
                . # # # .
                """))
        self.animacao_menu.append(images.create_image("""
                . # # # .
                # # # . .
                # # . . .
                # # # . .
                . # # # .
                """))
        self.animacao_menu.append(images.create_image("""
                # # # . .
                # # # # .
                # # . . .
                # # # # .
                # # # . .
                """))
        self.animacao_menu.append(images.create_image("""
                # # . . .
                # # # . .
                # # # . .
                # # # . .
                # # . . .
                """))
        self.animacao_menu.append(images.create_image("""
                # . . . .
                # # . . .
                . . . . .
                # # . . .
                # . . . .
                """))
        self.animacao_menu.append(images.create_image("""
                # . . . .
                . . . . .
                . . . . .
                . . . . .
                # . . . .
                """))
        self.animacao_menu.append(images.create_image("""
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                """))
        self.animacao_menu.append(images.create_image("""
                . # # . .
                # . . # .
                # # # # .
                # . . # .
                # . . # .
                """))
    def menu(self):
        while i < len(self.animacao_menu) and no_menu:
            stop_ost = True
            music.stop_all_sounds()
            basic.show_leds(self.animacao_menu[i])
            
class Pacman:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        led.plot(self.x, self.y)

    def input_pacman():
        if input.acceleration(Dimension.X) < -800:
            led.unplot(self.x, self.y)
            self.x += -1
            if self.x < 0:
                self.x = 4
            led.plot(self.x, self.y)
            incrementa_pontuacao()
        elif input.acceleration(Dimension.X) > 800:
            led.unplot(self.x, self.y)
            self.x += 1
            if self.x > 4:
                self.x = 0
            led.plot(self.x, self.y)
            incrementa_pontuacao()
        elif input.acceleration(Dimension.Y) < -800:
            led.unplot(self.x, self.y)
            self.y += -1
            if self.y < 0:
                self.y = 4
            led.plot(self.x, self.y)
            incrementa_pontuacao()
        elif input.acceleration(Dimension.Y) > 800:
            led.unplot(self.x, self.y)
            self.y += 1
            if self.y > 4:
                self.y = 0
            led.plot(self.x, self.y)
            incrementa_pontuacao(self, comida)

class Comida:
    def __init__(self, fantasma: Fantasma) -> None:
        self.x: int = randint(0, 4)
        self.y: int = randint(0, 4)
        if self.x == 2 and self.y == 2:
            self.x += 2
            self.y += -1
        if self.x == fantasma.x and self.y == fantasma.y:
            self.y += 1
            if self.y > 4:
                self.y = 0
    def on_every_interval():
        self.x = 0
        self.y = 0
        if no_jogo:
            if fanstasma.x != pacman.x or fantasma.y != pacman.y: 
                led.unplot(self.x, self.y)
                self.x = randint(0, 4)
                self.y = randint(0, 4)
                if self.x == 2 and self.y == 2:
                    self.x += 2
                    self.y += -1
                if self.x == fantasma.x and self.y == fantasma.y:
                    self.y += 1
                    if self.y > 4:
                        self.y = 0
                led.plot_brightness(self.x, self.y, 110)
loops.every_interval(5000, on_every_interval)

class Fantasma:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        choice = Math.random_boolean()
        if choice == True:
            self.x = randint(0, 1)
            if self.x == 1:
                self.x = 4
            else:
                self.y = randint(0, 1)
            if self.y == 1:
                self.y = 4
        if choice == True:
            self.y = randint(0, 4)
        else:
            self.x = randint(0, 4)
        led.plot(self.x, self.y)
        basic.pause(500)
        led.unplot(self.x, self.y)
        basic.pause(500)

    def persegue_pacman(pacman: Pacman) -> None:
        if self.y > pacman.y:
            self.y += -1
            led.plot(self.x, self.y)
            basic.pause(500)
            led.unplot(self.x, self.y)
            basic.pause(500)
        elif self.x < pacman.y:
            self.x += 1
            led.plot(self.x, self.y)
            basic.pause(500)
            led.unplot(self.x, self.y)
            basic.pause(500)
        elif self.x > pacman.x:
            self.x += -1
            led.plot(self.x, self.y)
            basic.pause(500)
            led.unplot(self.x, self.y)
            basic.pause(500)
        else:
            self.x += 1
            led.plot(self.x, self.y)
            basic.pause(500)
            led.unplot(self.x, self.y)
            basic.pause(500)

#BLOCO INICIAR
song_player = SongPlayer()
menu_game = UI_Manager()
pacman = Pacman(2, 2)
fantasma = Fantasma()
comida = Comida()
pontuacao = 0
maior_pontuacao = 0
power_up = False
no_jogo = False
no_menu = True
no_jogo = False
carrega_musicas()
stop_power_up = False
stop_background = False
stop_intro = False
basic.show_leds("""
                # . . . .
                . . . . .
                . . . . .
                . . . . .
                # . . . .
                """)
menu_game.menu()
start()

def on_button_pressed_a():
    global no_menu, no_jogo
    if not (no_jogo) and no_menu:
        no_menu = False
        basic.pause(100)
        no_jogo = True
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global maior_pontuacao, no_menu
    if not (no_jogo):
        maior_pontuacao = 0
        no_menu = False
        basic.show_string("Maior pontuacao:")
        basic.show_number(maior_pontuacao)
        basic.pause(2000)
        no_menu = True
        basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def fim_de_jogo():
    global no_jogo, power_up, pontuacao
    no_jogo = False
    stop_background = True
    music.stop_all_sounds()
    if power_up:
        basic.clear_screen()
        music._play_default_background(music.built_in_playable_melody(Melodies.ENTERTAINER),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_icon(IconNames.HAPPY)
        basic.pause(5000)
    else:
        basic.clear_screen()
        music._play_default_background(music.built_in_playable_melody(Melodies.FUNERAL),
            music.PlaybackMode.IN_BACKGROUND)
        basic.show_icon(IconNames.GHOST)
        basic.pause(5000)
    power_up = False
    pontuacao = 0

def start():
    global comidaY, comidaX, no_jogo, no_menu
    basic.pause(4)
    basic.clear_screen()
    SongPlayer.play_song(SongPlayer.pacman_intro)
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
    basic.pause(100)
    comidaY = 0
    comidaX = 0
    for transicaoY in range(5):
        if 0 % 2 == 0:
            for transicaoX in range(5):
                led.unplot(transicaoX, transicaoY)
                basic.pause(100)
        else:
            comidaX = 4
            for index in range(5):
                led.unplot(0, transicaoY)
                basic.pause(100)
                comidaX += -1
    no_jogo = True
    no_menu = False

def on_forever():
    if no_jogo:
        pacman.input_pacman()
        basic.pause(1000)
basic.forever(on_forever)

# Move o fantasma em direção ao pac-man até que os dois se encontrem, nesse momento é dado game over.

def on_forever3():
    if no_jogo and not (no_menu):
        while fantasma.x != pacman.y or fantasma.x != pacman.y:
            fantasma.persegue_pacman(pacman)
        stop_background = True
        basic.clear_screen()
        fim_de_jogo()
        basic.show_number(pontuacao)
        basic.clear_screen()
        no_menu = True
        menu_game.menu()
basic.forever(on_forever3)

