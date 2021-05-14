import pathlib


def wrapp_get_input(inputs_generator):
    def get_input():
        if inputs_generator is None:
            return input().rstrip()
        else:
            try:
                return next(inputs_generator)
            except StopIteration:
                return None
    return get_input


p = pathlib.Path(__file__)
path_to_file = p.parent / "input_data.txt"
if path_to_file.exists():
    with open(path_to_file) as f:
        inputs = f.readlines()

    inputs_generator = iter([i.rstrip() for i in inputs])
    get_input = wrapp_get_input(inputs_generator)
else:
    get_input = wrapp_get_input(None)


if __name__ == "__main__":
    
    for i in get_input():
        print(i)