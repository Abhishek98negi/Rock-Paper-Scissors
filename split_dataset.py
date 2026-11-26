import random
import shutil
from pathlib import Path

# Original dataset directory
base_dir = Path("data/rock_paper_scissors")

# Class names
classes = ["paper", "rock", "scissors"]

# Reproducibility
random.seed(42)


def create_subset(source_dir, destination_dir, percentage):

    for class_name in classes:

        # Source class folder
        source_class = source_dir / class_name

        # Destination class folder
        destination_class = destination_dir / class_name
        destination_class.mkdir(parents=True, exist_ok=True)

        # Get all image files
        images = [
            f for f in source_class.iterdir()
            if f.is_file() and f.suffix.lower() in
            [".jpg", ".jpeg", ".png", ".webp"]
        ]

        # Shuffle images
        random.shuffle(images)

        # Calculate number of images
        total_images = int(len(images) * percentage)

        # Select required images
        selected_images = images[:total_images]

        # Copy images
        for image in selected_images:
            shutil.copy2(image, destination_class / image.name)

        print(
            f"{class_name}: "
            f"{len(selected_images)} / {len(images)} images copied"
        )


# 1. Create 10% training dataset
create_subset(
    base_dir / "train",
    base_dir / "train_10_percent",
    0.10
)

# 2. Create 20% training dataset
create_subset(
    base_dir / "train",
    base_dir / "train_20_percent",
    0.20
)

# 3. Create 10% testing dataset
create_subset(
    base_dir / "test",
    base_dir / "test_10_percent",
    0.10
)

print("\nDataset splitting completed!")
