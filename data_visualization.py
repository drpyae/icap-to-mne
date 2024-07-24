import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
on_art = np.array([106490, 127402, 146826, 166969, 184624, 199345, 191588, 208480])
viral_load_tested = np.array([9700, 37575, 44048, 89760, 133468, 96911, 40682, 60260])
viral_load_suppressed = np.array([8421, 34678, 38861, 82306, 126167, 93034, 39461, 57763])

# Calculate viral load tested among those on ART
viral_load_tested_among_art = (viral_load_tested / on_art) * 100

# Calculate viral load suppressed percentage among those tested
percentage_suppressed = (viral_load_suppressed / viral_load_tested) * 100

# Create figure and axes
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot on_art
ax1.plot(years, on_art, 'b-o', label='People on ART')
ax1.set_xlabel('Year')
ax1.set_ylabel('People on ART', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Create a second y-axis to plot viral_load_tested and viral_load_suppressed
ax2 = ax1.twinx()
ax2.plot(years, viral_load_tested, 'g-s', label='Viral Load Tested', linestyle='--')
ax2.plot(years, viral_load_suppressed, 'r-d', label='Viral Load Suppressed', linestyle='--')
ax2.set_ylabel('Viral Loads', color='g')
ax2.tick_params(axis='y', labelcolor='g')

# Create a third y-axis for percentages (requires manual scaling)
ax3 = ax1.twinx()
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(years, viral_load_tested_among_art, 'm-x', label='Viral Load Tested % among ART', linestyle=':')
ax3.plot(years, percentage_suppressed, 'c-^', label='Viral Load Suppressed %', linestyle=':')
ax3.set_ylabel('Percentage', color='m')
ax3.tick_params(axis='y', labelcolor='m')

# Adding legends and title
fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')

plt.title('Data Visualization of ART, Viral Load Testing, and Suppression')
plt.grid(True)
plt.show()
