import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_classification_report(file_path=r"C:\Users\anish\OneDrive\Desktop\Coding\Python\PBL\project1\output.csv"):
    '''
    Reads the classification report from a CSV file and visualizes it.
    '''
    try:
        df_report = pd.read_csv(file_path, index_col=0)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found. Please ensure train_model.py has been run to generate it.")
        return

    # Drop the 'accuracy' row if it exists, as it's a summary, not per-class metric
    if 'accuracy' in df_report.index:
        df_report = df_report.drop('accuracy')

    # Drop 'macro avg' and 'weighted avg' for per-class visualization
    df_report = df_report.drop(columns=['support'], errors='ignore')
    df_report = df_report.drop(index=['macro avg', 'weighted avg'], errors='ignore')

    # Plotting precision, recall, f1-score
    df_report.plot(kind='bar', figsize=(15, 7))
    plt.title('Classification Report Metrics per Crop')
    plt.ylabel('Score')
    plt.xlabel('Crop')
    plt.xticks(rotation=45, ha='right')
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.savefig('project1_output.png')
    plt.show()

if __name__ == '__main__':
    visualize_classification_report()
