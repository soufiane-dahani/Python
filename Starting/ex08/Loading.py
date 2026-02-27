import os

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    size = os.get_terminal_size()
    bar_width = size.columns - 40

    for i in lst:
        percent = (i + 1) / total
        filled = int(bar_width * percent)

        bar = "█" * filled + " " * (bar_width - filled)
        progress = int(percent * 100)

        print(
            f"{progress}%|{bar}| {i+1}/{total}"
        , end="\r", flush=True)
        yield i

    print()