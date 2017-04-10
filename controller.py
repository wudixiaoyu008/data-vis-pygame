import pygame
import view
import model
from button import Button

BLACK = (0,0,0)
GRAY = (127, 127, 127)
RED = (255, 0, 0)

################# 'dem' or 'gop' ##################
class DataChangeButton1(Button):
	def __init__(self, text1, text2, rect):
		Button.__init__(self, text1, text2, rect)
		self.party = 'dem'

	def on_click(self, event):
		if (self.party is 'dem'):
			#  change color
			self.party = 'gop'
		else:
			#  change colro
			self.party = 'dem'
		# print (self.party)
		return self.party

	def draw(self, surface):
		if self.party is 'dem':
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

		if self.party is 'gop':
			pygame.draw.rect(surface, GRAY, self.rect)
			font = pygame.font.Font(None, 24)
			label_view = font.render(self.text1, False, BLACK)
			label_pos = label_view.get_rect()
			label_pos.centery = self.rect.centery
			label_pos.centerx = self.rect.centerx
			surface.blit(label_view, label_pos)

			pygame.draw.rect(surface, RED, self.rect2)
			font = pygame.font.Font(None, 24)
			label_view2 = font.render(self.text2, False, BLACK)
			label_pos2 = label_view2.get_rect()
			label_pos2.centery = self.rect2.centery
			label_pos2.centerx = self.rect2.centerx
			surface.blit(label_view2, label_pos2)


################# true or false ###################
class DataChangeButton2(Button):
	def __init__(self, text1, text2, rect):
		Button.__init__(self, text1, text2, rect)
		self.right = True

	def on_click(self, event):
		if (self.right is True):
			#  change color
			self.right = False
		else:
			#  change colro
			self.right = True
		# print (self.right)
		return self.right

	def draw(self, surface):
		if self.right is True:
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

		if self.right is False:
			pygame.draw.rect(surface, GRAY, self.rect)
			font = pygame.font.Font(None, 24)
			label_view = font.render(self.text1, False, BLACK)
			label_pos = label_view.get_rect()
			label_pos.centery = self.rect.centery
			label_pos.centerx = self.rect.centerx
			surface.blit(label_view, label_pos)

			pygame.draw.rect(surface, RED, self.rect2)
			font = pygame.font.Font(None, 24)
			label_view2 = font.render(self.text2, False, BLACK)
			label_pos2 = label_view2.get_rect()
			label_pos2.centery = self.rect2.centery
			label_pos2.centerx = self.rect2.centerx
			surface.blit(label_view2, label_pos2)


pygame.init()
screen = pygame.display.set_mode((1200, 800))

pygame.display.set_caption("Election Data Viewer")
pygame.display.update()

data = model.get_data()
screen_rect = screen.get_rect()
bc = view.BarChart(screen_rect, values=data)

################## display button ##################
button1 = DataChangeButton1("dem", "gop",
	pygame.Rect(screen_rect.width - 100, screen_rect.x + 30, 50, 30))

button2 = DataChangeButton2("raw", "%",
	pygame.Rect(screen_rect.width - 100, screen_rect.x + 120, 50, 30))

button3 = DataChangeButton2("up", "down",
	pygame.Rect(screen_rect.width - 100, screen_rect.x + 210, 50, 30))


# display loop
done = False

party = 'dem'
raw = True
ascend = True
data = model.get_data(party, raw, ascend)


while not done:
	screen.fill(view.BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
		else:
			button1.handle_event(event)
			party = button1.party
			button2.handle_event(event)
			raw = button2.right
			button3.handle_event(event)
			ascend = button3.right

	data = model.get_data(party, raw, ascend)
	# print (type(data))

	bc.set_values(data, 10000000)

	# bc = view.BarChart(screen_rect, values=data)

	bc.draw(screen)
	button1.draw(screen)
	button2.draw(screen)
	button3.draw(screen)
	pygame.display.update()
