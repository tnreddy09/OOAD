from Assignment02.shape import Circle, Rectangle, Square


def sort_shapes(shapes):
    for s in shapes:
        s.set_area()

    shapes = sorted(shapes, key=lambda x: x.area)

    return shapes


if __name__ == '__main__':
    shapes = []
    shapes.append(Circle(3))
    shapes.append(Square(4))
    shapes.append(Rectangle(3, 2))

    # sort all the shapes
    shapes = sort_shapes(shapes)

    print("Hi, We are sorted based on our areas!")

    for s in shapes:
        s.display_shape()
