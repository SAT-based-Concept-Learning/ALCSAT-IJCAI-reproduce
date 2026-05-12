This repository contains our implementation of bounded fitting for the description logic ALCQI(f) and instructions on how to reproduce the results from the paper _Bounded Fitting for Expressive Description Logics_ (IJCAI-ECAI 2026).

## Requirements
- Installation of Python 3
- uv package manager: `https://github.com/astral-sh/uv`
- SML-Benchmarks
    - The SML-Benchmarks can be obtained from <https://github.com/SmartDataAnalytics/SML-Bench>. Note that in order to download the benchmark `premierleague` from GitHub, Git Large File Storage (LFS) is required. 

## Reproduce all results
To reproduce all results reported in the paper run

```uv run reproduce_all.py <path to sml benchmarks repository folder>```

The contents of the files created in the process are explained below. Note that this may take a long time to finish, likely 1-2 days. Therefore there are instructions to reproduce specific tables or rows of table 1 below.

## SML-Benchmarks
To reproduce results shown in Table 1 (or Table 4 in the appendix), run

(row) Top: ``` uv run -m ijcai_benchmarks.cross_validation_top_bot  <path to sml benchmarks repository folder>```

(row) EvoLearner: ``` uv run -m ijcai_benchmarks.cross_validation_evolearner <path to sml benchmarks repository folder> ```

(row) TDL: ``` uv run -m ijcai_benchmarks.cross_validation_tdl <path to sml benchmarks repository folder> ```

(row) Theorem 2: ``` uv run -m ijcai_benchmarks.cross_validation_bisim_extract <path to sml benchmarks repository folder> ```

(row) Our Tool: ``` uv run -m ijcai_benchmarks.cross_validation_alcsat <path to sml benchmarks repository folder> ```

In all these cases two data files will be created, e.g. 
1. A .txt file with all data, e.g. ```reproduce-table1-therorem2.txt```
1. A .csv file with mean and standard derivation for accuracy, f1 score and size, computed from the data in 1., e.g. ```reproduce-table1-therorem2_mean_stdder.csv```

For Table 2 run 

``` uv run -m ijcai_benchmarks.intervals <path to sml benchmarks repository folder> ```
The file ```reproduce-table2.txt``` then contains the data shown in Table 2.


For Table 3 run

``` uv run -m ijcai_benchmarks.bisimulation <path to sml benchmarks repository folder> ```

The file ```reproduce-table3.txt``` then contains the data shown in Table 3.

For Table 5 (appendix) run ``` uv run -m ijcai_benchmarks.parallel ``` results will be shown in standard output.

## YAGO ALCQ Benchmarks
To reproduce results from Figure 1, run 

``` uv run -m alc_benchmarks.alc_benchmark ```

In each of the benchmarks in ```alcq_benchmarks/alcq_bisim_combined``` a file ```results.json``` will be created containing accuracies, f1 scores, concept sizes and concepts reported by the respective tools. In addition two files ```alcq_benchmarks/alcq_bisim_combined/data.csv``` and ```alcq_benchmarks/alcq_bisim_combined/data_avg.csv``` are created. The file ```alcq_benchmarks/alcq_bisim_combined/data_avg.csv``` contains the data points shown in Figure 1, that is, average accuracies and f1 scores by number of examples obtained from the results in ```alcq_benchmarks/alcq_bisim_combined/data.csv```.

## Run
For full instructions on how to run our implementation, run
`uv run spell_cli.py --help`