class TravelPartner:
    def __init__(self):
        self.destinations = {
            "1": {
                "persona": "Culture & History Buff",
                "location": "Egypt (Cairo & The Nile)",
                "areas": ["Giza Pyramids", "Luxor (Valley of the Kings)", "Aswan Nile Cruise"]
            },
            "2": {
                "persona": "Nature & Adventure Seeker",
                "location": "Patagonia (Chile & Argentina)",
                "areas": ["Torres del Paine", "El Chaltén (Fitz Roy)", "Perito Moreno Glacier"]
            },
            "3": {
                "persona": "Food & City Explorer",
                "location": "Mexico City, Mexico",
                "areas": ["Roma Norte & Condesa", "Coyoacán (Frida Kahlo House)", "Centro Histórico"]
            },
            "4": {
                "persona": "Zen & Spiritual Traveler",
                "location": "Bali, Indonesia",
                "areas": ["Ubud Rice Terraces", "Sidemen Village", "Uluwatu Temple"]
            }
        }

    def start_planning(self):
        print("--- ✈️ Welcome to your Travel suggestion partner! ---")
        print("What kind of traveler are you today?\n")
        
        for key, data in self.destinations.items():
            print(f"{key}. {data['persona']}")

        choice = input("\nSelect a number (1-4): ")

        if choice in self.destinations:
            dest = self.destinations[choice]
            print(f"\n✨ Excellent choice! For a {dest['persona']}, I recommend: **{dest['location']}**")
            print("-" * 50)
            print("Famous areas you MUST visit to make it memorable:")
            for area in dest["areas"]:
                print(f"📍 {area}")
            print("-" * 50)
            print("Pack your bags🧳! And have a safe flight ✈️")
        else:
            print("\n❌ Invalid choice. Please restart and pick a valid persona!")

# Run the program
if __name__ == "__main__":
    my_itinerary_partner = TravelPartner()
    my_itinerary_partner.start_planning()