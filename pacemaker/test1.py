import neurokit2 as nk  # Load the package

class test1:

    simulated_ecg = nk.ecg_simulate(duration=8, sampling_rate=200, heart_rate=80)

    nk.signal_plot(simulated_ecg, sampling_rate=200)  # Visualize the signal