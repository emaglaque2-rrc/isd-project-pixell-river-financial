"""This module defines the Subject class."""

__author__ = "Edraque Maglaque"
__version__ = "1.0.0"

from patterns.observer.observer import Observer
from abc import ABC, abstractmethod

class Subject(ABC):
    """
    Subject class: Responsible for maintaining a list of its observers 
                   and notifying them of state changes or events.
    
    """

    def __init__(self):
        """Initialize the observers list."""
        self._observers = []

    @abstractmethod
    def attach(self, observer: Observer):
        """
        Abstract attach method to be implemented in the concrete class.

        Args:
            observer (Observer): Observer to be added.
        
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        """
        Abstract detach method to be implemented in the concrete class.

        Args:
            observer (Observer): Observer to be removed.
        
        """
        pass

    @abstractmethod
    def notify(self, message: str):
        """
        Abstract notify method to be implemented in the concrete class.

        Args:
            message (str): The message to notify observers.
        
        """
        pass
