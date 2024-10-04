import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import glob

vol_range = np.arange(3.0, 10.5, 0.5)

data_path = ""
data_list = sorted(glob.glob(data_path))

outpath = ""


def generate_plot(num_of_sys, ahr_dic, bbr_dic, title, filename, unit=None, line=None):

    num_rows = 7
    num_cols = 5
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(10, 12), sharex=True)
    # fig, axs = plt.subplots(num_rows, num_cols, figsize=(18, 6), sharex=True)
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.15, top=0.8, wspace=0.1, hspace=0.4)

    ###### marker information
    markersize = 6
    alpha_n = 0.7
    ashape, bshape = 'o', 'd'
    amarkerst, bmarkerst = 'none', 'full'
    acolor, bcolor = '#eb7005', '#1f77b4'

    ahr_marker_style = dict(marker = ashape, markersize = markersize, fillstyle = amarkerst, color = acolor, alpha = alpha_n)
    bbr_marker_style = dict(marker=bshape, markersize=markersize, fillstyle=bmarkerst, color=bcolor, alpha=alpha_n)
    ahr_leg_style = dict(color=acolor, marker=ashape, fillstyle=amarkerst, lw=2, label='Rigid')
    bbr_leg_style = dict(color=bcolor, marker=bshape, fillstyle=bmarkerst, lw=2, label='Flexible')
    ########################

    plot_pairs = [(i, j) for i in range(num_rows) for j in range(num_cols)]
    system_plot_num = {}
    for i in range(num_of_sys):
        system_plot_num[list(ahr_dic.keys())[i]] = plot_pairs[i]

    max_list = []
    min_list = []
    for key, ahr_values in ahr_dic.items():
        bbr_values = bbr_dic[key]
        all_values = list(ahr_values) + list(bbr_values)
        max_val, min_val = max(all_values), min(all_values)
        max_list.append(max_val)
        min_list.append(min_val)



    for key, ahr_values in ahr_dic.items():
        row = system_plot_num[key][0]
        col = system_plot_num[key][1]
        bbr_values = bbr_dic[key]

        axs[row, col].plot(vol_range, ahr_values, **ahr_marker_style)
        axs[row, col].plot(vol_range, bbr_values, **bbr_marker_style)
        axs[row, col].set_xticks(np.arange(3.0, 10.1, 1.0))
        axs[row, col].xaxis.set_tick_params(labelsize=6)
        axs[row, col].grid(color='gray', alpha=0.2)

        if line:
            axs[row, col].axhline(y=line, color="grey", linestyle=":", label="bulk")

        axs[row, col].yaxis.set_tick_params(labelsize=5)
        # axs[row, col].set_xlabel("Volume", fontsize=7)
        axs[row, col].set_title(key, fontsize=8)
        if row == 6:
            axs[row, col].set_xlabel("Sub-volume distance $(\AA)$", fontsize=7)
        # axs[row, col].set_ylim(min_tick - dev, max_tick + dev)      ### for the same y range

    if isinstance(axs, np.ndarray):
        axs = axs.flatten()

    for p, ax in enumerate(axs):
        if p in [34, 35]:
            ax.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False,
                           labelbottom=False, labeltop=False, labelleft=False, labelright=False)

    legend_elements = [
        plt.Line2D([0], [0], **ahr_leg_style),
        plt.Line2D([0], [0], **bbr_leg_style),
        # plt.Line2D([0], [0], color="#ba0615", lw=2, label="bulk")
    ]
    # fig.legend(handles=legend_elements, loc='lower right', bbox_to_anchor=(0.985, 0.08), fontsize=15)
    fig.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(0.985, 0.996), ncol=2, fontsize=11)
    fig.suptitle(title, fontsize=14, y=0.985, x=0.03, ha='left', va='top')


    # if unit:
    #     plt.suptitle(title + " " + unit, fontsize=14, y=0.985, x=0.3)
    # else:
    #     plt.suptitle(title, fontsize=14, loc='left')
    # plt.title(title, fontsize=14, loc='left')
    plt.tight_layout()
    # plt.savefig(outpath + title + "_same_y_range.png")
    plt.savefig(outpath + filename + ".pdf", dpi=300)
    plt.show()

    return



def read_data(data_list, data_type):
    ahr_dic = {}
    bbr_dic = {}
    for data in data_list:
        system = data.split("/")[-1].split("_")[0].upper()
        df = pd.read_csv(data, index_col="Unnamed: 0")
        ahr_type, bbr_type = data_type + " (ahr)", data_type + " (bbr)"
        if data_type not in ["dTStot", "dTS/water", "dTStrans", "dTStrans/water", "dTSorient", "dTSorient/water"]:
            ahr_data, bbr_data = list(df.loc[:, ahr_type]), list(df.loc[:, bbr_type])
        elif data_type in ["dTStot", "dTS/water", "dTStrans", "dTStrans/water", "dTSorient", "dTSorient/water"]:
            ahr_data, bbr_data = list((-1)*df.loc[:, ahr_type]), list((-1)*df.loc[:, bbr_type])
        ahr_dic[system] = ahr_data
        bbr_dic[system] = bbr_data

    return ahr_dic, bbr_dic

### data_type_list = ['dE', 'dTStot', 'dA', 'E/water', 'dE/water', 'dTS/water', 'A/water', 'dA/water', 'water'] ###
### data_type_list = ['dEsw', 'dEww', 'Esw/water', 'Eww/water'] ###
### data_type_list = ['Nsw_acc , 'Nsw_don , 'Nww_acc , 'Nww_don , 'Nsw_acc/water , 'Nsw_don/water , 'Nww_acc/water , 'Nww_don/water]


Nsw_ahr, Nsw_bbr = read_data(data_list, "Nsw")
Nww_ahr, Nww_bbr = read_data(data_list, "Nww")
Nsw_norm_ahr, Nsw_norm_bbr = read_data(data_list, "Nsw/water")
Nww_norm_ahr, Nww_norm_bbr = read_data(data_list, "Nww/water")

dE_ahr, dE_bbr = read_data(data_list, "dE")
dTS_ahr, dTS_bbr = read_data(data_list, "dTStot")
dA_ahr, dA_bbr = read_data(data_list, "dA")
Enorm_ahr, Enorm_bbr = read_data(data_list, "E/water")
Snorm_ahr, Snorm_bbr = read_data(data_list, "dTS/water")
Anorm_ahr, Anorm_bbr = read_data(data_list, "A/water")
water_ahr, water_bbr = read_data(data_list, "water")

dEsw_ahr, dEsw_bbr = read_data(data_list, "dEsw")
dEww_ahr, dEww_bbr = read_data(data_list, "dEww")
Esw_norm_ahr, Esw_norm_bbr = read_data(data_list, "Esw/water")
Eww_norm_ahr, Eww_norm_bbr = read_data(data_list, "Eww/water")

dTStrans_ahr, dTStrans_bbr = read_data(data_list, "dTStrans")
dTSorient_ahr, dTSorient_bbr = read_data(data_list, "dTSorient")
dTStrans_norm_ahr, dTStrans_norm_bbr = read_data(data_list, "dTStrans/water")
dTSorient_norm_ahr, dTSorient_norm_bbr = read_data(data_list, "dTSorient/water")

length = len(data_list)
# generate_plot(length, dE_ahr, dE_bbr, "Total Solvent Energy ($E_{tot}$)", filename="dE_dpi300")
# generate_plot(length, dTS_ahr, dTS_bbr, "Total Solvent Entropy (\N{MINUS SIGN}T\u0394$S_{tot}$)", filename="dTStot_dpi300")
# generate_plot(length, dA_ahr, dA_bbr, "Total Solvent Helmholtz Free Energy ($A_{tot}$)", filename="dA_dpi300")
# generate_plot(length, Enorm_ahr, Enorm_bbr, "Solvent Energy per water (E / water)", filename="E_per_wat_dpi300")
# generate_plot(length, Snorm_ahr, Snorm_bbr, "Solvent Entropy per water (\N{MINUS SIGN}T\u0394S / water)", filename="S_per_wat_dpi300")
# generate_plot(length, Anorm_ahr, Anorm_bbr, "Solvent Helmholtz Free Energy per water (A / water)", filename="A_per_wat_dpi300")
# generate_plot(length, water_ahr, water_bbr, "Number of Water Molecules", filename="num_of_wat")
#
# generate_plot(length, dEsw_ahr, dEsw_bbr, "Protein – Water Interaction Energy ($E_{sw}$)", filename="dEsw_dpi300")
# generate_plot(length, dEww_ahr, dEww_bbr, "Water – Water Interaction Energy ($E_{ww}$)", filename="dEww_dpi300")
# generate_plot(length, Esw_norm_ahr, Esw_norm_bbr,
#               "Protein – Water Interaction Energy per water ($E_{sw}$ / water)", filename="Esw_per_wat_dpi300")
# generate_plot(length, Eww_norm_ahr, Eww_norm_bbr,
#               "Water – Water Interaction Energy per water ($E_{ww}$ / water)", filename="Eww_per_wat_dpi300")
#
# generate_plot(length, dTStrans_ahr, dTStrans_bbr, "Translational Entropy (\N{MINUS SIGN}T\u0394$S_{trans}$)", filename="dTStrans_dpi300")
# generate_plot(length, dTSorient_ahr, dTSorient_bbr, "Orientational Entropy (\N{MINUS SIGN}T\u0394$S_{orient}$)", filename="dTSorient_dpi300")
# generate_plot(length, dTStrans_norm_ahr, dTStrans_norm_bbr,
#               "Translational Entropy per water (T\u0394$S_{trans}$ / water)", filename="Strans_per_wat_dpi300")
# generate_plot(length, dTSorient_norm_ahr, dTSorient_norm_bbr,
#               "Orientational Entropy per water (T\u0394$S_{orient}$ / water)", filename="Sorient_per_wat_dpi300")
#
generate_plot(length, Nsw_ahr, Nsw_bbr, "Total Number of Protein - Water H-bonds", filename="Nsw_dpi300")
generate_plot(length, Nww_ahr, Nww_bbr, "Total Number of Water - Water H-bonds", filename="Nww_dpi300")
# generate_plot(length, Nsw_norm_ahr, Nsw_norm_bbr, "Number of Protein - Water H-bonds per water", filename="Nsw_per_wat_dpi300")
# generate_plot(length, Nww_norm_ahr, Nww_norm_bbr, "Number of Water - Water Hybonds per water", filename="Nww_per_wat_dpi300")


# max_tick, min_tick = round(max(max_list), 1), round(min(min_list), 1)
#
# if (max_tick - min_tick) >= 500:
#     dev = 50
# elif 200 <= (max_tick - min_tick) <= 500:
#     dev = 25
# elif 100 <= (max_tick - min_tick) <= 201:
#     dev = 10
# elif 10 <= (max_tick - min_tick) <= 100:
#     dev = 3.0
# elif (max_tick - min_tick) <= 10:
#     dev = 0.5