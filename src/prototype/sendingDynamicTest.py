import time
from picamera2 import Picamera2, Preview
import subprocess

picam = Picamera2()
config = picam.create_preview_configuration()
picam.configure(config)

# Start the camera preview
picam.start_preview(Preview.QTGL)
picam.start()
destination = "unicorn_jesus@192.168.77.189:/home/unicorn_jesus/pCloudDrive/TecStorm/images"

try:
    while True:
        # Generate a timestamped filename for each capture
        filename = time.strftime("image-%Y%m%d-%H%M%S.jpg")
        full_path = f"/home/tecstorm/Desktop/Tecstorm/{filename}"
        scp_command = f"scp {full_path} {destination}"
        print(full_path, scp_command)
        picam.capture_file(filename)
        print("B")
        # Call the transfer script to send the captured image
        transfer_script = "transfer.sh"  # Update with the path to transfer.sh
        transfer_process = subprocess.Popen(["bash", transfer_script, full_path])
        transfer_process.wait()  # Wait for the transfer to complete

        # Wait for 10 seconds between captures
        time.sleep(10)
        print("A")

except KeyboardInterrupt:
    # Stop the loop with a keyboard interrupt (Ctrl+C)
    print("Stopping camera capture.")

finally:
    # Ensure the camera is properly closed
    picam.close()

