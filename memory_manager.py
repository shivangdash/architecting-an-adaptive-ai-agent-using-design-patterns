"""
Memory Manager - Conversation History

Stores and manages conversation history across multiple turns.
Enables the agent to maintain context during multi-turn conversations.
"""


class MemoryManager:
    """Manages conversation history.
    
    Stores messages from both user and model to maintain context
    across multiple turns in a conversation.
    """

    def __init__(self):
        """Initialize empty history list."""
        self._history = []

    def get_history(self) -> list:
        """Get the current conversation history.
        
        Returns:
            list: History of messages in the current session
        """
        return self._history

    def set_history(self, history: list) -> None:
        """Set the conversation history.
        
        Args:
            history (list): New history to set
        """
        self._history = history
