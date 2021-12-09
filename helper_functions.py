def input_data(input_file):
    with open(input_file, encoding='utf-8', mode="r") as f:
        return f.read().strip().split('\n')
