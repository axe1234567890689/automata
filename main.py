import pygame

pygame.init()

font = pygame.font.SysFont("arial", 30)
terrain = {}
terrains = {}
bleu_print = {}
zoom = 10
#  pos_cam = []
pos = []
block = [(0, 0, 0), (255, 255, 0), (255, 150, 0), (255, 0, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255), (), (0, 200, 0), (0, 150, 200), (200, 200, 200)]
click = False
click_droit = False
taille_pinceau = 2
menu = "parametre"
parametre = {
    "size": [100, 100]
}
f = False
etape = True
type_select = 1
b_select = 0
screen_size = [1920, 1080]
boutons = {
    "parametre":{
        "CREATE": [1, [screen_size[0] - font.render("CREATE", False, (0, 0, 0)).get_width(), screen_size[1] - font.render("CREATE", False, (0, 0, 0)).get_height(), font.render("CREATE", False, (0, 0, 0)).get_width(), font.render("CREATE", False, (0, 0, 0)).get_height()], (0, 0, 0), (200, 200, 200), (200, 200, 200), (100, 100, 100), 5]
    }
}
cell_size = [int(screen_size[0] / zoom), int(screen_size[1] / zoom)]
screen = pygame.display.set_mode(screen_size)

screen.fill((0, 0, 0))
while True:
    mouse_pos = pygame.mouse.get_pos()

    if menu == "simulation":

        if click or click_droit:
            p_t = taille_pinceau / 2
            if p_t > int(p_t):
                p_t += 1
            p_t = int(p_t)
            x = int(mouse_pos[0] / zoom) - int(taille_pinceau / 2)
            while x < int(mouse_pos[0] / zoom) + p_t:
                if 0 < x < cell_size[0]:
                    y = int(mouse_pos[1] / zoom) - int(taille_pinceau / 2)
                    while y < int(mouse_pos[1] / zoom) + p_t:
                        if 0 < y < cell_size[1]:
                            if not click_droit:
                                terrains[x][y] = type_select
                            else:
                                terrains[x][y] = -1
                        y += 1
                x += 1

        for x in terrain:
            for y in terrain[x]:
                if terrains[x][y] == -1:
                    pass
                elif terrain[x][y] == 0:
                    if 1 < x:
                        if terrain[x - 1][y] == 1:
                            terrains[x - 1][y] = 0
                    if x < cell_size[0] - 1:
                        if terrain[x + 1][y] == 1:
                            terrains[x + 1][y] = 0
                    if 1 < y:
                        if terrain[x][y - 1] == 1:
                            terrains[x][y - 1] = 0
                    if y < cell_size[1] - 1:
                        if terrain[x][y + 1] == 1:
                            terrains[x][y + 1] = 0
                elif terrain[x][y] == 2:
                    if 1 < x:
                        if terrain[x - 1][y] == 0:
                            terrains[x - 1][y] = 2
                    if x < cell_size[0] - 1:
                        if terrain[x + 1][y] == 0:
                            terrains[x + 1][y] = 2
                    if 1 < y:
                        if terrain[x][y - 1] == 0:
                            terrains[x][y - 1] = 2
                    if y < cell_size[1] - 1:
                        if terrain[x][y + 1] == 0:
                            terrains[x][y + 1] = 2
                    terrains[x][y] = 1
                elif terrain[x][y] == 1:
                    if 1 < x:
                        if terrain[x - 1][y] == 2:
                            terrains[x - 1][y] = 1
                    if x < cell_size[0] - 1:
                        if terrain[x + 1][y] == 2:
                            terrains[x + 1][y] = 1
                    if 1 < y:
                        if terrain[x][y - 1] == 2:
                            terrains[x][y - 1] = 1
                    if y < cell_size[1] - 1:
                        if terrain[x][y + 1] == 2:
                            terrains[x][y + 1] = 1
                elif terrain[x][y] == 3:
                    if 1 < y < cell_size[1] - 1 and x < cell_size[0] - 1:
                        if terrain[x][y - 1] == 0 and terrain[x][y + 1] == 0:
                            terrains[x + 1][y] = 0
                        else:
                            terrains[x + 1][y] = 2
                elif terrain[x][y] == 4:
                    if 1 < x < cell_size[0] - 1:
                        if terrain[x - 1][y] == 0:
                            terrains[x + 1][y] = 2
                        elif terrain[x - 1][y] == 1:
                            terrains[x + 1][y] = 0
                elif terrain[x][y] == 7:
                    if 1 < x < cell_size[0] - 1:
                        terrains[x + 1][y] = terrain[x - 1][y]
                    if 1 < y < cell_size[1] - 1:
                        terrains[x][y + 1] = terrain[x][y - 1]
                elif terrain[x][y] == 8:
                    if 1 < x < cell_size[0] - 1:
                        terrains[x - 1][y] = terrain[x + 1][y]
                    if 1 < y < cell_size[1] - 1:
                        terrains[x][y - 1] = terrain[x][y + 1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_DOWN:
                    taille_pinceau -= 1
                    if taille_pinceau < 1:
                        taille_pinceau = 1
                elif event.key == pygame.K_UP:
                    taille_pinceau += 1
                elif event.key == pygame.K_f:
                    f = True
                elif event.unicode == "0":
                    type_select = 0
                elif event.unicode == "1":
                    type_select = 1
                elif event.unicode == "2":
                    type_select = 2
                elif event.unicode == "3":
                    type_select = 3
                elif event.unicode == "4":
                    type_select = 4
                elif event.unicode == "5":
                    type_select = 5
                elif event.unicode == "6":
                    type_select = 6
                elif event.unicode == "7":
                    type_select = 7
                elif event.unicode == "8":
                    type_select = 8
                elif event.unicode == "9":
                    type_select = 9
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 2:
                    if f:
                        pos = []
                        bleu_print = {}
                    elif pos and not bleu_print == {}:
                        xd = int(mouse_pos[0] / zoom) - pos[0]
                        yd = int(mouse_pos[1] / zoom) - pos[1]
                        for x in bleu_print:
                            if 0 < x + xd < cell_size[0]:
                                for y in bleu_print[x]:
                                    if 0 < y + yd < cell_size[1]:
                                        terrains[x + xd][y + yd] = bleu_print[x][y]
                elif event.button == 3:
                    click_droit = True
                elif event.button == 1:
                    x = int(mouse_pos[0] / zoom)
                    y = int(mouse_pos[1] / zoom)
                    if not f:
                        non = False
                        if 0 < x < cell_size[0] and 0 < y < cell_size[1]:
                            if not terrain[x][y] == 5:
                                click = True
                            else:
                                if x + 1 < cell_size[0]:
                                    if terrain[x + 1][y] == 0:
                                        terrains[x + 1][y] = 2
                                    elif terrain[x + 1][y] == 1:
                                        terrains[x + 1][y] = 0
                    else:
                        if not pos:
                            pos = [x + 1, y + 1]
                        else:
                            zx = pos[0]
                            while zx < x:
                                zy = pos[1]
                                bleu_print[zx] = {}
                                while zy < y:
                                    if not terrain[zx][zy] == -1:
                                        bleu_print[zx][zy] = terrain[zx][zy]
                                    zy += 1
                                zx += 1
                            pos = [x, y]
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    click_droit = False
                elif event.button == 1:
                    click = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_f:
                    f = False

        for x in terrains:
            for y in terrains[x]:
                if not terrain[x][y] == terrains[x][y] or terrain[x][y] == 6:
                    terrain[x][y] = terrains[x][y]
                    color = block[terrain[x][y] + 1]
                    if terrain[x][y] == 6:
                        if 0 < y:
                            if terrain[x][y - 1] == 0:
                                color = (255, 255, 255)
                            else:
                                color = (100, 100, 100)
                    pygame.draw.rect(screen, color, [x * zoom, y * zoom, zoom, zoom])

    elif menu == "parametre":

        for b in boutons[menu]:
            bouton = boutons[menu][b]
            if bouton[1][0] <= mouse_pos[0] <= bouton[1][0] + bouton[1][2] and bouton[1][1] <= mouse_pos[1] <= bouton[1][1] + bouton[1][3]:
                pygame.draw.rect(screen, bouton[5], bouton[1])
                color = bouton[4]
                b_select = bouton[0]
            else:
                pygame.draw.rect(screen, bouton[3], bouton[1])
                color = bouton[2]
            text = font.render(b, True, color)
            screen.blit(text, (bouton[1][0] + bouton[6], bouton[1][1] + bouton[6]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if b_select == 1:
                        cell_size = parametre["size"]
                        x = parametre["size"][0]
                        while x > 0:
                            terrain[x] = {}
                            terrains[x] = {}
                            y = parametre["size"][1]
                            while y > 0:
                                terrain[x][y] = -1
                                terrains[x][y] = -1
                                y -= 1
                            x -= 1
                        menu = "simulation"
                        screen.fill((0, 0, 0))
    pygame.display.flip()
