import pandas as pd
import matplotlib.pyplot as plt

# Read data from Excel file into a pandas DataFrame
data = pd.read_excel('C:/Users/Legion/Desktop/tankX/100000Bto10kTimes.xlsx', header=None, names=['y'])

# Create an 'x' column as the index of the DataFrame
data['x'] = data.index

# Apply moving average to smooth the data
window_size = 100  # Adjust the window size as needed
smoothed_data = data['y'].rolling(window=window_size, min_periods=1).mean()

# Set y-axis limits
plt.ylim(0.0, 0.04)

# Plot the smoothed data
plt.plot(data['x'], smoothed_data)
plt.xlabel('Sent message number')
plt.ylabel('Delay (s)')
plt.title('100k Bytes of Message Sent 10k Times')
plt.show()
