import sys


def read_input_from_file(path):
    with open(path) as f:
        lines = [l.strip() for l in f]
        return read_input_from_data(lines)


def read_input_from_stdin(_):
    lines = [l.strip() for l in sys.stdin]
    return read_input_from_data(lines)


def read_input_from_data(lines):
    assert len(lines) > 0
    lines = [int(l) for l in lines if l]
    n_pos = 0
    groups = []
    while n_pos < len(lines):
        n = lines[n_pos]
        grp_begin = n_pos + 1
        grp = lines[grp_begin: grp_begin + n]
        groups.append(grp)
        n_pos = grp_begin + n
    return groups


read_func_map = {
    "stdin": read_input_from_stdin,
    "file": read_input_from_file,
}


def main(input_path, read_from="stdin"):
    groups = read_func_map[read_from](input_path)
    output = [sorted(set(grp)) for grp in groups]
    print('\n'.join([str(i) for g in output for i in g]))


if __name__ == "__main__":
    groups = read_input_from_stdin(0)
    # groups = read_input_from_file("input.txt")
    output = [sorted(set(grp)) for grp in groups]
    print('\n'.join([str(i) for g in output for i in g]))
    # import fire
    # fire.Fire(main)
