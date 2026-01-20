def save_result(text, filename="output/results.txt"):
    with open(filename, "a") as f:
        f.write(text + "\n")
