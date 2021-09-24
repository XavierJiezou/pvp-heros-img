import matplotlib.pyplot as plt
import os


def show(root: str = './heros/', cols: int = 10):
    """Show all heros's images

    Args:
        root (str, optional): The path where images saved in. Defaults to './heros/'.
        cols (int, optional): Number of coloumns in picture arrangement.
    """
    plt.rcParams['font.sans-serif'] = ['Microsoft Yahei']
    rows = len(os.listdir(root))//cols+1
    plt.figure(figsize=(rows, cols*1.5))
    for index, name in enumerate(os.listdir(root)):
        plt.subplot(rows, cols, index+1)
        plt.title(name[:-4])
        plt.imshow(plt.imread(os.path.join(root, name)))
        plt.axis('off')
    plt.savefig('demo.jpg', bbox_inches='tight')


if __name__ == '__main__':
    show()
