# DVC-Practice-Project
Practicing DVC in a group, using DVC's pipelining and remote features.  This is different from the Git-like workflow, which mostly uses the `dvc add` and `dvc commit` commands, instead focusing on the `dvc run` and `dvc repro` commands to generate a DAG pipeline that complements a normal data science workflow.

## Goals

Using an interactive-focused workflow ("Get each Line Working", "Get the Script Working", "Get the Pipeline Working"), we'll:

  - Download Data (urllib)
  - Register Download Step to Pipeline (dvc init, dvc run)
  - Import Data Directly from Repo (dvc import)
  - Add Notebook and Reports to Pipeline (jupyter nbconvert)
  - Add Step to Pipeline via yaml file(dvc.yaml, dvc dag)
  - Add Parameterized Step to Pipeline (dvc run, dvc param)

## Dataset

Covid Data from the Owid group: 
  - Attribution: Hasell, J., Mathieu, E., Beltekian, D. et al. A cross-country database of COVID-19 testing. Sci Data 7, 345 (2020). https://doi.org/10.1038/s41597-020-00688-8
  - Link to Data: https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv
  
  
## References

**DVC Command Reference**:  https://dvc.org/doc/command-reference



## Some Useful Code Snippets

### Download a file from the internet in Python without Requests

```python
from urllib.request import urlretrieve
urlretrieve(url, to_filename)
```


### Add a new stage to the DVC pipeline

```
dvc run -n <stage-name> -d <script-path> -d <data-path> -o <output-paths> <command>
```

Example:

```
dvc run -n process -d scripts/process_data.py -d data/raw -o data/processed python scripts/process_data.py
```

### View hidden files in Jupyter Lab:

```
jupyter lab --ContentsManager.allow_hidden=True
```

### Execute a Jupyter notebook with nbconvert:

(note: the output is relative to the notebook, not to the shell working directory)

```
jupyter nbconvert --execute MyNotebook.ipynb --to html --output ..\reports\MyNotebook.html
```

