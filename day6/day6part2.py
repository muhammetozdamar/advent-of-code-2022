with open("day6\input.txt") as file:
    signal_raw = file.read().strip()
    signal_len = len(signal_raw);
    for i in range(signal_len-3):
        possible_marker = signal_raw[i:i+14]
        x=list(set(possible_marker))
        y=list(possible_marker)
        x.sort()
        y.sort()
        if(x==y):
            print(i+14)
            break
