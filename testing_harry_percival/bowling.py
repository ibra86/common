def score_frame(f):
    first, second = f
    return int(first) + int(second)


def score(frames):
    result = 0
    for frame in frames.split():
        result += score_frame(frame)
    return result
    # return sum(
    #     map(
    #         score_frame,
    #         frames.split()
    #     )
    # )
    # if '1' in frames:
    #     return 1
    #
    # return 0
