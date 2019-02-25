import pyperclip

INSTAGRAM_LINE_BREAK = ' '*13

def to_instagram_post(text):
    out = ""
    lines = text.splitlines()
    for line in lines:
        line_strip = line.strip()
        if not line: # new empty line
            line_strip = '\n' + INSTAGRAM_LINE_BREAK + '\n'
        out += line_strip
    return out

print(pyperclip.copy(to_instagram_post(pyperclip.paste())))