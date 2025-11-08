def recommend_music():
    print("=== Mood Music Recommender ===")
    mood = input("Enter your mood (happy/sad/focus/chill): ").strip().lower()

    music_library = {
        "happy": ["Happy Song 1", "Happy Song 2"],
        "sad": ["Soft Track 1", "Soft Track 2"],
        "focus": ["Lo-fi Beat 1", "Lo-fi Beat 2"],
        "chill": ["Calm Tune 1", "Calm Tune 2"]
    }

    if mood in music_library:
        print("\nRecommended for your mood:")
        for track in music_library[mood]:
            print(f"- {track}")
    else:
        print("\nSorry, mood not recognized. Try: happy, sad, focus, chill")


if __name__ == "__main__":
    recommend_music()
