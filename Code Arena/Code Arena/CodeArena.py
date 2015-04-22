# Code Arena
# Projeto de Programacao 1
#
# Alunos: 
# Matheus Maia e Danyel Rocha
#
# Orientadores:
# Dalton Serey, Joao Arthur e Jorge Figueiredo
#
# Monitores :
# Luiza Silveira e Klaudio Medeiros

import sys, os, pygame, random, time
from pygame.locals import *
pygame.init()

BLACK    = (   0,   0,   0)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
BLUE     = (  0,   0, 255)
pygame.mixer.pre_init(40800, -16, 2, 4098)
shot = pygame.mixer.Sound(os.path.join("Sounds", "Shoot.wav"))
click = pygame.mixer.Sound(os.path.join("Sounds","Click.wav"))
s_menu = pygame.mixer.Sound(os.path.join("Sounds", "Wonderwall.wav"))
s_jogo1 = pygame.mixer.Sound(os.path.join("Sounds", "WhatsisLove.wav"))
s_jogo2 =pygame.mixer.Sound(os.path.join("Sounds", "Paradise.wav"))
s_jogo3 = pygame.mixer.Sound(os.path.join("Sounds", "RickRoll.wav"))
s_jogo4 = pygame.mixer.Sound(os.path.join("Sounds", "Trololo.wav"))
s_jogo5 = pygame.mixer.Sound(os.path.join("Sounds", "Dare.wav"))
s_jogo6 = pygame.mixer.Sound(os.path.join("Sounds", "HeyYa.wav"))
s_jogo_lista = [s_jogo1, s_jogo2, s_jogo3, s_jogo4, s_jogo5, s_jogo6]
indice = random.randint(0,5)
s_jogo = s_jogo_lista[indice]
s_blur = pygame.mixer.Sound(os.path.join("Sounds", "Song2.wav"))
s_win = pygame.mixer.Sound(os.path.join("Sounds", "Ganhar.wav"))
s_lista = [s_menu, s_jogo, s_blur, s_win]


class Mouse():
    def coordenadas_cursor(self):
        return pygame.mouse.get_pos()

    def clica_botao(self, x, y, w, h, event):
        return Rect(x, y, w, h).collidepoint(self.coordenadas_cursor()) and event.type == MOUSEBUTTONUP
    
    def mouse_over(self, x, y, w, h, event):
        return Rect(x, y, w, h).collidepoint(self.coordenadas_cursor())

class Menu():

    def __init__(self):
        self.fase = 1
        self.vidas = 3
        self.personagem1 = "Menino" 
        self.personagem2 = "Robo" 
        
        self.personagem1_imgR = pygame.image.load(os.path.join("Sprites/Robo Azul", "SELECTA.png"))
        self.personagem1_imgM = pygame.image.load(os.path.join("Sprites/Menino Azul", "SELECTA.png"))
        self.personagem2_imgR = pygame.image.load(os.path.join("Sprites/Robo Vermelho", "SELECTA.png"))
        self.personagem2_imgM = pygame.image.load(os.path.join("Sprites/Menino Vermelho", "SELECTA.png"))
        self.personagem1_img = self.personagem1_imgM
        self.personagem2_img = self.personagem2_imgR
        
        self.creditos = pygame.image.load(os.path.join("Interface", "creditos1.png"))
        self.mostra = False
        
        self.font = pygame.font.SysFont('', 50, True, False)
        self.fasetx = self.font.render(str(self.fase), True, BLACK)
        self.vidastx = self.font.render(str(self.vidas), True, BLACK)

    def botao_jogar(self, event, mouse, lista_imagem, lista_imgs2):
        lista_imagem[0] = lista_imgs2[0]
        if mouse.mouse_over(250, 172, 300, 90, event):
            lista_imagem[1] = lista_imgs2[3]
        else:
            lista_imagem[1] = lista_imgs2[2]
            
        if mouse.clica_botao(250, 172, 300, 80, event):
            if self.mostra == False:
                click.play()
                return "SELECT"

    def botao_sair(self, event, mouse, lista_imagem, lista_imgs2):
        if mouse.mouse_over(250,342, 300, 60, event):
            lista_imagem[3] = lista_imgs2[7]
        else:
            lista_imagem[3] = lista_imgs2[6]
            
        if mouse.clica_botao(250,342, 300, 60, event):
            if self.mostra == False:
                pygame.quit()
                sys.exit()

    def botao_creditos(self, event, mouse, lista_imagem, lista_imgs2):
        if mouse.mouse_over(250, 272, 300, 60, event):
            lista_imagem[2] = lista_imgs2[5]
        else:
            lista_imagem[2] = lista_imgs2[4]

        if mouse.clica_botao(250, 272, 300, 80, event):
            self.mostra = True

        elif mouse.clica_botao(250, 272, 300, 80, event) or event.type == MOUSEBUTTONUP:
            self.mostra = False

    def botao_fase_menos(self, event, mouse, lista_imagem, lista_imgs2):
        if mouse.clica_botao(332, 202, 38, 38, event):
            if self.fase > 1:
                self.fase -= 1

    def botao_fase_mais(self, event, mouse, lista_imagem, lista_imgs2):
        if mouse.clica_botao(432, 202, 38, 38, event):
            if self.fase < 3:
                self.fase += 1

    def botao_vidas_menos(self, event, mouse, lista_imagem, lista_imgs2):
        if mouse.clica_botao(332, 280, 38, 38, event):
            if self.vidas > 1:
                self.vidas -= 1   

    def botao_vidas_mais(self, event, mouse, lista_imagem, lista_imgs2):
        if mouse.clica_botao(432, 280, 38, 38, event):
            if self.vidas < 6:
                self.vidas += 1

    def botao_azul_R(self, event, mouse, lista_imagem, lista_imgs2):
        if mouse.clica_botao(150, 280, 30, 45, event):
            if self.personagem1 == "Menino":
                self.personagem1 = "Robo"
            else:
                self.personagem1 = "Menino"
            return self.personagem1
 
    def botao_azul_E(self, event, mouse, lista_imagem, lista_imgs2):
        if mouse.clica_botao(210, 280, 30, 45, event):
            if self.personagem1 == "Menino":
                self.personagem1 = "Robo"
            else:
                self.personagem1 = "Menino"
            return self.personagem1

    def botao_verm_R(self, event, mouse, lista_imagem, lista_imgs2):
        if mouse.clica_botao(550, 280, 30, 45, event):
            if self.personagem2 == "Menino":
                self.personagem2 = "Robo"
            else:
                self.personagem2 = "Menino"
            return self.personagem2

    def botao_verm_E(self, event, mouse, lista_imagem, lista_imgs2):
        if mouse.clica_botao(610, 280, 30, 45, event):
            if self.personagem2 == "Menino":
                self.personagem2 = "Robo"
            else:
                self.personagem2 = "Menino"
            return self.personagem2

    def update(self, tela, imagens, coordenadas):
        for x in range(len(imagens)):
            tela.blit(imagens[x], coordenadas[x])
        if self.mostra == True:
            tela.blit(self.creditos,  [240,112])

    def update2(self, tela):
        if self.personagem1 == "Robo":
            self.personagem1_img = self.personagem1_imgR
        if self.personagem1 == "Menino":
            self.personagem1_img = self.personagem1_imgM
        if self.personagem2 == "Robo":
            self.personagem2_img = self.personagem2_imgR
        if self.personagem2 == "Menino":
            self.personagem2_img = self.personagem2_imgM
            
        tela.blit(self.personagem1_img, [188,185])
        tela.blit(self.personagem2_img, [588,185])
        self.fasetx = self.font.render(str(self.fase), True, BLACK)
        self.vidastx = self.font.render(str(self.vidas), True, BLACK)
        tela.blit(self.fasetx, [390, 201])
        tela.blit(self.vidastx, [390, 280])
        return self.vidas, self.fase

class Wall(pygame.sprite.Sprite):
 
    def __init__(self, x, y, width, height, color):

        super(Wall, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Room(object):
    wall_list = None
    enemy_sprites = None
    
    def __init__(self):
        self.wall_list_l = pygame.sprite.Group()
        self.wall_list = pygame.sprite.Group()
        self.wall_list_t = pygame.sprite.Group()
        self.wall_list_tt= pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

class Room1(Room):
    
    def __init__(self):
        Room.__init__(self)
        self.BK = pygame.image.load(os.path.join("Interface", "BG1.png"))
 
        walls = [[106, 0, 1, 600, RED],
                 [694, 0, 1, 600, RED],
                 
                 [180,68,1,71, BLACK],
                 [397,76,1,37, BLACK],
                 [534,76,1,37, BLACK],
                 [195,303,1,57, BLACK],
                 [330,228,1,46, BLACK],
                 [585,303,1,57, BLACK],
                 [247,415,1,72, BLACK],
                 [535,448,1,37, BLACK],


                 [289,68,1,71,BLACK],
                 [429,76,1,37,BLACK],
                 [566,76,1,37,BLACK],
                 [228,303,1,57,BLACK],
                 [490,228,1,46,BLACK],
                 [618,303,1,57,BLACK],
                 [410,415,1,72,BLACK],
                 [568,448,1,37,BLACK],


                 [0, 6, 800, 1, RED],
                 [0, 594, 800, 1, RED],

                 [183,65,104,1,BLACK],
                 [400,73,27,1,BLACK],
                 [537,73,27,1,BLACK],
                 [198,300,27,1,BLACK],
                 [333,225,154,1,BLACK],
                 [588,300,27,1,BLACK],
                 [250,412,157,1,BLACK],
                 [538,445,27,1,BLACK],
                 
                 [183,142,104,1,BLACK],
                 [400,116,27,1,BLACK],
                 [537,117,27,1,BLACK],
                 [198,363,27,1,BLACK],
                 [333,276,154,1,BLACK],
                 [588,363,27,1,BLACK],
                 [250,490,157,1,BLACK],
                 [538,489,27,1,BLACK]


                ]
        

        for item in walls[0:18]:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list_l.add(wall)
            self.wall_list.add(wall)
        for item in walls[18:36]:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list_t.add(wall)
            self.wall_list.add(wall)

class Room2(Room):
    def __init__(self):
        Room.__init__(self)
        self.BK = pygame.image.load(os.path.join("Interface", "BG2.png"))
        
        walls = [[106, 0, 1, 600, RED],
                 [694, 0, 1, 600, RED],
                 
                 [296,53,1,66, BLACK],
                 [597,158,1,62, BLACK],
                 [380,243,1,58, BLACK],
                 [282,413,1,88, BLACK],
                 [622,443,1,59, BLACK],

                 [515, 140, 1, 15, BLACK],
                 [582, 140, 1, 15, BLACK],


                 [200,53,1,66,BLACK],
                 [500,158,1,62,BLACK],
                 [300,243,1,58,BLACK],
                 [200,413,1,88,BLACK],
                 [470,443,1,59,BLACK],


                 [0, 6, 800, 1, RED],
                 [0, 594, 800, 1, RED],

                 [203,122,90,1,BLACK],
                 [503,223,91,1,BLACK],
                 [303,304,74,1,BLACK],
                 [203,504,76,1,BLACK],
                 [473,505, 146,1,BLACK],
                 
                 [500, 155, 15, 1, BLUE],
                 [582, 155, 15, 1, BLUE],
                 
                 
                 [202,50,90,1,BLACK],
                 [518,140,61,1,BLACK],
                 [303,240,74,1,BLACK],
                 [203,410,76,1,BLACK],
                 [473,440,146,1,BLACK]


                ]
        for item in walls[0:14]:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list_l.add(wall)
            self.wall_list.add(wall)
        for item in walls[14:28]:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list_t.add(wall)
            self.wall_list.add(wall)
            
class Room3(Room):
    def __init__(self):
        Room.__init__(self)
        self.BK = pygame.image.load(os.path.join("Interface", "BG3.png"))

        walls = [[106, 0, 1, 600, RED],
                 [694, 0, 1, 600, RED],
                 
                 [310,68,1,74, BLACK],
                 [210,243,1,91, BLACK],
                 [378,276,1,35, BLACK],
                 [520,245,1,91, BLACK],
                 [230,473,1,45, BLACK],
                 [375,423,1,45, BLACK],
                 [520,473,1,45, BLACK],

                 [374,145,1, 22, BLUE],
                 [423,145,1, 22, BLUE],
                 
                 [487,68,1,74, BLACK],
                 [289,245,1,91, BLACK],
                 [422,276,1,35, BLACK],
                 [599,243,1,91, BLACK],
                 [278,473,1,45, BLACK],
                 [423,423,1,45, BLACK],
                 [568,473,1,45, BLACK],


                 [0, 6, 800, 1, RED],
                 [0, 594, 800, 1, RED],

                 [313,65,171,1,BLACK],
                 [213,240,73,1,BLACK],
                 [381,276,42,1,BLACK],
                 [523,240,73,1,BLACK],
                 [233,470,42,1,BLACK],
                 [378,420,42,1,BLACK],
                 [523,470,42,1,BLACK],

                 [313,145,64,1,BLACK],
                 [423,145,64,1,BLACK],
                 [377,170,45,1,BLACK],
                 
                 [213,337,73,1,BLACK],
                 [378,314,44,1,BLACK],
                 [523,343,73,1,BLACK],
                 [233,521,42,1,BLACK],
                 [378,471,42,1,BLACK],
                 [523,521,42,1,BLACK],


                ]
        for item in walls[0:18]:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list_l.add(wall)
            self.wall_list.add(wall)
        for item in walls[18:37]:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list_t.add(wall)
            self.wall_list.add(wall)
    
class Tiro(pygame.sprite.Sprite):
    dx = 0
    dy = 0
    direita = True

    def __init__(self, x, y, change_x, change_y, direita):
        super(Tiro, self).__init__()
        self.image = pygame.Surface([8,8])
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.direita = direita
        self.dx = change_x*4/3.0
        self.dy = change_y*4/3.0
        self.cooldown = 0
        self.A_cooldown = 20
        self.hits = 2


        self.CEE = pygame.image.load(os.path.join("Sprites/Setas","CEE.png")).convert_alpha()
        self.CDD = pygame.image.load(os.path.join("Sprites/Setas","CDD.png")).convert_alpha()
        self.CC = pygame.image.load(os.path.join("Sprites/Setas","CC.png")).convert_alpha()
        self.CB = pygame.image.load(os.path.join("Sprites/Setas","CB.png")).convert_alpha()
        self.CBD = pygame.image.load(os.path.join("Sprites/Setas","CBD.png")).convert_alpha()
        self.CCD = pygame.image.load(os.path.join("Sprites/Setas","CCD.png")).convert_alpha()
        self.CCE = pygame.image.load(os.path.join("Sprites/Setas","CCE.png")).convert_alpha()
        self.CBE = pygame.image.load(os.path.join("Sprites/Setas","CBE.png")).convert_alpha()

        if (self.dx == 0 and self.dy ==0 and self.direita == True):
            self.dx= 4 
        elif (self.dx == 0 and self.dy ==0 and self.direita == False) : 
            self.dx = -4
   
    def img_correspondente(self, change_x, change_y):
        if change_x < 0 and change_y == 0 :
            self.image = self.CEE
        if change_x > 0 and change_y == 0:
            self.image = self.CDD
        if change_x == 0 and change_y < 0:
            self.image = self.CC
        if change_x == 0 and change_y > 0:
            self.image = self.CB
        if change_x > 0 and change_y > 0:
            self.image = self.CBD
        if change_x > 0 and change_y < 0:
            self.image = self.CCD
        if change_x < 0 and change_y < 0:
            self.image = self.CCE
        if change_x < 0 and change_y > 0:
            self.image = self.CBE
        
    def update(self, wallsl, wallst):
        self.img_correspondente(self.dx, self.dy)
        
        block_hit_list2 = pygame.sprite.spritecollide(self, wallst, False)
        block_hit_list = pygame.sprite.spritecollide(self, wallsl, False)



        for block in block_hit_list2:
            self.dy *= -1
            self.hits -= 1

        for block in block_hit_list:
            self.dx *= -1
            self.hits -= 1
            
        self.rect.x += self.dx
        self.rect.y += self.dy      
          
        if self.cooldown > 0:
            self.cooldown -= 1
        
        if self.hits <= 0 and self.cooldown == 0:
            self.cooldown = self.A_cooldown
            if self.dx != 0:
                if self.dx > 0:
                    self.dx -= self.dx/self.dx
                else:
                    self.dx += self.dx/self.dx
           
            if self.dy != 0:
                if self.dy > 0:
                    self.dy -= self.dy/self.dy
                else:
                    self.dy += self.dy/self.dy
        
            if self.dx == 0 and self.dy == 0:
                self.kill()

class Player(pygame.sprite.Sprite):
    
    change_x = 0
    change_y = 0
    right = False
    pos = [(225,35), (430,190), (255,530), (625, 535)]
    
    def __init__(self, x, y, lives, cor, personagem):
        super(Player, self).__init__() 
        self.lives = lives
        self.cooldown = 0
        self.cooldown1 = 0
        self.A_cooldown = 16
        self.B_cooldown = 24
        self.C_cooldown = 18
        self.troca = 0
        self.troca_b = False
        self.direita = True
        
        if personagem == "Robo":
            pasta = "Robo " + str(cor)
        elif personagem == "Menino":
            pasta = "Menino " + str(cor)
        
        self.E0 = pygame.image.load(os.path.join("Sprites/" + pasta, "E.png"))
        self.E1 = pygame.image.load(os.path.join("Sprites/" + pasta, "E1.png"))
        self.E = self.E0
        self.D0 = pygame.image.load(os.path.join("Sprites/" + pasta, "D.png"))
        self.D1 = pygame.image.load(os.path.join("Sprites/" + pasta, "D1.png"))
        self.D = self.D0
        self.C0 = pygame.image.load(os.path.join("Sprites/" + pasta, "C.png"))
        self.C1 = pygame.image.load(os.path.join("Sprites/" + pasta, "C1.png"))
        self.C = self.C0
        self.B0 = pygame.image.load(os.path.join("Sprites/" + pasta, "B.png"))
        self.B1 = pygame.image.load(os.path.join("Sprites/" + pasta, "B1.png"))
        self.B = self.B0
        self.BD0 = pygame.image.load(os.path.join("Sprites/" + pasta, "BD.png"))
        self.BD1 = pygame.image.load(os.path.join("Sprites/" + pasta, "BD1.png"))
        self.BD = self.BD0
        self.CD0 = pygame.image.load(os.path.join("Sprites/" + pasta, "CD.png"))
        self.CD1 = pygame.image.load(os.path.join("Sprites/" + pasta, "CD1.png"))
        self.CD = self.CD0
        self.CE0 = pygame.image.load(os.path.join("Sprites/" + pasta, "CE.png"))
        self.CE1 = pygame.image.load(os.path.join("Sprites/" + pasta, "CE1.png"))
        self.CE = self.CE0
        self.BE0 = pygame.image.load(os.path.join("Sprites/" + pasta, "BE.png"))
        self.BE1 = pygame.image.load(os.path.join("Sprites/" + pasta, "BE1.png"))
        self.BE = self.BE0
        self.image = self.D
        self.vidas_img = pygame.image.load(os.path.join("Interface","vida.png")).convert_alpha()
    
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def img_correspondente(self):

            
        if self.change_x == -3 and self.change_y == 0 :
            self.image = self.E
            self.direita = False    
        elif self.change_x == 3 and self.change_y == 0 or self.right == True:
            self.image = self.D
            self.direita = True
        if self.change_x == 0 and self.change_y == -3:
            self.image = self.C
        if self.change_x == 0 and self.change_y == 3:
            self.image = self.B
        if self.change_x == 3 and self.change_y == 3:
            self.image = self.BD
        if self.change_x == 3 and self.change_y == -3:
            self.image = self.CD
        if self.change_x == -3 and self.change_y == -3:
            self.image = self.CE
        if self.change_x == -3 and self.change_y == 3:
            self.image = self.BE
   
    def movimento(self, event, lista):
            if event.type == pygame.KEYDOWN:
                self.right = False
                if event.key == pygame.K_LEFT:
                    self.changespeed(-3, 0)
                if event.key == pygame.K_RIGHT:
                    self.changespeed(3, 0)
                if event.key == pygame.K_UP:
                    self.changespeed(0, -3)
                if event.key == pygame.K_DOWN:
                    self.changespeed(0, 3)
                if event.key == pygame.K_RETURN:
                    if self.cooldown == 0 :
                        if self.change_x or self.change_y != 0:
                            self.cooldown = self.A_cooldown
                        if self.change_y == -3 and self.change_x == 0:
                             self.cooldown = self.B_cooldown
                        else:
                            self.cooldown = self.C_cooldown
                        bala = Tiro(self.rect.center[0], self.rect.center[1], self.change_x, self.change_y, self.direita)
                        lista.add(bala)
 
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.changespeed(3, 0)
                if event.key == pygame.K_RIGHT:
                    self.changespeed(-3, 0)
                if event.key == pygame.K_UP:
                    self.changespeed(0, 3)
                    self.right = True
                if event.key == pygame.K_DOWN:
                    self.changespeed(0, -3)
                    self.right = True
                    
                    
    def movimento2(self, event, lista):
            if event.type == pygame.KEYDOWN:
                self.right = False
                if event.key == pygame.K_a:
                    self.changespeed(-3, 0)
                if event.key == pygame.K_d:
                    self.changespeed(3, 0)
                if event.key == pygame.K_w:
                    self.changespeed(0, -3)
                if event.key == pygame.K_s:
                    self.changespeed(0, 3)
                if event.key == pygame.K_SPACE:
                        if self.change_x or self.change_y != 0:
                            self.cooldown = self.A_cooldown
                        if self.change_y == -3:
                             self.cooldown = self.B_cooldown
                        else:
                            self.cooldown = self.C_cooldown
                        bala = Tiro(self.rect.center[0], self.rect.center[1], self.change_x, self.change_y, self.direita)
                        lista.add(bala)
                        
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.changespeed(3, 0)
                if event.key == pygame.K_d:
                    self.changespeed(-3, 0)
                if event.key == pygame.K_w:
                    self.changespeed(0, 3)
                    self.right = True
                if event.key == pygame.K_s:
                    self.changespeed(0, -3)
                    self.right = True
       
       
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y
    
    def ganhador(self, vidas1, vidas2):
        if vidas1 == 0:
            return "dois"
        elif vidas2 == 0:
            return "um"
    
    def vidas(self, tela, barraX):
        for x in range(self.lives):
            barraY = x*80 + 100
            tela.blit(self.vidas_img, [barraX, barraY])
    
    def update(self, walls, balas):
        
        
        if (self.troca % 20 )== 0:
            self.troca += 1
            if self.troca_b == False:
                self.troca_b = True
            elif self.troca_b == True:
                self.troca_b = False


        if self.change_x or self.change_y != 0:
            self.troca += 1


        if self.troca_b == True:
            self.E, self.D, self.C, self.B = self.E1, self.D1, self.C1, self.B1
            self.BE, self.BD, self.CE, self.CD = self.BE1, self.BD1, self.CE1, self.CD1
        if self.troca_b == False:
            self.E, self.D, self.C, self.B = self.E0, self.D0, self.C0, self.B0
            self.BE, self.BD, self.CE, self.CD = self.BE0, self.BD0, self.CE0, self.CD0
        
        
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.cooldown1 > 0:
            self.cooldown1 -= 1

        kill_hit_list = pygame.sprite.spritecollide(self, balas, False)
        for kill in kill_hit_list:
            if self.cooldown == 0:
                shot.play()
                self.lives -= 1
                self.rect.y = -1500
                self.rect.x = -1500
                self.cooldown1 = 150
        if self.lives > 0 and self.cooldown1 == 2:
            self.cooldown = 50
            self.renascer = random.randint(0,3)
            self.rect.y = self.pos[self.renascer][1]
            self.rect.x = self.pos[self.renascer][0]
        
        
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Pause():
    pausa = bool
    def __init__(self, tela):
        pausa = pygame.image.load(os.path.join("Interface","bp0.png"))
        bp1 = pygame.image.load(os.path.join("Interface","bp1.png"))
        bp2 = pygame.image.load(os.path.join("Interface","bp2.png"))
        bp3 = pygame.image.load(os.path.join("Interface", "bp3.png"))
        bp4 = pygame.image.load(os.path.join("Interface","bp4.png"))
        self.comojogar = pygame.image.load(os.path.join("Interface","CJ.png"))
        self.b_botoes = [pausa, bp1, bp2, bp3, bp4]
        self.c_botoes = [[200, 50],[310,205],[425,205],[310, 315],[425, 315]]
        self.tela = tela
        self.pausa = False
        pausa = self.pausa
        self.mudo = False
        self.cont = 0
        self.indice = 0
        self.mostra = False

    def mostrar(self, event):
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.cont += 1
                    if self.cont%2 == 0:
                        self.pausa = False
                    else:  
                        self.pausa = True
                        
            
    def b_retomar(self, event, mouse, pausa):
        if self.pausa == True:
            if mouse.clica_botao(310, 95, 270, 80, event):
                self.cont += 1
                self.pausa = False
                
    def b_menu(self, event, mouse):
        if self.pausa == True:
            if mouse.clica_botao(310, 425, 270, 80, event):
                return True
            
    def b_sound(self, event, mouse, pausa):
        if self.pausa == True:
            if mouse.clica_botao(310, 200, 100, 100, event):
                if self.mudo == False:
                    for x in s_lista:
                        x.set_volume(0.0)
                    self.mudo = True
                else:
                    for x in s_lista:
                        x.set_volume(1.0)
                    self.mudo = False
                
    def b_musica(self, event, mouse, pausa, indice):
        if self.pausa == True:
            if mouse.clica_botao(425, 210, 100, 100, event):
                pygame.mixer.stop()
                self.indice += 1
                indice = self.indice
                
                if self.indice > 5:
                    self.indice = 0
                s_jogo_lista[self.indice].play(-1,0,0)
                                                                                             
    def b_restart(self, event, mouse, pausa):
        if self.pausa == True:
            if mouse.clica_botao(310, 315, 100, 100, event):
                self.cont += 1
                self.pausa = False
                return True
        
    def b_comojogar(self, event, mouse, pausa):
        if self.pausa == True:
            if mouse.clica_botao(425, 315, 100, 100, event):
                self.mostra = True
            elif mouse.clica_botao(425, 315, 100, 100, event) or event.type == MOUSEBUTTONUP:
                self.mostra = False
                
    def update(self):
        if self.pausa == True:
            for x in range(len(self.b_botoes)):
                self.tela.blit(self.b_botoes[x], self.c_botoes[x])    
        if self.mostra == True and self.pausa == True:
            self.tela.blit(self.comojogar, [300,190])

class GameOver():
    def __init__(self, tela, ganhador):
        if ganhador == "um":
            self.faixa1 = pygame.image.load(os.path.join("Interface","faixa1.png"))
        elif ganhador == "dois":
            self.faixa1 = pygame.image.load(os.path.join("Interface","faixa3.png"))
       
        self.faixa2 = pygame.image.load(os.path.join("Interface", "faixa2.png"))
        self.b1 = pygame.image.load(os.path.join("Interface", "bgo1.png"))
        self.b2 = pygame.image.load(os.path.join("Interface", "bgo2.png"))
        

        self.acabou = True
        self.tela = tela
        self.x1 = -500
        self.x2 = 800
        self.y1 = 150
        self.y2 = 270
        
    def animacao(self):
        if self.acabou == True:
            if self.x1 <= 120:
                self.x1 += 3
                self.x2 -= 3
            self.tela.blit(self.faixa1,[self.x1, self.y1])
            self.tela.blit(self.faixa2,[self.x2, self.y2])
            self.tela.blit(self.b1,[280,400])
            self.tela.blit(self.b2,[420,400])
            
    def botao1(self, event, mouse):
            if mouse.clica_botao(280, 400, 100, 100, event):
                return True
    
    def botao2(self, event, mouse, lista, vidas):
        if mouse.clica_botao(420, 400, 100, 100, event):
            self.acabou = False
            return True

def carrega_img(arquivo):

    imagem = pygame.image.load(os.path.join("Interface", arquivo))
    return imagem.convert_alpha()

def main():

    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()

    #Default do jogo
    acabou = False
    pausa = False
    cont = 0
    vidas = 3
    fase = 1
    FPS = 60
    tamanho_tela = (800,600)
    
    #Tela/Mouse
    screen = pygame.display.set_mode(tamanho_tela)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Code Arena")
    mouse = Mouse()
    menu = Menu()
    
    #Grupos com os personagens/ com as flechas/ Fases
    all_sprites_list = pygame.sprite.Group()
    sprites = pygame.sprite.Group()
    rooms = [Room1(), Room2(), Room3()]
    
    #Carrega as Imagens
    na_tela = "MENU"
    s_menu.play(-1)
    locais = ["B0.png", "B1.png", "J0.png", "J1.png", "O0.png", "O1.png", "S0.png", "S1.png"]
    imagens = []
    for x in locais:
        imagens.append(carrega_img(x))
    main_menu_imgs = []
    main_menu_imgs = ["B1.png" , "J0.png",  "O0.png",  "S0.png" ]
    COORDENADAS = [[0,0], [250, 172], [250, 272], [250,342]]
    personagem1, personagem2 = "Robo", "Robo"

    while True:
    
        while na_tela == "MENU":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #Pega os eventos do Mouse
                mouse.coordenadas_cursor()
                menu.botao_sair(event, mouse, main_menu_imgs,imagens)
                if menu.botao_jogar(event, mouse, main_menu_imgs,imagens):
                    na_tela = "SELECT"
                menu.botao_creditos(event, mouse, main_menu_imgs,imagens)
                
            #Update
            screen.fill(WHITE)
            menu.update(screen, main_menu_imgs,COORDENADAS )
         
            pygame.display.flip()
            clock.tick(FPS)
     
        while na_tela == "SELECT":
            pygame.display.set_caption("Code Arena")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                mouse.coordenadas_cursor()

                #Voltar
                if mouse.clica_botao(305, 435, 190, 30, event):
                    na_tela = "MENU"
                
                #Jogar
                if mouse.clica_botao(305, 375, 190, 50, event):
                    s_jogo.play(-1,0,0)
                    click.play()
                    na_tela = "JOGO"
                    room = rooms[fase-1]
                    player1 = Player(225, 35, vidas, "Azul", personagem1)
                    player2 = Player(625, 535, vidas, "Vermelho", personagem2)
                    all_sprites_list.add(player1, player2)
                    s_menu.stop()
                    pausar = Pause(screen)
                    acabou = False
                
                #Outros botoes    
                menu.botao_fase_menos(event, mouse, main_menu_imgs,imagens)
                menu.botao_fase_mais(event, mouse, main_menu_imgs,imagens)
                menu.botao_vidas_menos(event, mouse, main_menu_imgs,imagens)
                menu.botao_vidas_mais(event, mouse, main_menu_imgs,imagens)
                menu.botao_azul_E(event, mouse, main_menu_imgs,imagens)
                menu.botao_azul_R(event, mouse, main_menu_imgs,imagens)
                menu.botao_verm_E(event, mouse, main_menu_imgs,imagens)
                menu.botao_verm_R(event, mouse, main_menu_imgs,imagens)
                personagem1, personagem2 = menu.personagem1, menu.personagem2
               


            screen.fill(WHITE)
            screen.blit(imagens[1], (0,0))
         
            menu.update2(screen)
            vidas, fase = menu.update2(screen)[0],menu.update2(screen)[1] 
            
            vidas2 = vidas
            pygame.display.flip()
            clock.tick(FPS)
     
        while na_tela == "JOGO":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                pygame.display.set_caption("Code Arena")

               
                #Eventos para quando o jogo estiver pausado
                pausar.mostrar(event)
                if pausar.pausa != True:
                    player1.movimento(event, sprites)
                    player2.movimento2(event, sprites)
                else:
                    player1.change_x , player1.change_y = 0,0 
                    player2.change_x , player2.change_y = 0,0 
                pausar.b_retomar(event, mouse, pausa)
                pausar.b_sound(event, mouse, pausa)
                if pausar.b_restart(event, mouse, pausa):
                        all_sprites_list.empty()
                        sprites.empty()
                        player1 = Player(255,35,vidas2,"Azul", personagem1)
                        player2 = Player(625,535,vidas2,"Vermelho", personagem2)
                        all_sprites_list.add(player1, player2)
                        acabou = False
                        ganhador = None
                        pausa = False
                pausar.b_comojogar(event, mouse, pausa)
                pausar.b_musica(event, mouse, pausa, indice)

                #Botao voltar para Menu
                if pausar.b_menu(event, mouse) == True:
                    all_sprites_list.empty()
                    sprites.empty()
                    na_tela = "MENU"
                    s_jogo.stop()
                    s_menu.play()
                
                #Eventos para pegar quando o joga acabar
                if acabou == "atualizar":
                    gameover.botao1(event, mouse)
                    
                    if gameover.botao1(event, mouse) == True:
                        all_sprites_list.empty()
                        sprites.empty()
                        na_tela = "MENU"
                        acabou = None
                        ganhador = None
                        s_blur.stop()
                        s_win.stop()
                        s_jogo.stop()
                        s_menu.play()


                        
                    
                    if gameover.botao2(event, mouse, all_sprites_list, vidas) == True:
                        all_sprites_list.empty()
                        sprites.empty()
                        player1 = Player(225,35,vidas2,"Azul", personagem1)
                        player2 = Player(625,535,vidas2,"Vermelho", personagem2)
                        all_sprites_list.add(player1, player2)
                        acabou = False
                        ganhador = None
                        s_blur.stop()
                        s_jogo.play(-1,0,0)

            screen.fill(WHITE)
            if pausar.pausa == False:
                sprites.update(room.wall_list_l, room.wall_list_t)
            pausar.update()
            room.wall_list.draw(screen)
            screen.blit(room.BK, [0,0])
            player1.img_correspondente()
            player2.img_correspondente()
            player1.update(room.wall_list, sprites)
            player2.update(room.wall_list, sprites)
            all_sprites_list.draw(screen)
            sprites.draw(screen)
            pausar.update()
            player1.vidas(screen, 15)
            player2.vidas(screen, 715)

            #Oque fazer quando jogo acabar
            if acabou == False:
                ganhador = player1.ganhador(player1.lives, player2.lives)
                if ganhador != None:
                    acabou = True
                    gameover = GameOver(screen, ganhador)
                    acabou = "atualizar"
                    s_jogo.stop()
                    s_win.play()
                    s_blur.play()
                    
            #Atualizacao da animacao do GameOver
            if acabou == "atualizar": 
                gameover.animacao()
         
            pygame.display.flip()
            clock.tick(FPS)

if __name__=='__main__':
    main()
