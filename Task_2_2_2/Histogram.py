import numpy as np
import matplotlib.pyplot as plt

# Define the data set
data = np.array([1.056758e+00, 3.318082e+00, 4.679206e-01, 5.256411e-02, 4.851076e+00,
                 3.305760e+00, 2.581244e+00, 4.543890e+00, 2.646524e+00, -8.341800e-01,
                 1.741208e+00, 1.456692e+00, 3.663700e+00, -4.023350e-01, 7.356970e-02,
                 5.096034e+00, 3.140314e+00, 4.446659e+00, 3.445955e-01, 4.140983e+00,
                 2.605912e+00, 4.331365e+00, 5.152833e-01, 4.848759e+00, 2.912395e+00,
                 2.716824e+00, 4.173090e-01, 2.418383e+00, 1.296928e+00, 5.897134e-01,
                -1.558617e+00, 2.417447e+00, 3.109619e+00, 9.974995e-01, 1.296415e+00,
                 3.926677e+00, 2.480073e+00, 2.268261e+00, 1.402753e+00, 4.529485e+00,
                1.687028e+00, 8.323950e-01, 4.650862e+00, -2.572316e-02, 2.631416e+00,
                 2.434791e+00, 3.440645e-01, 3.512072e+00, 1.158222e+00, -9.059330e-01,
                -1.326038e-01, 2.594978e+00, 2.034997e+00, 5.565526e-01, 2.236369e+00,
                 8.793293e-01, 4.011296e+00, 2.404089e+00, 3.118667e+00, 1.427750e+00,
                -7.163665e-02, 2.617395e+00, 3.016632e-01, 2.728523e+00, 1.149039e+00,
                 1.358022e+00, 2.079934e+00, 2.907011e+00, -1.697016e-01, 4.418781e-01,
                 3.818860e-01, 1.486813e+00, 1.413229e+00, 1.846377e+00, 2.538681e+00,
                 6.253344e-01, -1.033849e+00, 1.902263e-01, 2.290648e+00, 2.089263e-01,
                 2.244208e+00, 1.738666e+00, 4.331891e+00, 2.037501e+00, 2.076274e+00,
                 9.649393e-01, 1.828179e+00, 6.133765e-02, 3.126590e+00, 1.664204e+00,
                 2.121098e+00, -2.883550e+00, -5.782144e-01, 7.716635e-01, 2.475823e-01,
                 4.225282e-01, 3.683213e+00, 5.767834e-01, 4.425516e-01, -1.135242e+00,
                -8.380443e-01, 9.475000e-01, -1.016550e+00, 1.776046e+00, 3.413548e+00,
                 6.564890e-03, 3.520610e+00, 8.009465e-01, 2.747771e+00, 3.489225e+00,
                -4.024225e-02, 2.458246e+00, 4.875557e-01, 1.469855e+00, 4.182901e-02,
                 2.867330e+00, 2.748365e+00, 1.082312e+00, -1.320431e+00, 1.649947e+00])

# Create the histogram
plt.hist(data, bins=10)

# Set the axis labels and title
plt.xlabel('Data')
plt.ylabel('Frequency')
plt.title('Histogram')

# Display the plot
plt.show()
