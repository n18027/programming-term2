from datetime import datetime

start_time = datetime.now()

date = list(map(lambda x: x, range(1, 1000000)))

fin_time = datetime.now()

print(fin_time - start_time)
