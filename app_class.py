class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'start'
       
   def run(self):
        while self.running:
            if self.state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
   
   ######################### Helper Functions ###########################
    def draw_text(self, words, screen, pos, size, color, font_name, centered = False): 
        font = pygame.font.SysFont(font_name, size) 
        text = font.render(words, False, color)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0] - text_size[0]//2
            pos[1] = pos[1] - text_size[1]//2
        screen.blit(text, pos)
        
   def load(self):
        #self.background = pygame.image.load('maze.png')
        self.background = pygame.image.load('C:\\Users\\Udochi Nwachukwu\\OneDrive\\Documents\\PacmanGame\\maze.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))
   
   ############### Video 2 ############################################
    
   def load(self):
        #self.background = pygame.image.load('maze.png')
        self.background = pygame.image.load('C:\\Users\\Udochi Nwachukwu\\OneDrive\\Documents\\PacmanGame\\maze.png')
        self.background = pygame.transform.scale(self.background, (MAZE_WIDTH, MAZE_HEIGHT))
        
        # Openning walls file
        # Creatint walls list wihth co-ords of walls
        with open("C:\\Users\\Udochi Nwachukwu\\OneDrive\\Documents\\PacmanGame\\walls.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "1":
                        self.walls.append(vec(xidx, yidx))
                    elif char == "C":
                        self.coins.append(vec(xidx, yidx)) 
                    elif char == "P":
                        self.p_pos = [xidx, yidx]
                    elif char in ["2", "3", "4", "5"]:
                        self.e_pos.append([xidx, yidx])
                    elif char == "B":
                        pygame.draw.rect(self.background, BLACK, (xidx * self.cell_width, yidx * self.cell_height, self.cell_width, self.cell_height))
    
    ############### Video 3 ############################################
    
    def make_enemies(self):
        for idx, pos in enumerate(self.e_pos):
            self.enemies.append(Enemy(self, vec(pos), idx))

    def draw_grid(self):
        for x in range(WIDTH//self.cell_width):
            pygame.draw.line(self.background, GREY, (x * self.cell_width, 0), (x * self.cell_width, HEIGHT))
        for x in range(HEIGHT//self.cell_height):
            pygame.draw.line(self.background, GREY, (0, x * self.cell_height), (WIDTH, x * self.cell_height))
        #for coin in self.coins:
            #pygame.draw.rect(self.background, (167, 179, 34), (coin.x * self.cell_width, coin.y * self.cell_height, self.cell_width, self.cell_height))

    def reset(self):
        self.player.lives = 3
        self.player.current_score = 0
        self.player.grid_pos = vec(self.player.starting_pos)
        self.player.pix_pos = self.player.get_pix_pos()
        self.player.direction *= 0
        for enemy in self.enemies:
            enemy.grid_pos = vec(enemy.starting_pos)
            enemy.pix_pos = enemy.get_pix_pos()
            enemy.direction *= 0
        self.coins = []
        with open("C:\\Users\\Udochi Nwachukwu\\OneDrive\\Documents\\PacmanGame\\walls.txt", 'r') as file:
            for yidx, line in enumerate(file):
                for xidx, char in enumerate(line):
                    if char == "C":
                        self.coins.append(vec(xidx, yidx))
        self.state = "playing"

  ############################ Video 5 ###################################
