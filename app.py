import requests
import numpy as np

def main():
    print("Python program running inside Docker in GitHub Actions!")
    print("Numpy test:", np.array([1, 2, 3]) * 2)

    r = requests.get("https://api.github.com")
    print("GitHub API status:", r.status_code)

if __name__ == "__main__":
    main()
