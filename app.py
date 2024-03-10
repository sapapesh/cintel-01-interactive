import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# Import modules for plot rendering
import seaborn as sns
from palmerpenguins import load_penguins

# Add page options for the overall app.
ui.page_opts(title="Sarah's Shiny App with Plot",fillable=True)

# Create a sidebar with a slider input
with ui.sidebar():
    # Add a slider for specifying the number of bins in the histogram.
    # The ui.input_slider function is called with 5 arguments:
    # 1. A string ID ("selected number of bins") that uniquely identifies this input.
    # 2. A string label ("Number of Bins") to be displayed alongside the slider.
    # 3. An integer representing the minimum number of bins
    # 4. An integer representing the maximum number of bins
    # 5. An integer representing the initial value of the slider
    ui.input_slider("selected_number_of_bins", "Number of Bins", 2, 150, 10)

@render.plot(title="A histogram showing random data distribution")
def draw_histogram():
    # Define the number of points to generate. Use optional type hinting to indicate this is an integer.
    count_of_points: int = 120
    # Set a random seed to ensure reproducibility.
    np.random.seed(54)
    # Generate random data:
    # - np.random.randn(count_of_points) generates 'count_of_points' samples from a standard normal distribution.
    # - Each sample is then scaled by 10 (to increase the spread) and shifted by 25 (to cener the distribution around 50).
    random_data_array = 50 + 5 * np.random.randn(count_of_points)
    # Create a histogram of the random data using matplotlib's hist() function:
    # - The first argument is the data array.
    # - The second argument specifies the number of bins, dynamically set by the input slider's current value.
    # - The 'density' parameter, when True, normalizes the histogram so that the total area under the histogram equals 1.
    plt.hist(random_data_array, input.selected_number_of_bins(), density=True, color="red")

@render.plot(alt="Penguin Data")
def draw_scatterplot():
    penguins = load_penguins()
    sns.scatterplot(
        data=penguins,
        x="flipper_length_mm",
        y="body_mass_g",
        palette=["#FF8C00", "#159090", "#A034F0"],
    )
    plt.xlabel("Flipper Length")
    plt.ylabel("Body Mass")
    plt.title("Flipper Length vs Body Mass")
