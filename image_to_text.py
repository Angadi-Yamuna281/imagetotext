import google.generativeai as genai
from PIL import Image
import io

# 🔹 Configure the API key (Replace with your actual API key)
genai.configure(api_key="AIzaSyCvx-Kpjcl9_A32HCvNpTRfaKjnq5GVt-Q")

# 🔹 Use the latest available model
model = genai.GenerativeModel("gemini-1.5-pro")  # Or use "gemini-1.5-flash" for speed

def image_to_text(image_path):
    try:
        # 🔹 Open and read the image file
        with open(image_path, "rb") as img_file:
            image = img_file.read()

        # 🔹 Prepare the image for input
        image_data = {"mime_type": "image/jpeg", "data": image}

        # 🔹 Generate caption using a list input format
        response = model.generate_content([image_data, "Describe this image."])

        # 🔹 Return generated text
        return response.text if response else "No response generated."

    except FileNotFoundError:
        return f"❌ Error: File '{image_path}' not found."
    except IOError:
        return f"❌ Error: '{image_path}' is not a valid image file."
    except Exception as e:
        return f"❌ Unexpected Error: {e}"

# 🔹 Run the script
if __name__ == "__main__":
    image_path = input("Enter the image file path: ").strip().strip('"')  # Remove extra quotes
    caption = image_to_text(image_path)
    print(f"🖼️ Generated Caption: {caption}")
