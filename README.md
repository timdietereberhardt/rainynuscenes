# RainyNuScenes: A Data Partition for Benchmarking Contaminated Vehicle Cameras through Rain

This repository contains the official Python implementation for the research paper **"RainyNuScenes: A Data Partition for Benchmarking Contaminated Vehicle Cameras through Rain."** 

## 📌 Overview
RainyNuScenes is a novel dataset designed to benchmark the impact of **water droplets on vehicle-mounted cameras** in Advanced Driver Assistance Systems (**ADAS**). The dataset is an extension of the widely-used **NuScenes dataset**, featuring **762 annotated images** with over **1,700 labeled water droplets**, enabling precise evaluation of their effects on perception systems.

### 🔬 Research Focus
This work addresses the challenges posed by **adverse weather conditions**, particularly rain, on camera-based perception systems. We provide:
- A **detailed dataset** for water droplet detection and segmentation.
- A **comparative analysis** with related datasets like **WoodScape**.
- Benchmarking of **CNN-based segmentation models** trained on RainyNuScenes and other datasets.
- Insights into **model generalizability and robustness** for real-world ADAS applications.

## 📂 Repository Contents
- **`data/`** – Dataset and annotations (or instructions to access them).
- **`models/`** – Pre-trained models for droplet detection and segmentation.
- **`notebooks/`** – Jupyter notebooks for visualization and analysis.
- **`src/`** – Implementation of training, evaluation, and benchmarking scripts.
- **`README.md`** – This documentation file.

## License
This project is licensed under the license of NuScenes https://www.nuscenes.org/terms-of-use


## Getting Started
### Installation
Required dependencies (see `requirements.txt`)

Clone the repository and install dependencies:
```bash
git clone https://github.com/timdietereberhardt/rainynuscenes.git
cd rainynuscenes
pip install -r requirements.txt

## Getting Started
### Prerequisites
Required dependencies (see `requirements.txt`)
