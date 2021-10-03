# SURFACE-HRC-DETECTION
Dataset: NEU surface detection Hot roll coil
  1800 image grayscale
  300 image for each sample
  size 200x200 pixels
  6 labels
    rolled-in scale (RS)
    patches (Pa)
    crazing (Cr)
    pitted surface (PS)
    inclusion (In)
    scratches (Sc)
Extract annimation
  python extractAnnimationNEU-DET.py
 or
  EXTRACT ANNIMATION NEU SURFACE HRC.ipynb for notebook


#DEEP LEARNING MODEL
-multi class object detection
  - keras, tensorflow
  - CNNs, R-CNN
  - sigle class detected for earch image -> multiple
  - pretrain VGG16
  
