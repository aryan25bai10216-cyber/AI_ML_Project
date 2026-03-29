# ✈️ TravelPartner Suggestion Tool

A lightweight, object-oriented Python application that acts as a personalized travel consultant. By selecting a "Traveler Persona," users receive curated recommendations for world-class locations and must-visit landmarks.

## 🌟 Features

* **Persona-Based Logic:** Tailored suggestions for History Buffs, Nature Seekers, Foodies, and Spiritual Travelers.
* **Dynamic Mapping:** Uses a structured dictionary to map personas to specific regions and lists of attractions.
* **Interactive CLI:** A simple, user-friendly command-line interface for input and output.
* **Clean Architecture:** Written using Python Classes for better scalability and organization.

---

## 🗺️ How It Works

The program initializes a `TravelPartner` class containing a database of destinations. When executed, it:
1.  Displays a list of available **Traveler Personas**.
2.  Prompts the user to select a number corresponding to their vibe.
3.  Fetches and prints the recommended **Country/City** and a **Must-Visit** list of areas.

### Sample Output:
```text
--- ✈️ Welcome to your Travel suggestion partner! ---
What kind of traveler are you today?

1. Culture & History Buff
2. Nature & Adventure Seeker
3. Food & City Explorer
4. Zen & Spiritual Traveler

Select a number (1-4): 2

✈️ Excellent choice! For a Nature & Adventure Seeker, I recommend: **Patagonia (Chile & Argentina)**
--------------------------------------------------
Famous areas you MUST visit to make it memorable:
📍 Torres del Paine
📍 El Chaltén (Fitz Roy)
📍 Perito Moreno Glacier
--------------------------------------------------
Pack your bags 🧳! And have a safe flight ✈️

````

### 🚀 Getting Started

### Prerequisites
* Python 3.x installed on your machine.

## 🛠️ Code Structure

* `__init__`: Stores the `self.destinations` dictionary, acting as the local database.
* `start_planning()`: Handles the logic for user input, validation, and terminal formatting.
* `__main__`: Standard entry point to instantiate the class and trigger the workflow.

## 📝 Future Enhancements

- [ ] Add more destinations and personas.
- [ ] Implement an option to save the itinerary to a `.txt` file.
- [ ] Integration with a weather API to show current conditions at the destination.
