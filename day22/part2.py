from collections import namedtuple
from dataclasses import dataclass
import copy

Cube = namedtuple('Cube', ['x', 'y', 'z'])


@dataclass
class Brick:
    start: Cube
    end: Cube
    brick_id: int


def cubes(brick_id: int) -> list[Cube]:
    brick = bricks[brick_id]
    if brick.start.x != brick.end.x:
        for x in range(min(brick.start.x, brick.end.x), max(brick.start.x, brick.end.x)+1):
            yield (x, brick.start.y, brick.start.z)
    elif brick.start.y != brick.end.y:
        for y in range(min(brick.start.y, brick.end.y), max(brick.start.y, brick.end.y)+1):
            yield (brick.start.x, y, brick.start.z)
    else:
        for z in range(min(brick.start.z, brick.end.z), max(brick.start.z, brick.end.z)+1):
            yield (brick.start.x, brick.start.y, z)


def is_falling(brick: Brick, invisible_brick_id: int = -1) -> bool:
    if brick.brick_id == invisible_brick_id:
        return False
    is_vertical_brick = brick.start.z != brick.end.z
    if is_vertical_brick:
        z = min(brick.start.z, brick.end.z)
        if z == 1:
            return False
        brick_id_below = world.get((brick.start.x, brick.start.y, z-1))
        return brick_id_below in [None, invisible_brick_id]
    else:
        if brick.start.z == 1:
            return False
        for x, y, z in cubes(brick.brick_id):
            brick_id_below = world.get((x, y, z-1))
            if brick_id_below not in [None, invisible_brick_id]:
                return False
        return True


def drop_tick(invisible_brick_id: int = -1) -> set[int]:
    falling_brick_ids = set()
    max_z = max(z for _, _, z in world.keys())
    min_z = 1 if invisible_brick_id == - 1 \
        else max(bricks[invisible_brick_id].start.z, bricks[invisible_brick_id].end.z) + 1

    for z in range(min_z, max_z+1):
        current_bricks = (brick for brick in bricks
                          if brick.start.z == z or brick.end.z == z)
        for brick in current_bricks:
            if not is_falling(brick, invisible_brick_id=invisible_brick_id):
                continue
            falling_brick_ids.add(brick.brick_id)
            for x, y, z in cubes(brick.brick_id):
                del world[(x, y, z)]
                world[(x, y, z-1)] = brick.brick_id
            brick.start = Cube(brick.start.x, brick.start.y, brick.start.z-1)
            brick.end = Cube(brick.end.x, brick.end.y, brick.end.z-1)

    return falling_brick_ids


def drop_until_done():
    while len(drop_tick()) > 0:
        pass


input_data = open('input.txt').read().splitlines()
bricks = []
world = dict()
for line in input_data:
    start, end = line.split('~')
    start = Cube(*[int(coords) for coords in start.split(',')])
    end = Cube(*[int(coords) for coords in end.split(',')])
    brick = Brick(start, end, brick_id=len(bricks))
    bricks.append(brick)
    for x, y, z in cubes(brick.brick_id):
        world[(x, y, z)] = brick.brick_id

drop_until_done()

sum_other_falling_bricks = 0
for brick in bricks:
    world_copy = world.copy()
    bricks_copy = copy.deepcopy(bricks)
    falling_brick_ids = set()
    while True:
        length_before = len(falling_brick_ids)
        falling_brick_ids.update(drop_tick(invisible_brick_id=brick.brick_id))
        if len(falling_brick_ids) == length_before:
            break
    sum_other_falling_bricks += len(falling_brick_ids)
    world = world_copy
    bricks = bricks_copy
print(sum_other_falling_bricks)
