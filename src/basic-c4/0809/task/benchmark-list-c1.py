from datetime import datetime
start_time = datetime.now()

data = []
for i in range(1, 1000000):
    data.append(i)

fin_time = datetime.now()

print(fin_time - start_time)
