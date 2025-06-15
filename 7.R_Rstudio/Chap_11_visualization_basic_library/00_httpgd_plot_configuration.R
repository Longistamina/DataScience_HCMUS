# For more robust plot viewing similar to RStudio, install the httpgd package and configure your VSCode settings

## Install httpgd package
# install.packages("httpgd")
# conda install -c conda-forge r-httpgd


## Then open >Preferences: Open User Settings (JSON), and add these configurations
# {
#     "r.plot.useHttpgd": true,
#     "r.bracketedPaste": true,
#     "r.sessionWatcher": true,
#     "r.alwaysUseActiveTerminal": true,
#     "editor.formatOnSave": true
# }

## Then Ctrl+S to save the JSON settings file
