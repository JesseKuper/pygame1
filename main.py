import pygame
import random


running = True
while running:
    pygame.init()
    screenWidth = 1280
    screenHeight = 720
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
    lifes = 3
    health = False

    def pause(screen, selected):
        screen.fill("yellow")
        option = ""
        tel = 0
        o1 = o2 = "black"
        list = [o1, o2]
        for i in list:
            if selected == tel:
                list[tel] = "white"
            tel +=1

        font = pygame.font.SysFont(None, 24)
        img = font.render("Resume", True, list[0])
        screen.blit(img, (20, 20))

        font = pygame.font.SysFont(None, 24)
        img = font.render("Quit", True, list[1])
        screen.blit(img, (20, 40))
        return option


    def startMenu(screen, selected):
        menu = True
        play = False
        tel = 0
        e1 = e2 = e3 = e4 = "black"
        list = [e1, e2, e3, e4]
        for i in list:
            if selected == tel:
                list[tel] = "white"
            tel +=1
        font = pygame.font.SysFont(None, 24)
        img = font.render('CLICK SPATIE OM TE KIEZEN', True, "red")
        screen.blit(img, (20, 0))

        font = pygame.font.SysFont(None, 24)
        img = font.render('ENTER', True, list[0])
        screen.blit(img, (20, 20))

        font = pygame.font.SysFont(None, 24)
        img = font.render('ENTER2', True, list[1])
        screen.blit(img, (20, 40))

        font = pygame.font.SysFont(None, 24)
        img = font.render('ENTER3', True, list[2])
        screen.blit(img, (20, 60))

        font = pygame.font.SysFont(None, 24)
        img = font.render('ENTER4', True, list[3])
        screen.blit(img, (20, 80))
        return menu, play

    def Game(screen, xpos, ypos, expos, eypos, score, lifes, health):
        play = True
        menu = False
        lane1 = pygame.draw.rect(screen, "white", pygame.Rect((screenWidth/2) -10, 0, 80, screenHeight))
        lane2 = pygame.draw.rect(screen, "white", pygame.Rect((screenWidth/2) + movepos - 10, 0, 80, screenHeight))
        lane3 = pygame.draw.rect(screen, "white", pygame.Rect((screenWidth/2) - movepos - 10, 0, 80, screenHeight))
        fireball = pygame.image.load("fireball.png")
        water = pygame.image.load("water.png")
        
        player = pygame.draw.rect(screen, "white", pygame.Rect(xpos, ypos, 60, 60))
        enemy = pygame.draw.rect(screen, "white", pygame.Rect(expos, eypos, 60, 60))

        if health == 1:
            screen.blit(fireball, enemy)
        else:
            screen.blit(water, enemy)
        screen.blit(fireball, player)
        

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
                if pressedkey.key == pygame.K_SPACE:
                    if selected == 0:
                        menu = False
                        play = True 

        pygame.display.flip()

        clock.tick(160) 



    
    while play:
        screen.fill("grey")
        spawns = [screenWidth/2, (screenWidth/2) + movepos, (screenWidth/2) - movepos  ]
        if paused == False:
            menu, play, player, enemy = Game(screen, xpos, ypos, expos, eypos, score, lifes, health)
            eypos += speed
            if lifes == 0:
                play = False
                menu = True
            if health == 1:
                if player.colliderect(enemy):
                    lifes += 1
                    eypos = screenHeight + 10
            else:
                if player.colliderect(enemy):
                    lifes -= 1
                    eypos = screenHeight + 10
            if eypos > screenHeight:
                health = random.randint(1, 20)
                speed = speed * 1.2
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
            option = pause(screen, pselected)
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
                    if pressedkey.key == pygame.K_SPACE:
                        if pselected == 0:
                            paused = False
                            menu, play, player, enemy  = Game(screen, xpos, ypos, expos, eypos, score, lifes, health)
                        if pselected == 1:
                            paused = False
                            play = False
                            startMenu(screen, selected)
        
            
        

        pygame.display.flip()

        clock.tick(60) 

    if running == False:
        pygame.quit()
