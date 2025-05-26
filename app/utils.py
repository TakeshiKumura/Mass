from typing import List, Tuple
import math

def is_primitive(a: int, b: int, c: int) -> bool:
    return math.gcd(a, b) == 1 and math.gcd(b, c) == 1 and math.gcd(a, c) == 1

def generate_primitive_pythagorean_triples(limit: int) -> List[Tuple[int, int, int]]:
    triples = []
    for m in range(2, int(limit ** 0.5) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                if c <= limit:
                    triple = tuple(sorted((a, b, c)))
                    triples.append(triple)
    return triples
