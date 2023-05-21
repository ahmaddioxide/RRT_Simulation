import pygame
from RRTbasePy import RRTGraph
from RRTbasePy import RRTMap
import time

def main():
    map_dimensions = (512, 512)
    start_position = (50, 50)
    goal = (400, 400)
    obstacle_dimension = 30
    obstacle_number = 50
    iteration = 0
    t1 = 0

    pygame.init()
    screen = pygame.display.set_mode(map_dimensions)
    map = RRTMap(start_position, goal, map_dimensions, obstacle_dimension, obstacle_number)
    graph = RRTGraph(start_position, goal, map_dimensions, obstacle_dimension, obstacle_number)

    obstacles = graph.makeobs()
    map.drawMap(obstacles)

    t1 = time.time()
    while not graph.path_to_goal():
        time.sleep(0.01)
        elapsed = time.time() - t1
        t1 = time.time()
        # Raise an exception if timeout
        if elapsed > 10:
            print('Timeout. Re-initiating the calculations.')
            raise

        if iteration % 10 == 0:
            X, Y, Parent = graph.bias(goal)
            pygame.draw.circle(map.map, map.grey, (X[-1], Y[-1]), map.nodeRad * 2, 0)
            pygame.draw.line(map.map, map.Blue, (X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]), map.edgeThickness)

        else:
            X, Y, Parent = graph.expand()
            pygame.draw.circle(map.map, map.grey, (X[-1], Y[-1]), map.nodeRad * 2, 0)
            pygame.draw.line(map.map, map.Blue, (X[-1], Y[-1]), (X[Parent[-1]], Y[Parent[-1]]), map.edgeThickness)

        if iteration % 5 == 0:
            pygame.display.flip()
        iteration += 1

    map.drawPath(graph.getPathCoords())
    pygame.display.flip()

    # Add a delay of 2 seconds
    time.sleep(2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                return

if __name__ == '__main__':
    result = False
    while not result:
        try:
            main()
            result = True
        except:
            result = False
