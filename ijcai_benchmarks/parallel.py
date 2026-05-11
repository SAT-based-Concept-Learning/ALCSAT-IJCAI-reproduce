import time
from alcsat import L_OP
from spell.structures import structure_from_owl
from spell.fitting_alc import FittingALC
import sys,os


def run(sml_path):    
    workers = [1, 2, 3, 4, 5, 6, 7, 8]
    runs = 3
    benchmarks = ["mammographic", "carcinogenesis", "lymphography"]
    a = []    
    outfile = "reproduce-table5.txt"
    with open(outfile, mode="w") as outfile:
        _ = outfile.write("bench, worker, time\n")
        for benchmark in benchmarks:
            exs_folder = '1'
            if benchmark == "mutagenesis":
                exs_folder = '42'
            A = structure_from_owl(os.path.join(sml_path, 'learningtasks', benchmark, 'owl', 'data', f'{benchmark}.owl'))
            pospath = os.path.join(sml_path, 'learningtasks', benchmark, 'owl', 'lp', exs_folder, 'pos.txt')
            negpath = os.path.join(sml_path, 'learningtasks', benchmark,'owl', 'lp', exs_folder, 'neg.txt')

            P: list[int] = []
            with open(pospath, encoding="UTF-8") as file:
                for line in file.readlines():
                    ind = line.rstrip()
                    P.append(A.indmap[ind])

            N: list[int] = []
            with open(negpath, encoding="UTF-8") as file:
                for line in file.readlines():
                    ind = line.rstrip()
                    N.append(A.indmap[ind])

            times: dict[int, list[float]] = {}

            for w in workers:
                times[w] = []
                for run in range(runs):
                    start = time.perf_counter()

                    f = FittingALC(
                        A,
                        8,
                        P,
                        N,
                        op=L_OP["alc"],
                        workers=w,
                        max_q=2,
                    )

                    acc, _, _ = f.solve_incr_approx(8)

                    end = time.perf_counter()

                    print("==== TOOK {}".format(end - start))
                    times[w].append(end - start)

            for w in workers:
                print(f"Benchmark {benchmark}, Worker {w} : {sum(times[w]) / runs}s")
                l = f"Benchmark {benchmark}, Worker {w} : {sum(times[w]) / runs}s"
                a.append(l)
                outfile.write(l)
                outfile.write("\n")
                outfile.flush()
        for x in a:
            print(x)        


def main():
    run(sys.argv[1])
    
if __name__ == "__main__":
    main()
