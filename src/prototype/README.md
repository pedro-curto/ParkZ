## Prototype

This prototype represents an early stage of development for the ParkZ project. Please note that it is incomplete and contains scattered scripts.

The production code for ParkZ was left at the competition and is not included in this repository.

For more information about the ParkZ project, please refer to the competition documentation.

## Concept

- Our prototype uses the `yolov8n` model to detect hotwheel cars in a parking lot (in our case, a mockup made with a printed sheet with parking slots)
- A script captured the images through a Raspberry Pi camera and sent these images to another computer, where they were processed
and a preview would appear with the associated bounding boxes, labels, and confidence scores, along with some output in the 
terminal window

