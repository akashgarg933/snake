import pygame
import time
import random

pygame.init()
clock=pygame.time.Clock()

orange=(255,123,7)
black=(0,0,0)
red=(213,50,80)
green=(0,255,0)
blue=(50,153,213)

display_width=600
display_height=400
dis= pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('snake game')
snake_block=10
snake_l=[]
snake_speed=15

def snake(snake_block,snake_l):
    for x in snake_l:
        pygame.draw.rect(dis,orange,[x[0],x[1],snake_block,snake_block])

def snakegame():
    x1=display_width/2
    y1=display_height/2
    x1_change=0
    y1_change=0
    game_over=False
    game_end=False
    
    snake_l=[]
    l_snake=1

    foodx=round(random.randrange(0,display_width - snake_block)/10.0)*10.0
    foody=round(random.randrange(0,display_height - snake_block)/10.0)*10.0
    
    while not game_over :
        while(game_end==True):
            score=l_snake-1
            score_font = pygame.font.SysFont("comicsansms",35)
            value=score_font.render("your score : "+str(score),True,green)
            dis.blit(value,[display_width/3,display_height/3])
            pygame.display.update()

            for event in pygame.event.get():
                if(event.type ==pygame.QUIT):
                    game_over=True
                    game_end=False
            
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                game_over=True
            print(event)
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_LEFT):
                    x1_change=-snake_block
                    y1_change=0
                elif(event.key==pygame.K_RIGHT):
                    x1_change=snake_block
                    y1_change=0
                elif(event.key==pygame.K_UP):
                    x1_change=0
                    y1_change=-snake_block
                elif(event.key==pygame.K_DOWN):
                    x1_change=0
                    y1_change=snake_block
        if(x1>=display_width or x1<0 or y1>display_height or y1<0):
            game_end=True
        x1+=x1_change
        y1+=y1_change
        dis.fill(black)
        pygame.draw.rect(dis,green,[foodx,foody,snake_block,snake_block])
        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_l.append(snake_head)

        if(len(snake_l)>l_snake):
            del snake_l[0]

        for x in snake_l[:-1]:
            if(x==snake_head):
                game_end=True
        snake(snake_block,snake_l)
        
        pygame.display.update()

        if(x1==foodx and y1==foody):
            foodx=round(random.randrange(0,display_width - snake_block)/10.0)*10.0
            foody=round(random.randrange(0,display_height - snake_block)/10.0)*10.0
            l_snake+=1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
snakegame()
