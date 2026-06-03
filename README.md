# PCB Solder Defect Classifier 🔬

A machine learning-based inspection system designed to automatically classify and locate defects in printed circuit board (PCB) solder joints. Developed as a BSIT capstone project at Colegio De San Gabriel Archangel, this application provides a full-stack solution from image upload to real-time AI inference and bounding-box rendering.

##  Features
* **Real-Time Inference:** Upload images (JPG/PNG) and receive instant classification using a custom-trained AI model.
* **Bounding Box Detection:** Automatically draws precise bounding boxes around identified defects (e.g., Solder Bridges, Spikes, Insufficient Solder).
* **Confidence Scoring:** Displays the model's certainty percentage for every detected flaw.
* **Inspection Dashboard:** Tracks total images analyzed, defect counts, and most common issues.
* **Modern UI:** A clean, responsive, single-page interface built with React.

##  Tech Stack
* **Frontend:** React (bundled via `esbuild`), HTML5, CSS3
* **Backend:** Python 3.12, FastAPI, Uvicorn
* **Machine Learning:** Ultralytics (YOLOv8)
* **Image Processing:** Pillow (PIL)

##  Project Structure
```text
my-pcb-app/
├── main.py                          # FastAPI backend server
├── requirements.txt                 # Python dependencies
├── best.pt                          # Trained YOLOv8 model weights
└── static/
    ├── index.html                   # Main HTML entry point
    ├── PCBSolderDefectClassifier.jsx # React frontend source code
    └── bundle.js                    # Compiled JavaScript (generated)
1. Backend Setup
Clone the repository and set up your Python virtual environment:

PowerShell
# Create a virtual environment using Python 3.12
py -3.12 -m venv venv

# Activate the virtual environment (Windows)
.\venv\Scripts\activate

# Install the required ML and server dependencies
pip install -r requirements.txt
2. Frontend Setup
Install the required React packages and compile the interface:

PowerShell
# Install React dependencies
npm install react react-dom

# Bundle the JSX file into standard JavaScript
npx esbuild static/PCBSolderDefectClassifier.jsx --bundle --outfile=static/bundle.js --loader:.jsx=jsx --jsx=automatic
Note: You must re-run this esbuild command anytime you make changes to the .jsx file.

3. Running the Application
Start the FastAPI server:

PowerShell
python main.py
