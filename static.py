import sys
import itertools

# Generator matrix G
G = [
    [1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

def encode_message(message_bits):
    return [
        sum(m * g for m, g in zip(message_bits, col)) % 2
        for col in zip(*G)
    ]

def matches(received, codeword):
    return all(r == 'e' or int(r) == c for r, c in zip(received, codeword))

def decode(received_str):
    if len(received_str) != 8 or any(c not in '01e' for c in received_str):
        return "Error"

    received = list(received_str)
    candidates = []

    for bits in itertools.product([0, 1], repeat=4):
        codeword = encode_message(bits)
        if matches(received, codeword):
            candidates.append(bits)

    if len(candidates) == 1:
        return ''.join(str(b) for b in candidates[0])
    else:
        return "Error"


if __name__ == "__main__":
    inputs = ["100101ee", "e0ee01ee", "01ee1eee", "01eee001"]
    for inp in inputs:
        print(f"{inp} -> {decode(inp)}")
