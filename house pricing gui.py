import tkinter as tk
from tkinter import ttk, messagebox
import joblib
import pandas as pd

# Load the saved model
model_path = "C:/Users/DELL/Desktop/ds tools/final project/projeto/house_pricing_model.pkl"
model = joblib.load(model_path)

# Initialize Tkinter
root = tk.Tk()
root.title("House Price Prediction")

# Set window size and background color
root.geometry("600x400")
root.configure(bg="#F4F4F9")

# Define input variables
rooms_var = tk.IntVar()
bathrooms_var = tk.IntVar()
area_var = tk.DoubleVar()
property_var = tk.StringVar()
city_var = tk.StringVar()
ownership_var = tk.StringVar()
furnishing_var = tk.StringVar()
building_status_var = tk.StringVar()

# Dropdown options
property_options = ["Apartment", "Chalet", "Duplex", "Penthouse", "Townhouse", "Twin House"]
city_options = ["Cairo", "Giza", "Matrouh", "Suez"]
ownership_options = ["First Residence", "Resale"]
furnishing_options = ["Furnished", "Unfurnished"]
building_status_options = ["ready", "under construction"]

# Helper function to style widgets
def style_widget(widget):
    widget.config(font=("Arial", 12), bd=0, relief="flat", highlightthickness=0)

# Input fields
tk.Label(root, text="Rooms", bg="#F4F4F9").grid(row=0, column=0, padx=10, pady=10)
rooms_entry = tk.Entry(root, textvariable=rooms_var)
style_widget(rooms_entry)
rooms_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Bathrooms", bg="#F4F4F9").grid(row=1, column=0, padx=10, pady=10)
bathrooms_entry = tk.Entry(root, textvariable=bathrooms_var)
style_widget(bathrooms_entry)
bathrooms_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Area", bg="#F4F4F9").grid(row=2, column=0, padx=10, pady=10)
area_entry = tk.Entry(root, textvariable=area_var)
style_widget(area_entry)
area_entry.grid(row=2, column=1, padx=10, pady=10)

# Dropdown menus
tk.Label(root, text="Property Type", bg="#F4F4F9").grid(row=3, column=0, padx=10, pady=10)
property_menu = ttk.Combobox(root, textvariable=property_var, values=property_options)
property_menu.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root, text="City", bg="#F4F4F9").grid(row=4, column=0, padx=10, pady=10)
city_menu = ttk.Combobox(root, textvariable=city_var, values=city_options)
city_menu.grid(row=4, column=1, padx=10, pady=10)

tk.Label(root, text="Ownership", bg="#F4F4F9").grid(row=5, column=0, padx=10, pady=10)
ownership_menu = ttk.Combobox(root, textvariable=ownership_var, values=ownership_options)
ownership_menu.grid(row=5, column=1, padx=10, pady=10)

tk.Label(root, text="Furnishing", bg="#F4F4F9").grid(row=6, column=0, padx=10, pady=10)
furnishing_menu = ttk.Combobox(root, textvariable=furnishing_var, values=furnishing_options)
furnishing_menu.grid(row=6, column=1, padx=10, pady=10)

tk.Label(root, text="Building Status", bg="#F4F4F9").grid(row=7, column=0, padx=10, pady=10)
building_status_menu = ttk.Combobox(root, textvariable=building_status_var, values=building_status_options)
building_status_menu.grid(row=7, column=1, padx=10, pady=10)

# Prediction function
def predict_price():
    try:
        # Prepare input data without normalization (no scaling applied to area)
        features = [
            rooms_var.get(),
            bathrooms_var.get(),
            area_var.get(),  # Use area directly without scaling
            int(property_var.get() == "Apartment"),
            int(property_var.get() == "Chalet"),
            int(property_var.get() == "Duplex"),
            int(property_var.get() == "Penthouse"),
            int(property_var.get() == "Townhouse"),
            int(property_var.get() == "Twin House"),
            int(building_status_var.get() == "ready"),
            int(building_status_var.get() == "under construction"),
            int(furnishing_var.get() == "Furnished"),
            int(furnishing_var.get() == "Unfurnished"),
            int(ownership_var.get() == "First Residence"),
            int(ownership_var.get() == "Resale"),
            int(city_var.get() == "Cairo"),
            int(city_var.get() == "Giza"),
            int(city_var.get() == "Matrouh"),
            int(city_var.get() == "Suez"),
        ]
        
        # Column names for the model (should match the feature order used in training)
        feature_columns = [
            "Rooms", "Bathrooms", "Area", "Property Type_Apartment", "Property Type_Chalet", 
            "Property Type_Duplex", "Property Type_Penthouse", "Property Type_Townhouse", 
            "Property Type_Twin House", "Building Status_ready", "Building Status_under construction", 
            "Furnishing_Furnished", "Furnishing_Unfurnished", "Ownership_First Residence", 
            "Ownership_Resale", "City_Cairo", "City_Giza", "City_Matrouh", "City_Suez"
        ]
        
        # Create a DataFrame with the same columns as the model was trained on
        input_data = pd.DataFrame([features], columns=feature_columns)
        
        # Predict price
        price_prediction = model.predict(input_data)[0]
        
        # Show prediction in a message box
        messagebox.showinfo("Prediction Result", f"Predicted Price: {price_prediction:.2f}")
        
    except Exception as e:
        # Show error in a message box
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Prediction button
predict_button = tk.Button(root, text="Predict Price", command=predict_price, bg="#00BFFF", fg="white", font=("Arial", 12), relief="flat")
predict_button.grid(row=8, column=0, columnspan=2, pady=20)

# Start GUI
root.mainloop()
