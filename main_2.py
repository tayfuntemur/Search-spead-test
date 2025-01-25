import time

class PhoneDirectory:
    def __init__(self):
        # Veri yapıları
        self.list_directory = []
        self.dict_directory = {}
        self.sorted_directory = []

    def add_contact(self, name, phone):
        # Liste
        self.list_directory.append((name, phone))
        
        # Hash Tablosu (Sözlük)
        self.dict_directory[name] = phone
        
        # Sıralı Liste
        self.sorted_directory.append((name, phone))
        self.sorted_directory.sort(key=lambda x: x[0])  # İsme göre sırala

    def linear_search(self, name):
        start_time = time.time()
        for contact in self.list_directory:
            if contact[0].lower() == name.lower():
                end_time = time.time()
                return contact, (end_time - start_time) * 1000
        end_time = time.time()
        return None, (end_time - start_time) * 1000

    def dict_search(self, name):
        start_time = time.time()
        if name in self.dict_directory:
            end_time = time.time()
            return (name, self.dict_directory[name]), (end_time - start_time) * 1000
        end_time = time.time()
        return None, (end_time - start_time) * 1000

    def binary_search(self, name):
        start_time = time.time()
        left, right = 0, len(self.sorted_directory) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_name = self.sorted_directory[mid][0]

            if mid_name.lower() == name.lower():
                end_time = time.time()
                return self.sorted_directory[mid], (end_time - start_time) * 1000
            elif mid_name.lower() < name.lower():
                left = mid + 1
            else:
                right = mid - 1

        end_time = time.time()
        return None, (end_time - start_time) * 1000

def main():
    directory = PhoneDirectory()

    # Örnek kontakları ekle
    contacts = [
        ("Tayfun Temur", "05321112233"),
        ("Murat Bardakci", "05542223344"),
        ("Betül Koç", "05453334455"),
        ("Elif Turan", "05554445566")
    ]

    directory.add_contact("kemal sunal","05432345376")
    for name, phone in contacts:
        directory.add_contact(name, phone)

    # Arama işlemi
    search_name = input("Aramak istediğiniz ismi girin: ")

    # Arama sonuçları
    linear_result, linear_time = directory.linear_search(search_name)
    dict_result, dict_time = directory.dict_search(search_name)
    binary_result, binary_time = directory.binary_search(search_name)

    print("\nArama Sonuçları:")
    print(f"Linear Search: {linear_result}, Süre: {linear_time:.4f} ms")
    print(f"Dictionary Search: {dict_result}, Süre: {dict_time:.4f} ms")
    print(f"Binary Search: {binary_result}, Süre: {binary_time:.4f} ms")

if __name__ == "__main__":
    main() 