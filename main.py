import pygame

pygame.init()

font = pygame.font.SysFont("arial", 30)
inter_au_gation = pygame.image.load("inter_au_gation.png")
inter_au_gation = pygame.transform.scale(inter_au_gation, [50, 50])
terrain = {}
terrains = {}
bleu_print = {}
zoom = 10
rgb = [200, 200, 200]
pos = []
click = False
click_droit = False
taille_pinceau = 2
menu = "parametre"
selec = "elec"
s_menu = "shema"
parametre = {
    "size": [100, 100],
    "elec": {
        "color": [(0, 0, 0), (255, 255, 0), (255, 150, 0), (255, 0, 0), (255, 0, 255), (0, 255, 255), (255, 255, 255), (100, 100, 100), (255, 255, 255)],
        "nb": [],
        "propagation": [[0, 1], [2, 0]],
        "shema": [[-2, -2, 2, -2, -2, -2, -2, 1, -2, -2], [0, -2, 6, -2, -2, -2, -2, 7, -2, -2], [1, -2, 7, -2, -2, -2, -2, 6, -2, -2], [0, -2, 3, -2, 0, -2, -2, 3, 0, -2], [1, -2, 3, -2, -2, -2, -2, 3, 2, -2], [-2, -2, 3, -2, 1, -2, -2, 3, 2, -2], [-2, 1, 4, -2, -2, -2, -2, 4, 0, -2], [-2, 0, 4, -2, -2, -2, -2, 4, 2, -2]]
    },
    "jeux de la vie": {
        "color": [(0, 0, 0), (255, 255, 255)],
        "nb": [[1, 0, [[[0, 1], -1, [0]], [[3], 0, [-2]], [[4, 5, 6, 7, 8], -1, [0]]]]],
        "propagation": [],
        "shema": []
    }
}
f = False
etape = True
pause = False
type_select = 0
b_select = 0
screen_size = [1920, 1080]
boutons = {
    "simulation": {},
    "parametre": {
        "CREATE": [1, [screen_size[0] - font.render("CREATE", False, (0, 0, 0)).get_width(),
                       screen_size[1] - font.render("CREATE", False, (0, 0, 0)).get_height(),
                       font.render("CREATE", False, (0, 0, 0)).get_width(),
                       font.render("CREATE", False, (0, 0, 0)).get_height()], (0, 0, 0), (200, 200, 200),
                   (200, 200, 200), (100, 100, 100), 5, 30],
        "": [2, [0, 0, 100, 100], (0, 0, 0), (200, 200, 200),
                   (200, 200, 200), (100, 100, 100), 0, 30]
    },
    "rgb": {
        "": [0, [110, 100, 50, screen_size[1] - 200], (0, 0, 0), (200, 0, 0), (0, 0, 0), (100, 0, 0), 0, 30],
        " ": [1, [200, 100, 50, screen_size[1] - 200], (0, 0, 0), (0, 200, 0), (0, 0, 0), (0, 100, 0), 0, 30],
        "  ": [2, [290, 100, 50, screen_size[1] - 200], (0, 0, 0), (0, 0, 200), (0, 0, 0), (0, 0, 100), 0, 30],
        "CREATE": [3, [screen_size[0] - font.render("CREATE", False, (0, 0, 0)).get_width(),
                       screen_size[1] - font.render("CREATE", False, (0, 0, 0)).get_height(),
                       font.render("CREATE", False, (0, 0, 0)).get_width(),
                       font.render("CREATE", False, (0, 0, 0)).get_height()], (0, 0, 0), (200, 200, 200),
                   (200, 200, 200), (100, 100, 100), 5, 30],
        "CANCEL": [4, [screen_size[0] - font.render("CANCEL", False, (0, 0, 0)).get_width() - font.render("CREATE", False, (0, 0, 0)).get_width() - 20,
                       screen_size[1] - font.render("CANCEL", False, (0, 0, 0)).get_height(),
                       font.render("CANCEL", False, (0, 0, 0)).get_width(),
                       font.render("CANCEL", False, (0, 0, 0)).get_height()], (0, 0, 0), (200, 200, 200),
                   (200, 200, 200), (100, 100, 100), 5, 30]
    }
}
cell_size = [int(screen_size[0] / zoom), int(screen_size[1] / zoom)]
screen = pygame.display.set_mode(screen_size)


def shem(shema, x, y):
    if 1 < y or shema[0] == -2:
        if shema[0] == -2 or terrain[x][y - 1] == shema[0]:
            if 1 < x or shema[1] == -2:
                if shema[1] == -2 or terrain[x - 1][y] == shema[1]:
                    if x < cell_size[0] - 1 or shema[3] == -2:
                        if shema[3] == -2 or terrain[x + 1][y] == shema[3]:
                            if y < cell_size[1] - 1 or shema[4] == -2:
                                if shema[4] == -2 or terrain[x][y + 1] == shema[4]:
                                    if not shema[5] == -2:
                                        terrains[x][y - 1] = shema[5]
                                    if not shema[6] == -2:
                                        terrains[x - 1][y] = shema[6]
                                    terrains[x][y] = shema[7]
                                    if not shema[8] == -2:
                                        terrains[x + 1][y] = shema[8]
                                    if not shema[9] == -2:
                                        terrains[x][y + 1] = shema[9]


def prop(nb_centre, nb_a_changer, x, y):
    if 1 < x:
        if terrain[x - 1][y] == nb_a_changer:
            terrains[x - 1][y] = nb_centre
    if x < cell_size[0] - 1:
        if terrain[x + 1][y] == nb_a_changer:
            terrains[x + 1][y] = nb_centre
    if 1 < y:
        if terrain[x][y - 1] == nb_a_changer:
            terrains[x][y - 1] = nb_centre
    if y < cell_size[1] - 1:
        if terrain[x][y + 1] == nb_a_changer:
            terrains[x][y + 1] = nb_centre


def entier(text):
    if text == "0" or text == "1" or text == "2" or text == "3" or text == "4" or text == "5" or text == "6" or text == "7" or text == "8" or text == "9":
        return True
    return False


def écrir(text, color, taille, pos):
    font = pygame.font.SysFont("arial", taille)
    text = font.render(text, False, color)
    screen.blit(text, pos)


screen.fill((0, 0, 0))


def compt(x, y, param, param1):
    nb = 0
    if 1 < x:
        if param == terrain[x - 1][y]:
            nb += 1
        if param1:
            if 1 < y:
                if param == terrain[x - 1][y - 1]:
                    nb += 1
            if y < cell_size[0] - 1:
                if param == terrain[x - 1][y + 1]:
                    nb += 1
    if x < cell_size[0] - 1:
        if param == terrain[x + 1][y]:
            nb += 1
        if param1:
            if 1 < y:
                if param == terrain[x + 1][y - 1]:
                    nb += 1
            if y < cell_size[0] - 1:
                if param == terrain[x + 1][y + 1]:
                    nb += 1
    if 1 < y:
        if param == terrain[x][y - 1]:
            nb += 1
    if y < cell_size[0] - 1:
        if param == terrain[x][y + 1]:
            nb += 1
    return nb


while True:
    mouse_pos = pygame.mouse.get_pos()

    b_select = -1

    for b in boutons[menu]:
        bouton = boutons[menu][b]
        if bouton[1][0] <= mouse_pos[0] <= bouton[1][0] + bouton[1][2] and bouton[1][1] <= mouse_pos[1] <= \
                bouton[1][1] + bouton[1][3]:
            pygame.draw.rect(screen, bouton[5], bouton[1])
            color = bouton[4]
            b_select = bouton[0]
        else:
            pygame.draw.rect(screen, bouton[3], bouton[1])
            color = bouton[2]
        écrir(b, color, bouton[7], (bouton[1][0] + bouton[6], bouton[1][1] + bouton[6]))

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

        if not pause:
            for x in terrain:
                for y in terrain[x]:
                    for i in parametre[selec]["propagation"]:
                        if terrain[x][y] == i[0]:
                            prop(i[0], i[1], x, y)
                    for i in parametre[selec]["shema"]:
                        if terrain[x][y] == i[2]:
                            shem(i, x, y)
                    for i in parametre[selec]["nb"]:
                        t = False
                        nb = compt(x, y, i[1], i[0])
                        for o in i[2]:
                            if not t:
                                if o[2][0] == -2:
                                    for u in o[0]:
                                        if nb == u:
                                            print(nb, o, i)
                                            terrains[x][y] = o[1]
                                            t = True
                                else:
                                    for p in o[2]:
                                        if p == terrain[x][y]:
                                            for u in o[0]:
                                                if nb == u:
                                                    terrains[x][y] = o[1]
                                                    t = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_SPACE:
                    pause = not pause
                elif event.key == pygame.K_DOWN:
                    taille_pinceau -= 1
                    if taille_pinceau < 1:
                        taille_pinceau = 1
                elif event.key == pygame.K_UP:
                    taille_pinceau += 1
                elif event.key == pygame.K_f:
                    f = True
            elif event.type == pygame.MOUSEWHEEL:
                type_select += event.y
                if type_select >= len(parametre[selec]["color"]) - 1:
                    type_select = 0
                elif type_select < 0:
                    type_select = len(parametre[selec]["color"]) - 2
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
                    color = parametre[selec]["color"][terrain[x][y] + 1]
                    if terrain[x][y] == 6:
                        if 0 < y:
                            if terrain[x][y - 1] == 0:
                                color = (255, 255, 255)
                            else:
                                color = (100, 100, 100)
                    pygame.draw.rect(screen, color, [x * zoom, y * zoom, zoom, zoom])
        pygame.draw.rect(screen, parametre[selec]["color"][type_select + 1], [0, 0, zoom, zoom])

    elif menu == "parametre":

        font = pygame.font.SysFont("arial", 200)
        text = font.render("+", False, (0, 0, 0))
        screen.blit(text, (-10, -60))
        font = pygame.font.SysFont("arial", 30)

        pygame.draw.rect(screen, (150, 150, 150), [155, 0, len(parametre[selec]["color"]) * 55 + 15, 70])

        for i in range(len(parametre[selec]["color"])):
            pygame.draw.rect(screen, parametre[selec]["color"][i], [(i + 3) * 55, 10, 50, 50])

        d = int(screen_size[0] / 400)
        for i in range(len(parametre[selec][s_menu])):
            m = parametre[selec][s_menu][i]
            y = int(i / d)
            x = (i - y * d) * 405 + 10
            pygame.draw.rect(screen, (100, 100, 100), [x, y * 180 + 120, 395, 170])
            if not m[0] == -2:
                pygame.draw.rect(screen, parametre[selec]["color"][m[0] + 1], [x + 55, y * 180 + 125, 50, 50])
            else:
                screen.blit(inter_au_gation, (x + 55, y * 180 + 125))
            if not m[1] == -2:
                pygame.draw.rect(screen, parametre[selec]["color"][m[1] + 1], [x + 5, y * 180 + 175, 50, 50])
            else:
                screen.blit(inter_au_gation, (x + 5, y * 180 + 175))
            if not m[2] == -2:
                pygame.draw.rect(screen, parametre[selec]["color"][m[2] + 1], [x + 55, y * 180 + 175, 50, 50])
            else:
                screen.blit(inter_au_gation, (x + 55, y * 180 + 175))
            if not m[3] == -2:
                pygame.draw.rect(screen, parametre[selec]["color"][m[3] + 1], [x + 105, y * 180 + 175, 50, 50])
            else:
                screen.blit(inter_au_gation, (x + 105, y * 180 + 175))
            if not m[4] == -2:
                pygame.draw.rect(screen, parametre[selec]["color"][m[4] + 1], [x + 55, y * 180 + 225, 50, 50])
            else:
                screen.blit(inter_au_gation, (x + 55, y * 180 + 225))
            pygame.draw.rect(screen, (0, 0, 0), [x + 55, y * 180 + 125, 50, 50], 5)
            pygame.draw.rect(screen, (0, 0, 0), [x + 5, y * 180 + 175, 50, 50], 5)
            pygame.draw.rect(screen, (0, 0, 0), [x + 55, y * 180 + 175, 50, 50], 5)
            pygame.draw.rect(screen, (0, 0, 0), [x + 105, y * 180 + 175, 50, 50], 5)
            pygame.draw.rect(screen, (0, 0, 0), [x + 55, y * 180 + 225, 50, 50], 5)
            écrir(">", (0, 0, 0), 50, [x + 160, y * 180 + 175])
            if not m[5] == -2:
                pygame.draw.rect(screen, parametre[selec]["color"][m[5] + 1], [x + 245, y * 180 + 125, 50, 50])
            else:
                screen.blit(inter_au_gation, (x + 245, y * 180 + 125))
            if not m[6] == -2:
                pygame.draw.rect(screen, parametre[selec]["color"][m[6] + 1], [x + 195, y * 180 + 175, 50, 50])
            else:
                screen.blit(inter_au_gation, (x + 195, y * 180 + 175))
            if not m[7] == -2:
                pygame.draw.rect(screen, parametre[selec]["color"][m[7] + 1], [x + 245, y * 180 + 175, 50, 50])
            else:
                screen.blit(inter_au_gation, (x + 245, y * 180 + 175))
            if not m[8] == -2:
                pygame.draw.rect(screen, parametre[selec]["color"][m[8] + 1], [x + 295, y * 180 + 175, 50, 50])
            else:
                screen.blit(inter_au_gation, (x + 295, y * 180 + 175))
            if not m[9] == -2:
                pygame.draw.rect(screen, parametre[selec]["color"][m[9] + 1], [x + 245, y * 180 + 225, 50, 50])
            else:
                screen.blit(inter_au_gation, (x + 245, y * 180 + 225))
            pygame.draw.rect(screen, (0, 0, 0), [x + 245, y * 180 + 125, 50, 50], 5)
            pygame.draw.rect(screen, (0, 0, 0), [x + 195, y * 180 + 175, 50, 50], 5)
            pygame.draw.rect(screen, (0, 0, 0), [x + 245, y * 180 + 175, 50, 50], 5)
            pygame.draw.rect(screen, (0, 0, 0), [x + 295, y * 180 + 175, 50, 50], 5)
            pygame.draw.rect(screen, (0, 0, 0), [x + 245, y * 180 + 225, 50, 50], 5)

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
                    elif b_select == 2:
                        screen.fill((0, 0, 0))
                        menu = "rgb"

    elif menu == "rgb":
        if click:
            if -1 < b_select < 3:
                rgb[b_select] = int((mouse_pos[1] - 100) / (screen_size[1] - 200) * 255)

        pygame.draw.rect(screen, (0, 0, 0), [100, (rgb[0] / 255) * (screen_size[1] - 200) + 90, 60, 20])
        pygame.draw.rect(screen, (0, 0, 0), [190, (rgb[1] / 255) * (screen_size[1] - 200) + 90, 60, 20])
        pygame.draw.rect(screen, (0, 0, 0), [280, (rgb[2] / 255) * (screen_size[1] - 200) + 90, 60, 20])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                click = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                if event.button == 1 and b_select >= 0:
                    if b_select == 3:
                        parametre[selec]["color"].append(rgb)
                        rgb = [200, 200, 200]
                        menu = "parametre"
                        screen.fill((0, 0, 0))
                    elif b_select == 4:
                        menu = "parametre"
                        screen.fill((0, 0, 0))

    pygame.display.flip()

    if menu == "rgb":
        pygame.draw.rect(screen, rgb, [50, 50, screen_size[0] - 100, screen_size[1] - 100])
