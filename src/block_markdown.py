

def markdown_to_blocks(raw_markdown):
    md_blocks = []
    new_block = []
    for line in raw_markdown.splitlines():
        if line == "":
            if len(new_block) > 0:
                md_blocks.append('\n'.join(new_block))
            new_block = []
        else:
            new_block.append(line)
    md_blocks.append('\n'.join(new_block))
    return md_blocks


