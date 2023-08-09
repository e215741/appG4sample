from pygame.locals import *
import pygame
import sys
import random
import math
import time
from pygame import mixer

width = 1248 # 画面サイズ横
height = 702 # 画面サイズ縦

def make_question(): # 問題を作成する関数
    total = random.randint(500, 3000) # 合計 500〜3000の間からランダムで出題
    payment = random.randint(total + 1, 3000) # 支払い
    payment = math.ceil(payment / 100) * 100
    change = payment - total # お釣り
    return total, payment, change
quest = make_question()
# quest[0] = total
# quest[1] = payment
# quest[2] = change

def num_clear(): # 定数を初期化する関数
    new_input_total = 0
    new_guest_num = 10
    new_life = 3
    new_score = 0
    return new_input_total, new_guest_num, new_life, new_score
clear = num_clear()

def time_count(endT, startT): # ゲーム時間を計測する関数 00時間00分00秒の形で返す
    elapsed_time = int(endT - startT)
    elapsed_hour = elapsed_time // 3600
    elapsed_minute = (elapsed_time % 3600) // 60
    elapsed_second = (elapsed_time % 3600 % 60)
    progress_time = str(elapsed_hour).zfill(2) + "時間" + str(elapsed_minute).zfill(2) + "分" + str(elapsed_second).zfill(2)+ "秒" 
    return progress_time

def evalate(resltT): # ゲームの評価を時間ごとに決める関数
    if resltT < 60:
        return "Execellent"
    elif resltT < 120:
        return "Very Good"
    elif resltT < 240:
        return "Good"
    elif resltT < 300:
        return "Average"
    else:
        return "Poor"

def show_start(): # タイトル画面のview関数
    screen.blit(design[0], designRect[0]) # 背景
    screen.blit(gameButton[0], gameButtonRect[0]) # ボタンを配置
    screen.blit(gameButton[1], gameButtonRect[1])
    
def show_game(): # ゲーム画面のview関数
    screen.blit(design[1], designRect[0]) # 背景
       
    input_total_text = font.render(str(input_total) + " 円", True, (0, 0, 0) )
    input_total_rect = input_total_text.get_rect(center=(374, 438))
    screen.blit(input_total_text, input_total_rect) # お釣りテキスト

    total_text = font.render(str(quest[0])+ " 円", True, (0, 0, 0) )
    total_rect = total_text.get_rect(center=(382, 289))
    screen.blit(total_text, total_rect) # 小計テキスト
    
    payment_text = font.render(str(quest[1])+ " 円", True, (0, 0, 0) )
    payment_rect = payment_text.get_rect(center=(416, 360))
    screen.blit(payment_text, payment_rect) # お預かりテキスト
    
    guest_text = font.render("あと " + str(guest_num) + " 人", True, (0, 0, 0) )
    guest_rect = guest_text.get_rect(center=(802, 160))
    screen.blit(guest_text, guest_rect) # 人数テキスト
    
    life_text = font.render(str(life) + " /3", True, (255, 255, 255) )
    life_rect = life_text.get_rect(center=(170, 58))
    screen.blit(life_text, life_rect) # ライフテキスト
    
    tim_text1 = font3.render(time_count(time.time(), time_sta), True,(0, 0, 0))
    tim_rect1 = tim_text1.get_rect(center=(460, 62))
    screen.blit(tim_text1, tim_rect1) # 時間テキスト
    
def show_end(): # エンド画面のview関数
    screen.blit(design[2], designRect[0]) # 背景

    end_text = font.render(str(clear[1] - guest_num) + " 問クリア！", True, (0, 0, 0) )
    end_rect = end_text.get_rect(center=(352, height // 2))
    screen.blit(end_text, end_rect) #何問クリアテキスト

    tim_text2 = font.render(time_count(time_end, time_sta) + "!",True,(0, 0, 0))
    tim_rect2 = tim_text2.get_rect(center=(352, 412))
    screen.blit(tim_text2, tim_rect2) # 時間テキスト
    
    eva_text = font.render(evalate(game_cler_time) + "!!",True,(0, 0, 0))
    eva_rect = eva_text.get_rect(center=(352, height // 5))
    screen.blit(eva_text, eva_rect) # 評価テキスト
        
def show_over(): # ゲームオーバー画面のview関数
    screen.blit(design[3], designRect[0]) # 背景

def show_credit(): # クレジット画面のview関数
    screen.blit(design[0], designRect[0]) # 背景
    screen.blit(gameButton[1], gameButtonRect[1])
    screen.blit(irasuto, irasutoRect[0])
    
    credit_text = font2.render( "制作チーム",True, (0, 0, 0))
    credit_rect = credit_text.get_rect(center=(440, 540))
    screen.blit(credit_text, credit_rect)
    
    credit_text = font2.render( "知能情報基礎演習2",True, (0, 0, 0))
    credit_rect = credit_text.get_rect(center=(440, 560))
    screen.blit(credit_text, credit_rect)
    
    credit_text = font2.render( "グループ4",True, (0, 0, 0))
    credit_rect = credit_text.get_rect(center=(440, 580))
    screen.blit(credit_text, credit_rect)
    
def play_se(file_name): # 効果音再生する関数
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file_name) 
    sound.play()

def play_bgm(file_name): # bgm再生する関数
    pygame.mixer.init()
    mixer.music.load(file_name)
    mixer.music.play(-1)

# 画面ごとの画像をロード
design = []
design.append(pygame.transform.scale(pygame.image.load("start_sc.png"), (width, height)))
design.append(pygame.transform.scale(pygame.image.load("game_sc.png"), (width, height)))
design.append(pygame.transform.scale(pygame.image.load("end_sc.png"), (width, height)))
design.append(pygame.transform.scale(pygame.image.load("over_sc.png"), (width, height)))
designRect = [Rect(0, 0, width, height)]

def Sakura(x, y): # 桜を表示する関数
    screen.blit(sakura, (x, y))

gameButton = [] # 画像を読み込んで画像の大きさを指定(button_width, button_height)
gameButton.append(pygame.transform.scale(pygame.image.load("start_b.png"), (150, 363)))
gameButton.append(pygame.transform.scale(pygame.image.load("credit_b.png"), (125 , 297)))

# その他(桜,イラスト)
sakura = pygame.transform.scale(pygame.image.load("sakura.png"), (100, 100))

irasuto = pygame.transform.scale(pygame.image.load("saikounoirasuto.PNG"), (11*45, 14.8*45))
irasutoRect = [Rect(200, 50, 11*45, 14.8*45)]

# ゲームボタンの範囲を表す矩形(left, top, rect_width, rect_height)
gameButtonRect = [Rect(291, 347, 150, 363), # スタートボタン
                  Rect( 83, 413, 125, 297), # お品書きボタン
                  Rect(158, 490, 307,  80), # 精算するボタン
                  Rect(915,   5, 333, 165), # タイトルへボタン
                  Rect(218, 585, 190,  48)] # クリアボタン

# 入力ボタンの範囲を表す矩形((left, top, rect_width, rect_height),(入力値))
inputButtonRect = [(Rect( 482, 587, 108, 115), 1  ),
                   (Rect( 606, 587, 108, 115), 5  ), 
                   (Rect( 734, 587, 108, 115), 10 ), 
                   (Rect( 860, 587, 108, 115), 50 ), 
                   (Rect( 986, 587, 108, 115), 100), 
                   (Rect(1112, 587, 108, 115), 500),]

# 定数
input_total = 0 # 入力値が保存される
guest_num = 10 # お客さんの数
life = 3 # ライフの数
gamescene = 0 # 0 タイトル画面、1 ゲーム画面、2 エンド画面、3 ゲームオーバー画面、-1 クレジット画面
sakura1_y, sakura2_y, sakura3_y, sakura4_y, sakura5_y = 0, 100, 50, 150, 100

# フォントの初期化
pygame.font.init()
font = pygame.font.Font("v7.ttf", 48) # フォントの種類とサイズ
font2 = pygame.font.Font("ipaexg.ttf", 20)
font3 = pygame.font.Font("v7.ttf", 28)

pygame.init() # pygame初期化(最初に必要)
screen = pygame.display.set_mode((width, height)) # 画面作成
pygame.display.set_caption("レジ道") # ゲームタイトル

# ゲームループ
running = True

while running:
    # イベントの処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit() # ゲームの終了処理
            sys.exit()
            
        if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1): # 左クリックが押された場合の画面ごとの処理
            if (gamescene == 0) and (gameButtonRect[0].collidepoint(event.pos)): # スタート画面の処理
                play_se("始めい.wav")
                input_total, guest_num, life, score = num_clear()
                quest = make_question()
                time_sta = time.time()
                play_bgm("ゲーム画面.mp3")
                gamescene = 1                
            elif (gamescene == 0) and (gameButtonRect[1].collidepoint(event.pos)):
                play_se("maou_se_system35.wav")
                gamescene = -1
                
            elif gamescene == 1: # ゲーム画面の処理
                for button_rect, number in inputButtonRect:
                    if button_rect.collidepoint(event.pos):
                        play_se("お金.wav")
                        input_total += number
                if gameButtonRect[4].collidepoint(event.pos):
                    play_se("クリア音.wav")
                    input_total = 0 
                if gameButtonRect[2].collidepoint(event.pos):
                    if input_total == quest[2]:
                        play_se("正解音.wav")
                        guest_num -= 1
                        quest = make_question()
                        if guest_num != 0:
                            input_total = 0
                        elif guest_num == 0:
                            time_end = time.time() #タイマーを止める
                            game_cler_time = time_end - time_sta
                            mixer.music.stop()
                            gamescene = 2
                            play_se("クリア画面.wav")
                    elif input_total != quest[2]:
                        play_se("不正解.wav")
                        input_total = 0
                        life -= 1
                        if life == 0:
                            time_end = time.time()
                            mixer.music.stop()
                            gamescene = 3
                            play_se("ゲームオーバー.wav")

            elif gamescene == 2: # エンド画面の処理
                if gameButtonRect[3].collidepoint(event.pos):
                    play_se("タイトルに戻る.wav")
                    gamescene = 0

            elif gamescene == 3: # ゲームオーバー画面の処理
                if gameButtonRect[3].collidepoint(event.pos):
                    play_se("タイトルに戻る.wav")
                    gamescene = 0

            elif gamescene == -1: # クレジット画面の処理
                if gameButtonRect[1].collidepoint(event.pos):
                    gamescene = 0
        
    if gamescene == 0: # 画面ごとの処理
        show_start()
        if (sakura1_y != height):
            sakura1_y += 2  
            sakura1_x = 100 * math.sin(sakura1_y/100 + 45) + 50
            Sakura(sakura1_x, sakura1_y)
        else:
            sakura1_y = 0
            Sakura(sakura1_x, sakura1_y)
            
        if (sakura2_y != height):
            sakura2_y += 2  
            sakura2_x = 100 * math.sin(sakura2_y/100 + 45) + 150
            Sakura(sakura2_x, sakura2_y)
        else:
            sakura2_y = 0
            Sakura(sakura2_x, sakura2_y)
            
        if (sakura3_y != height):
            sakura3_y += 2  
            sakura3_x = 100 * math.sin(sakura3_y/100 + 45) + 250
            Sakura(sakura3_x, sakura3_y)
        else:
            sakura3_y = 0
            Sakura(sakura3_x, sakura3_y)
            
        if (sakura4_y != height):
            sakura4_y += 2  
            sakura4_x = 100 * math.sin(sakura4_y/100 + 45) + 350
            Sakura(sakura4_x, sakura4_y)
        else:
            sakura4_y = 0
            Sakura(sakura4_x, sakura4_y)
        
        if (sakura5_y != height):
            sakura5_y += 2  
            sakura5_x = 100 * math.sin(sakura5_y/100 + 45) + 450
            Sakura(sakura5_x, sakura5_y)
        else:
            sakura5_y = 0
            Sakura(sakura5_x, sakura5_y)
            
        
    elif gamescene == 1:
        show_game()
    elif gamescene == 2:
        show_end()
    elif gamescene == 3:
        show_over()
    elif gamescene == -1:
        show_credit()
    else:
        print("error")
        running = False
        pygame.quit() # ゲームの終了処理
        sys.exit()

    pygame.display.update()
