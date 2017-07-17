from pathlib import Path
import matplotlib

NEMPLOT_DEFAULT_PARAMETERS = {"MAIN_FILE_PATH" : Path('.'),
"FIGURES_DIR_NAME" : "figures",
"LATEX_FONT": "Computer Modern",
"FIGSIZE_CM" : 20,
"FONTSIZE" : 15,
"FIGSIZE_CM_SMALL" : 8,
"FONTSIZE_SMALL" : 8,
"PLOT_EXTENSION" : '.png',
"DPI" : 800}

NEMPLOT_DEFAULT_PARAMETERS["FIGSIZE_INCHES"] = \
                    NEMPLOT_DEFAULT_PARAMETERS["FIGSIZE_CM"]/2.54
NEMPLOT_DEFAULT_PARAMETERS["FIGSIZE_INCHES_SMALL"] = \
                    NEMPLOT_DEFAULT_PARAMETERS["FIGSIZE_CM_SMALL"]/2.54
NEMPLOT_DEFAULT_PARAMETERS["FIG_FILE_PATH"] = (
            NEMPLOT_DEFAULT_PARAMETERS["MAIN_FILE_PATH"] /
            Path(NEMPLOT_DEFAULT_PARAMETERS["FIGURES_DIR_NAME"]))

nemplot_parameters = NEMPLOT_DEFAULT_PARAMETERS.copy()

def set_fontsize(fontsize):

    nemplot_parameters["FONTSIZE"] = fontsize

def set_figsize_cm(value):

    nemplot_parameters["FIGSIZE_CM"] = value
    nemplot_parameters["FIGSIZE_INCHES"] = (nemplot_parameters["FIGSIZE_CM"]/
                                            2.54)

def set_main_path(path):

    nemplot_parameters["MAIN_FILE_PATH"] = Path(path)
    nemplot_parameters["FIG_FILE_PATH"] = (
            nemplot_parameters["MAIN_FILE_PATH"] /
            Path(nemplot_parameters["FIGURES_DIR_NAME"]))

def set_figures_dir(directory):

    nemplot_parameters["FIGURES_DIR_NAME"] = directory
    nemplot_parameters["FIG_FILE_PATH"] = (
            nemplot_parameters["MAIN_FILE_PATH"] /
            Path(nemplot_parameters["FIGURES_DIR_NAME"]))

def set_plot_extension(ext):

    nemplot_parameters["PLOT_EXTENSION"] = ext

def set_dpi(value):

    nemplot_parameters["DPI"] = value

def update_latex_parameters():
    mpl_params = {'text.usetex': True,
                      'font.family': 'serif',
                      'font.serif': nemplot_parameters["LATEX_FONT"],
                      'text.latex.preamble': [r'\usepackage{engsymbols}',
                                              r'\usepackage{magref}']}
    matplotlib.rcParams.update(mpl_params)

def set_latex_font(fontname):

    nemplot_parameters["LATEX_FONT"] = fontname
    update_latex_parameters()
