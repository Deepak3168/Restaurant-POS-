from abc import ABC,abstractmethod



class PaymentService(ABC):

    @abstractmethod
    def process_payment():
        pass 
    
