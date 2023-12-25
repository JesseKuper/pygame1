import pygame
import random


running = True
while running:
    pygame.init()
    screenWidth = 1980#1280
    screenHeight = 1080#720
    screen = pygame.display.set_mode((screenWidth, screenHeight))
    clock = pygame.time.Clock()
    running = True
    selected = 0
    pselected = 0
    play = False
    menu = True
    paused = False
    xpos = screenWidth /2
    ypos = screenHeight - 100
    expos = screenWidth /2
    eypos = 0
    movepos = screenWidth / 3
    score = 0
    speed = 3
    acc = 1.1
    lifes = 3
    sps = random.randint(1, 3)
    psps = random.randint(1, 3)
    gameover = False

    def pause(screen, selected, gameover, score):
        if gameover:
            screen.fill("red")
        else:
            screen.fill("grey")
        option = ""
        tel = 0
        o1 = o2 = "black"
        list = [o1, o2]
        for i in list:
            if selected == tel:
                list[tel] = "white"
            tel +=1

        if gameover:
            list[1] = "White"
            font = pygame.font.SysFont(None, 200)
            img = font.render(f"Score: {score}", True, list[0])
            screen.blit(img, ((screenWidth/4), (screenHeight/4)))
        else:
            font = pygame.font.SysFont(None, 200)
            img = font.render("Resume", True, list[0])
            screen.blit(img, ((screenWidth/4), (screenHeight/4)))

        font = pygame.font.SysFont(None, 100)
        img = font.render("Quit", True, list[1])
        screen.blit(img, ((screenWidth/4), (screenHeight/2)))
        return option


    def startMenu(screen, selected):
        menu = True
        play = False
        tel = 0
        e1 = "black"
        e2 = e3 = e4 = "red"
        e1n = e2n = e3n = e4n = 100
        color = [e1, e2, e3, e4]
        size = [e1n, e2n, e3n, e4n]
        for i in color:
            if selected == tel:
                size[tel] = 125
                color[tel] = "white"
            tel +=1


        font = pygame.font.SysFont(None, size[0])
        img = font.render('PLAY', True, color[0])
        screen.blit(img, (20, 20))

        font = pygame.font.SysFont(None, size[1])
        img = font.render('SCORES(Werkt nog niet)', True, color[1])
        screen.blit(img, (20, 120))

        font = pygame.font.SysFont(None, size[2])
        img = font.render('ENTER3', True, color[2])
        screen.blit(img, (20, 220))

        font = pygame.font.SysFont(None, size[3])
        img = font.render('ENTER4', True, color[3])
        screen.blit(img, (20, 320))
        return menu, play




    def Game(screen, xpos, ypos, expos, eypos, score, lifes, sps, psps):
        play = True
        menu = False
        lane1 = pygame.draw.rect(screen, "white", pygame.Rect((screenWidth/2) - ((screenWidth/10) -60) /2, 0, screenWidth/10, screenHeight))
        lane2 = pygame.draw.rect(screen, "white", pygame.Rect((screenWidth/2) + movepos - ((screenWidth/10) -60) /2, 0, screenWidth/10, screenHeight))
        lane3 = pygame.draw.rect(screen, "white", pygame.Rect((screenWidth/2) - movepos - ((screenWidth/10) -60) /2, 0, screenWidth/10, screenHeight))

        rock = pygame.image.load("rock.png")
        paper = pygame.image.load("paper.png")
        scissors = pygame.image.load("scissors.png")

        
        player = pygame.draw.rect(screen, "white", pygame.Rect(xpos, ypos, 60, 60))
        enemy = pygame.draw.rect(screen, "white", pygame.Rect(expos, eypos, 60, 60))

        if sps == 1:
            screen.blit(rock, enemy)
        elif sps == 2:
            screen.blit(paper, enemy)
        elif sps == 3:
            screen.blit(scissors, enemy)

        if psps == 1:
            screen.blit(rock, player)
        elif psps == 2:
            screen.blit(paper, player)
        elif psps == 3:
            screen.blit(scissors, player)
        

        font = pygame.font.SysFont(None, 60)
        img = font.render(f"SCORE: {score}", True, "black")
        screen.blit(img, (20, 20))

        font = pygame.font.SysFont(None, 60)
        img = font.render(f"LIFE'S: {lifes}", True, "black")
        screen.blit(img, (screenWidth - 200, 20))

        return menu, play, player, enemy


    while menu:
        screen.fill("grey")
        menu, play = startMenu(screen, selected)
        for pressedkey in pygame.event.get():
            if pressedkey.type == pygame.QUIT:
                running = False
            if pressedkey.type == pygame.KEYDOWN:
                if pressedkey.key == pygame.K_UP:
                    if selected > 0 and selected <= 3:
                        selected -= 1
                if pressedkey.key == pygame.K_DOWN:
                    if selected >= 0 and selected < 3:
                        selected += 1
                if pressedkey.key == pygame.K_RETURN:
                    if selected == 0:
                        menu = False
                        play = True 

        pygame.display.flip()

        clock.tick(160) 



    
    while play:
        check = ["12", "23", "31"]
        screen.fill("grey")
        spawns = [screenWidth/2, (screenWidth/2) + movepos, (screenWidth/2) - movepos  ]
        if paused == False:
            menu, play, player, enemy = Game(screen, xpos, ypos, expos, eypos, score, lifes, sps, psps)
            eypos += speed
            if lifes == 0:
                gameover = True
                paused = True
            if player.colliderect(enemy):
                win = False
                for i in check:
                    if str(sps) + str(psps) == i:
                        lifes += 1
                        eypos = screenHeight + 10
                        win = True
                if win == False:
                    lifes -= 1
                    eypos = screenHeight + 10
            if eypos > screenHeight:
                sps = random.randint(1, 3)
                psps = random.randint(1, 3)
                speed = speed * acc
                if speed > 10:
                    speed = 10
                score += 1
                eypos = 0
                expos = random.choice(spawns)
            for pressedkey in pygame.event.get():
                if pressedkey.type == pygame.QUIT:
                    running = False
                if pressedkey.type == pygame.KEYDOWN:
                    if pressedkey.key == pygame.K_ESCAPE:
                        paused = True
                    if pressedkey.key == pygame.K_d:
                        if xpos == (screenWidth /2) + movepos:
                            pass
                        else:
                            xpos += movepos
                            ypos += 0
                    if pressedkey.key == pygame.K_a:
                        if xpos == (screenWidth /2) - movepos:
                            pass
                        else:
                            xpos += -movepos
                            ypos += 0
        if paused:
            option = pause(screen, pselected, gameover, score)
            for pressedkey in pygame.event.get():
                if pressedkey.type == pygame.KEYDOWN:
                    #if pressedkey.key == pygame.K_ESCAPE:
                        #paused = True
                    #voor als esc weer resume wilt zijn
                    if pressedkey.key == pygame.K_UP:
                        if pselected > 0 and pselected <= 1:
                            pselected -= 1
                    if pressedkey.key == pygame.K_DOWN:
                        if pselected >= 0 and pselected < 1:
                            pselected += 1
                    if pressedkey.key == pygame.K_RETURN:
                        if gameover:
                            pselected = 1
                        if pselected == 0:
                            paused = False
                            menu, play, player, enemy  = Game(screen, xpos, ypos, expos, eypos, score, lifes, sps, psps)
                        if pselected == 1:
                            paused = False
                            play = False
                            startMenu(screen, selected)
        
            
        

        pygame.display.flip()

        clock.tick(60) 

    if running == False:
        pygame.quit()
