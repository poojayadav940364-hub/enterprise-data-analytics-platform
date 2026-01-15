import matplotlib.pyplot as plt

def plot_protocol_distribution(df):
    """
    Visualize distribution of network protocols
    """
    df['proto'].value_counts().plot(kind='bar')
    plt.title("Protocol Distribution in IoT Network Traffic")
    plt.xlabel("Protocol")
    plt.ylabel("Count")
    plt.show()
