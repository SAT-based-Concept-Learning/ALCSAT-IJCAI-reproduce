import ijcai_benchmarks.bisimulation
import ijcai_benchmarks.intervals
import ijcai_benchmarks.parallel
import ijcai_benchmarks.cross_validation_alcsat
import ijcai_benchmarks.cross_validation_bisim_extract
import ijcai_benchmarks.cross_validation_evolearner
import ijcai_benchmarks.cross_validation_tdl
import ijcai_benchmarks.cross_validation_top_bot
from alc_benchmarks.alc_benchmark import run_alcq_benchmarks
import sys

def reproduce_all(sml_path):
    ijcai_benchmarks.cross_validation_alcsat.run(sml_path)
    ijcai_benchmarks.cross_validation_bisim_extract.run(sml_path)
    ijcai_benchmarks.cross_validation_evolearner.run(sml_path)
    ijcai_benchmarks.cross_validation_tdl.run(sml_path)
    ijcai_benchmarks.cross_validation_top_bot.run(sml_path)
    ijcai_benchmarks.bisimulation.run(sml_path)
    ijcai_benchmarks.intervals.run(sml_path)
    ijcai_benchmarks.parallel.run(sml_path)
    run_alcq_benchmarks()
    
def main():
    reproduce_all(sys.argv[1])

if __name__ == "__main__":
    main()
