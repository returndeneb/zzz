from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

def generate_caption(image_path):
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    caption = model.generate(**inputs)
    print("Generated Caption:", processor.decode(caption[0], skip_special_tokens=True))

if __name__ == "__main__":
    image_path = "input_image.png"
    generate_caption(image_path)
