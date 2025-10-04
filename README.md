# Smart Crop Recommendation 🌱

A machine learning project that recommends the most suitable crop to grow based on soil and environmental conditions.  

---

## 📌 Features
- Data preprocessing and cleaning  
- Trained ML model for crop recommendation  
- Saved model and encoder for quick predictions  
- Inference script to predict crops from user input  
- Visualization scripts for data insights  

---

## 📂 Project Structure
```
├── Crop_Recommendation(in).csv        # Dataset  
├── crop_encoder.joblib                # Saved encoder  
├── crop_recommendation_model.joblib   # Trained ML model  
├── diagrams.py                        # Visualization script  
├── inference.py                       # Inference / prediction script  
├── preprocessing.py                   # Preprocessing logic  
├── output.csv                         # Sample prediction output  
├── project1_output.png                # Example plot  
└── statement                          # Project description / notes  
```

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.7+  
- Recommended libraries:  
  ```
  numpy
  pandas
  scikit-learn
  matplotlib
  seaborn
  joblib
  ```

### Installation
```bash
# Clone repository
git clone https://github.com/Anishp-cell/Smart-crop-recommendation.git
cd Smart-crop-recommendation

# (Optional) create virtual environment
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## 🚀 Usage

1. **Preprocess data**
   ```bash
   python preprocessing.py
   ```

2. **Run inference (predict crop)**
   ```bash
   python inference.py
   ```

3. **Generate visualizations**
   ```bash
   python diagrams.py
   ```

Predictions are saved in `output.csv`.

---

## 📊 Model & Data
- **Dataset:** `Crop_Recommendation(in).csv`  
- **Model:** `crop_recommendation_model.joblib`  
- **Encoder:** `crop_encoder.joblib`  
- **Output:** Recommended crops stored in `output.csv`

---

## 🤝 Contributing
1. Fork the repo  
2. Create a feature branch (`feature/new-idea`)  
3. Commit your changes  
4. Push to your fork  
5. Open a Pull Request  

---

## 📜 License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact
- Author: **Anishp-cell**  
- GitHub: [Smart Crop Recommendation](https://github.com/Anishp-cell/Smart-crop-recommendation)
