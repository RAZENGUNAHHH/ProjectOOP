import pygame

class Fighter():
    
    # inint Fighter
    #  x, y is coordinate
    def __init__(self,player, x,y , flip , data , sprite_sheet , animation_step):
        # x,y is coordinate
        self.size = data[0]
        self.flip = flip
        self.image_scale = data[1]
        self.offset = data[2]
        self.running = False
        #  0 :idle 1:run 2:jump 3:attack1 4:attack2 5:hit 6:death
        self.frame_index = 0
        self.action = 0  
        self.animation_list = self.load_images(sprite_sheet, animation_step)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = pygame.Rect(x,y,80,180)
        self.vel_y = 0
        self.jump = False
        self.attack_type = 0
        self.attacking = False
        self.update_time = pygame.time.get_ticks()
        self.health = 100
        self.hit = False
        self.alive = True
        self.player = player



    def load_images(self , sprite_sheet , animate_steps):
        # extract sheet
        animation_list = []
        for y , animation in enumerate(animate_steps):
            temp_img_list = []
            for x in range(animation):
                # resize image
                temp_image = sprite_sheet.subsurface(x*self.size,y*self.size , self.size , self.size) 
                temp_img_list.append(pygame.transform.scale(temp_image , (self.size * self.image_scale , self.size * self.image_scale)))
            animation_list.append(temp_img_list)
        return animation_list


    # speed Character
    def move(self , screen_width , screen_height , surface ,target):
        # dx , dy are Values that change all the time
        self.running = False
        self.attack_type = 0
        GRAVITY = 2
        SPEED = 10
        dx = 0
        dy = 0
        #  get keypress
        key = pygame.key.get_pressed()
        if self.player == 1:
            if self.attacking == False and self.alive == True:
                if key[pygame.K_a]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_d]:
                    dx = SPEED
                    self.running = True
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -30 
                    self.jump = True
                if key[pygame.K_r] or key[pygame.K_t]:
                    self.attack(surface , target)
                    # determine which attack type was used
                    if key[pygame.K_r]:
                        self.attack_type = 1
                    if key[pygame.K_t]:
                        self.attack_type = 2
        else:
            if self.attacking == False and self.alive == True:
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                    self.running = True
                if key[pygame.K_RIGHT]:
                    dx = SPEED
                    self.running = True
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -30 
                    self.jump = True
                if key[pygame.K_KP1] or key[pygame.K_KP2]:
                    self.attack(surface , target)
                    # determine which attack type was used
                    if key[pygame.K_KP1]:
                        self.attack_type = 1
                    if key[pygame.K_KP2]:
                        self.attack_type = 2
            
            



        # apply gravity
        self.vel_y += GRAVITY    
        dy += self.vel_y
        # set player stays on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width  - self.rect.right
        if self.rect.bottom + dy > screen_height - 110:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 110 -self.rect.bottom
        if self.rect.centerx > target.rect.centerx:
            self.flip = True
        else:
            self.flip = False
        #  update player position
        self.rect.x += dx
        self.rect.y += dy



    def update(self):
        animate_cooldown = 100
        # update frame for each action
        if self.health <= 0 :
            self.health = 0
            self.alive = False
            self.update_action(6)
        elif self.hit:
            self.update_action(5)
        elif self.attacking == True:
            if self.attack_type == 1 :
                self.update_action(3)
            elif self.attack_type == 2:
                self.update_action(4)
        elif self.jump:
            self.update_action(2)
        elif self.running:
            self.update_action(1)
        else:
            self.update_action(0)
        self.image = self.animation_list[self.action][self.frame_index]
        #  loop image frame index 
        if pygame.time.get_ticks() - self.update_time > animate_cooldown:
            self.frame_index += 1
            self.update_time = pygame.time.get_ticks()
        # character idle
        if self.frame_index == len(self.animation_list[self.action]):
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action])-1
            else:
                self.frame_index = 0
                if self.action == 3 or self.action == 4:
                    self.attacking = False
                # check if damage was taken
                if self.action == 5:
                    self.hit = False
                    self.attacking = False
            
        


    # method
    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    # method attack
    def attack(self , surface , target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip) , self.rect.y , 2*self.rect.width , self.rect.height)
        if attacking_rect.colliderect(target.rect):
            target.health -= 10
            target.hit = True
    def draw(self , surface):
        print(self.attack_type)
        # surface is scree of program
        img_flip = pygame.transform.flip(self.image , self.flip , False)
        # blite have property width and height
        surface.blit(img_flip, (self.rect.x  - (self.offset[0] * self.image_scale), self.rect.y - (self.offset[1] * self.image_scale)))

    
