<div align="center">
    <img src="https://raw.githubusercontent.com/OgawaSama/air-quality/master/tree.png" alt="tiny tree" width="1000"/>

</div> 

# Decision Trees for Air Quality Dataset

This program creates a decision tree for solving the Air Quality assessment problem, where multiple variables may help determine a region's air quality.
The `data.csv` is from [Kaggle](https://www.kaggle.com/datasets/mujtabamatin/air-quality-and-pollution-assessment) by Mujtaba Mateen.

This program allows the user to specify a method in which to determine the Tree's depth, their targetted accuracy, which rendering engine to use and whether or not to run benchmarks instead.

The default parameters are:
* No maximum depth defined, runs until exhausted;
* If `--depth minimum` is selected, target accuracy is 0.85;
* Test/Train ratio is 30/70;
* Graphviz as the renderer;
* `data.csv` as the dataset file;
* `tree.png` as the Tree's image output file;
* `metrics.csv` as the benchmark's output file;
* 250 as the number of benchmarking runs.

## Extra Information
A code for preprocessing the `data.csv` is found at `preprocessing.py` and it generates `cleaned.csv`.  
This code was copied from a fork in [gabi-pinheiro's repo](https://github.com/gabi-pinheiro/air-quality/blob/b2cbdaa49ee1b51c6b10f6f22de274b508793294/pre-processing.py) and _slightly_ edited to work on the existing code here.  

The generated ROC Curve uses One-vs-Rest Macro-Average to try and consider the minority classes as equal value as the majority ones.  
The visualization of this curve can be found at `macro_roc.png` after running the algorithm, though it is not generated when benchmarking.

The benchmarking algorithm uses Stratified R-Fold Cross-Validation, with R=10. It does take a while to complete running, do not worry.  

When generating the ROC Curve with Matplotlib, it might generating a warning regarding `**kwargs`. This does not (currently) affect the program's result and should not worry the user. Attempts to solve it proved unfruitful.


## Running the program

### Windows
To run this program, simply create and activate a virtual environment with
```shell
python -m venv [envname]
[envname]\Scripts\activate
```

Install the needed packages with
```shell
pip install -r requirements.txt
```

Install the latest Graphviz version through their [website](https://www.graphviz.org/download/)  
And add it to your PATH.
It can be done by editing the System Variables or by executing in Python: 
```py
import os
os.environ["PATH"] += os.pathsep + 'path/to/Graphviz/bin/'
```
Where you change `path/to` with the proper path to your installed Graphviz package.


And then run the program with
```shell
python decisiontree.py
```
### Linux
To run this program, simply create and activate a virtual environment with
```shell
python -m venv [envname]
source [envname]/bin/activate
```

Install the needed packages with
```shell
pip install -r requirements.txt
```

If in Debian* or Ubuntu*, install the latest Graphviz version with
```shell
sudo apt install graphviz
```
If in Arch*, you can install Graphviz and add it manually to your PATH  
<sup><sub> I did it this way but forgot how, sorry⠀⠀⠀⠀orz </sub></sup>

And then run the program with
```shell
python decisiontree.py
```

