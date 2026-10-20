import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("week3_logistics_dataset.csv")

print("Total shipments:", len(df))
print("On-time delivery rate (%):", (df["On_Time"].eq("Yes").mean() * 100).round(2))
print("Average delivery days:", df["Delivery_Days"].mean().round(2))
print("Average shipping cost:", df["Shipping_Cost_INR"].mean().round(2))

# Compare delivery time by transport mode
df.groupby("Transport_Mode")["Delivery_Days"].mean().sort_values().plot(kind="bar")
plt.title("Average Delivery Time by Transport Mode")
plt.xlabel("Transport Mode")
plt.ylabel("Average Delivery Days")
plt.tight_layout()
plt.show()

# Compare cost by transport mode
df.groupby("Transport_Mode")["Shipping_Cost_INR"].mean().sort_values().plot(kind="bar")
plt.title("Average Shipping Cost by Transport Mode")
plt.xlabel("Transport Mode")
plt.ylabel("Average Shipping Cost (INR)")
plt.tight_layout()
plt.show()

# On-time performance by region
(df.groupby("Region")["On_Time"].apply(lambda x: x.eq("Yes").mean() * 100)
 .sort_values().plot(kind="bar"))
plt.title("On-Time Delivery Rate by Region")
plt.xlabel("Region")
plt.ylabel("On-Time Delivery (%)")
plt.tight_layout()
plt.show()

# Delay versus customer satisfaction
plt.scatter(df["Delay_Days"], df["Customer_Satisfaction_1_to_5"], alpha=0.6)
plt.title("Delivery Delay vs Customer Satisfaction")
plt.xlabel("Delay (days)")
plt.ylabel("Customer Satisfaction (1-5)")
plt.tight_layout()
plt.show()
