# Indian Food Calorie Calculator 🍛
This project uses a custom-trained Roboflow computer vision model to detect Indian food items in an image and estimate their total calories automatically.

## Features
- Detects multiple Indian food items in a single image (e.g., roti, daal, rice, idli, etc.)
- Calculates total estimated calories based on detected items
- Easy-to-use: just run the script and enter the image path!
- API key is securely managed using a `.env` file
- 
## How It Works
1. You provide the path to a food image.
2. The script uses a trained Roboflow model to detect food items.
3. The script prints out a calorie breakdown and the total estimated calories.
