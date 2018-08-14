aho = [
    "アホ" if i % 3 == 0 else "アホ"
            if "3" in str(i) else str(i)
    for i in range(1, 41)]

print(aho)
