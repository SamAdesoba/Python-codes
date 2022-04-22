import math


def get_vertex():
    x = float(input("x"))
    y = float(input("y"))
    return x, y


def get_distance():
    print("First point")
    x1, y1 = get_vertex()
    print("Second point")
    x2, y2 = get_vertex()
    print("third point")
    x3, y3 = get_vertex()
    return x1, x2, x3, y1, y2, y3


def euclidean_distance(x1, x2, y1, y2):
    """This call the distance between two points"""
    return math.sqrt(((y2 - y1) ** 2) + ((x2 - x1) ** 2))


def pythagoras_hyp(x1, x2, x3, y1, y2, y3):
    """This calculates the hypotenuse of a right-angled triangle"""
    side_1 = euclidean_distance(x1, x2, y1, y2)
    side_2 = euclidean_distance(x1, x3, y1, y3)
    hyp = math.sqrt(side_1 ** 2 + side_2 ** 2)
    return hyp


hyp = int(pythagoras_hyp(1, 6, 9, 1, 5, 9))
print("the hypotenus is ", hyp)


def change_liat_value(lst: list) -> None:
    lst[0] = 100


a = [1, 2, 3, 4, 5, 6]
change_liat_value(a)
print(a)


