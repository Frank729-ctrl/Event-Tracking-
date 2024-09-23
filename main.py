from datetime import datetime

class EventTracker:
    def __init__(self):
        self.events = []

    def start_event(self, event_name):
        start_time = datetime.now()
        self.events.append({'name': event_name, 'start': start_time, 'end': None})
        print(f"Event '{event_name}' started at {start_time}.")

    def end_event(self, event_name):
        end_time = datetime.now()
        for event in self.events:
            if event['name'] == event_name and event['end'] is None:
                event['end'] = end_time
                print(f"Event '{event_name}' ended at {end_time}.")
                return
        print(f"Event '{event_name}' not found or already ended.")

    def get_event_duration(self, event_name):
        for event in self.events:
            if event['name'] == event_name:
                if event['end']:
                    duration = event['end'] - event['start']
                    print(f"Duration of event '{event_name}': {duration}")
                    return duration
                else:
                    print(f"Event '{event_name}' has not ended yet.")
                    return None
        print(f"Event '{event_name}' not found.")
        return None

# Example usage
tracker = EventTracker()
tracker.start_event("Meeting")
# Do something
tracker.end_event("Meeting")
tracker.get_event_duration("Meeting")
