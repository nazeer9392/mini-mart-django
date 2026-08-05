import os
import cloudinary
import cloudinary.uploader

# Replace these with your Cloudinary credentials
cloudinary.config(
    cloud_name="ehl0ky0k",
    api_key="197284196949985",
    api_secret="1vCHXh5ofFbEnxxWworwQn_Qgs4",
)

MEDIA_DIR = "media"

for root, dirs, files in os.walk(MEDIA_DIR):
    for file in files:
        path = os.path.join(root, file)

        # Keep folder structure (products/, categories/, profiles/, etc.)
        folder = os.path.dirname(os.path.relpath(path, MEDIA_DIR))

        print(f"Uploading {path}...")

        result = cloudinary.uploader.upload(
            path,
            folder=folder
        )

        print("Uploaded:", result["secure_url"])

print("All images uploaded successfully!")