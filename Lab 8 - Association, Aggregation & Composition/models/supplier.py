class Supplier:
    def __init__(self, supplier_id, name, contact_email):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email
    
    def display_info(self):
        return (
            f"Supplier ID: {self.supplier_id}\n"
            f"Name: {self.name}\n"
            f"Contact Email: {self.contact_email}\n"
        )
    