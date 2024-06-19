import tkinter as tk

def open_window():
    window = tk.Toplevel(root)
    window.title("Fraction to Decimal Conversion")
    window.geometry("400x400")

    # Define some colors
    bg_color = "#40E0D0"
    entry_bg_color = "#FF0000"
    button_bg_color = "#ADD8E6"

    # Create the GUI elements
    label1 = tk.Label(window, text="Enter numerator:")
    label1.pack()

    entry1 = tk.Entry(window, bg=entry_bg_color)
    entry1.pack()

    label2 = tk.Label(window, text="Enter denominator (enter 0 to quit):")
    label2.pack()

    entry2 = tk.Entry(window, bg=entry_bg_color)
    entry2.pack()

    button = tk.Button(window, text="Calculate", bg=button_bg_color, command=lambda: calculate(entry1, entry2, result_text))
    button.pack()

    result_label = tk.Label(window, text="Result:", bg=bg_color)
    result_label.pack()

    result_text = tk.Text(window, height=10, width=50, bg=entry_bg_color)
    result_text.pack()

    # Set the background colors
    window.configure(bg=bg_color)
    for child in window.winfo_children():
        child.configure(bg=bg_color)

def calculate(entry1, entry2, result_text):
    x = int(entry1.get())
    y = int(entry2.get())

    result_text.delete(1.0, tk.END)

    if y == 0:
        return

    # Find the decimal representation of the fraction
    decimal = x / y
    decimal_str = str(decimal)
    integer_part, fraction_part = decimal_str.split(".")

    # Find the repeating decimal representation
    repeating_part = fraction_part[0:2]
    l = len(fraction_part)
    for i in range(2, l):
        if fraction_part[i] == repeating_part[0]:
            break
        else:
            repeating_part = repeating_part + fraction_part[i]

    output = integer_part + "." + repeating_part
    # Format the output string
    if repeating_part == "":
        output_str = f"{x} \n{'-' * len(str(x))} = {decimal_str} \n{y}"
    else:
        output_str = f"{x} {' ' * (3 + len(integer_part))} {'-' * (len(repeating_part) - 1)} \n{'-' * len(str(x))} = {output} \n{y}"

    result_text.insert(tk.END, output_str + '\n')

#create a main window
root = tk.Tk()
root.title("Repeating Decimals")
root.configure(bg = "#8601AF")
# Create the heading
heading_label = tk.Label(root, text="Repeating Decimals", font=("Arial", 90, "bold"), bg="#8601AF")
heading_label.pack(pady=200)


button = tk.Button(root, text="Proceed", command=open_window, font=("Arial", 35))
button.pack()

root.mainloop()
