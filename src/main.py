import csv

def load_music_data(file_path):
    music_library = {}
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            mood = row["mood"].strip().lower()
            song = row["song"].strip()
            music_library.setdefault(mood, []).append(song)
    return music_library


def recommend_music():
    print("=== Mood Music Recommender ===")
    mood = input("Enter your mood (happy/sad/focus/chill): ").strip().lower()

    music_library = load_music_data("data/songs.csv")

    if mood in music_library:
        print("\nRecommended for your mood:")
        for track in music_library[mood]:
            print(f"- {track}")
    else:
        print("\nMood not recognized. Options: " + ", ".join(music_library.keys()))


if __name__ == "__main__":
    recommend_music()
