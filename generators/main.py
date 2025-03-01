from typing import Iterator, Union

def rng_generator(end: Union[int, None] = None) -> Iterator[int]:
    """
    Number generator.

    :param end: Iteration limit. If None, genaretes infinite sequence of integers starting from 1.
    :return: iterator object that yields integer numbers.
    """
    num = 1
    while True:
        yield num
        num += 1
        if end is not None and num > end:
            break