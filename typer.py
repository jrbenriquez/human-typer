import time
from human_typer import Human_typer

My_Typer = Human_typer(keyboard_layout="qwerty", average_cpm=1000)

text = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

print("Switch to the application and focus on the field you want to paste on")
delay = 5
print(f"In {delay}....")
for i in range(delay):
    print(delay - 1 - i)
    time.sleep(1)

My_Typer.keyboard_type(text)
