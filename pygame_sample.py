from pygame.locals import *
import pygame
import sys 
import random
import math
import time

result = 0
guest_num = 10
life = 3
score = 0

def make_question(): # 問題を作成する関数
    total = random.randint(500, 2000) # 合計
    payment = random.randint(total + 1, 3000) # 支払い
    payment = math.ceil(payment / 100) * 100
    change = payment - total # お釣り
    return total, payment, change
quest = make_question()
# quest[0] = total
# quest[1] = payment
# quest[2] = change

def num_clear():# 定数を初期化する関数
    new_result = 0
    new_guest_num = 10
    new_life = 3
    new_score = 0
    return new_result, new_guest_num, new_life, new_score

def time_count(endT, startT):# ゲーム時間を計測する関数
    elapsed_time = int(endT - startT)
    elapsed_hour = elapsed_time // 3600
    elapsed_minute = (elapsed_time % 3600) // 60
    elapsed_second = (elapsed_time % 3600 % 60)
    return str(elapsed_hour).zfill(2) + "時間" + str(elapsed_minute).zfill(2) + "分" + str(elapsed_second).zfill(2)+ "秒" 


gamescene = 0  # 0 タイトル画面、1 ゲーム画面、2 エンド画面、3 ゲームオーバー画面、-1 エラー
width = 1000 # 画面サイズ横
height = 600 # 画面サイズ縦

gameButton = [] # 画像を読み込んで画像の大きさを指定(button_width, button_height)
gameButton.append(pygame.transform.scale(pygame.image.load("start_b.png"), (140, 100)))
gameButton.append(pygame.transform.scale(pygame.image.load("clear_b.png"), (140, 100)))
gameButton.append(pygame.transform.scale(pygame.image.load("ok_b.png"), (100, 100)))
gameButton.append(pygame.transform.scale(pygame.image.load("end_b.png"), (200, 200)))

# 画像の表示位置を表す矩形(left, top, rect_width, rect_height)
gameButtonRect = [Rect(400, 400, 140, 100), # gameButton[0]の位置
                  Rect(750, 400, 140, 100), # gameButton[1]の位置
                  Rect(900, 400, 100, 100), # gameButton[2]の位置
                  Rect(400, 400, 200, 200)] # gameButton[3]の位置

inputButton = []
inputButton.append(pygame.transform.scale(pygame.image.load("1yen_img.PNG"), (100, 100)))
inputButton.append(pygame.transform.scale(pygame.image.load("5yen_img.PNG"), (110, 110)))
inputButton.append(pygame.transform.scale(pygame.image.load("10yen_img.PNG"), (117, 117)))
inputButton.append(pygame.transform.scale(pygame.image.load("50yen_img.PNG"), (105, 105)))
inputButton.append(pygame.transform.scale(pygame.image.load("100yen_img.PNG"), (113, 113)))
inputButton.append(pygame.transform.scale(pygame.image.load("500yen_img.PNG"), (132, 132)))

inputButtonRect = [(Rect(0, 400, 100, 100), 1), 
                    (Rect(120, 400, 100, 100), 5), 
                    (Rect(240, 400, 100, 100), 10), 
                    (Rect(360, 400, 100, 100), 50), 
                    (Rect(480, 400, 100, 100), 100),
                    (Rect(600, 400, 100, 100), 500)]

# フォントの初期化
FONT_PATH = "ipaexg.ttf"
pygame.font.init()
font = pygame.font.Font(FONT_PATH, 32) # フォントサイズ

pygame.init() # pygame初期化(最初に必要)
screen = pygame.display.set_mode((width, height)) # 画面作成
pygame.display.set_caption("sample game") # ゲームタイトル

# ゲームループ
running = True

while running:
    screen.fill((238,249,255))  # 背景を塗りつぶす(red, green, blue)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit() # ゲームの終了処理
            sys.exit()
            
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):# 左クリックが押された場合
            if (gamescene == 0) and (gameButtonRect[0].collidepoint(event.pos)):
                result ,guest_num,life, score = num_clear()
                quest = make_question()
                time_sta = time.time()
                gamescene = 1
            elif gamescene == 1:
                for button_rect, number in inputButtonRect:
                    if button_rect.collidepoint(event.pos):
                        result += number
                if gameButtonRect[1].collidepoint(event.pos):
                    result = 0 
                if gameButtonRect[2].collidepoint(event.pos):
                    if result == quest[2]:
                        guest_num -= 1
                        quest = make_question()
                        if guest_num != 0:
                            result = 0
                        elif guest_num == 0:
                            time_end = time.time() #タイマーを止める
                            gamescene = 2
                    elif result != quest[2]:
                        result = 0
                        life -= 1
                        if life == 0:
                            time_end = time.time()
                            gamescene = 2
            elif (gamescene == 2) and (gameButtonRect[3].collidepoint(event.pos)):
                gamescene = 0

    # イベントの処理
    if gamescene == 0:
        screen.blit(gameButton[0], gameButtonRect[0]) # ボタンを配置
    elif gamescene == 1:
        screen.blit(gameButton[1], gameButtonRect[1])
        screen.blit(gameButton[2], gameButtonRect[2])
        for i in range(6):
            screen.blit(inputButton[i], inputButtonRect[i][0])
            
        result_text = font.render("お釣りは " + str(result) + " 円です", True, (0, 0, 0) )
        result_rect = result_text.get_rect(center=(width // 2, height // 2))
        screen.blit(result_text, result_rect)
    
        total_text = font.render("　　小計 " + str(quest[0]) + " 円", True, (0, 0, 0) )
        total_rect = total_text.get_rect(center=(width // 2, height // 3))
        screen.blit(total_text, total_rect)
        
        payment_text = font.render("お支払い " + str(quest[1]) + " 円", True, (0, 0, 0) )
        payment_rect = payment_text.get_rect(center=(width // 2, height // 4))
        screen.blit(payment_text, payment_rect)
        
        guest_text = font.render("残りお客さん " + str(guest_num) + " 人", True, (0, 0, 0) )
        guest_rect = guest_text.get_rect(center=(width // 2, height // 8))
        screen.blit(guest_text, guest_rect)
        
        life_text = font.render("残機： " + str(life), True, (0, 0, 0) )
        life_rect = life_text.get_rect(center=(width // 8, height // 8))
        screen.blit(life_text, life_rect)
        
        tim_text2 = font.render(time_count(time.time(), time_sta), True,(0,0,0))
        tim_rect2 = tim_text2.get_rect(center=(width // 8, height // 5))
        screen.blit(tim_text2, tim_rect2)

    
        
    elif gamescene == 2:
        screen.blit(gameButton[3], gameButtonRect[3])

        end_text = font.render(str(10 - guest_num) + " 問クリア！僕を押すとタイトルに戻るよ", True, (0, 0, 0) )
        end_rect = end_text.get_rect(center=(width // 2, height // 2))
        screen.blit(end_text, end_rect)

        tim_text = font.render("記録!! " + time_count(time_end, time_sta) + "!!!",True,(0,0,0))
        tim_rect = tim_text.get_rect(center=(width // 2, height // 8))
        screen.blit(tim_text, tim_rect)
    else:
        print("error")
        running = False
        pygame.quit() # ゲームの終了処理
        sys.exit()
    
    

    pygame.display.update()