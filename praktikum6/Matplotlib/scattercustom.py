import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 1, 8, 7, 5]
warna = ['red', 'blue', 'green', 'orange', 'purple', 'brown']
ukuran = [50, 100, 200, 80, 60, 120]

plt.scatter(x, y, c=warna, s=ukuran, alpha=0.7, edgecolors='black')
plt.title('Kustomisasi Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid(True)
plt.show()
