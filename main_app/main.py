from Multi_Repo_AP_algorithms.main import arithmetic_progression, arithmetic_progression_beyond
from Multi_Repo_AP_generators.main import rng_generator

def main() -> None:
    a, n, d = 2, 5, 3
    nn = 20

    result0 = arithmetic_progression(a, n, d)
    result1 = arithmetic_progression_beyond(a, d)

    [
        print(f'Finite progression:   {next(result0)}', end=', ') if i == 1 else
        print(next(result0), end='.\n') if i == n else
        print(next(result0), end=', ') for i in rng_generator(n)
    ]
    [
        print(f'Infinity progression: {next(result1)}', end=', ') if i == 1 else
        print(next(result1), end='.\n') if i == nn else
        print(next(result1), end=', ') for i in rng_generator(nn)
    ]


if __name__ == "__main__":
    main()