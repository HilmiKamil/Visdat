import matplotlib.pyplot as plt

# Contoh data
x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 1, 8, 7, 5]

# Membuat scatter plot
plt.scatter(x, y)

# Menambahkan judul dan label sumbu
plt.title('Contoh Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Menampilkan plot
plt.show()
