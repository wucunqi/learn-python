import math

# 计算点积，同维度乘积之和
def get_dot(vec_a, vec_b):
    if len(vec_a) != len(vec_b):
        raise ValueError('vec_a and vec_b must have same length')

    dot_sum = 0
    for a, b in zip(vec_a, vec_b):
        dot_sum += a * b

    return dot_sum

# 计算模长
def get_norm(vec):
    sum_square = 0
    for v in vec:
        sum_square += v * v
    return math.sqrt(sum_square)

def cosine_similarity(vec_a, vec_b):
    return get_dot(vec_a, vec_b) / (get_norm(vec_a) * get_norm(vec_b))

if __name__ == '__main__':
    vec_a = [0.5, 0.5]
    vec_b = [0.7, 0.7]
    print(cosine_similarity(vec_a, vec_b))