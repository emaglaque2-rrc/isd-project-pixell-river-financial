"""This module defines the Observer class."""

__author__ = "Edraque Maglaque"
__version__ = "1.0.0"

from abc import ABC, abstractmethod

class Observer(ABC):
    """
    Observer class: Interface for all concrete observers that need to 
                    be notified of changes in the subject.
    
    """

    @abstractmethod
    def update(self, message: str):
        """
        Abstract update method to be implemented by concrete observers.

        Args:
            message (str): Message to be sent to observer(s).
        
        """

        pass
    