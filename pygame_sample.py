from pygame.locals import *
import pygame
import sys 
import random
import math

# total = random.randint(500, 2000) # 合計
# payment = random.randint(total + 1, 3000) # 支払い
# payment = math.ceil(payment / 10) * 10
# change = payment - total # お釣り

def make_question():
    total = random.randint(500, 2000) # 合計
    payment = random.randint(total + 1, 3000) # 支払い
    payment = math.ceil(payment / 10) * 10
    change = payment - total # お釣り
    return total, payment, change

c = make_question()
# c[0] = total
# c[1] = payment
# c[2] = change

# 数字の初期化
result = 0
guest_num = 10
life = 3
score = 0

gamescene = 0  # 0 タイトル画面、1 ゲーム画面、2 エンド画面、-1 エラー

pygame.init() # pygame初期化(最初に必要)

width = 1000 # 画面サイズ
height = 600
screen = pygame.display.set_mode((width, height)) # 画面作成
pygame.display.set_caption("sample game")


gamebuttonrect = Rect(400, 400, 100, 100) # 画像の表示位置を表す矩形(left, top, width, height)

gameButton = []
gameButton.append(pygame.transform.scale(pygame.image.load("start_b.png"), (140, 100)))
gameButton.append(pygame.transform.scale(pygame.image.load("clear_b.png"), (140, 100)))
gameButton.append(pygame.transform.scale(pygame.image.load("ok_b.png"), (100, 100)))
gameButton.append(pygame.transform.scale(pygame.image.load("end_b.png"), (200, 200)))

inputButton = []
inputbuttonrect = [(pygame.Rect(0, 400, 100, 100), 1), 
                    (pygame.Rect(120, 400, 100, 100), 5), 
                    (pygame.Rect(240, 400, 100, 100), 10), 
                    (pygame.Rect(360, 400, 100, 100), 50), 
                    (pygame.Rect(480, 400, 100, 100), 100),
                    (pygame.Rect(600, 400, 100, 100), 500)]

inputbuttonrect2 = [pygame.Rect(0, 400, 100, 100), 
                    pygame.Rect(120, 400, 100, 100), 
                    pygame.Rect(240, 400, 100, 100), 
                    pygame.Rect(360, 400, 100, 100), 
                    pygame.Rect(480, 400, 100, 100),
                    pygame.Rect(600, 400, 100, 100),]

inputButton.append(pygame.transform.scale(pygame.image.load("1yen_img.PNG"), (100, 100)))
inputButton.append(pygame.transform.scale(pygame.image.load("5yen_img.PNG"), (110, 110)))
inputButton.append(pygame.transform.scale(pygame.image.load("10yen_img.PNG"), (117, 117)))
inputButton.append(pygame.transform.scale(pygame.image.load("50yen_img.PNG"), (105, 105)))
inputButton.append(pygame.transform.scale(pygame.image.load("100yen_img.PNG"), (113, 113)))
inputButton.append(pygame.transform.scale(pygame.image.load("500yen_img.PNG"), (132, 132)))

# フォントの初期化
FONT_PATH = "ipaexg.ttf"
pygame.font.init()
font = pygame.font.Font(FONT_PATH, 24)

# ゲームループ
running = True

while running:
    screen.fill((238,249,255))  # 背景を塗りつぶす

    # イベントの処理
    if gamescene == 0:
        screen.blit(gameButton[0], Rect(400, 400, 100, 100))
    elif gamescene == 1:
        screen.blit(gameButton[1], Rect(750, 400, 140, 100))
        screen.blit(gameButton[2], Rect(900, 400, 100, 100))
        for i in range(6):
            screen.blit(inputButton[i], inputbuttonrect2[i])
            
        result_text = font.render("お釣りは " + str(result) + " 円です", True, (0, 0, 0) )
        result_rect = result_text.get_rect(center=(width // 2, height // 2))
        screen.blit(result_text, result_rect)
    
        total_text = font.render("　　小計 " + str(c[0]) + " 円", True, (0, 0, 0) )
        total_rect = total_text.get_rect(center=(width // 2, height // 3))
        screen.blit(total_text, total_rect)
        
        payment_text = font.render("お支払い " + str(c[1]) + " 円", True, (0, 0, 0) )
        payment_rect = payment_text.get_rect(center=(width // 2, height // 4))
        screen.blit(payment_text, payment_rect)
        
        guest_text = font.render("残りお客さん " + str(guest_num) + " 人", True, (0, 0, 0) )
        guest_rect = guest_text.get_rect(center=(width // 2, height // 8))
        screen.blit(guest_text, guest_rect)
        
        life_text = font.render("残機： " + str(life), True, (0, 0, 0) )
        life_rect = life_text.get_rect(center=(width // 8, height // 8))
        screen.blit(life_text, life_rect)
        
    elif gamescene ==2:
        screen.blit(gameButton[3], Rect(400, 400, 200, 200))
        
        end_text = font.render(str(10 - guest_num) + " 問クリア！僕を押すとタイトルに戻るよ", True, (0, 0, 0) )
        end_rect = end_text.get_rect(center=(width // 2, height // 2))
        screen.blit(end_text, end_rect)
    else:
        print("error")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit() # ゲームの終了処理
            sys.exit()
            
        if (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1):
            if gamebuttonrect.collidepoint(event.pos):
                if gamescene == 0:
                    gamescene = 1
                elif gamescene == 1:
                    pass
                elif gamescene == 2:
                    gamescene = 0
                else:
                    gamescene = -1
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # 左クリックが押された場合
                if gamescene == 1:
                    pos = pygame.mouse.get_pos()
                    for button_rect, number in inputbuttonrect:
                        if button_rect.collidepoint(pos):
                            result += number
                    if Rect(750, 400, 100, 100).collidepoint(pos):
                        result = 0 
                    if Rect(900, 400, 100, 100).collidepoint(pos):
                        if result == c[2]:
                            guest_num -= 1
                            make_question()
                            if guest_num != 0:
                                result = 0
                            elif guest_num == 0:
                                gamescene = 2
                        elif result != c[2]:
                            result = 0
                            life -= 1
                            if life == 0:
                                gamescene = 2

    pygame.display.update()