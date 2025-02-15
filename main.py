import os
from PIL import Image
import torch
import clip
import numpy as np  # <-- Make sure to import NumPy for similarity calculations

# (Assuming that you already have these from Step 1)
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def index_images(image_folder):
    """
    Scans the provided folder for images, preprocesses them, computes their embeddings,
    and returns a dictionary mapping image file paths to their embeddings.
    """
    # Supported image extensions
    valid_extensions = (".png", ".jpg", ".jpeg", ".bmp", ".gif")
    
    # Gather all image file paths in the folder
    image_paths = [
        os.path.join(image_folder, filename)
        for filename in os.listdir(image_folder)
        if filename.lower().endswith(valid_extensions)
    ]
    
    # Dictionary to hold image path -> embedding mapping
    image_embeddings = {}
    
    # Process each image
    for path in image_paths:
        try:
            # Load the image and convert to RGB (if not already)
            image = Image.open(path).convert("RGB")
            # Preprocess the image as required by CLIP
            image_input = preprocess(image).unsqueeze(0).to(device)
            # Compute the embedding (no gradient calculation needed)
            with torch.no_grad():
                embedding = model.encode_image(image_input)
            # Normalize the embedding for consistent similarity comparisons
            embedding = embedding / embedding.norm(dim=-1, keepdim=True)
            # Save the embedding in CPU memory (as a NumPy array)
            image_embeddings[path] = embedding.cpu().numpy()
        except Exception as e:
            print(f"Error processing {path}: {e}")
    
    return image_embeddings

def search_images(query, image_embeddings, top_k=10):
    """
    Given a text query and a dictionary of precomputed image embeddings,
    this function returns the top_k image paths that best match the query,
    filtering out results with a similarity score <= 0.2.
    """
    # Tokenize the query and compute its embedding using CLIP's text encoder.
    text_tokens = clip.tokenize(query).to(device)
    with torch.no_grad():
        text_embedding = model.encode_text(text_tokens)
    
    # Normalize the text embedding to ensure consistent similarity comparisons.
    text_embedding = text_embedding / text_embedding.norm(dim=-1, keepdim=True)
    text_embedding = text_embedding.cpu().numpy()  # Move to CPU for NumPy operations
    
    # Compute cosine similarity between the query and each image embedding.
    similarities = []
    for path, embedding in image_embeddings.items():
        # Since embeddings are normalized, the dot product is equivalent to cosine similarity.
        similarity = np.dot(embedding, text_embedding.T).item()
        if similarity > 0.2:  # Filter out low-score images
            similarities.append((path, similarity))
    
    # Sort the images by similarity in descending order.
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    return similarities[:top_k]  # Return the top-k results that meet the threshold


# For testing the complete functionality:
if __name__ == "__main__":
    # Replace this with the path to your image folder
    image_folder = "D:/Pachmari/images"
    
    # Call the indexing function and retrieve embeddings
    embeddings = index_images(image_folder)
    
    # Print out the indexed image paths (and optionally check their embedding shapes)
    print("Indexed images:")
    for path, embedding in embeddings.items():
        print(f"{path} - Embedding shape: {embedding.shape}")
    
    # Now prompt the user for a search query
    user_query = input("Enter your search query: ")
    
    # Retrieve the top matching images
    top_matches = search_images(user_query, embeddings, top_k=5)
    
    # Display the results
    print("\nTop matching images:")
    for path, score in top_matches:
        print(f"{path} - Similarity: {score:.4f}")
