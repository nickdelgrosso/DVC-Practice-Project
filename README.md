# DVC-Practice-Project
Practicing DVC in a group, using DVC's pipelining and remote features.


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


### View hidden files in Jupyter Lab:

```
jupyter lab --ContentsManager.allow_hidden=True
```

### Execute a Jupyter notebook with nbconvert:

(note: the output is relative to the notebook, not to the shell working directory)

```
jupyter nbconvert --execute MyNotebook.ipynb --to html --output ..\reports\MyNotebook.html
```

