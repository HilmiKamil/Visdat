import matplotlib.pyplot as plt

labels = 'Cyber Security', 'Software Engineering', 'Data Engineering', 'Network Engineering'
sizes = [35, 30, 25, 10]

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')


plt.title("Distribusi Jumlah Peminatan Teknik Informatika STT NF\n Muhamad Hilmi Kamil (0110223293)\nProdi : Teknik Informatika | Peminatan : Software Engineering", 
        fontsize=10, fontweight='bold')

plt.show()
