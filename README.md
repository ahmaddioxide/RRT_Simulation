# RRT Path Planning Algorithm

RRT Path Planning Algorithm
This project implements the Rapidly-Exploring Random Tree (RRT) algorithm for path planning. The RRT algorithm is widely used in robotics and motion planning to find feasible paths for a robot to navigate from a start position to a goal position in a given map with obstacles.

## Demo

![Simulation](https://github.com/ahmaddioxide/RRT_Simulation/assets/75989502/cae77ea9-e275-4253-a63d-1af72571f671)


## Features
Implements the RRT algorithm for path planning.
Provides a graphical map representation using Pygame.
Supports custom map dimensions, start and goal positions, and obstacle configurations.
Visualizes the start position, goal position, obstacles, and the found path.
Allows for easy modification and extension of the algorithm for different scenarios.

## Description
The project consists of two main classes: RRTMap and RRTGraph.

The RRTMap class handles the visualization of the map and uses the Pygame library to create a graphical representation of the map. It allows you to define the map dimensions, start and goal positions, and the number and dimensions of obstacles. The class provides functions to draw the map, including the start and goal positions and the obstacles, as well as the path found by the RRT algorithm.

The RRTGraph class implements the RRT algorithm and represents the graph structure required for exploration. It provides functions for initializing the graph, adding nodes and edges, calculating distances, sampling points in the environment, connecting nodes, and finding the nearest node. The class also includes functions for collision checking with obstacles, expanding the graph, and finding a path from the start to the goal position.

The project includes a main script that demonstrates the usage of the RRT algorithm. It initializes a map, creates an instance of the RRTGraph class, and performs the RRT algorithm to find a path from the start to the goal position. The resulting path is then visualized on the map using the RRTMap class.

## Usage
To use the RRT path planning algorithm, follow these steps:

Initialize a RRTMap object, specifying the map dimensions, start and goal positions, and obstacle configurations.
Create a RRTGraph object, passing the start and goal positions, map dimensions, and obstacle configurations.
Run the RRT algorithm by calling the necessary functions in the RRTGraph class to expand the graph and find a path.
Visualize the map, start and goal positions, obstacles, and the found path using the RRTMap class.
You can customize the map dimensions, start and goal positions, and obstacle configurations to match your specific scenario. The algorithm will explore the map and find a feasible path from the start to the goal position, avoiding obstacles.

## Examples
The project includes examples that demonstrate how to use the RRT path planning algorithm. These examples showcase different map configurations and obstacle layouts, allowing you to see the algorithm in action and understand its behavior in various scenarios.

## Future Enhancements
This project serves as a starting point for implementing and experimenting with the RRT algorithm. Here are some potential future enhancements you can consider:

Implement different variations of the RRT algorithm, such as RRT* or RRT-Connect, to improve path quality and efficiency.
Integrate additional path planning algorithms for comparison and evaluation.
Enhance the visualization by adding interactive controls and real-time updates.
Extend the project to support dynamic obstacles and real-time path adaptation.

## References
Rapidly-Exploring Random Trees (RRT)
[Lavalle, S. M. (1998). Rapidly-exploring random
 
 
