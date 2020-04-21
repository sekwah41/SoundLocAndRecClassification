import pandas
from os.path import join as join_path
from wavefile import WaveReader

usl = "../resources/UrbanSound8K/"

us_meta = pandas.read_csv(usl + 'metadata/UrbanSound8K.csv')

audio_data = []
for i, entry in us_meta.iterrows():
    file_loc = join_path(usl, "audio", 'fold' + str(entry["fold"]), str(entry["slice_file_name"]))
    with WaveReader(file_loc) as r:
        # Probably easier way with this library to read the bit depth.
        audio_data.append((r.channels, r.samplerate, int((r.byterate) / (r.samplerate * r.channels) * 8)))

audio_df = pandas.DataFrame(audio_data, columns=['num_channels', 'sample_rate', 'bit_depth'])

# Overview of data
print("Number of channels")
print(audio_df.num_channels.value_counts(normalize=True))

print("\nSample Rates")
print(audio_df.sample_rate.value_counts(normalize=True))

print("\nBit Depth")
print(audio_df.bit_depth.value_counts(normalize=True))
