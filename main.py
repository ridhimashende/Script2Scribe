from PIL import Image, ImageDraw, ImageFont
import random

class ManualWriter:
    def __init__(self):
        self.W = 2480  # A4 width 300 DPI
        self.H = 3508  # A4 height
        self.margin = 200

    def create_page(self, text, output="Page85_LVDT.png"):
        # White A4 page
        img = Image.new('RGB', (self.W, self.H), 'white')
        draw = ImageDraw.Draw(img)

        # Load font - if ttf not found, default will be used
        try:
            font = ImageFont.truetype("arial.ttf", 65)
        except:
            font = ImageFont.load_default()

        x, y = self.margin, self.margin
        line_height = 110

        # Draw light blue ruled lines like manual
        for ly in range(self.margin, self.H, line_height):
            draw.line([(80, ly), (self.W-80, ly)], fill=(180, 200, 255), width=2)

        # Write text like blue pen
        for word in text.split():
            rx = random.randint(-2, 2)
            ry = random.randint(-3, 3)
            draw.text((x+rx, y+ry), word + " ", font=font, fill=(10, 20, 150))
            
            x += len(word) * 38
            if x > self.W - self.margin - 200:
                x = self.margin
                y += line_height
                if y > self.H - 250:
                    break

        img.save(output)
        print(f"Done! Saved: {output}")

# ---- TERA DATA YAHAN DAAL ----
if __name__ == "__main__":
    practical_answer = """
    XIV Observations and Calculations Page 85
    Sr No Positive Displacement Output Voltage Negative Displacement Output Voltage
    1 Null Position 0mm 0.00V Null Position 0mm 0.00V
    2 1mm 0.42V 1mm 0.41V
    3 2mm 0.86V 2mm 0.85V
    4 3mm 1.25V 3mm 1.24V
    5 4mm 1.68V 4mm 1.67V
    6 5mm 2.10V 5mm 2.08V
    7 7.5mm 2.95V 7.5mm 2.92V
    8 10mm 3.80V 10mm 3.76V
    
    XV Results Sensitivity 0.42 V per mm Null voltage 0V
    XVI Interpretation Output voltage directly proportional to displacement
    XVII Conclusion LVDT is linear transducer for small displacement
    """

    writer = ManualWriter()
    writer.create_page(practical_answer)
