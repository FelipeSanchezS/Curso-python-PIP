import matplotlib.pyplot as plt

def generate_pie_char():
    labels =['A','B','C']
    values =[200, 34, 120]
    ##esto genera una imagen    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig('py.png')
    plt.close()