class ConversationMemory:
    def __init__(self):
        self.sessions = {}

    def add_message(self, session_id, role, content):
        history = self.sessions.setdefault(session_id, [])

        history.append({
            "role": role,
            "content": content,
        })

    def get_history(self, session_id):
        return self.sessions.get(session_id, [])

    def clear_session(self, session_id):
        self.sessions.pop(session_id, None)
