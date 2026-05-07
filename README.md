This repository contains our implementation of bounded fitting for the description logic ALCQI(f) and instructions on how to reproduce the results from the paper.

## Requirements
- Installation of Python 3
- uv package manager


## SML-Benchmarks
The SML-Benchmarks can be obtained from <https://github.com/SmartDataAnalytics/SML-Bench>. Note that in order to download the benchmark `premierleague` from GitHub, Git Large File Storage (LFS) is required. To reproduce results shown in Table 1 (or Table 4 in the appendix), run

(row) Top: ``` uv run -m ijcai-benchmarks.cross-validation-top-bot  <path to sml benchmarks repository folder>```

(row) EvoLearner: ``` uv run -m ijcai-benchmarks.cross-validation-evolearner <path to sml benchmarks repository folder> ```

(row) TDL: ``` uv run -m ijcai-benchmarks.cross-validation-tdl <path to sml benchmarks repository folder> ```

(row) Theorem 2: ``` uv run -m ijcai-benchmarks.bisim-extract <path to sml benchmarks repository folder> ```

(row) Our Tool: ``` uv run -m ijcai-benchmarks.cross-validation-alcsat <path to sml benchmarks repository folder> ```

For Table 2 run ``` uv run -m ijcai-benchmarks.intervals <path to sml benchmarks repository folder> ```

For Table 3 run ``` uv run -m ijcai-benchmarks.bisimulation <path to sml benchmarks repository folder> ```

In all these cases data files will be created, e.g. ```reproduce-table1-therorem2.txt```. These files contain all data from which results shown in the table were created. For Table 1, the actual values shown in the paper are the means and standard deviations computed from this data. By running ```uv run -m ijcai-benchmarks.process-cross-validation-output <path to one of the output files>``` the means and standard deviations are computed for the file given file and then printed in LaTeX-compatible code which was used directly to generate Table 1.

For Table 5 (appendix) run ``` uv run -m ijcai-benchmarks.parallel ``` results will be shown in standard output.

## YAGO ALCQ Benchmarks
To reproduce results from Figure 1, run 

``` uv run -m alc_benchmarks.alc_benchmark ```

In each of the benchmarks in ```alcq_benchmarks/alcq_bisim_combined``` a file ```results.json``` will be created containing accuracies, f1 scores, concept sizes and concepts reported by the respective tools. In addition two files ```alcq_benchmarks/alcq_bisim_combined/data.csv``` and ```alcq_benchmarks/alcq_bisim_combined/data_avg.csv``` are created. The file ```alcq_benchmarks/alcq_bisim_combined/data_avg.csv``` contains the data points shown in Figure 1.


## Run
For full instructions on how to run our implementation, run
`uv run spell_cli.py --help`