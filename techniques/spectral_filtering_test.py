import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from spectral_filtering.spectral_filtering import spectral_filtering

# Load the WAV file
# Airport
sample_rate1, data1 = wav.read("../audio_files/airport.wav")
# Cafe
sample_rate2, data2 = wav.read("../audio_files/cafe.wav")
# Rainstorm
sample_rate3, data3 = wav.read("../audio_files/rainstorm.wav")

# Extract the channels
# Airport
channel1_1 = data1[:, 0]
channel1_2 = data1[:, 1]
# Cafe
channel2_1 = data2[:, 0]
channel2_2 = data2[:, 1]
# Rainstorm
channel3_1 = data3[:, 0]
channel3_2 = data3[:, 1]

# Find filtered by spectral filtering def
# Airport
filtered_channel1_2 = spectral_filtering(channel1_1, channel1_2)
# Cafe
filtered_channel2_2 = spectral_filtering(channel2_1, channel2_2)
# Rainstorm
filtered_channel3_2 = spectral_filtering(channel3_1, channel3_2)

# Save the filtered data to a new WAV file
# Airport
path1 = "../filtered_audio_files/" + "sf_airport.wav"
wav.write(path1, sample_rate1, filtered_channel1_2.astype(np.int16))
# Cafe
path2 = "../filtered_audio_files/" + "sf_cafe.wav"
wav.write(path2, sample_rate1, filtered_channel2_2.astype(np.int16))
# Rainstorm
path3 = "../filtered_audio_files/" + "sf_rainstorm.wav"
wav.write(path3, sample_rate1, filtered_channel3_2.astype(np.int16))

# Create a time array for plotting
time = np.arange(len(channel1_2)) / sample_rate1


# Def for each audio = each figure
def plot(channel, filtered_channel, title):
    # Create figure for plotting
    plt.figure(figsize=(16, 9))
    plt.title(title, fontsize=20)

    # Plot both original and filtered signal
    plt.plot(channel, label="Original")
    plt.plot(filtered_channel, label="Filtered")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.legend(fontsize="large")

    # Show plot
    plt.show()
    # Close figure
    plt.close()


# Plotting all
plot(channel1_2, filtered_channel1_2, "Airport Noise")  # Airport
plot(channel2_2, filtered_channel2_2, "Cafe Noise")  # Cafe
plot(channel3_2, filtered_channel3_2, "Rainstorm Noise")  # Rainstorm
