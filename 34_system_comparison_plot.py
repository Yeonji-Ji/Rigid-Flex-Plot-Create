import matplotlib.pyplot as plt
import pandas as pd

save_path = ""
reg = "cav"
fig_name = "V" + reg + "_number_of_water.png"
prop1 = "water"
# prop2 = "Nww/water"

y_label = 'Number of water molecules ('r'$V_{' + reg + '}$'')'

diff_label_dist = 5
n1, n2 = 25, 320
cap_loc = "upper left"


data_path = ""
df = pd.read_csv(data_path)

system_list = []
Eahr = []
Ebbr = []
Ediff = []

sorted_indices = (df["Unnamed: 0"]).argsort()

Ediff_sort_idx = df.index[sorted_indices].tolist()

for idx in Ediff_sort_idx:
    if df.loc[idx, "Unnamed: 0"] != "Average":
        system_list.append(df.loc[idx, "Unnamed: 0"].upper())
        Eahr.append(df.loc[idx, prop1+" (ahr)"])
        Ebbr.append(df.loc[idx, prop1+" (bbr)"])
        Ediff.append(round(df.loc[idx, prop1+" diff (ahr - bbr)"], 2))
        # Ediff.append(round((df.loc[idx, prop1+" (ahr)"] + df.loc[idx, prop2+" (ahr)"]) - (df.loc[idx, prop1+" (bbr)"] + df.loc[idx, prop2+" (bbr)"]), 2))

# Creating the plot
fig, ax1 = plt.subplots(figsize=(18, 6))

# Scatter points for A and B, with the x-axis for systems and y-axis for values
ax1.scatter(system_list, Eahr, color='#EB7016', label='Rigid', s=100, marker='o', zorder=3)
ax1.scatter(system_list, Ebbr, color='#2077B4', label='Flexible', s=100, marker='D', zorder=2)

# ax1.axhline(y=-12.259, color="gray", linestyle="--", label="Bulk")


# Adding connecting lines for each system
for i, sys in enumerate(system_list):
    ax1.plot([system_list[i], system_list[i]], [Ebbr[i], Eahr[i]], 'black', linewidth=1, zorder=1)
    mid_point = (Eahr[i] + Ebbr[i]) / 2

    Ediff[i] = "{:.2f}".format(abs(Ediff[i]))
    if Eahr[i] >= Ebbr[i]:
        ax1.text(system_list[i], Eahr[i] + diff_label_dist, Ediff[i], ha='center', color='red', fontsize=11, weight='bold', rotation=45)
    elif Ebbr[i] >= Eahr[i]:
        ax1.text(system_list[i], Ebbr[i] + diff_label_dist, Ediff[i], ha='center', color='green', fontsize=11, weight='bold', rotation=45)


# Labeling and styling
ax1.set_xticks(system_list)
ax1.set_xticklabels(system_list, rotation=45, fontsize=15)
ax1.set_ylabel(y_label, fontsize=15)
ax1.set_ylim([n1, n2])

ax1.legend(prop={'size': 16}, loc=cap_loc, ncol=3)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
ax1.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.savefig(save_path + fig_name, dpi=200)
plt.show()

