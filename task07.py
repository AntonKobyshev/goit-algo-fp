import numpy as np
import matplotlib.pyplot as plt

def simulate_dice_rolls_numpy(num_simulations):
    # Використовуємо numpy для генерації кидків кубиків та обчислення суми
    dice_rolls = np.random.randint(1, 7, size=(num_simulations, 2))
    total_sums = np.sum(dice_rolls, axis=1)

    # Використовуємо np.bincount для підрахунку кількості випадінь для кожної суми
    sum_counts = np.bincount(total_sums, minlength=13)[2:]

    # Обчислюємо ймовірності для кожної суми
    probabilities = sum_counts / num_simulations

    return probabilities

def display_probabilities(probabilities):
    print(" Sum    Probability ")
    print("--------------------")
    for sum_val, prob in enumerate(probabilities, start=2):
        print(f"{sum_val:^6d}    {prob:.4f}")

def plot_probabilities(probabilities):
    sums = np.arange(2, 13)

    plt.bar(sums, probabilities, align='center', alpha=0.7)
    plt.xlabel('Sum of Dice')
    plt.ylabel('Probability')
    plt.title('Probabilities of Sum of Two Dice Rolls')
    plt.xticks(sums)

    plt.show()

if __name__ == "__main__":
    num_simulations = 10000000  

    probabilities = simulate_dice_rolls_numpy(num_simulations)

    display_probabilities(probabilities)

    plot_probabilities(probabilities)
