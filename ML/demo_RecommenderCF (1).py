import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def main():

    # -------------------------------------------------------
    # 1. Load User Ratings
    # -------------------------------------------------------
    ratings = pd.read_csv("u.data", sep="\t",
                          names=["user_id", "item_id", "rating", "timestamp"])

    # -------------------------------------------------------
    # 2. Load Bollywood Movie Titles (item_id + title)
    # -------------------------------------------------------
    movies = pd.read_csv("Movie_Id_Titles_clean.csv")

    # Merge ratings with movie titles
    df = pd.merge(ratings, movies, on="item_id")

    # -------------------------------------------------------
    # 3. Create User-Movie Rating Matrix
    # -------------------------------------------------------
    moviemat = df.pivot_table(index="user_id", columns="title", values="rating")

    # -------------------------------------------------------
    # 4. Ratings Summary (Mean + Count)
    # -------------------------------------------------------
    ratings_summary = df.groupby("title")["rating"].agg(["mean", "count"])
    ratings_summary.columns = ["avg_rating", "num_ratings"]


    # -------------------------------------------------------
    # 5. Recommendation Function
    # -------------------------------------------------------
    def recommend(movie_name):

        print(f"\n Searching: {movie_name}")

        # Fuzzy match
        matches = [title for title in moviemat.columns if movie_name.lower() in title.lower()]
        if len(matches) == 0:
            print(" Movie not found. Try typing part of the name.\n")
            return
        
        movie_name = matches[0]
        print(f" Matched: {movie_name}\n")

        movie_ratings = moviemat[movie_name]

        # Compute correlation
        corr = moviemat.corrwith(movie_ratings)

        # Convert to DataFrame
        corr_df = pd.DataFrame(corr, columns=["Correlation"])
        corr_df.dropna(inplace=True)

        # Join ratings count
        corr_df = corr_df.join(ratings_summary["num_ratings"], how="left")

        # Filter out low-support movies
        corr_df = corr_df[corr_df["num_ratings"] >= 25]

        if corr_df.empty:
            print(" Not enough rating data to compute recommendations.\nTry another movie.")
            return

        # Sort
        corr_df = corr_df.sort_values("Correlation", ascending=False)

        print(" Top Recommendations:\n")
        print(corr_df.head(5)[["Correlation"]])


    # -------------------------------------------------------
    # 6. Interactive User Input
    # -------------------------------------------------------
    print("\n Bollywood Collaborative Filtering Recommender Ready!")
    print("Type a movie name (or 'exit' to stop)\n")

    while True:
        movie = input("Enter movie name: ")
        if movie.lower() == "exit":
            print("\n Exiting recommender. Goodbye!\n")
            break
        recommend(movie)


if __name__ == "__main__":
    main()
