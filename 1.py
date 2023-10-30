import random
import time
import matplotlib.pyplot as plt


sizes = []
times = []


for size in range(1000, 101000, 1000):

start = time.time()

r = [random.randint(1, 100) for _ in range(size)]

end = time.time()
c = end - start


sizes.append(size)
times.append(c)


plt.figure(figsize=(10, 6))
plt.plot(sizes, times, marker='o', linestyle='-')
plt.title('Зависимость времени создания списка от его размера')
plt.xlabel('Размер списка')
plt.ylabel('Время создания (секунды)')
plt.grid(True)


plt.show()