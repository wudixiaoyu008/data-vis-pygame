import pygame

BLACK = (0,0,0)
GRAY = (127, 127, 127)
RED = (255, 0, 0)


class Button:

        def __init__(self, text1, text2, rect):
                self.text1 = text1
                self.text2 = text2
                self.rect = rect
                self.rect2 = pygame.Rect(
                        self.rect.x,
                        self.rect.y + self.rect.height,
                        self.rect.width,
                        self.rect.height
                )

        def draw(self, surface):
                pygame.draw.rect(surface, RED, self.rect)
                font = pygame.font.Font(None, 24)
                label_view = font.render(self.text1, False, BLACK)
                label_pos = label_view.get_rect()
                label_pos.centery = self.rect.centery
                label_pos.centerx = self.rect.centerx
                surface.blit(label_view, label_pos)

                pygame.draw.rect(surface, GRAY, self.rect2)
                font = pygame.font.Font(None, 24)
                label_view2 = font.render(self.text2, False, BLACK)
                label_pos2 = label_view2.get_rect()
                label_pos2.centery = self.rect2.centery
                label_pos2.centerx = self.rect2.centerx
                surface.blit(label_view2, label_pos2)



        def handle_event(self, event):
                if event.type == pygame.MOUSEBUTTONDOWN:
                        (x, y) = pygame.mouse.get_pos()
                        if x >= self.rect.x and \
                            x <= self.rect.x + self.rect.width and \
                            y >= self.rect.y and \
                            y <= self.rect.y + self.rect.height * 2:
                          self.on_click(event)

        def on_click(self, event):
                print("button clicked")
