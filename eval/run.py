import csv
import os

# Import hàm hoặc module xử lý chính từ thư mục src của bạn
# (Hãy điều chỉnh import theo đúng cấu trúc code thực tế trong thư mục src)
# from src.main import process_input 

def run_benchmark():
    csv_path = os.path.join(os.path.dirname(__file__), 'cases.csv')
    
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    correct = 0
    total = 0

    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += 1
            input_data = row.get('input')
            expected = row.get('expected_output')
            
            # --- Thay thế dòng này bằng hàm gọi mô hình/logic thực tế của bạn ---
            # actual_output = process_input(input_data)
            actual_output = input_data  # Giả định kết quả
            # -------------------------------------------------------------------

            if actual_output == expected:
                correct += 1

    if total == 0:
        print("No test cases found.")
        return

    accuracy = (correct / total) * 100
    print(f"Benchmark Results: {correct}/{total} correct")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    run_benchmark()