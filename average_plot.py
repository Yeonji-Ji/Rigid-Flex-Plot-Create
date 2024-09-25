import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


individual_fig_path = "/Users/yeonji/Dropbox/myfolder_data/gist_integration_data_figs/Data_and_Figures/Figures_revised/Average/"

vol_range = np.arange(3.0, 10.5, 0.5)
path = "/Users/yeonji/Dropbox/myfolder_data/gist_integration_data_figs/Data_and_Figures/Figures_revised/Average/"


def generate_plot(ahr_data, ahr_err, bbr_data, bbr_err, filename, ylim=None, line=None, block=None):
    path_to_save = individual_fig_path + filename

    num_rows = 2
    num_cols = 3
    fig, axs = plt.subplots(num_rows, num_cols, figsize=(14, 8), sharex=True)
    plt.subplots_adjust(left=0.1, right=0.9, bottom=0.15, top=0.85, wspace=0.1, hspace=0.4)

    cap = 6
    eline = 1
    lw = 1
    ashape, bshape = 'o', 'D'
    acolor, bcolor = '#eb7005', '#1f77b4'


    axs[0][0].errorbar(vol_range, ahr_data[0], yerr=ahr_err[0], lw=lw, elinewidth=eline, capsize=cap, label="ahr", marker=ashape, color=acolor)
    axs[0][0].errorbar(vol_range, bbr_data[0], yerr=bbr_err[0], lw=lw, elinewidth=eline, capsize=cap, label="bbr", marker=bshape, color=bcolor)
    axs[0][1].errorbar(vol_range, ahr_data[1], yerr=ahr_err[1], lw=lw, elinewidth=eline, capsize=cap, label="ahr", marker=ashape, color=acolor)
    axs[0][1].errorbar(vol_range, bbr_data[1], yerr=bbr_err[1], lw=lw, elinewidth=eline, capsize=cap, label="bbr", marker=bshape, color=bcolor)
    axs[0][2].errorbar(vol_range, ahr_data[2], yerr=ahr_err[2], lw=lw, elinewidth=eline, capsize=cap, label="ahr", marker=ashape, color=acolor)
    axs[0][2].errorbar(vol_range, bbr_data[2], yerr=bbr_err[2], lw=lw, elinewidth=eline, capsize=cap, label="bbr", marker=bshape, color=bcolor)
    axs[1][0].errorbar(vol_range, ahr_data[3], yerr=ahr_err[3], lw=lw, elinewidth=eline, capsize=cap, label="ahr", marker=ashape, color=acolor)
    axs[1][0].errorbar(vol_range, bbr_data[3], yerr=bbr_err[3], lw=lw, elinewidth=eline, capsize=cap, label="bbr", marker=bshape, color=bcolor)
    axs[1][1].errorbar(vol_range, ahr_data[4], yerr=ahr_err[4], lw=lw, elinewidth=eline, capsize=cap, label="ahr", marker=ashape, color=acolor)
    axs[1][1].errorbar(vol_range, bbr_data[4], yerr=bbr_err[4], lw=lw, elinewidth=eline, capsize=cap, label="bbr", marker=bshape, color=bcolor)
    axs[1][2].errorbar(vol_range, ahr_data[5], yerr=ahr_err[5], lw=lw, elinewidth=eline, capsize=cap, label="ahr", marker=ashape, color=acolor)
    axs[1][2].errorbar(vol_range, bbr_data[5], yerr=bbr_err[5], lw=lw, elinewidth=eline, capsize=cap, label="bbr", marker=bshape, color=bcolor)

    axs[0][0].axhline(y=line, color="gray", linestyle="--", label="bulk") # Bulk E

    for row in range(num_rows):
        for col in range(num_cols):
            axs[row][col].xaxis.set_tick_params(labelsize=10)
            axs[row][col].yaxis.set_tick_params(labelsize=10)
            axs[row][col].grid(color='gray', alpha=0.2)
            if row == 1:
                axs[row][col].set_xlabel("Sub-volume Distance " + "$(\AA)$", fontsize=11, fontfamily='serif',style='italic')
            if col == 0:
                axs[row][col].set_ylabel("kcal/mol", fontsize=10.5, fontfamily='serif', style='italic')


    axs[0][0].set_title("Energy per water ($E_{tot}$ / water)", fontsize=12.5, fontfamily='serif')
    axs[0][1].set_title("Entropy per water (\N{MINUS SIGN}T\u0394S / water)", fontsize=12.5, fontfamily='serif')
    axs[0][2].set_title("Free Energy per water ( $A_{tot}$ / water)", fontsize=12.5, fontfamily='serif')
    axs[1][0].set_title("Total Energy ($E_{tot}$)", fontsize=12.5, fontfamily='serif')
    axs[1][1].set_title("Total Entropy (\N{MINUS SIGN}T\u0394$S_{tot}$)", fontsize=12.5, fontfamily='serif')
    axs[1][2].set_title("Total Helmholtz Free Energy ($E_{tot}$)", fontsize=12.5, fontfamily='serif')


    legend_elements = [
        plt.Line2D([0], [0], color='#eb7005', lw=2, label='Rigid'),
        plt.Line2D([0], [0], color='#1f77b4', lw=2, label='Flexible'),
        # plt.Line2D([0], [0], color="#ba0615", lw=2, label="bulk")
    ]
    # fig.legend(handles=legend_elements, loc='center right', bbox_to_anchor=(1, 0.55), ncol=1, fontsize=11)
    # fig.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(0.985, 1.01), ncol=2, fontsize=10)
    # for a in axs[0, :]:
    #     a.tick_params(labelbottom=True)

    plt.tight_layout()
    fig.savefig(path_to_save + ".png", dpi=300)
    plt.show()

    return


avg_csv_file = "/Users/yeonji/Dropbox/myfolder_data/gist_integration_data_figs/Data_and_Figures/Data/avg_by_reg.csv"
std_csv_file = "/Users/yeonji/Dropbox/myfolder_data/gist_integration_data_figs/Data_and_Figures/Data/avg_by_reg_std_err.csv"
df = pd.read_csv(avg_csv_file, index_col="Unnamed: 0")
err = pd.read_csv(std_csv_file, index_col="Unnamed: 0")

ahr_data = {}
ahr_err = {}
bbr_data = {}
bbr_err = {}

ahr_data[0], bbr_data[0] = (df.loc[:, "E/water (ahr)"]).tolist(), (df.loc[:, "E/water (bbr)"]).tolist()
ahr_err[0], bbr_err[0] = err.loc[:, "E/water (ahr)"].tolist(), err.loc[:, "E/water (bbr)"].tolist()

ahr_data[1], bbr_data[1] = (-1*df.loc[:, "dTS/water (ahr)"]).tolist(), (-1*df.loc[:, "dTS/water (bbr)"]).tolist()
ahr_err[1], bbr_err[1] = err.loc[:, "dTS/water (ahr)"].tolist(), err.loc[:, "dTS/water (bbr)"].tolist()

ahr_data[2], bbr_data[2] = (df.loc[:, "A/water (ahr)"]).tolist(), (df.loc[:, "A/water (bbr)"]).tolist()
ahr_err[2], bbr_err[2] = err.loc[:, "A/water (ahr)"].tolist(), err.loc[:, "A/water (bbr)"].tolist()
#
ahr_data[3], bbr_data[3] = df.loc[:, "dE (ahr)"].tolist(), df.loc[:, "dE (bbr)"].tolist()
ahr_err[3], bbr_err[3] = err.loc[:, "dE (ahr)"].tolist(), err.loc[:, "dE (bbr)"].tolist()

ahr_data[4], bbr_data[4] = ((-1)*df.loc[:, "dTStot (ahr)"]).tolist(), ((-1)*df.loc[:, "dTStot (bbr)"]).tolist()
ahr_err[4], bbr_err[4] = err.loc[:, "dTStot (ahr)"].tolist(), err.loc[:, "dTStot (bbr)"].tolist()

ahr_data[5], bbr_data[5] = df.loc[:, "dA (ahr)"].tolist(), df.loc[:, "dA (bbr)"].tolist()
ahr_err[5], bbr_err[5] = err.loc[:, "dA (ahr)"].tolist(), err.loc[:, "dA (bbr)"].tolist()

# print(ahr_data[1])
# print(ahr_err)

generate_plot(ahr_data, ahr_err, bbr_data, bbr_err, "avg_six", line=-12.259)