import matplotlib.pyplot as plt
import pandas as pd

save_path = ""                                  # path to save figures
reg = "cav"                                     # disp (3A) or cav (10A)
fig_name = "V" + reg + "_A_total_marker.png"    #figure name
prop1 = "dA"                                    # data to show


y_label = 'Total Solvent Free Energy ($A_{tot}$' +', '+ ''r'$V_{' + reg + '}$'')'   # title of the figure

diff_label_dist = 7         # distance between label and the top data
n1, n2 = 25, 250            # y_lim
cap_loc = "upper right"     # loc of leg


data_path = ""  # data file
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

# marker information
ashape, bshape = 'o', 'd'
amarkerst, bmarkerst = 'none', 'full'
acolor, bcolor = '#eb7005', '#1f77b4'
ahr_marker_style = dict(marker=ashape, linewidth=2.0, s=100, facecolors=amarkerst, edgecolors=acolor)
bbr_marker_style = dict(marker=bshape, linewidth=0.5, s=100, facecolors=bcolor, edgecolors=bcolor)

# Rigid-Flexible data difference label style
red_style = dict(ha='center', color='red', fontsize=11, weight='bold', rotation=45)
green_style = dict(ha='center', color='green', fontsize=11, weight='bold', rotation=45)

# Creating the plot
fig, ax1 = plt.subplots(figsize=(18, 6))

# Scatter points for A and B, with the x-axis for systems and y-axis for values
ax1.scatter(system_list, Eahr, label='Rigid', zorder=3, **ahr_marker_style)
ax1.scatter(system_list, Ebbr, label='Flexible', zorder=2, **bbr_marker_style)

# ax1.axhline(y=-12.259, color="gray", linestyle="--", label="Bulk")



# Adding connecting lines for each system
for i, sys in enumerate(system_list):
    ax1.plot([system_list[i], system_list[i]], [Ebbr[i], Eahr[i]], 'black', linewidth=0.5, zorder=1)
    mid_point = (Eahr[i] + Ebbr[i]) / 2

    Ediff[i] = "{:.2f}".format(abs(Ediff[i]))
    if Eahr[i] >= Ebbr[i]:
        ax1.text(system_list[i], Eahr[i] + diff_label_dist, Ediff[i], **red_style)
    elif Ebbr[i] >= Eahr[i]:
        ax1.text(system_list[i], Ebbr[i] + diff_label_dist, Ediff[i], **green_style)


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

