import itertools
import math
def entropy(p, n):
    p2 = itertools.product(*([p for _ in range(n)]))

    s = 0
    for item in p2:
        prob = 1
        for i in item:
            prob *= i
        s += prob * math.log2(1/prob)

    print(s)

def huffman_code(p, n):
    sequences = list(itertools.product(*([[0,1] for _ in range(n)])))

    probs = {}
    for sequence in sequences:
        probs[(sequence,)] = 0.9**(sequence.count(0)) * 0.1**(sequence.count(1))

    codes = {sequence: "" for sequence in sequences}

    while len(probs) > 1:
        smallest_prob = min(probs.values())
        for sequence in probs:
            if probs[sequence] == smallest_prob:
                smallest_key = sequence
                break
        del probs[smallest_key]
        second_smallest_prob = min(probs.values())

        for sequence in probs:
            if probs[sequence] == second_smallest_prob:
                second_smallest_key = sequence
                break
        del probs[second_smallest_key]

        probs[smallest_key + second_smallest_key] = smallest_prob + second_smallest_prob

        for sequence in smallest_key:
            codes[sequence] = "0" + codes[sequence]
        for sequence in second_smallest_key:
            codes[sequence] = "1" + codes[sequence]
    return codes

        
def average_length(p, code):
    expected_lengths = {}
    for sequence in code:
        probability = p[0]**sequence.count(0) * p[1]**sequence.count(1)
        print(sequence, probability)
        expected_lengths[sequence] = len(code[sequence]) * probability

    return sum(expected_lengths.values())


p = [0.6, 0.4]

n = 4
entropy(p, n)
code = huffman_code(p,n)
print(average_length(p, code))
for c in sorted(code.keys(), key=lambda x: x.count(0)):
    print("".join(map(str, c)),":", code[c])


