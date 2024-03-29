import matplotlib.pyplot as plt

LATENCY_PATH = "output/latency/"
THROUGHPUT_PATH = "output/throughput/"

EXPERIMENT_TIME_SATURN = 10
EXPERIMENT_TIME_C3 = 10

CHART_RENDER_WITH_TEX = True

""" 
Processes the latencies and returns the medium latency for each 
experiment.
"""
def latency(inputs):
    total_latency = []
    for experiment in inputs:
        processed_lines = []
        num_results = 0
        experiment_latency = 0
        experiment_path = LATENCY_PATH + experiment
        experiment_file = open(experiment_path)

        for line in experiment_file.readlines():
            processed_lines.append(line.strip().split(','))

        experiment_file.close()

        for line in processed_lines:
            line.pop(0)
            num_results = num_results + len(line)
            for latency in line:
                experiment_latency = experiment_latency + int(latency)

        medium_latency = int(experiment_latency / num_results)

        total_latency.append(medium_latency / 10)

    return total_latency


""" 
Processes the throughputs and returns 
the medium throughput of each experiment.
"""
def throughput(inputs, time):
    total_throughput = []
    for experiment in inputs:
        processed_lines = []
        experiment_throughput = 0
        experiment_path = THROUGHPUT_PATH + experiment
        experiment_file = open(experiment_path)

        for line in experiment_file.readlines():
            processed_lines.append(line.strip())
        
        experiment_file.close()
        processed_lines.pop(0) # TODO: Probably delete from output

        for result in processed_lines:
            splitted = result.split(',')
            throughput = int(splitted[1])
            experiment_throughput = experiment_throughput + throughput
        
        total_throughput.append(int(experiment_throughput / time))
    
    return total_throughput


def plot_graph(latencies, throughputs, str_label):
    plt.title('Latency / Throughput')
    plt.xlabel('Throughput (Op/s)')
    plt.ylabel('Perceived Latency (ms)')
    
    # plt.plot(throughputs, latencies, linestyle="dashed")
    plt.plot(throughputs, latencies, 'o-', label=str_label, linestyle="dashdot", ms="4")

if __name__ == "__main__":
    input_saturn = [
        "saturn-3-clients.txt",
        "saturn-5-clients.txt",
        "saturn-10-clients.txt",
        "saturn-15-clients.txt",
        "saturn-20-clients.txt",
        "saturn-25-clients.txt",
        "saturn-30-clients.txt",
        "saturn-35-clients.txt",
        "saturn-50-clients.txt",
        "saturn-55-clients.txt",
        "saturn-60-clients.txt",
        "saturn-65-clients.txt",
        "saturn-80-clients.txt",
        "saturn-100-clients.txt",
        "saturn-150-clients.txt",
        "saturn-200-clients.txt",
        "saturn-250-clients.txt",
        "saturn-300-clients.txt",
    ]

    input_c3 = [
        "c3-3-clients.txt",
        "c3-5-clients.txt",
        "c3-10-clients.txt",
        "c3-15-clients.txt",
        "c3-20-clients.txt",
        "c3-25-clients.txt",
        "c3-30-clients.txt",
        "c3-35-clients.txt",
        "c3-50-clients.txt",
        "c3-55-clients.txt",
        "c3-60-clients.txt",
        "c3-65-clients.txt",
        "c3-80-clients.txt",
        "c3-100-clients.txt",
        "c3-150-clients.txt",
        "c3-200-clients.txt",
        "c3-250-clients.txt",
        "c3-300-clients.txt",
    ]

    input_c3sat = [
        "c3sat-3-clients.txt",
        "c3sat-5-clients.txt",
        "c3sat-10-clients.txt",
        "c3sat-15-clients.txt",
        "c3sat-20-clients.txt",
        "c3sat-25-clients.txt",
        "c3sat-30-clients.txt",
        "c3sat-35-clients.txt",
        "c3sat-50-clients.txt",
        "c3sat-55-clients.txt",
        "c3sat-60-clients.txt",
        "c3sat-65-clients.txt",
        "c3sat-80-clients.txt",
        "c3sat-100-clients.txt",
        "c3sat-150-clients.txt",
        "c3sat-200-clients.txt",
        "c3sat-250-clients.txt",
        "c3sat-300-clients.txt",
    ]

    if CHART_RENDER_WITH_TEX:
        plt.rcParams.update({
            "text.usetex": True,    
            "font.family": "serif",
        })

    throughputs_saturn = throughput(input_saturn, EXPERIMENT_TIME_SATURN)
    latencies_saturn = latency(input_saturn)

    throughputs_c3 = throughput(input_c3, EXPERIMENT_TIME_C3)
    latencies_c3 = latency(input_c3)

    latencies_c3sat = latency(input_c3sat)
    throughputs_c3sat = throughput(input_c3sat, EXPERIMENT_TIME_C3)

    plt.style.use('seaborn-paper')
    plot_graph(latencies_saturn, throughputs_saturn, 'Saturn')
    plot_graph(latencies_c3, throughputs_c3, 'C3')
    plot_graph(latencies_c3sat, throughputs_c3sat, 'C3 + Saturn')
    plt.legend()
    plt.tight_layout()
    plt.savefig('plot-latency-throughput.pdf')
