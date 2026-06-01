import numpy as np

def normalized_array(data):
    """
    מנרמלת מערך נתונים לטווח של [0, 1] לפי שיטת Min-Max Scaling.

    נוסחה לביצוע:
    x_norm = (x - min) / (max - min)

    פרמטרים:
    data (list or np.array): מערך של מספרים.

    החזרה:
    מערך מנורמל. אם כל הערכים במערך זהים, יש להחזיר מערך של אפסים. np.array
    """
    # לצורך חישובים וקטוריים numpy array-המרת הקלט ל
    data = np.array(data)

    # --- כיתבו את הקוד שלכם כאן ---
    
    # בדיקה מהירה אם המערך ריק לחלוטין
    if data.size == 0:
        return np.array([])
        
    # חילוץ ערך המינימום וחישוב הטווח (מקסימום פחות מינימום)
    minimum = data.min()
    data_range = data.max() - minimum
    
    # טיפול במצב שבו כל האיברים במערך זהים (טווח אפס)
    if data_range == 0:
        return np.zeros(data.shape)
        
    # ביצוע הנרמול והחזרת המערך החדש
    return (data - minimum) / data_range

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
