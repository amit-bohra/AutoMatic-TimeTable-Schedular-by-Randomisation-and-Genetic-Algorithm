# Timetable with GUI and Scroll

## Introduction

This project is a Python script that generates a timetable for various subjects, teachers, and batches using genetic algorithms. It then displays the generated timetable using a GUI built with Tkinter. The GUI includes a scrollable interface to easily navigate through the timetable.

## Installation and Requirements

### Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- time (standard library)
- random (standard library)

### Installation

1. Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

2. Clone this repository or download the script directly.

3. No additional packages need to be installed as all required modules are part of the Python standard library.

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory where `timetable with gui and scroll.py` is located.

3. Run the script using Python:

    ```bash
    python timetable\ with\ gui\ and\ scroll.py
    ```

4. The script will generate a timetable and display it in a GUI window. You can scroll through the timetable using the provided scrollbar.

### Key Functions

- **subjectlistnew(total_subject_list)**: Sorts the subjects based on the number of batches.
- **cgen()**: Generates a random chromosome for the genetic algorithm.
- **crossover(chrome1, chrome2)**: Performs crossover between two chromosomes.
- **mutate(chrome, vales)**: Mutates a given chromosome.
- **fitness(chrome)**: Calculates the fitness score of a given chromosome.
- **afterfitness(chrome)**: Updates the relevant data structures after a chromosome passes the fitness test.
- **working()**: Main function that orchestrates the timetable generation using genetic algorithms.
- **populate(frame)**: Populates the Tkinter frame with the timetable data.
- **onFrameConfigure(canvas)**: Configures the scroll region for the Tkinter canvas.

### GUI Elements

- The GUI is created using Tkinter, with a canvas and scrollbar to allow for easy navigation through the timetable.
- Each cell in the timetable is color-coded for better visualization.

## Notes

- The script uses a genetic algorithm to generate the timetable, which involves creating a population, evaluating fitness, performing crossover, and mutating individuals.
- The timetable is displayed in a scrollable Tkinter GUI, making it easy to navigate
