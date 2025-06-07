
def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line.lstrip("# ")

    raise Exception("There must always be a H1 header")
