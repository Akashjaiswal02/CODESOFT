#****** CALCULATOR ******

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = entry_operation.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero!"
        else:
            result = "Invalid operation."

        label_result.config(text=f"Result: {str(result)}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please check your entries.")

root = tk.Tk()
root.title("Simple Calculator")

label_num1 = tk.Label(root, text="Enter the first number:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter the second Number:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

label_operation = tk.Label(root, text="Enter the operation (+, -, *, /):")
label_operation.pack()
entry_operation = tk.Entry(root)
entry_operation.pack()

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()

label_result = tk.Label(root, text="Result: ")
label_result.pack()

root.mainloop()