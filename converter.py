import linecache
import re
import time
import pandas


def main():
    print("Starting convert\n")
    start_time = time.clock()
    file = 'StreamingHistory0.json'  # Choose your input file here

    num_lines = sum(1 for line in open(file))

    lines = []
    for i in range(1, num_lines):  # convert json into lines
        line = linecache.getline(file, i)
        line = line.strip()
        lines.append(line)

    i = 3
    all_songs = []
    while i < num_lines:
        indiv_song_clean = []
        indiv_song = lines[i:i+3]

        for j in indiv_song:
            strng = match(j)
            indiv_song_clean.append(strng)

        if indiv_song_clean[2] >= 30000:  # Filter out songs that were listened to for less than 30 seconds.
            song_merged = indiv_song_clean[0] + ", " + indiv_song_clean[1]
            all_songs.append(song_merged)
        i = i+6

    print(all_songs)

    output_file = pandas.DataFrame(all_songs)  # For some reason I couldn't get this to work without pandas
    output_file.to_csv('output.csv', index=False, header=False)  # Make sure that the output file exist and is empty!

    print("\nConvert finished in " + str(time.clock() - start_time), "seconds.")


def match(strng):  # extract relevant info
    match_info = re.search(r":(.*)", strng).group()
    match_info = match_info[2:]
    if match_info[0] == "\"":  # artist or song title
        match_info = match_info[:-1]
    else:  # song duration
        match_info = int(match_info)
    return match_info


main()
