import matplotlib.pyplot as plt

def plot_strategy(p, t):
    l = list(range(1, len(p) + 1))
    c = []
    
    for x in p:
        if x[1] == 'Soft':
            c.append('red')
        elif x[1] == 'Medium':
            c.append('gold')
        else:
            c.append('whitesmoke')
            
    plt.figure(figsize=(12, 2))
    plt.bar(l, [1] * len(l), color=c, edgecolor='black')
    plt.title(f"Optimal Strategy - {t:.2f}s")
    plt.xlim(0, len(l) + 1)
    plt.yticks([])
    plt.xticks(l, ["" if i % 5 != 0 else str(i) for i in l])
    plt.show()