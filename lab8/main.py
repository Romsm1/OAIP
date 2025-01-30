from nearby import nearby
def main():
    data = [
        ("abc", 123, "zxc"),
        ("sdf", 456, "nmb"),
        ("yui", 987, "plk")
    ]
    soted_data = sorted(data, key=lambda x: (x[2], -x[1], len(x[0]), -x[1]))
    print(soted_data)


    text = "Expanding the space available for living"
    words = text.split()
    max_len = max(map(len, words))
    result = list(map(lambda word: "*" * (max_len - len(word)) + word, words))

    print("\n".join(result))

    data1 = ["100100011", "0001100001", "100001001", "1110010111"]
    print(*nearby(data1, places=4), sep="\n")

if __name__ == '__main__':
    main()