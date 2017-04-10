import pygame

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# a class to display a horizontal bar chart in pygame
class BarChart:

	# rect: a pygame.rect encoding size and position
	def __init__(self, rect=pygame.Rect(0,0,600,400), values=[], ticks=5,
		plot_area_width_ratio=0.95, plot_area_height_ratio=0.85, bar_color=GREEN,
		max_val=10000000):

		self.rect = rect
		self.background = BLACK
		self.label_color = WHITE
		self.bar_color = bar_color
		self.ticks = ticks

		# constant ratios for portions of the display
		self.plot_area_width_ratio = plot_area_width_ratio
		self.plot_area_height_ratio = plot_area_height_ratio
		self.label_area_width_ratio = 1.0 - self.plot_area_width_ratio
		self.scale_area_height_ratio = 1.0 - self.plot_area_height_ratio

		self.scale_area = pygame.Rect(
			rect.x + rect.width * self.label_area_width_ratio,
			rect.y + rect.height * self.plot_area_height_ratio,
			rect.width * self.plot_area_width_ratio,
			rect.height * self.scale_area_height_ratio
		)

		self.label_area = pygame.Rect(
			rect.x,
			rect.y,
			rect.width * self.label_area_width_ratio,
			rect.height * self.plot_area_height_ratio
		)

		self.plot_area = pygame.Rect(
			rect.x + self.label_area.width,
			rect.y,
			rect.width * self.plot_area_width_ratio,
			rect.height * self.plot_area_height_ratio
		)

		self.set_values(values, max_val)

	# values: a list of tuples of the form (var_name, value), return the maximum value of the barchart
	def set_values(self, values, max_val):
		self.values = values
		# figure out max value
		max_data = 0
		for v in self.values:
			if v[1] > max_data:
				max_data = v[1]
		if max_data < 1:
			self.max_val = 1
		else:
			self.max_val = max_val if max_val > max_data else max_data

	# update the BarChart.draw() method
	def draw(self, surface):
		self.draw_bars(surface)
		self.draw_labels(surface)
		self.draw_scale(surface)

	def get_bar_height(self):
		return self.plot_area.height / len(self.values)

	def draw_labels(self, surface):
		bar_num = 0
		for v in self.values:
			label_text = v[0]
			font = pygame.font.Font(None, 18)
			label_view = font.render(label_text, False, WHITE)
			label_pos = label_view.get_rect()
			label_pos.centery = self.rect.y + \
				self.get_bar_height() * bar_num + \
				self.get_bar_height() / 2
			label_pos.x = self.rect.x + 10
			surface.blit(label_view, label_pos)
			bar_num += 1

	########## need to use ticks ###########
	def draw_scale(self, surface):
		scale_label_spacing = self.scale_area.width / ( self.ticks )

		for i in range(self.ticks):
			font = pygame.font.Font(None, 24)
			scale_label_view = font.render(str(i * self.max_val / (self.ticks - 1)), False, WHITE)
			scale_label_pos = scale_label_view.get_rect()
			scale_label_pos.y = self.scale_area.y + 10
			scale_label_pos.x = self.scale_area.x + \
				i * scale_label_spacing
			surface.blit(scale_label_view, scale_label_pos)

	########## draw bar, need to use bar_color ###################
	def draw_bars(self, surface):
		bar_num = 0
		for v in self.values:
			bar_length = self.plot_area.width / self.ticks * (self.ticks - 1) * v[1] / self.max_val
			b = Bar(self.bar_color,
				bar_length,
				self.plot_area.height / len(self.values))
			y_pos = self.plot_area.y + bar_num * b.height
			bar_num += 1
			b.draw(surface, self.plot_area.x, y_pos)


class Bar:
	def __init__(self, color, length, height, padding=0.1):
		self.length = length
		self.color = color
		self.height = height
		self.padding = padding

	def draw(self, surface, x, y):
		padding_height = self.height * self.padding
		adjusted_height = self.height - 2 * padding_height
		pygame.draw.rect(surface, self.color, [x, y + padding_height, self.length, adjusted_height])


# SELF-TESTING MAIN
if __name__ == "__main__":

	pygame.init()

	screen = pygame.display.set_mode((1000,700))

	pygame.display.set_caption("Bar Chart Test")
	pygame.display.update()

	data =	[
			("apples", 6),
			("bananas", 7),
			("grapes", 4),
			("pineapple", 1),
			("cherries", 15)
			]

	# display using default values
	bc = BarChart(values=data)

	data2 = [
			('Jenny', 80),
			('Stanley', 90),
			('Timothy', 92)
			]

	# override all of the defaults
	bc2 = BarChart(
		rect=pygame.Rect(0,400,800,150),
		values=data2,
		ticks=5,
		plot_area_width_ratio=0.85,
		plot_area_height_ratio=0.9,
		bar_color=RED,
		max_val=100
		)

	# display loop
	done = False
	while not done:
		screen.fill(BLACK)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		bc.draw(screen)
		bc2.draw(screen)
		pygame.display.update()
