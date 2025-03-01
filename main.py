from generators.main import rng_generator

def arithmetic_progression(a, n, d):
    yield from (a + (n - 1) * d for n in rng_generator(n))

def arithmetic_progression_beyond(a, d):
    yield from (a + n * d for n in rng_generator('inf'))