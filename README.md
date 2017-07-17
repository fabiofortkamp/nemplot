# nemplot - Easier matplotlib

The package `nemplot` (from *nem*, the Danish word for *easy*) defines wrapper functions to create plots with all the same apperance, in particular the same size and fonts.

To install it:

1. Clone the repository into a directory of choice
2. From this directory, run:

```shell
pip install .
```

3. Move to another directory as a test, start Python and run:

```python
>>> import nemplot
```

If you do not see any error messages, everything was installed successfully.

The most basic usage is:

```python
import nemplot

fig,axis = nemplot.create_plot(title="Instantaneous profile", xlabel="B",ylabel="Q")
```

The `fig` and `axis` objects can then be used to plot things and draw legends.

Another important function is `nemplot.save_figure(fig,name)`, which will save the `fig` object with filename `name` inside the `figures` directory. The extension is automatically added.

`nemplot`can be customized. the customization mechanism uses a dictionary accessible via `nemplot.nemplot_parameters`. To view all parameters:

```python
from nemplot import nemplot_parameters

print(nemplot_parameters)
```

The fields names are self-explanatory and can be used anywhere:

```python
import nemplot
from nemplot import nemplot_parameters

fig,axis = nemplot.create_plot(title="Instantaneous profile", xlabel="B",ylabel="Q")
axis.plot(...)

axis.legend(fontsize=nemplot_parameters["FONTSIZE"])
```

To modify the paramters, there are specific functions, that you can inspect by typing `nemplot.set_<TAB>` in IPython. It is not recommended to directly modify the dictionary, as there are parameters that are coupled (for instance, when you modify `nemplot_parameters["FIGSIZE_CM"]`, the field `nemplot_parameters["FIGSIZE_INCHES"]`, that is actually used by the plotting functions to create the figures, should be updated accordingly).
