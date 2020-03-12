import math

import pygame

from algorithms_visualization.colors import COLORS
from algorithms_visualization.core import App


class SortVisualizationApp(App):
    def __init__(self):
        super(SortVisualizationApp, self).__init__()
        self.circle_pos = self.circle_x, self.circle_y = self.width/2, self.height/2

    def draw_circle(self, values_list):
        step = 2 * math.pi/(len(values_list) - 2)
        theta = step

        for value in values_list:
            x = self.circle_x + value * math.cos(theta)
            y = self.circle_y - value * math.sin(theta)
            theta += step

            pygame.draw.line(self._display_surf, COLORS.get('white'), self.circle_pos, (x, y), 2)

    def on_render(self):
        self._display_surf.fill(COLORS['black'])
        self.draw_circle(range(50, 500))
        pygame.display.flip()


class MergeSortApp(SortVisualizationApp):
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

            # self.on_loop()
            self.on_render()
        self.on_cleanup()
