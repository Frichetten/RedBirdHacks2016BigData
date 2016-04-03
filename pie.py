import matplotlib.pyplot as plt

labels = 'Failure To Pay Attention', 'Speeding', 'Alcohol', 'Failure to Keep Right of Center', 'Failure To Yield r.o.w', 'Running Off Road', 'Asleep at Wheel', 'Physical/Mental Difficulty', 'Failure To Obey Traffic Signal', 'Other'
sizes = [39, 27, 20, 15, 12, 8, 7, 6, 6, 15]
colors = ['red', 'orange', 'yellow', 'pink', 'purple', 'blue', 'green', 'gold', 'silver', 'grey']
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)
  
plt.axis('equal')
plt.show()
