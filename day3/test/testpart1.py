from day3.src.part1 import solve


def test():
    input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
    assert solve(input.splitlines()) == 4361


def test2():
    input = """......124..................418.......587......770...........672.................564............................438..........512......653....
665/...*......................*599.....*.983......794*..140..*...........@..963*....................445........*......*.........709.....*...
.......246.....581......701..........108....%.532........../.73..699...927............................*....579.354.464..............298..86."""

    assert solve(input.splitlines()) == 10303


def test3():
    input = """..............397.........803...84............627..........704.983..........*................522............................*....541........
.....32....$.....#...643*..............116........./905......*..../...........311......811$.*........*890..........924..670........=....882.
......*.....81.....*.....636.......317...*...................899.............*....*698............626....................-..+..@.......*....
.......877......256.714...................825.........458....................869..............................54............28.823..110....."""

    assert solve(input.splitlines()) == 15849


def test4():
    input = """......2...574%..................#.698...475.....*...........652./...........464.163$...*..338*966.........................../.....534..386.."""

    assert solve(input.splitlines()) == 2041


def test5():
    input = """..................655....*....................795..30...922*.......978...+.&.........539...........-....719.................599.............
......2...574%..................#.698...475.....*...........652./...........464.163$...*..338*966.........................../.....534..386..
......*.......................404..#............747...703........231...-...............................................................*...."""

    assert solve(input.splitlines()) == 8480


def test6():
    input = """.......14........899...845..........*..........+.....46........634........914.....84../...............*.....*780.......878..%36.435.........
542.....*...........$........*833...257..329-.147...........+........150..*......*.......907...........429.........................*....#..."""

    assert solve(input.splitlines()) == 5157


def test7():
    input = """.........*824.............890.......269....893..271*139..645....*...................233...%................428...........*.........79.......
..........................#............*.................@.../...316...844.............*........@439...287*......*974.....182...............
....*.....50.......671+.................267........634*....417............-.598.....531....891................331................358.....341
.883.561..*....428.........../14...742...........@.....654.....809../716.......*456.....=....*........$..............................607....
...........835..*..796*............*..............321......612*.......................299..203....962..431..........277.......40......$.....
......+591.....916.....294.........446..111......................237*77.....&........................-................*...150*....*......873
....%..................................*.....................819............522.................922................738.........214.595..&..."""

    assert solve(input.splitlines()) == 27541