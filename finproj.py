materials = dict()
 
with open("materials.csv") as file:
	table = file.read()
 
rows = table.split("\n")
 
x=0
 
for row in rows:
	materials[x] = row
	column = row.split(",")
	x = x + 1
 
for key, value in materials.items():
	print(f'{key}: {value}')
 
materials_table = {}
 
def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Tensile strength must be a positive number.")
            else:
                return value
        except ValueError:
            print("Error: Please enter a valid number.")
			
#1

def add_material():
    name = input("Material Name: ").strip()
 
    if name in materials:
        choice = input("Material already exists. Do you want to update it? (yes/no): ").lower()
        if choice == "yes":
            new_strength = int(input("Enter new tensile strength (MPa): "))
            materials[name] = new_strength
            print(f"{name} updated successfully.")
        else:
            print("No changes made.")
    else:
        strength = int(input("Tensile Strength (MPa): "))
        materials[name] = strength
        print("Material added successfully!")
 
#2

def view_strongest_material():
    if not materials_table:
        print("No materials available.")
        return
 
    try:
        strongest = max(materials_table, key=materials_table.get)
        print(f"Strongest material: {strongest} ({materials_table[strongest]} MPa)")
 
    except Exception as x:
        print("Error determining strongest material:", x)
        print("Current data:", materials_table)

#3
 
def update_material():
    name = input("Enter the material name to update: ").strip()
 
    if name in materials:
        new_strength = int(input("Enter new tensile strength (MPa): "))
        materials[name] = new_strength
        print(f"{name} updated successfully.")
 
    else:
        print("Material not found.")
        choice = input("Do you want to add it? (yes/no): ").lower()
 
        if choice == "yes":
            strength = int(input("Enter tensile strength (MPa): "))
            materials[name] = strength
            print(f"{name} added successfully.")
#4
 
def delete_material():
    name = input("Enter the material to delete: ").strip()
 
    if name in materials:
        del materials[name]
        print(f"{name} has been deleted.")
 
    else:
        print("Material not found.")

#5









#6










#7









#8





 
while True:
    print("\n=== Material Strength Calculator ===")
    print("1. Add Material")
    print("2. View Strongest Material")
    print("3. Update Material")
    print("4. Delete Material")
    print("5. Display All Materials")
    print("6. Save to CSV")
    print("7. Load from CSV")
    print("8. Exit")
 
    choice = input("Enter your choice: ")
 
    if choice == "1":
    	add_material()
    elif choice == "2":
    	view_strongest_material()
    elif choice == "3":
    	update_material()
    elif choice == "4":
    	delete_material()
    elif choice == "5":
    	sort_choice = input("Sort by (name/strength)? ").lower()
    	view_materials(sort_by=sort_choice)
    elif choice == "6":
    	save_to_csv()
    elif choice == "7":
    	load_from_csv()
    elif choice == "8":
    	exit_program()
 
else:
	print("Invalid choice. Please select 1–8.")
