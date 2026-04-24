def analyze_query(query):
    if "SELECT *" in query:
        print("Using SELECT * may reduce performance.")

    if "WHERE" in query:
        print("Consider adding indexing for better performance.")

    print("Analysis complete.")


if __name__ == "__main__":
    q = input("Enter SQL query: ")
    analyze_query(q)
