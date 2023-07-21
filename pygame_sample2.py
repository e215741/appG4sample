from pygame.locals import *
import pygame
import sys 
import random
import math


def make_qest(self):
    sum = random.randint(500, 2000) # 合計
    payment = random.randint(sum + 1, 2000) # 支払い
    payment = math.ceil(payment / 10) * 10
    change = payment - sum # お釣り
    return sum, payment, change

pygame.init() # pygame初期化(最初に必要)

width = 1000 # 画面サイズ
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("sample game")


# ゲームループ
def main():
    while True:
        screen.fill((0,0,0)) # ウィンドウの背景色
        # イベントの取得
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit() #閉じるボタンが押されたらプログラムを終了
                sys.exit
        pygame.display.update()

if __name__ == '__main__':
    main()