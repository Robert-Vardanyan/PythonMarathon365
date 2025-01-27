import matplotlib.pyplot as plt
import numpy as np

def generate_fibonacci_sequence(n):
    """
    Generate a Fibonacci sequence of length n.

    Parameters:
    n (int): Number of terms in the Fibonacci sequence.

    Returns:
    list: The Fibonacci sequence as a list of integers.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def visualize_fibonacci_spiral(sequence):
    """
    Visualize the Fibonacci sequence as a spiral.

    Parameters:
    sequence (list): The Fibonacci sequence to visualize.
    """
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, polar=True)

    # Normalize the Fibonacci sequence to use as radii
    radii = np.array(sequence[1:], dtype=float)  # Exclude the first term (0)
    radii = radii / max(radii) if len(radii) > 0 else []

    # Generate angles for the spiral
    angles = np.linspace(0, 4 * np.pi, len(radii))  # 4 * pi for multiple rotations

    # Plot the spiral
    ax.plot(angles, radii, linestyle='-', marker='o', color='blue', label='Fibonacci Spiral')
    ax.set_title('Fibonacci Sequence Spiral', va='bottom')
    ax.legend()
    plt.show()

def main():
    print("Welcome to the Fibonacci Sequence Generator and Spiral Visualizer!")
    while True:
        try:
            n = int(input("Enter the number of Fibonacci terms to generate: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue

            sequence = generate_fibonacci_sequence(n)
            print("Generated Fibonacci Sequence:", sequence)
            visualize_fibonacci_spiral(sequence)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
