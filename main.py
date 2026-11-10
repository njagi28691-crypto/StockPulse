"""
StockPulse : Inventory & Sales Intelligence Engine
Main CLI Entry Point & Menu Router
"""
from py_compile import main
import sys

def print_banner():
  print("=" * 65)
  print(f"{'STOCKPULSE : INVENTORY & SALES INTELLIGENCE':^65 }")
  print("=" * 65)

  def print_menu():
    print("\n[1] View Inventory Catalog")
    print("[2] Add New Products")
    print("[3] Update Stock Quantity")
    print("[4] Search Product (Case-Insesitive)")
    print("[5] Record a sale (Generates Tuple Audit)")
    print("[6] View Sales Report & Analytics")
    print("[7] Exit program")
    print("-" * 65)

  def get_validated_choice():
    """Ensure menu selection is a valid interger between 1 and 7."""
    while True:
        try:
            choice = int(input("Select an option (1-7): ").strip())
            if 1<= choice <=7:
                return choice
            print("❌ Invalid choice. Please enter a number between 1 and 7.")
        except ValueError:
           print("❌ Invalid input. Please enter a numeric digit.")

  def main():
      inventory_db = {
        "SKU001" : {"NAME": "Maize Flour 2kg", "price":140.0, "stock": 45, "category": "Grains"},
        "SKU002" :{"NAME": "Cooking Oil 1L", "price": 320.0, "stock": 20,"category": "Pantry"},
        "SKU003" :{"NAME": "Sugar 1 KG", "price":130.0,"stock": 30, "category": "Grains"}
      }

      sales_log = []

      print_banner()
      while True:
         print_menu()
         choice = get_validated_choice()

         if choice == 1:
            print("\n📦---CURRENT INVENTORY CATALOG---")
              #TODO:
            print("[Stub]Displaying inventory table...")

         elif choice == 2:
            print("\n---ADD NEW PRODUCT ---")
            sku = input("Enter SKU (e.g., SKU004): ").strip().upper()
            name = input("Enter Product Name: ").strip()

            try:
               price = float(input("Enter Price (KES): ").strip())
            except ValueError:
               print("❌ Error: Price must be a decimal and stock must be a whole number.")
               continue
            category = input("Enter Category: ").strip()
            # TODO:
            print(f"[stub] SUccessfully prepated to add {name} under SKU {sku}.")

         elif choice == 3:
              print("\n---UPDATE STOCK QUANTITY ---")
              sku = input("ENter SKU to update: ").strip().upper()
              # TODO:
              print(f"[stub] Stock adjustment routine for {sku} initiated.")

         elif choice == 4:
              print("\n---SEARCH PRODUCT ---")
              query = input("Enter product name or keyword to search: ").strip()
              # TODO:
              print(f"[stub] Searching inventory for keyword: '{query}'")

         elif choice == 5:
              print("\n🛒---RECORD A SALE ---")
              sku = input("Enter SKU sold: ").strip().upper()
              try:
                  qty = int(input("Enter quantity sold: ").strip())
              except ValueError:
                 print("❌ Error: Quantity must be a valid integer.")
                 continue
              #TODO:
              print(f"[Stub] Sale recorded for {qty} units of {sku}.")

         elif choice == 6:
            print("\n📊---SALES REPORT & ANALYTICS ---")
            # TODO:
            print("[Stub] Generating sales and inventory analytics summary ...")

         elif choice == 7:
            print("\nExiting StockPulse. saving session data ... Goodbye!")
            sys.exit(0)

         print("\n" + "-" *65)
         input("Press Enter to return to the main menu...")

if __name__ == "__main__" :
    main()

      



                 




        







      
