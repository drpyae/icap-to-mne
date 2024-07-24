import matplotlib.pyplot as plt
import numpy as np

# Data
years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
on_art = np.array([106490, 127402, 146826, 166969, 184624, 199345, 191588, 208480])
viral_load_tested = np.array([9700, 37575, 44048, 89760, 133468, 96911, 40682, 60260])
viral_load_suppressed = np.array([8421, 34678, 38861, 82306, 126167, 93034, 39461, 57763])


# Viusalization of people on ART over the years.
plt.figure(figsize=(10, 6))
plt.plot(years, on_art, marker='o', linestyle='-', color='b', label='People on ART')
plt.xlabel('Year')
plt.ylabel('Number of People on ART')
plt.title('Number of People on ART Over the Years')
plt.grid(True)
plt.legend()
plt.show()

# Calculating metrics
viral_load_testing_coverage = (viral_load_tested / on_art) * 100
viral_load_suppression_percentage = (viral_load_suppressed / viral_load_tested) * 100

# Create a bar chart for 'On ART' and 'Viral Load Tested'
fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar for On ART
bar1 = ax1.bar(years - 0.2, on_art, width=0.4, label='On ART', color='skyblue')
# Bar for Viral Load Tested
bar2 = ax1.bar(years + 0.2, viral_load_tested, width=0.4, label='Viral Load Tested', color='orange')

# Line for Viral Load Testing Coverage
ax2 = ax1.twinx()
line1 = ax2.plot(years, viral_load_testing_coverage, label='Viral Load Testing Coverage (%)', color='darkblue', linewidth=2, marker='o')

# Labels and Legends
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Number of People', fontsize=14)
ax2.set_ylabel('Percentage (%)', fontsize=14)
ax1.set_title('Viral Load Testing and Coverage among PLHIV on ART (2015-2022)', fontsize=16)

# Adding grid
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Adding legends
bars = bar1 + bar2
lines = line1
legend_labels = [bar.get_label() for bar in bars] + [line.get_label() for line in lines]
ax1.legend(tuple(bars) + tuple(lines), legend_labels, loc='upper left')


# Create a secondary plot for Viral Load Suppression
fig, ax3 = plt.subplots(figsize=(14, 8))

# Bar for Viral Load Suppression
bar3 = ax3.bar(years - 0.2, viral_load_suppressed, width=0.4, label='Viral Load Suppression', color='lightgreen')

# Line for Viral Load Suppression Percentage
ax4 = ax3.twinx()
line2 = ax4.plot(years, viral_load_suppression_percentage, label='Viral Load Suppression %', color='darkgreen', linewidth=2, marker='o')

# Labels and Legends
ax3.set_xlabel('Year', fontsize=14)
ax3.set_ylabel('Number of People', fontsize=14)
ax4.set_ylabel('Percentage (%)', fontsize=14)
ax3.set_title('Viral Load Suppression and Suppression % (2015-2022)', fontsize=16)

# Adding grid
ax3.grid(axis='y', linestyle='--', alpha=0.7)

# Adding legends
bars2 = bar3
lines2 = line2
legend_labels2 = [bar.get_label() for bar in bars2] + [line.get_label() for line in lines2]
ax3.legend(tuple(bars2) + tuple(lines2), legend_labels2, loc='upper left')

# Show plot
plt.show()
