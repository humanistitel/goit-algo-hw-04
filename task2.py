import turtle
import math


def koch_segment(t: turtle.Turtle, length: float, level: int) -> None:
    """Draw a single Koch curve segment recursively."""
    if level == 0:
        t.forward(length)
        return

    length /= 3
    koch_segment(t, length, level - 1)
    t.left(60)
    koch_segment(t, length, level - 1)
    t.right(120)
    koch_segment(t, length, level - 1)
    t.left(60)
    koch_segment(t, length, level - 1)


def draw_koch_snowflake(level: int, size: float = 300) -> None:
    """Draw a Koch snowflake with the given recursion level."""
    screen = turtle.Screen()
    screen.title(f"Koch Snowflake — Level {level}")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()

    # Position the turtle so the snowflake is centered
    t.goto(-size / 2, size / (2 * math.sqrt(3)))
    t.pendown()
    t.pencolor("blue")

    for _ in range(3):
        koch_segment(t, size, level)
        t.right(120)

    t.hideturtle()
    screen.mainloop()


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
