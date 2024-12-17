class Plant:
    def __init__(self, name, position, plot=None):
        self.name = name  # Name of the plant
        self.position = position  # Position as a tuple (x, y)
        self.plot = plot  # Plot number

    def __repr__(self):
        return f"Plant(name={self.name}, position={self.position}, plot={self.plot})"


def load_plants():
    with open('example.txt', 'r') as file:
        array = [list(line.strip()) for line in file if line.strip()]
    plants = []
    for y, row in enumerate(array):
        for x, char in enumerate(row):
            plant = Plant(name=char, position=(x, y))
            plants.append(plant)
    return plants


def create_plots(plants_of_the_same_name):
    def add_neighbors_recursively(plant, current_plot, plants):
        plant.plot = current_plot
        for neighbor in find_neighbors(plant, plants):
            if neighbor.plot is None:
                add_neighbors_recursively(neighbor, current_plot, plants)

    current_plot_id = 1

    for plant in plants_of_the_same_name:
        if plant.plot is None:
            current_plot = f"plot_{current_plot_id}"
            add_neighbors_recursively(plant, current_plot, plants_of_the_same_name)
            current_plot_id += 1


def find_first_filled_plot(plants):
    for plant in plants:
        if plant.plot is not None:
            return plant.plot
    return None


def find_neighbors(plant, plants):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # (x, y) deltas for up, down, left, right
    neighbors = []

    for dx, dy in directions:
        neighbor_position = (plant.position[0] + dx, plant.position[1] + dy)
        for p in plants:
            if p.position == neighbor_position and p.name == plant.name:  # Check both position and name
                neighbors.append(p)
                break  # Stop searching once a match is found
    return neighbors


def find_number_of_neighbors(plant, plants):
    return len(find_neighbors(plant, plants))


def count_corners(group_of_plants, all_plants):
    directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # Skosy
    corners = 0
    position_set = set(positions)  # Optymalizacja dla szybkiego sprawdzania pozycji

    for x, y in positions:
        for dx, dy in directions:
            diagonal_position = (x + dx, y + dy)
            if diagonal_position in position_set:  # Jeśli wierzchołek po skosie jest w grupie, ignorujemy
                continue
            for plant in plants:  # Sprawdź, czy istnieje inna roślina na pozycji po skosie
                if plant.position == diagonal_position and plant.name != group_name:
                    corners += 1
                    break  # Jeśli znalazłeś różną nazwę, przejdź do następnego skosu
    return corners


def part_one():
    plants = load_plants()
    for name in set(plant.name for plant in plants):
        filtered_plants = [plant for plant in plants if plant.name == name]
        create_plots(filtered_plants)
    grouped = {}
    for plant in plants:
        if plant.plot is not None:
            key = (plant.plot, plant.name)
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(plant)
    result = 0
    for key, group in grouped.items():
        area = len(group)
        perimeter = sum(4 - find_number_of_neighbors(plant, plants) for plant in group)
        result += area * perimeter
    print(result)


def positions_to_squares(positions, size):
    return [
        [
            (x - size / 2, y - size / 2),
            (x + size / 2, y - size / 2),
            (x + size / 2, y + size / 2),
            (x - size / 2, y + size / 2),
        ]
        for x, y in positions
    ]


def part_two():
    plants = load_plants()
    for name in set(plant.name for plant in plants):
        filtered_plants = [plant for plant in plants if plant.name == name]
        create_plots(filtered_plants)
    grouped = {}
    for plant in plants:
        if plant.plot is not None:
            key = (plant.plot, plant.name)
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(plant)
    result = 0
    for key, group in grouped.items():
        area = len(group)
        corners = count_corners(group, plants)
        print(area, corners)
        result += area * corners
    print(result)


if __name__ == "__main__":
    # part_one()
    part_two()
