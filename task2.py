import math
import matplotlib.pyplot as plt


def koch_points(x1: float, y1: float, x2: float, y2: float, level: int, points: list) -> None:
    """Recursively compute all line-segment endpoints for one Koch edge."""
    if level == 0:
        points.append((x2, y2))
        return

    # Divide segment into thirds
    dx = (x2 - x1) / 3
    dy = (y2 - y1) / 3

    ax, ay = x1 + dx, y1 + dy          # 1/3 point
    bx, by = x1 + 2 * dx, y1 + 2 * dy  # 2/3 point

    # Peak of the equilateral triangle
    px = ax + (bx - ax) * math.cos(math.radians(60)) - (by - ay) * math.sin(math.radians(60))
    py = ay + (bx - ax) * math.sin(math.radians(60)) + (by - ay) * math.cos(math.radians(60))

    koch_points(x1, y1, ax, ay, level - 1, points)
    koch_points(ax, ay, px, py, level - 1, points)
    koch_points(px, py, bx, by, level - 1, points)
    koch_points(bx, by, x2, y2, level - 1, points)


def draw_koch_snowflake(level: int) -> None:
    """Draw a Koch snowflake with the given recursion level using matplotlib."""
    # Equilateral triangle vertices (pointing up, centred at origin)
    r = 1.0
    vertices = [
        (r * math.cos(math.radians(90 + i * 120)),
         r * math.sin(math.radians(90 + i * 120)))
        for i in range(3)
    ]

    all_x, all_y = [], []
    for i in range(3):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % 3]
        all_x.append(x1)
        all_y.append(y1)
        pts: list = []
        koch_points(x1, y1, x2, y2, level, pts)
        for px, py in pts:
            all_x.append(px)
            all_y.append(py)

    # Close the shape
    all_x.append(all_x[0])
    all_y.append(all_y[0])

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.plot(all_x, all_y, color="royalblue", linewidth=0.8)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(f"Koch Snowflake — Level {level}", fontsize=14)
    plt.tight_layout()
    plt.show()


def get_recursion_level() -> int:
    while True:
        try:
            level = int(input("Enter the recursion level (0 or more): "))
            if level < 0:
                print("Level must be 0 or greater.")
            else:
                return level
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    level = get_recursion_level()
    draw_koch_snowflake(level)
