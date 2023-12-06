# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import norm
from sklearn.mixture import GaussianMixture

# Importing data from CSV files
df_arr = pd.read_csv('AEP-arrivals-cleaned.csv')
df_dept = pd.read_csv('AEP-departures-cleaned.csv')

# Converting 'Scheduled Arrival' and 'Scheduled Departure' to datetime format
df_arr['Scheduled Arrival'] = pd.to_datetime(df_arr['Scheduled Arrival'])
df_dept['Scheduled Departure'] = pd.to_datetime(df_dept['Scheduled Departure'])

# Extracting the hour from 'Scheduled Arrival' and 'Scheduled Departure'
df_arr['Hour'] = df_arr['Scheduled Arrival'].dt.hour
df_dept['Hour'] = df_dept['Scheduled Departure'].dt.hour

# Concatenating the 'Hour' columns from both dataframes
df = pd.concat([df_arr['Hour'], df_dept['Hour']])

# Plotting the histogram of the data
plt.hist(df, bins=24, density=True, alpha=0.5, color='gray', label='Data')

# Fitting a normal distribution to the data
mu, std = norm.fit(df)

# Creating a range of x values from the minimum to the maximum of the data
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)

# Calculating the PDF of the normal distribution
p = norm.pdf(x, mu, std)

# Plotting the PDF of the normal distribution
plt.plot(x, p, 'k', label='Normal PDF', color="black")

# Reshaping the data to fit the Gaussian Mixture Model (GMM)
data = df.values.reshape(-1,1)

# Fitting a bimodal distribution to the data using GMM
gmm_bimodal = GaussianMixture(n_components=2)
gmm_bimodal.fit(data)

# Getting the parameters of the bimodal distribution
weights = gmm_bimodal.weights_
means = gmm_bimodal.means_
covariances = gmm_bimodal.covariances_

# Creating a range of x values from the minimum to the maximum of the data
x = np.linspace(df.min(), df.max(), 1000)

# Calculating the PDF of the bimodal distribution
pdf = np.zeros_like(x)
for i in range(gmm_bimodal.n_components):
    pdf += weights[i] * norm.pdf(x, means[i, 0], np.sqrt(covariances[i, 0]))

# Plotting the PDF of the bimodal distribution
plt.plot(x, pdf, label='Bimodal PDF', color="royalblue")

# Fitting a trimodal distribution to the data using GMM
gmm_trimodal = GaussianMixture(n_components=3)
gmm_trimodal.fit(data)

# Getting the parameters of the trimodal distribution
weights = gmm_trimodal.weights_
means = gmm_trimodal.means_
covariances = gmm_trimodal.covariances_

# from the minimum to the maximum of the data
x = np.linspace(df.min(), df.max(), 1000)

# Calculating the PDF of the trimodal distribution
pdf = np.zeros_like(x)
for i in range(gmm_trimodal.n_components):
    pdf += weights[i] * norm.pdf(x, means[i, 0], np.sqrt(covariances[i, 0]))

# Plotting the PDF of the trimodal distribution
plt.plot(x, pdf, label='Trimodal PDF', color="salmon")

# Displaying the legend and showing the plot
plt.legend()
plt.show()