class Notebook:
    def __init__(self):
        self.notes = []
    def add_note(self, note):
        self.notes.append(note)
    def show_notes(self):
        for x in range(len(self.notes)):
            print(f"{x+1}. {self.notes[x]}")
n = Notebook()
n.add_note("Buy groceries")
n.add_note("Read a book")
n.add_note("Call the doctor")
n.show_notes()
     