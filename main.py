class Event:
        def __init__(self, payload):
             self.payload = payload

class ApplicationSubmittedEvent(Event):
    def __init__(self, applicant, company):
        super().__init__({'applicant': applicant, 'company': company})

class CommunicationQueue:
    def __init__(self):
        self.queue = []

    def add_event(self, event):
                   self.queue.append(event)
        print(f"Event added: {type(event).__name__} with payload {event.payload}")
    
    def process_events(self):
        while self.queue:
            event = self.queue.pop(0)
            print(f"Processing event: {type(event).__name__} with payload {event.payload}")

class Applicant:
         def __init__(self, name):
                self.name = name
    
        def apply(self, company, queue):
              print(f"{self.name} applied to {company.name}")
        event = ApplicationSubmittedEvent(self, company)
        queue.add_event(event)

class Company:
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
        
        queue = CommunicationQueue()

        alice = Applicant(name="suleyman")
            acme_corp = Company(name="QUlo sulo")
        alice.apply(acme_corp, queue)
            queue.process_events()






                



