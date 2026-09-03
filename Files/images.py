from pathlib import Path
import cv2

# Locate the Images folder (one level up from Files/)
BASE_DIR = Path(__file__).resolve().parent.parent / "Images"

# Load the images (adjust extensions like .jpg/.png to match your actual files)
img1_path = str(BASE_DIR / "baboon1.png")
img2_path = str(BASE_DIR / "baboon2.png")

img1 = cv2.imread(img1_path)
img2 = cv2.imread(img2_path)

# Verify successful loading
if img1 is None or img2 is None:
    print(f"Error: Could not find images in {BASE_DIR}")
    print(f"Checking path 1: {img1_path}")
    print(f"Checking path 2: {img2_path}")
else:
    cv2.imshow("Baboon 1", img1)
    cv2.imshow("Baboon 2", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
