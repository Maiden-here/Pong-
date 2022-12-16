import pygame,sys


pygame.init()

class Button:
    global screen
    
    def __init__(self,screen,width:int,height:int,pos = (0,0),text = "Click Me!",font = 'broadway',top_color = (0,0,200),hover_color = (200,200,200)) -> None:
        self.pressed = False
        self.button_pressed = False

        #top rect
        self.width = width
        self.height = height
        self.top_rect = pygame.Rect((pos),(self.width,self.height))  
        self.top_color = top_color
        self.hover_color = hover_color
        self.current_color = self.top_color

        #text
        self.screen = screen
        self.text_font = pygame.font.SysFont(font,30)
        self.rendered_text = self.text_font.render(text,True,(0,0,0))
        self.text_rect = self.rendered_text.get_rect(center = self.top_rect.center)

    def draw_button(self):
        self.check_click()
        pygame.draw.rect(self.screen,self.current_color,self.top_rect,border_radius = 7) 
        self.screen.blit(self.rendered_text,self.text_rect)

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()     
        if self.top_rect.collidepoint(mouse_pos):
            self.current_color = self.hover_color
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed == True:
                    print("clicked")
                    self.button_pressed = True
                    if self.button_pressed == True:
                        self.top_rect.center = (2000,2000)
                        self.text_rect.center = (self.top_rect.center)
                    else:
                        self.top_rect.center = (self.width, self.height)
                    self.pressed = False
        else:
            self.current_color = self.top_color
        return self.button_pressed
